from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

def index(request):
    #return HttpResponse("Rango says hello world! <a href='/rango/about'>About</a>")
    context = RequestContext(request)
    context_dict = {'boldmessage' : 'i am bold font from the context'}
    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    return HttpResponse("Rango Says: Here is the about page. <a href='/rango/'>Index</a>")