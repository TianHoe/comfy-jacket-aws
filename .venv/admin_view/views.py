from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from admin_view.forms import BouquetForm, CategoryForm
# from .models import Bouquet, Category
from sample_app.models import Category, Product
from order.models import Order

def ShowAllBouquet(request):
    category = request.GET.get('category')

    if category == None:
        bouquets = Product.objects.all()
    else:
        bouquets = Product.objects.filter(category__category=category)
    

    page_num = request.GET.get("page")

    paginator = Paginator(bouquets, 12)

    try:
        bouquets = paginator.page(page_num)
    except PageNotAnInteger:
        bouquets = paginator.page(1)
    except EmptyPage:
        bouquets = paginator.page(paginator.num_pages)

    categories = Category.objects.all()

    context = {
        'bouquets': bouquets,
        'categories': categories
    }

    return render(request, 'showbouquet.html', context)

def BouquetDetails(request, pk):
    eachBouquet = Product.objects.get(id=pk)

    context = {
        'eachBouquet': eachBouquet
    }

    return render(request, 'bouquetdetail.html', context)

def addBouquet(request):
    form = BouquetForm()

    if request.method == 'POST':
        form = BouquetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(request.FILES)
            return redirect('showBouquets')
    else:
        form = BouquetForm()

    context = {
        'form': form
    }

    return render(request, 'addbouquet.html', context)

def updateBouquet(request, pk):
    bouquet = Product.objects.get(id=pk)

    form = BouquetForm(instance=bouquet)

    if request.method == 'POST':
        form = BouquetForm(request.POST, request.FILES, instance=bouquet)
        
        if form.is_valid():
            form.save()
            return redirect('showBouquets')

    context = {
        'form': form,
        'image': bouquet.image
    }

    return render(request, 'updatebouquet.html', context)

def deleteBouquet(request, pk):
    bouquet = Product.objects.get(id=pk)

    bouquet.delete()

    return redirect('showBouquets')

def searchEngine(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            bouquets = Product.objects.filter(name__icontains=query)
            return render(request, 'searchengine.html', {'bouquets': bouquets})
        else:
            print("No Information to show")
            return render(request, 'searchengine.html', {})

def vieworder(request):
    orders = Order.objects.all()

    page_num = request.GET.get("page")

    paginator = Paginator(orders, 10)

    try:
        orders = paginator.page(page_num)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)


    context = {
        'orders': orders
    }
    return render(request, 'orders.html', context)

def addCategory(request):
    catform = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showBouquets')
    else:
        form = CategoryForm()

    context = {
        'catform': catform
    }

    return render(request, 'addcategory.html', context)

def deleteCategory(request, pk):
    bouquet = Category.objects.get(id=pk)

    bouquet.delete()

    return redirect('showBouquets')