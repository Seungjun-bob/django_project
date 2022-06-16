from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import random
from datetime import datetime

def exercise1(request):
    import datetime
    now = datetime.datetime.now()
    nowDate = now.strftime('%m월 %d일')
    # date = request.GET.get('nowDate')
    name = request.GET.get('name', '강승준')
    context = { 'name':name, 'date':nowDate }

    return render(request, 'exercise1.html', context)

def exercise2(request):
    type = request.GET.get('type')
    if type == 'memberslist':
        context = {
            'memberslist': ['권진우', '강승준', '성민아', '조민석'],
        }
    elif type == 'number':
        context = {
            'msg1':'우리 팀 인원은 4명입니다.'
        }
    else:
        context = {
            'msg2':'type=memberlist 또는 type=number로 쿼리를 전달하세요'
        }

    return render(request, 'exercise2.html', context)

def exercise3(request):
    context = None
    if request.method == 'POST':
        name = request.POST.get("name", "비공개")
        memo = request.POST.get("memo", "없음")
        context = {
            'info': {
                'info1': name,
                'info2': memo,
            }
        }
    return render(request, 'exercise3.html', context)

def product1(request):
    return render(request, 'product1.html')

def basket1(request):
    pid = request.GET.get('pid')
    src = "/static/images/"+pid+".jpg"
    dt = datetime.now()
    context = {
        'current_date':dt,
        'src':src}
    return render(request, 'basket1.html', context)