from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Short_Cut
from django.urls import reverse


def visit(request, original_url):
    print('in visit')
    url = request.POST['original_url']
    return redirect(url)


def visit_direct(request, shortcut):
    go = Short_Cut.objects.get(shortcut=shortcut).original_url
    return redirect(go)
    # return HttpResponse(go)


def index(request):
    print("you called index")
    context = {'shortcut_list': Short_Cut.objects.all()}
    return render(request, 'URL_shortener_app/index.html', context)


def shorten_URL(request):
    if request.method == 'POST':
        text = request.POST['to_shorten']
        shortcut = request.POST['shortcut']
        Short_Cut(original_url=text, shortcut=shortcut).save()
    return HttpResponseRedirect(reverse('URL_shortener_app:index'))
