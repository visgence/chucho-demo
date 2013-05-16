from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from settings import APP_PATH, DEBUG
dajaxice_autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', RedirectView.as_view(url='/demo/')),
    url(r'^demo/', include('demo.urls')),
    url(r'^chucho/', include('chucho.urls')),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)

urlpatterns += staticfiles_urlpatterns()

if DEBUG:
    urlpatterns += url(r'^images\/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': APP_PATH + 'chucho/static/plugins/slickGrid/images'}),
