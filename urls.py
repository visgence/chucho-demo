from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns(
    '',
    url(r'^$', RedirectView.as_view(url='/demo/')),
    url(r'^demo/', include('demo.urls')),
    url(r'^chucho/', include('chucho.urls')),
)

urlpatterns += staticfiles_urlpatterns()
