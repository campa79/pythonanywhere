from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required #Login para ingresar a una vista
from django.contrib.auth import logout

# Create your views here.

def home(request):
	return render(request, 'core/home.html')

@login_required #viene del Decorator para que requiera login.
def products(request):
	return render(request, 'core/products.html')

def exit(request):
	logout(request)
	return redirect('home')