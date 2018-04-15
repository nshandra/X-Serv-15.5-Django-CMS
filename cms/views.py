from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from cms.models import Pages
# Create your views here.


def main(request):
    resp = "Available pages: "
    pages = Pages.objects.all()
    for page in pages:
        resp += "<br><a href=/" + page.name + ">" + page.name + "</a>"
    return HttpResponse(resp)


def get_page(request, requested_name):
    try:
        return HttpResponse(Pages.objects.get(name=requested_name).page)
    except Pages.DoesNotExist:
        return HttpResponseNotFound("<h1>Page does not exist.</h1>")
