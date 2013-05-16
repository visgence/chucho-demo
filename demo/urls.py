from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'demo.views',
    url(r'^$', 'index', name='demo-index'),
    url(r'^login/$', 'login', name='demo-login'),
    url(r'^logout/$', 'logout', name='demo-logout'),
    url(r'^login-page/$', 'login_page', name='demo-login-page'),
    )
