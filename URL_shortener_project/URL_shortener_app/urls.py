from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'URL_shortener_app' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('visit/', views.visit, name='visit'),
    path('shorten_URL/', views.shorten_URL, name='shorten_URL'),
    path('you_lose_dinosaur/', TemplateView.as_view(template_name="URL_shortener_app/you_lose_dinosaur.html"), name='you_lose_dinosaur'),
    path('<shortcut>/', views.visit_direct, name='visit_direct')
    # path('', views.test, name='index')
]
