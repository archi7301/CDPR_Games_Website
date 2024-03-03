from django.shortcuts import render, HttpResponse

def hello(request):
    return render(request=request, template_name='index.html')

