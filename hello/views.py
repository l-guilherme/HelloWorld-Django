from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django! <br> por Luiz Guilherme Barcellos <br> em 25/06/2024")
