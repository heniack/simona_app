from django.shortcuts import render,redirect
from django.http import HttpResponse
from catalogo.models import Categories, Products
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



@login_required
def catalogo_completo(request):
    productos_alimentos = Products.objects.filter(category_id = 1)
    productos_bebidas = Products.objects.filter(category_id = 2)
    productos_limpieza = Products.objects.filter(category_id = 3)
    productos_tabaco = Products.objects.filter(category_id = 4)
    productos_farmacia = Products.objects.filter(category_id = 5)
    productos_infusiones = Products.objects.filter(category_id = 6)
    usuario = request.user.username
    return render(request, 'catalogo/catalogo_completo.html', {'productos_alimentos': productos_alimentos, 
                                                     'productos_bebidas': productos_bebidas, 
                                                     'productos_limpieza': productos_limpieza, 
                                                     'productos_tabaco': productos_tabaco, 
                                                     'productos_farmacia': productos_farmacia,
                                                     'productos_infusiones': productos_infusiones,
                                                     'usuario': usuario})

def alimentos(request):
    productos = Products.objects.filter(category_id = 1)
    return render(request, 'catalogo/alimentos.html', {'productos': productos})

def bebidas(request):
    productos = Products.objects.filter(category_id = 2)
    return render(request, 'catalogo/bebidas.html', {'productos': productos})

def farmacia(request):
    productos = Products.objects.filter(category_id = 5)
    return render(request, 'catalogo/farmacia.html', {'productos': productos})

def limpieza(request):
    productos = Products.objects.filter(category_id = 3)
    return render(request, 'catalogo/limpieza.html', {'productos': productos})

def infusiones(request):
    productos = Products.objects.filter(category_id = 6)
    return render(request, 'catalogo/infusiones.html', {'productos': productos})

def tabaco(request):
    productos = Products.objects.filter(category_id = 4)
    return render(request, 'catalogo/tabaco.html', {'productos': productos})



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'catalogo/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('catalogo_completo')
            else:
                form.add_error(None, 'Usuario o contraseña inválidos.')
    else:
        form = LoginForm()
    return render(request, 'catalogo/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('catalogo/login.html')







    

