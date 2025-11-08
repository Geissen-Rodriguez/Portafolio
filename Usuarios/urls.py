from Usuarios.views.views import HomePageView
from Usuarios.views.views import MenuView
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    
    # 1. ¡COMAS EXTRAS ELIMINADAS!
    path('menu/', MenuView.as_view(), name='menu'), 
    
    # Vistas comentadas, pero listas para cuando las necesites:
    # path('tech/', TechPageView.as_view(), name='tech'),
    # path('stack-nuevo/', StackCreateView.as_view(), name='stack_crear'),
    # path('stack/<int:pk>/', StackDetailView.as_view(), name='stack_detalle'),
    
    # Vistas de autenticación
    path('login/', LoginView.as_view(template_name='login/index.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]