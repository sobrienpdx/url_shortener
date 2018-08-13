from django.urls import path
from . import views

app_name = 'URL_shortener_app' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('shorten_URL/', views.shorten_URL, name='shorten_URL')
    # path('', views.test, name='index')
]
