#from django.shortcuts import render
from django.shortcuts import render_to_response
#from django.http import HttpResponse
from django.template import RequestContext
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from rango.forms import PageForm
from utility.url_encoding import *

def index(request):
    #return HttpResponse("Rango says hello world! <a href='/rango/about'>About</a>")

    context = RequestContext(request)

    #context_dict = {'boldmessage' : 'i am bold font from the context'}

    category_list = Category.objects.order_by('-likes') #[:5]
    context_dict = {'categories': category_list}

    for category in category_list:
        category.url = encode_url(category.name)

    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    #return HttpResponse("Rango Says: Here is the about page. <a href='/rango/'>Index</a>")
    context = RequestContext(request)
    context_dict = { }
    return render_to_response('rango/about.html', context_dict, context)

def category(request, category_name_url):
    context = RequestContext(request)

    category_name = decode_url(category_name_url)
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

def add_page(request, category_name_url):
    context = RequestContext(request)

    category_name = decode_url(category_name_url)
    context_dict = {'category_name': category_name}
    context_dict['category_name_url'] = category_name_url

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            # This time we cannot commit straight away.
            # Not all fields are automatically populated!
            form.save(commit=False)
            context_dict['form'] = form

            # Retrieve the associated Category object so we can add it.
            # Wrap the code in a try block - check if the category actually exists!
            try:
                cat = Category.objects.get(name=category_name)
                Page.category = cat
            except Category.DoesNotExist:
                # If we get here, the category does not exist.
                # Go back and render the add category form as a way of saying the category does not exist.
                return render_to_response('rango/add_category.html', {}, context)

            # Also, create a default value for the number of views.
            Page.views = 0

            # With this, we can then save our new model instance.
            Page.save()

            # Now that the page is saved, display the category instead.
            return category(request, category_name_url)
        else:
            print form.errors
    else:
        form = PageForm()

    return render_to_response('rango/add_page.html', context_dict, context)