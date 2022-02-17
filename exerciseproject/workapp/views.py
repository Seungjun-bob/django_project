from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def exercise1(request):
    import datetime
    now = datetime.datetime.now()
    nowDate = now.strftime('%m월 %d일')
    # date = request.GET.get('nowDate')
    name = request.GET.get('name', '강승준')
    context = { 'name':name, 'date':nowDate }

    return render(request, 'exercise1.html', context)
# Create your views here.
