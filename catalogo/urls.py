from django.urls import path
from . import views

urlpatterns = [
    path("", views.catalogo_completo, name="catalogo_completo"),
    path("alimentos/", views.alimentos, name="alimentos"),
    path("bebidas/", views.bebidas, name="bebidas"),
    path("farmacia/", views.farmacia, name="farmacia"),
    path("limpieza/", views.limpieza, name="limpieza"),
    path("infusiones/", views.infusiones, name="infusiones"),
    path("tabaco/", views.tabaco, name="tabaco"),
    path("register/", views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('login/', views.logout_view, name='logout')
]