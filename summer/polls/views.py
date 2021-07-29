from django.shortcuts import render

def index_templates(request):
    return render(request, 'index.html')