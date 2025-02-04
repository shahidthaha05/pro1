from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os
from django.contrib.auth.models import *
from django.contrib import messages
from .models import Product, Size
from .form import ProductForm


# Create your views here.

def chrome_login(req):
    if 'chrome' in req.session:
        return redirect(home)
    
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['passwd']
        data=authenticate(username=uname,password=password)
        if data:
            if data.is_superuser:
                login(req,data)
                req.session['chrome']=uname   #create session
                return redirect(home)
            else:
                
                login(req,data)
                req.session['user']=uname   
                return redirect(user_home)
        else:
            messages.warning(req,'Invalid username or password.')
            return redirect(chrome_login)
    else:
        return render(req,'login.html')
    


def chrome_login1(req):
    if 'chrome' in req.session:
        return redirect(home)
    
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['passwd']
        data=authenticate(username=uname,password=password)
        if data:
            if data.is_superuser:
                login(req,data)
                req.session['chrome']=uname   #create session
                return redirect(home)
            else:
                
                login(req,data)
                req.session['user']=uname   
                return redirect(user_home)
        else:
            messages.warning(req,'Invalid username or password.')
            return redirect(chrome_login)
    else:
        return render(req,'login.html')
    
    
def home(req):
    if 'chrome' in req.session:
        data=Product.objects.all()
        return render(req,'shop/home.html',{'data':data})
    else:
        return redirect(chrome_login)

def intro(req):
    if 'chrome' in req.session:
        data=Product.objects.all()
        return render(req,'shop/intro.html',{'data':data})
    else:
        return redirect(chrome_login)
    
def chrome_logout(req):
    req.session.flush()          #delete session
    logout(req)
    return redirect(chrome_login)

def add_prod(req):
    if 'chrome' in req.session:
        if req.method == 'POST':
            form = ProductForm(req.POST, req.FILES)
            if form.is_valid():
                product = form.save()
                product.sizes.set(req.POST.getlist('sizes'))  # Ensure multiple sizes are saved
                return redirect('home')  # Redirect to home after adding
            else:
                print(form.errors)  # Debugging: Print form errors
        else:
            form = ProductForm()
        return render(req, 'shop/add_prod.html', {'form': form})
    else:
        return redirect('chrome_login')
    

def edit(req, pid):
    if 'chrome' in req.session:
        product = Product.objects.get(pk=pid)
        sizes = Size.objects.all()  # Get all available sizes
        
        if req.method == 'POST':
            product.pro_id = req.POST['prd_id']
            product.name = req.POST['prd_name']
            product.base_price = req.POST['prd_price']
            product.offer_price = req.POST['ofr_price']
            product.dis = req.POST['dis']
            product.quantity = req.POST['quantity']  # Update quantity
            
            # Update image if provided
            img = req.FILES.get('img')
            if img:
                product.img = img
            
            product.save()

            # Update sizes
            selected_sizes = req.POST.getlist('sizes')  # Get list of selected size IDs
            product.sizes.set(selected_sizes)  # Update many-to-many relationship

            return redirect('home')  # Redirect back to home page

        return render(req, 'shop/edit.html', {'product': product, 'sizes': sizes})
    else:
        return redirect('chrome_login')


def delete(req,pid):
    data=Product.objects.get(pk=pid)
    url=data.img.url
    og_path=url.split('/')[-1]
    os.remove('media/'+og_path)
    data.delete()
    return redirect(home)


from django.shortcuts import render
from .models import Buy, Booking, Order

def bookings(request):
    # Get all Buy objects with related product and user data
    buy = Buy.objects.select_related('product', 'user').all().order_by('-date')
    
    # Get all Order objects related to the Buy objects (assuming there's a way to link Buy to Order)
    orders = Order.objects.all()

    # Create combined data
    combined_data = zip(buy, orders)

    return render(request, 'shop/bookings.html', {'combined_data': combined_data})








# ---------------user--------------

def register(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        password=req.POST['password']
        try:
            data=User.objects.create_user(first_name=name,email=email,password=password,username=email)
            data.save()
            return redirect(chrome_login)
        except:
            messages.warning(req,'User already exists.')
            return redirect(register)
    else:
        return render(req,'user/register.html')
    

def user_home(req):
    if 'user' in req.session:
        data=Product.objects.all()
        return render(req,'user/home.html',{'data':data})
    else:
        return redirect(chrome_login)
    

def view_pro(req,pid):
    data=Product.objects.get(pk=pid)
    return render(req,'user/view_pro.html',{'data':data})

def add_to_cart(req, pid):
    if 'user' not in req.session:
        return redirect('chrome_login')

    product = Product.objects.get(pk=pid)
    user = User.objects.get(username=req.session['user'])

    size_id = req.POST.get('size')  # Get selected size from form
    selected_size = Size.objects.get(id=size_id) if size_id else None  # Fetch size object
    quantity = int(req.POST.get('quantity', 1))  # Get selected quantity

    # Check if product with same size exists in cart
    cart_item, created = Cart.objects.get_or_create(user=user, product=product, size=selected_size)

    if not created:
        cart_item.quantity += quantity  # If product is already in cart, increase quantity
    else:
        cart_item.quantity = quantity

    cart_item.save()
    
    print(f"Added to Cart: ID {cart_item.id}, Product {cart_item.product.name}, Size {cart_item.size.name}, Quantity {cart_item.quantity}")

    return redirect('view_cart')






def view_cart(req):
    if 'user' not in req.session:  # Ensure user is logged in
        return redirect('chrome_login')

    user = User.objects.get(username=req.session['user'])
    cart_det = Cart.objects.filter(user=user)

    # Check if the cart contains data
    print("Cart Items:", cart_det)  # Debugging

    for item in cart_det:
        item.total_price = item.product.offer_price * item.quantity  # Calculate total price

    return render(req, 'user/view_cart.html', {'cart_det': cart_det})




def delete_cart(req,id):
    cart=Cart.objects.get(pk=id)
    cart.delete()
    return redirect(view_cart)


def user_buy(req,cid):
    user=User.objects.get(username=req.session['user'])
    cart=Cart.objects.get(pk=cid)
    product=cart.product
    price=cart.product.offer_price
    buy=Buy.objects.create(user=user,product=product,price=price)
    buy.save()
    return redirect(order_create)


def user_buy1(req,pid):
    user=User.objects.get(username=req.session['user'])
    product=Product.objects.get(pk=pid)
    price=product.offer_price
    buy=Buy.objects.create(user=user,product=product,price=price)
    buy.save()
    return redirect(order_create)


def user_bookings(req):
    user=User.objects.get(username=req.session['user'])
    buy=Buy.objects.filter(user=user)[::-1]
    return render(req, 'user/bookings.html' ,{'buy':buy})



# views.py
from django.shortcuts import render, redirect
from .form import OrderForm
from .models import Order

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_success')  # Redirect to success page
    else:
        form = OrderForm()
    
    return render(request, 'user/book_product.html', {'form': form})

def order_success(request):
    return render(request, 'user/order_success.html')






