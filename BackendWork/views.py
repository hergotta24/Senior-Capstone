from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from BackendWork.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from BackendWork.models import User, Product, Category, ProductReviews
from django.shortcuts import render, get_object_or_404


class UserLoginView(View):
    @staticmethod
    def get(request):
        return render(request, 'login.html')

    @staticmethod
    def post(request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid login credentials.'}, status=401)


# accounts/views.py

class UserRegisterView(View):
    @staticmethod
    def get(request):
        return render(request, 'register.html')

    @staticmethod
    def post(request):
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password1 = data.get('password1')
        password2 = data.get('password2')

        form_data = {
            'email': email,
            'username': username,
            'password1': password1,
            'password2': password2,  # Assuming you want both password fields to have the same value
        }

        form = UserCreationForm(form_data)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Account Registered! Redirecting you to login to sign in...'}, status=200)
        else:
            return JsonResponse({'message': form.errors}, status=401)


class AccountManagementView(View):
    @staticmethod
    @login_required(login_url='/login/')
    def get(request):
        user = request.user
        form = UserChangeForm(instance=user)
        return render(request, 'account_management.html', {'form': form})

    @staticmethod
    @login_required(login_url='/login/')
    def post(request):
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        phone_number = data.get('phone_number')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404)

        if user != request.user:
            return JsonResponse({'error': 'You are not authorized to update this user'}, status=403)

        user.first_name = first_name
        user.last_name = last_name
        user.phone_number = phone_number
        user.save()

        return JsonResponse({'message': 'Account Information Updated!!!'}, status=200)


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def storefront(request):
    return render(request, 'storefront.html')

class VendorView(View):
    @staticmethod
    def get(request, store_id):
        products = Product.objects.filter(soldByStoreId_id=store_id)
        return render(request, 'vendor.html', {'products': products})


def createproduct(request):
    return render(request, 'createproduct.html')


def custom_logout(request):
    logout(request)
    return redirect('/')

def deleteProduct(request, productid):
    get_object_or_404(Product, id=productid)
    Product.objects.filter(productId=productid).delete()
    return redirect('storefront/')
    # I assume it should redirect to the storefront, but I'm not entirely sure. Can just change this if it's wrong

class ProductDetailView(View):
    @staticmethod
    def get(request, product_id):
        product = get_object_or_404(Product, productId=product_id)
        reviews = ProductReviews.objects.filter(productId=product.productId)
        return render(request, 'product_detail.html', {'product': product, 'reviews': reviews})


class UpdateProductView(View):
    @staticmethod
    def post(request, product_id):
        product = get_object_or_404(Product, productId=product_id)

        data = json.loads(request.body)
        name = data.get('product_name')
        price = data.get('price')
        description = data.get('description')
        qoh = data.get('qoh')
        category = data.get('category')
        image = data.get('image')
        category = Category.objects.get(name=category)

        # need to vaildation

        product.name = name
        product.price = price
        product.description = description
        product.qoh = qoh
        product.image = image
        product.category = category

        product.save()

        return render(request, 'product_detail.html', {'product': product, 'message': 'Product Information Updated!!!'})
