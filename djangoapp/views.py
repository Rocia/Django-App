from django.shortcuts import render_to_response, RequestContext
from djangoapp.script import prime

#create your views here
def my_view(request):
    a= prime(1,10)
    b='string'
    c=10
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))