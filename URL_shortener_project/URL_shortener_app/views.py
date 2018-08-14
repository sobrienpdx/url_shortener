from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Short_Cut
from django.urls import reverse
import requests, random


def visit(request, original_url):
    print('in visit')
    url = request.POST['original_url']
    return redirect(url)


def visit_direct(request, shortcut):
    go = get_object_or_404(Short_Cut, shortcut=shortcut)
    return redirect(go.original_url)
    # return HttpResponse(go)


def index(request):
    print("you called index")
    context = {'shortcut_list': Short_Cut.objects.all()}
    return render(request, 'URL_shortener_app/index.html', context)


def shorten_URL(request):
    if request.method == 'POST':
        url = request.POST['to_shorten']
        print("URL recieved")
        if not url.startswith('http'):
            url = 'http://' + url
            print("added http to url")
        if Short_Cut.objects.filter(original_url=url).exists():
            print("that url does exist in the database!")
            go = get_object_or_404(Short_Cut, original_url=url)
            # return HttpResponse(f'the new url for {url} is localhost800{go.shortcut}')
            context = {'shortcut': go, 'url': url}
            return render(request, 'URL_shortener_app/index.html', context)
        print("it wasn't in the data base")
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("that is a good url")
                chars = "abcdefghijklmnopqrstuvwxzyABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
                while True:
                    value = "".join(random.choice(chars) for _ in range(5))
                    if value not in Short_Cut.objects.all():
                        Short_Cut(original_url=url, shortcut=value).save()
                        context = {'shortcut': value, 'url': url}
                        # return HttpResponse(f'the new url for {url} is localhost800{value}')
                        return render(request, 'URL_shortener_app/index.html', context)
            else:
                raise Exception
        except:
            return redirect('URL_shortener_app:you_lose_dinosaur')
            # return HttpResponse("that didn't work! Are you sure your url was correct?")
