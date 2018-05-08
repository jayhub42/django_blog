from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'blog/welcome.html')  # return HttpResponse("index Hello, this is how monte works.")