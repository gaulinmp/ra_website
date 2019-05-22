# -*- coding: utf-8 -*-

from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from django.utils.html import format_html


from .models import ProjectID, TextBlob

def edgar_url(obj):
    html_root = '//www.sec.gov/Archives/edgar/data'

    html = (f'<a href="{html_root}/{obj.cik}/{obj.accession}/'
            f'{obj.accession}-index.html" target=_blank>EDGAR Index</a>')

    if obj.edgarfname is not None:
        html.append(f'&nbsp;&nbsp;&nbsp;<a href="{html_root}/{obj.cik}/'
                    f'{obj.accession}/{obj.edgarfname}" target=_blank>'
                    f'Direct ({obj.edgarfname})</a>')

    return format_html(html)

#
#    Project ID Viewer that filters out just interesting flags
#
class IgnoreReviewedFormSet(BaseInlineFormSet):
    """
    This FormSet is basically the code that gets the objects to display inline
    in the Project section of the admin interface.

    Below, it is limited to just one accession per page, but all the texts from that
    accession.

    If you just wanted one text to display per page, that would be:
    """
    def get_queryset(self):
        if not hasattr(self, '_queryset'):
            # qs = super().get_queryset().filter(reviewed=False)[:10]
            first_obj = (super().get_queryset() # Call parent
                .filter(reviewed=False) # just get those not yet reviewed
                .order_by('cik') # go low to high by CIK
                .first()) # just get the first one

            if first_obj is None:
                # No un-reviewed texts found
                self._queryset = qs
                return self._queryset

             # Now do the query again, to get all texts from that first accession
            self._queryset = (super().get_queryset()
                .filter(reviewed=False) # comment out to get all the accession's texts
                .filter(accession=first_obj.accession))

        return self._queryset


class TextBlobEditInline(admin.StackedInline):
    """Inline for editing, hides some fields"""
    class Media:
        css = {"all": ("css/extra_admin.css", )}
    model = TextBlob
    formset = IgnoreReviewedFormSet
    fieldsets = (
        ("◄♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦☻ Info ☻♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦►",
          {'fields':
            ( '_text', '_url',
              ('cik', 'accession', 'edgarfname'),
            ),
           'classes': ('example', 'subrow', 'center' )
          }
        ),
        ("Scraped Data",
          {'fields':
            ( ('scrape_worked', 'extract_number', 'extract_text', ),
              ('reviewed', 'flag_for_review', ),
              ('notes', )
            ),
           'classes': ('example', 'subrow', )
          }
        )
    )
    readonly_fields = ('_text', '_url', 'cik', 'accession', 'edgarfname')
    ordering = ('cik', 'accession', )
    extra = 0
    max_num = 5

    def _url(self, obj):
        return edgar_url(obj)

    def _text(self, obj):
        """
        Wrapper for scraped text. If your text is html, change this to:

        return format_html(obj.text)
        """
        return (obj.text)



class ProjectIDEditAdmin(admin.ModelAdmin):
    model = ProjectID
    fields = ('project', )
    inlines = [TextBlobEditInline, ]
    list_filter = ('project', )

admin.site.register(ProjectID, ProjectIDEditAdmin)


#
#    Text Blob Admin standalone stuff thingy
#
class TextBlobAdmin(admin.ModelAdmin):
    model = TextBlob
    fields = (
        ('project', '_url'),
        ('cik', 'accession', 'edgarfname', ),
        'text',
        ('reviewed', 'flag_for_review'),
        ('scrape_worked', 'extract_number', 'extract_text', ),
        'notes',
    )
    # This sets up the filters on the right side of the admint page, so you can
    # filter the texts to those reviewed, those flagged for further review, etc
    list_filter = ('project', 'reviewed', 'flag_for_review', 'scrape_worked',)

    # Add fields here you wish to be read-only
    readonly_fields = ('_url', )

    def _url(self, obj):
        return edgar_url(obj)

admin.site.register(TextBlob, TextBlobAdmin)
