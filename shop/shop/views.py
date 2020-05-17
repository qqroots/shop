from django.shortcuts import redirect, render
from django import http
from product.models import Product
from order.models import OrderItem,Order
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

def base(request):
    return render(request,'base.html')

# def logout(request):
#     #to do 
#     return HttpResponseRedirect('/')

def index(request):
    return render(request,'index.html',)

def get_shop(request):
    products = Product.objects.all()
    return render(request,'shop.html',locals())

def get_order(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    # if 'id' in request.GET and request.GET['id'] != '':
        # ids = request.GET.getlist('id',[])           #html有勾選的項目取出其產品id
        # qtys = request.GET.getlist('product_qty',[]) #html有勾選的項目取出其數量
        # content = dict(zip(ids,qtys))
    # else:
    #     raise Http404

    if 'product_qty' in request.POST:
    # if any(request.POST[i] for i in request.POST['product_qty']) != None :
        products = Product.objects.all()
        ids = []
        for p in products:
            p_id = p.pk
            ids.append(p_id)
        qtys = request.POST.getlist('product_qty',[])
        content = dict(zip(ids,qtys))
    else:
        raise Http404

    order_items = []
    total = 0
    for i in content:
        if content[i] != '':
            p = Product.objects.get(id=i)
            order_items.append([p.pk,p.product_name,p.product_price,content[i]])
            total += int(p.product_price) * int(content[i])
    if total == 0:
        raise Http404
    return render(request,'order_item.html',locals())

def order_confrim(request):
    if request.user:
        user_id = request.user.pk
        user_name = request.user.username

    ids = request.POST.getlist('product_pk',[])   #html有勾選的項目取出其產品id
    qtys = request.POST.getlist('product_qty',[]) #html有勾選的項目取出其數量
    content = dict(zip(ids,qtys))
    total = request.POST.get('total',False) #容易有MultiValueDictKeyError 因為check box是多選
    # total = request.POST['total'] #容易有MultiValueDictKeyError
    
    order = Order.objects.create(order_user=request.user.pk ,order_total=total) #先創造一筆空的Order物件

    order_items = []
    for i in content:
        p = Product.objects.get(id=i)
        order_item = OrderItem.objects.create(
            product_name=p.product_name, product_price=p.product_price, product_qty=content[i],order=order
            )
        order_items.append(order_item)
    return render(request,'order_confirm.html',locals())


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # print("Errors", form.errors)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            # form = UserCreationForm()
            # context = {'form': form}
            # error = True
            return render(request,'register.html',locals())
    else:
        # error = False
        form = UserCreationForm()
        context = {'form': form}
        return render(request,'register.html',locals())


def user_order(request):
    if request.user:
        user_id = request.user.pk
        user_name = request.user.username
    
    orders = Order.objects.filter(order_user=user_id)
    # order_item = order_no.orderitem_set.all()
    return render(request,'user_order.html',locals())
    