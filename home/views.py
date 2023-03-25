from django.shortcuts import render , get_object_or_404, redirect, HttpResponse
from .models import Product, Category, Enquiry , Contact
from .models import Subscribtion as subscrib  
from home.forms import Enquiry, Subscribtion , contact_form
from django.contrib import messages
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

# Create your views here.

def home(request):

    
    query = request.GET.get('search')
    
    
    if request.method == 'GET':
        query = request.GET.get('search')
        if query:
            if prod:
                payload = []
                prod = Product.objects.filter(title__icontains=query) 
                for prod_obj in prod:

                    payload.append(prod_obj.title) 
                    
                return JsonResponse({'status':200,'data': payload})
        
    # search = request.GET.get['search']

    
       
    if request.method == 'POST':
        form = Subscribtion(request.POST)
        email = request.POST.get('email')
        print(email)
        
        if form.is_valid():
            if subscrib.objects.filter(email=email).exists() == False:
                form.save()
                messages.success(request, 'You have successfully subscribed to our newsletter')
                return redirect(request.META['HTTP_REFERER'])
            else:
                messages.error(request, 'Email already registered')
        else:
            messages.error(request, 'Invalid form data')
            messages.error(request, form.errors)
        

        
    else:
        
        form = Subscribtion(request.POST)
        

    prod = Product.objects.all()

    categories = Category.objects.all()

    top_collection = Product.objects.all()[0:8]
    return render(request, 'home.html',{'prod':prod, 'top_collection':top_collection,'categories' : categories ,'form':form,'contact_form':contact_form})

def base(request):
    categories = Category.objects.all()
    

    return render(request, 'base.html',{'categories' : categories })



def shop(request):
    prod = Product.objects.all()
    category = request.GET.get('category')
    if category is not None:
        prod = Product.objects.filter(category__title=category)

    paginator = Paginator(prod, 9) # Show 10 products per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()
    return render(request, 'shop.html', {'page_obj': page_obj, 'categories': categories, 'prod':prod,})


def serach(request):

    prod = Product.objects.all()
    category = request.GET.get('category')

    query = request.GET.get('search')
    
    
    if request.method == 'GET':
        query = request.GET.get('search')
        if query:
            prod = Product.objects.filter(title__icontains=query)
            # if prod:
            #     payload = []
            #     prod = Product.objects.filter(title__icontains=query) 
            #     for prod_obj in prod:

            #         payload.append(prod_obj.title) 
                    
            #     return JsonResponse({'status':200,'data': payload})
            categories = Category.objects.all()
            paginator = Paginator(prod, 100) # Show 10 products per page.
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'serach.html', {'prod':prod, 'categories' : categories ,'page_obj':page_obj})
            
        else:
            print("No information to show")
            categories = Category.objects.all()
            return render(request, 'serach.html', {'categories' : categories})


    search = request.GET.get['search']
    
    prod = Product.objects.filter(category_title__icontains=search).order_by('-id')

    return render(request, 'serach.html',{ 'prod':prod ,})


def searchmaaz(request):


    prod = Product.objects.all()
    category = request.GET.get('category')

    
    if request.method == 'GET':
        query = request.GET.get('search')
        if query:
            if prod:
                payload = []
                prod = Product.objects.filter(title__icontains=query)[:5] 
                for prod_obj in prod:

                    payload.append(prod_obj.title) 
                    
                return JsonResponse({'status':200,'data': payload})
            categories = Category.objects.all()
            paginator = Paginator(prod, 100) # Show 10 products per page.
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'serach.html', {'prod':prod, 'categories' : categories ,'page_obj':page_obj})
            
        else:
            print("No information to show")
            categories = Category.objects.all()
            return render(request, 'serach.html', {'categories' : categories})


    search = request.GET.get['search']
    
    prod = Product.objects.filter(category_title__icontains=search).order_by('-id')

    return render(request, 'serach.html',{ 'prod':prod ,})
   










def contact(request):
    categories = Category.objects.all()
    form = contact_form(request.POST)


    if request.method == 'POST':
        form = contact_form(request.POST)
        email = request.POST.get('email')
        # print(email)
        
        if form.is_valid():
            if Contact.objects.filter(email=email).exists() == False:
                form.save()
                messages.success(request, 'Successfully Submitted')
                return redirect(request.META['HTTP_REFERER'])
            else:
                messages.error(request, 'Email already registered')
        else:
            messages.error(request, 'Invalid form data')
            messages.error(request, form.errors)
        
    else:
        
        form = contact_form(request.POST)



    return render(request, 'contact.html', {'categories' : categories,'form':form,})

def aboutus(request):
    categories = Category.objects.all()

    return render(request, 'about.html', {'categories' : categories})


def prod_detail(request, id):
    categories = Category.objects.all()

    prod = Product.objects.all()

    prod_id = Product.objects.all().filter(id = id)
    product = get_object_or_404(Product, pk=id)
    
    related_prod = Product.objects.all().exclude(id = id)[:4]
    # form = Enquiry()
    # form = form(initial={'name': 'Peter'})
    
    
    if request.method == 'POST':
            form = Enquiry(request.POST)
            if form.is_valid():
                
                
                form.save()
                messages.success(request, 'Enquiry request submitted successfully.')
                return redirect(request.META['HTTP_REFERER'])
            else:
                messages.error(request, 'Invalid form submission.')
                messages.error(request, form.errors)
    else:
        
        form = Enquiry(request.POST or None,initial={'Product': product.title })
        
        


    return render(request, 'prod_detail.html', {'prod_id': prod_id, 'categories' : categories, 'related_prod':related_prod,'form':form,'prod':prod})







def quickview(request, id):
    categories = Category.objects.all()

    prod = Product.objects.all().filter(id = id)   
   
        
        


    return render(request, 'quickview.html', {'prod': prod, 'categories' : categories,})