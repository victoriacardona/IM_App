from django.shortcuts import render

def im_app(request):
    return render(request,'main.html')

def im_app_formulario(request):
    return render(request,'formulario.html')
# Create your views here.
