from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'demo.views',
    url(r'^$', 'index', name='demo-index'),
    )
