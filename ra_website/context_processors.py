# -*- coding: utf-8 -*-

from django.conf import settings

def google_analytics(request):
    """
    Use the variables returned in this function to
    render your Google Analytics tracking code template.
    """
    ga_prop_id = getattr(settings, 'GOOGLE_ANALYTICS_PROPERTY_ID', False)
    ga_domain = getattr(settings, 'GOOGLE_ANALYTICS_DOMAIN', False)
    # if not settings.DEBUG and ga_prop_id and ga_domain:
    if ga_prop_id or ga_domain:
        return {
            'GOOGLE_ANALYTICS_PROPERTY_ID': ga_prop_id,
            'GOOGLE_ANALYTICS_DOMAIN': ga_domain,
        }
    return {}

def get_current_next(request):
    _next_dict = request.GET.copy()
    try:
        _next_dict['page'] = int(_next_dict.get('page', 1)) + 1
    except ValueError:
        _next_dict['page'] = 2
    return {
       'current_path': request.get_full_path(),
       'next_page_path': request.path,
       'next_page_query': _next_dict.urlencode(),
       'next_page': '{}?{}'.format(request.path, _next_dict.urlencode()),
     }
