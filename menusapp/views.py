from django.shortcuts import render
from .models import Testimonials

# Create your views here.

def homepage(request):
    testimonials = Testimonials.objects.all()
    context       = {'testimonials':testimonials,}
    return render(request, 'menusapp/index.html',context)
