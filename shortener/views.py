from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from django.http import HttpResponse

def home(request):
    if request.method == "POST":
        long_url = request.POST.get("long_url")
        if long_url:
            url_obj, created = URL.objects.get_or_create(long_url=long_url)
            return render(request, "shortener/result.html", {
                "short_url": request.build_absolute_uri(f"/{url_obj.short_code}"),
                "expiry_date": url_obj.expiry_date
            })
    return render(request, "shortener/home.html")

def redirect_url(request, code):
    url_obj = get_object_or_404(URL, short_code=code)
    if url_obj.is_expired():
        return HttpResponse("<h1>Sorry, this link has expired.</h1>")
    return redirect(url_obj.long_url)
