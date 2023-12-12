from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<h1>Hey, Django Server</h1>")

def success_page(request):
    return HttpResponse("""<h2 style ="color : Blue ">Hey, You are getting response from Django Server</h2>""")
