from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage.html')

def learn(request):
    return render(request, 'learn.html')
