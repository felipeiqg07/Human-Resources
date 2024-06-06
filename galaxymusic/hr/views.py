from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404,render



def index(request):
    
    return render(request, "hr/index.html")



