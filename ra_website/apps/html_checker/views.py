# -*- coding: utf-8 -*-

import os
import re
import json
import datetime as dt
import logging
from html.parser import HTMLParser

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render # render_to_response
# from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
# # from django.conf import settings as SETTINGS
# from django.contrib.auth.views import redirect_to_login

from .forms import UploadFileForm
from .utils import handle_uploaded_file, handle_download_file
from .models import ProjectID, TextBlob

LOGGER = logging.getLogger(__name__)

#
#    View methods
#
def view(request, project_id_array=None, reviewed=True):
    blobs = TextBlob.objects

    if project_id_array:
        blobs = blobs.filter(project_id__in=project_id_array)
    if reviewed:
        blobs = blobs.filter(reviewed=True)

    return render(request, 'html_checker/viewer.html',
                    {'blobs': blobs,}
                 )

def add_note(request):
    h = HTMLParser()
    pid = request.GET.get('id', -1)
    note = h.unescape(request.GET.get('note', ''))
    try:
        pid = int(pid)
    except ValueError:
        pid = -1

    tb = TextBlob.objects.filter(pk=pid).first()
    if not tb:
        return HttpResponse('{"success":false, "id": '+pid+'}',
                            content_type="application/json")
    tb.notes = note
    tb.save()
    return HttpResponse(json.dumps({'success':True, 'id':pid, 'note':note}),
                        content_type="application/json")

@csrf_protect
def upload(request):
    """
    Upload file to add data to database.
    Can be json file of format:
    [{'cik': 20, 'accession': 'xxx',...}, ...]

    or an excel file, with the first row being the field names:
    cik  |  accession  |  text
    -----+-------------+-------------------------------------------------------------
    20   | xxxxxxxxxxx | It was the best of websites, it was the worst of websites.

    Don't add any fields in your json/excel that aren't in the database.
    This isn't robust, after all.
    """
    if request.method == 'POST':
        import pandas as pd

        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            project_name = form.cleaned_data['project_name']
            pid, created = ProjectID.objects.get_or_create(project=project_name)

            df = handle_uploaded_file(form.cleaned_data['upload_type'],
                                      request.FILES['upload_file'])

            LOGGER.info("UPLOAD: {} project: {} with {} rows uploaded.".format(
                        "New" if created else "Old", pid, len(df)))

            # Format dates to be datetime objects
            for c in ('filedate', 'datadate'):
                if c in df:
                    df[c] = pd.to_datetime(df[c])

            TextBlob.objects.bulk_create(
                [TextBlob(project=pid, **row) for row in df.to_dict('records')])

            # next_url = reverse('html_checker:index')
            next_url = '/admin/html_checker/projectid/{}/'.format(pid.id)
            return HttpResponseRedirect(next_url)
    else:
        form = UploadFileForm()
    c = {}
    # c.update(csrf(request))
    c['form'] = form
    c['next'] = 'upload'
    return render(request, 'html_checker/upload.html', c)


def download(request):
    blobs = (TextBlob.objects
                     .filter(reviewed=1))

    resp = HttpResponse(content_type='application/vnd.ms-excel')
    resp['Content-Disposition'] = 'attachment; filename="time_series_packages.tsv"'
    resp['Content-Disposition'] = 'attachment; filename=ra_website_data.xlsx'
    resp.write(handle_download_file(blobs))
    return resp
