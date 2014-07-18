from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from utility.url_encoding import *

def index(request):
    #return HttpResponse("Rango says hello world! <a href='/rango/about'>About</a>")

    context = RequestContext(request)

    #context_dict = {'boldmessage' : 'i am bold font from the context'}

    category_list = Category.objects.order_by('-likes') #[:5]
    context_dict = {'categories': category_list}

    for category in category_list:
        category.url = encode(category.name, ' ', '_')

    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    #return HttpResponse("Rango Says: Here is the about page. <a href='/rango/'>Index</a>")
    context = RequestContext(request)
    context_dict = { }
    return render_to_response('rango/about.html', context_dict, context)

def category(request, category_name_url):
    context = RequestContext(request)

    category_name = encode(category_name_url, '_', ' ')
    context_dict = {'category_name': category_name}

    try:
        category = Category.objects.get(name=category_name)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass

    return render_to_response('rango/category.html', context_dict, context)

def add_category(request):
    # Get the context from the request.
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('rango/add_category.html', {'form': form}, context)