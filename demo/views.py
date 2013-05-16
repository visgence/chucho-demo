#System imports
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from settings import SESSION_TIMEOUT


def check_access(request):
    request.session.set_expiry(SESSION_TIMEOUT)
        
    if request.user.is_authenticated():
        if request.user.is_active:
            return request.user
        else:
            return None
    else:
        return None


def index(request):
   
    response = check_access(request)
    if response is None:
        return HttpResponseRedirect('/demo/login-page/')
    
    t = loader.get_template('index.html')
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))


def login_page(request):

    response = check_access(request)
    if response is not None:
        return HttpResponseRedirect('/')

    t = loader.get_template('login.html')
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))


def login(request):
    
    response = check_access(request)
    if response is not None:
        return HttpResponseRedirect('/')

    error = ''
    if request.method == 'POST':
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/')
            else:
                error = "Account disabled"
        else:
            error = "Invalid login";

    request.user = None
    t = loader.get_template('login.html');
    c = RequestContext(request, {'error':error})
    return HttpResponse(t.render(c))

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect("/")


