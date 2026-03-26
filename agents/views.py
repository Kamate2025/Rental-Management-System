from django.shortcuts import render


def agents_list(request):
    return render(request, 'agents/agents_list.html')