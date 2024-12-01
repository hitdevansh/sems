from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import Customer,Product,Cart,OrderPlaced,PasswordResetToken
from .forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from .helpers import send_forget_password_mail
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator 
from django.shortcuts import render, redirect
import uuid



def ForgetPassword(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            
            user_obj = User.objects.filter(username=username).first()
            if not user_obj:
                messages.error(request, 'No user found with this username.')
                return redirect('/forget-password/')
            
            # Generate a unique token
            token = str(uuid.uuid4())
            
            # Create or update the PasswordResetToken
            password_reset_token, created = PasswordResetToken.objects.get_or_create(user=user_obj)
            password_reset_token.token = token
            password_reset_token.save()
            
            # Send email with forget password token
            send_forget_password_mail(user_obj.email, token)
            
            messages.success(request, 'An email has been sent with instructions to reset your password.')
            return redirect('/forget-password/')
                
    except Exception as e:
        print(e)
        messages.error(request, 'An error occurred while processing your request.')
    
    return render(request, 'app/forget-password.html')

def ChangePassword(request, token):
    context = {}

    try:
        # profile_obj = User.objects.filter(forget_password_token=token).first()
        profile_obj = PasswordResetToken.objects.filter(token=token).first()
        context = {'user_id': profile_obj.user.id}

        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')

            if user_id is None:
                messages.error(request, 'No user id found.')
                return redirect(f'/change-password/{token}/')

            if new_password != confirm_password:
                messages.error(request, 'Passwords do not match.')
                return redirect(f'/change-password/{token}/')

            user_obj = User.objects.get(id=user_id)

            # Validate the new password using custom constraints
            try:
                validate_custom_password(new_password)
            except ValidationError as e:
                messages.error(request, f"Password validation failed: {', '.join(e.messages)}")
                return redirect(f'/change-password/{token}/')

            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('/accounts/login/')

    except Exception as e:
        messages.error(request, f"An error occurred: {e}")

    return render(request, 'app/change-password.html', context)




class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',{'form':form})
    
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!! Registered successfully...')
            form.save()
        return render(request,'app/customerregistration.html',{'form':form})

class ProductView(View):
    def get(self,request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')  
        
        return render(request,'app/home.html',{'topwears':topwears,'bottomwears':bottomwears,'mobiles':mobiles})

class ProductDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product=product.id)&Q(user = request.user)).exists()
        return render(request,'app/productdetail.html',{'product':product,'already':item_already_in_cart})

@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id') 
    product = Product.objects.get(id = product_id)
    Cart(user = user,product = product).save()
    return redirect('/cart')

@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user = user)
        amount = 0.0
        shipping_amount = 70.0
        totalamount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user==user]
        if cart_product:
            for p in cart_product:
                tempa = (p.quantity * p.product.discounted_price)
                amount+=tempa 
                totalamount = amount + shipping_amount
            return render(request,'app/addtocart.html',{'carts':cart,'totalamount':totalamount,'amount':amount,'shipping_amount':shipping_amount})
        else:
            return render(request,'app/emptycart.html')

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user = request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        totalamount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempa = (p.quantity * p.product.discounted_price)
            amount+=tempa 
        
        data = {
            'quantity': c.quantity,
            'amount' : amount,
            'totalamount' : amount + shipping_amount
        }

        return JsonResponse(data)
       
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user = request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        totalamount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempa = (p.quantity * p.product.discounted_price)
            amount+=tempa 

        data = {
            'quantity': c.quantity,
            'amount' : amount,
            'totalamount' : amount + shipping_amount
        }

        return JsonResponse(data)

def removecart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user = request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        totalamount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempa = (p.quantity * p.product.discounted_price)
            amount+=tempa 

        data = {
            'amount' : amount,
            'totalamount' : amount + shipping_amount
        }

        return JsonResponse(data)

@login_required
def buy_now(request):
    return render(request, 'app/buynow.html')

@login_required
def profile(request):
    return render(request, 'app/profile.html')

@login_required
def address(request):
    add = Customer.objects.filter(user = request.user)
    return render(request, 'app/address.html',{'add':add})

@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user = request.user)
    print(op)
    return render(request, 'app/orders.html',{'orders_all':op})

@login_required
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user = user)
    cart_prod = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_ammount = 70.0
    cart_product = [p for p in Cart.objects.all() if p.user==request.user]
    if cart_prod:
        for p in cart_product:
            tempa = (p.quantity * p.product.discounted_price)
            amount+=tempa
        
    return render(request, 'app/checkout.html',{'add':add,'totalamount':amount+shipping_ammount,'cart_items':cart_prod})

@login_required
def payment_done(request):
    print("cones in payment-odne")
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
        c.delete()

    return redirect("orders")

def mobile(request,data=None):
    if data == None:
        mobiles = Product.objects.filter(category='M')
    elif data == 'Redmi' or data=='Samsung':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'below':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=20000)
    elif data == 'above':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=20000)
    return render(request, 'app/mobile.html',{'mobiles':mobiles})

def topwear(request,data=None):
    if data == None:
        topwears = Product.objects.filter(category='TW')
    elif data == 'men':
        topwears = Product.objects.filter(category='TW').filter(gender='M')
    elif data == 'women':
        topwears = Product.objects.filter(category='TW').filter(gender='F')
    return render(request, 'app/topwear.html',{'topwears':topwears})

def bottomwear(request,data=None):
    if data == None:
        bottomwears = Product.objects.filter(category='BW')
    elif data == 'men':
        bottomwears = Product.objects.filter(category='BW').filter(gender='M')
    elif data == 'women':
        bottomwears = Product.objects.filter(category='BW').filter(gender='F')
    return render(request, 'app/bottomwear.html',{'bottomwears':bottomwears})

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})
    
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=user,name = name , locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,'Congratulations!! Your profile has been updated successfully!!')
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})
    


# password constrints
def validate_custom_password(password):
    # Implement your custom password constraints
    # Example: Minimum length 8, maximum length 12, at least one special character, one uppercase letter, and one digit
    if len(password) < 8 or len(password) > 12:
        raise ValidationError("Password must be between 8 and 12 characters.")

    if not any(char.isdigit() for char in password):
        raise ValidationError("Password must contain at least one digit.")

    if not any(char.isupper() for char in password):
        raise ValidationError("Password must contain at least one uppercase letter.")

    if not any(char.isalnum() for char in password):
        raise ValidationError("Password must contain at least one special character.")