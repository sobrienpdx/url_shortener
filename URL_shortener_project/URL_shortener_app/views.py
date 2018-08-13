from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Short_Cut
from django.urls import reverse

def test(request):
    print("you called test")
    return HttpResponse('ok-test')

def shorten_URL(request):
    if request.method == 'POST':
        text = request.POST['to_shorten']
        shortcut = request.POST['shortcut']
        Short_Cut(original_url=text, shortcut=shortcut).save()
    return HttpResponseRedirect(reverse('URL_shortener_app:index'))

# def shorten_URL(request):
#     return(HttpResponse('ok'))


def index(request):
    print("you called index")
    context = {'shortcut_list': Short_Cut.objects.all()}
    return render(request, 'URL_shortener_app/index.html', context)
# Create your views here.

# def index(request):
#     # context = {<name-value pairs>}
#     return render(request, '<app name>/<template name>.html', context)
