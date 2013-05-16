#System imports
from django.http import HttpResponse
from django.template import RequestContext, loader
import datetime as dateTime

from demo.models import DemoUser, DemoInfo

def index(request):
    
    t = loader.get_template('index.html')
    c = RequestContext(request, {})

    return HttpResponse(t.render(c))
