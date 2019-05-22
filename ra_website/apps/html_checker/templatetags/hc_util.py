from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(needs_autoescape=True)
def get_sec_index(blob, autoescape=True):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    url = "http://www.sec.gov/Archives/edgar/data/{}/{}/{}-index.htm"
    url = url.format(blob.cik, blob.accession, blob.accession)

    return mark_safe(esc(url))
