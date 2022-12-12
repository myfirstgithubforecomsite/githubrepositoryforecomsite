from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.


from .models import *


#def home(request):
 #prod=products.objects.all()
 #return render(request,'home.html',{'pr':prod})


def home(request, c_slug=None):
    c_page = None
    prod = None
    if c_slug!= None:
        c_page = get_object_or_404(category, slug=c_slug)
        prod = products.objects.filter(categ=c_page, available=True)
    else:
        prod = products.objects.all().filter(available=True)
    categ = category.objects.all()

    paginator = Paginator(prod,4)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {'pr': prod, 'categ': categ, 'pg':pro})

def product_details(request,c_slug,product_slug):
    try:
        prod=products.objects.get(categ__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'pr':prod})

def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=products.objects.all().filter(Q(name__contains=query)|Q(description__contains=query))
    return render(request,'search.html',{'qr':query,'pr':prod})

