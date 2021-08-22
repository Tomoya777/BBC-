from django.shortcuts import render

def index_templates(request):
    return render(request, 'index.html')

def index_templates1(request):
    return render(request, 'active.html')