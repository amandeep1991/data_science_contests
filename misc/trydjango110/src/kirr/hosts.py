from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www_name'),
    host(r'(?!www).*', 'kirr.hostsconf.urls', name='wildcard'),
)

'''
# Currently django-hosts implements it in above way, but there are chances that this will change to below as this is more uniform to django style:

from kirr.hostsconf import urls as redirect_urls

host_patterns = [
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', settings.redirect_urls, name='www'),
]

'''