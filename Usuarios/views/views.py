from django.views.generic import TemplateView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

class HomePageView(TemplateView): # Hereda primero de LoginRequiredMixin
    template_name = 'home/home.html'
    

class TechPageView(LoginRequiredMixin, TemplateView):
    # Heredar de LoginRequiredMixin ahora requiere autenticación
    template_name = 'tech/index.html'
    
class MenuView(LoginRequiredMixin, TemplateView):
    # CORRECTO: Requiere login (es el menú interno)
    template_name = 'menu.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        # En una vista protegida, sabes que user.is_authenticated es True
        context['grupo'] = user.groups.first().name if user.groups.exists() else 'Sin grupo'
        return context



# class StackCreateView(LoginRequiredMixin, CreateView):
#     model = Stack
#     template_name = 'stack/create.html'
#     fields = ['nombre', 'descripcion']
#     success_url = '/'
#     login_url = 'login'


# class StackDetailView(LoginRequiredMixin, DetailView):
#     model = Stack
#     template_name = 'stack/detail.html'
#     login_url = 'login'
