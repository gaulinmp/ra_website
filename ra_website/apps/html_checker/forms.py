# -*- coding: utf-8 -*-

from django import forms
# https://docs.djangoproject.com/en/2.2/topics/forms/
# https://docs.djangoproject.com/en/2.2/ref/forms/fields/

class UploadFileForm(forms.Form):
    project_name = forms.CharField(label="Project Name", max_length=255)
    upload_type = forms.ChoiceField(label="Upload File Type",
        choices=[('json', 'JSON Document'),
                 ('xlsx', 'Excel File'),])
    upload_file = forms.FileField(label="File to Upload")
