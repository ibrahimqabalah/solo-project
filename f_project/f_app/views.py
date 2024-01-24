from django.shortcuts import render,redirect
from django.contrib import messages
import bcrypt

from .models import *
# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    errors=User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request, value)
        
        return redirect("/")
    else:
        password= request.POST['password']
        hashed=bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
        usr=User.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],email=request.POST['email'],password=hashed,admin=False)
        request.session['guest']=usr.first_name
        request.session['id']=usr.id
        request.session['admin']=usr.admin
        return redirect("/products")
    
def login(request):
    user=User.objects.filter(email=request.POST['email'])
    if user:
        logged=user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged.password.encode()):
            request.session['id']=logged.id
            request.session['guest']=logged.first_name
            request.session['admin'] = logged.admin
            return redirect("/products")
        else:
            messages.error(request,"Invalid credentials!")

            return redirect("/")
    else:

        messages.error(request,"Invalid credentials!")
        return redirect("/")

def main(request):
    if not 'id' in request.session:
        messages.error(request,"you have to login first!")
        return redirect("/")
    else:
        return render(request,"products.html ")


def logout(request):
    request.session.flush()
    return redirect("/")
# ###Products View

def products(request):
    context={
    'products':Product.objects.all(),
    }
    return render(request, 'products.html', context)

# ###New Product View
def new_product(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        image_url = request.POST.get('image_url')
        #user_id = request.user
        product = Product(title=title, price=price, image_url=image_url)
        product.save()
        return redirect('products')
    return render(request, 'new_products.html')

def product_details(request, product_id):
    context={
    'product': Product.objects.get(id=product_id)
    }
    return render(request, 'product_details.html', context)

# ###Edit Product View
def edit_product(request, product_id):
    context={
        'product':Product.objects.get(id=product_id)
    }
    if request.method == 'POST':
        context['product'].title = request.POST.get('title')
        context['product'].price = request.POST.get('price')
        context['product'].image_url = request.POST.get('image_url')
        context['product'].save()
        return redirect('product_details', product_id=product_id)
    return render(request, 'edit_product.html', context)
                                                 
# ###View Cart
def view_cart(request):
    user = User.objects.get(id=request.session['id'])
    print(user.id)
    context={
    'cart_items': Cart.objects.filter(user_id=user)
    }
    print(context["cart_items"])
    return render(request, 'cart.html', context)

# ###Add to Cart
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    print(product.title)
    user = User.objects.get(id=request.session['id'])
    print(user.id)
    old_cart_item = Cart.objects.filter(user_id=user).filter(product_title=product.title)
    if len(old_cart_item) != 0:
        old_cart_item[0].quantity += 1
        old_cart_item[0].save()
    else:
        new_cart_item = Cart(user_id=user, product_title=product.title, product_price=product.price, quantity=1)
        new_cart_item.save()
    return redirect('view_cart')

# ###Update Cart
def update_cart(request, cart_id):
    context={
    'cart_item': Cart.objects.get(id=cart_id)
    }
    if request.method == 'POST':
        context['cart_item'].quantity = request.POST.get('quantity')
        context['cart_item'].save()
        return redirect('view_cart')
    return render(request, 'update_cart.html', context)

# ###Delete from Cart
def delete_from_cart(request, cart_id):
    Cart.objects.get(id=cart_id).delete()
    return redirect('view_cart')  
                                               
def purchase(request):
    
    return render(request,'purchases.html')

def about(request):
    return render(request,'about_us.html')

