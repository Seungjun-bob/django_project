from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import random
from datetime import datetime

def exam1(request):
    template = loader.get_template('exam1.html')
    return HttpResponse(template.render(None, request))

def exam2(request) :
    name = request.GET.get('name', "유니코")
    context = {'result' : name}
    return render(request, 'exam2.html', context)

def exam3(request) :
    context = {'number' : 5, "food" : "샌드위치"}
    return render(request, 'exam3.html', context)

def exam4(request) :
    context = {'numbers':[1,2,3,4,5,6]}
    # return render(request, 'exam4.html', context)
    return render(request, 'exam4_1.html', context)

def exam5(request) :
    name = request.GET.get('name', "게스트")
    address = request.GET.get('address', "작성안함")
    context = { 'name':name, 'address':address }
    return render(request, 'exam5.html', context)

def exam6(request) :
    if request.method == 'POST':
        num = int(request.POST['number'])
        context = { 'num' : num*num }
    else :
        context = None
    return render(request, 'exam6.html', context)

def exam7(request):
    foods = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(foods)
    context = {
        'pick': pick,
    }
    return render(request, 'exam7.html', context)

def exam8(request) :
    query = 'q' in request.GET
    if query :
        result = request.GET['q']
    else:
        result = 'q=xxx 형식으로 쿼리를 보내지 않았슈'
    context = {
        'result': result,
    }
    return render(request, 'exam8.html', context)

def exam9(request):
    context = None
    foodstr = ""
    if request.method == 'POST':
        foods = request.POST.getlist("food", "없음")
        for f in foods :
            foodstr += f+" "
        fcolor = request.POST.get("fcolor", "없음")
        year = request.POST.get("year", "없음")
        memo = request.POST.get("memo", "없음")
        birth = request.POST.get("birth", "없음")
        context = {
            'info': {
                'info1' : foodstr,
                'info2': fcolor,
                'info3': year,
                'info4': memo,
                'info5': birth,
            }
        }
    return render(request, 'exam9.html', context)

def exam10(request, name):
    context = {
        'name': name,
    }
    return render(request, 'exam10.html', context)


def exam11(request, name, age):
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'exam11.html', context)


def exam12(request, num1, num2):
    result = num1 * num2
    context = {
        'num1': num1,
        'num2': num2,
        'result': result,
    }
    return render(request, 'exam12.html', context)


def exam13(request):
    foods = ['짜장면', '초밥', '차돌짬뽕', '콩국수']
    empty_list = []
    messages = 'Life is short, You need Python'
    datetime_now = datetime.now()
    context = {
        'foods': foods,
        'empty_list': empty_list,
        'messages': messages,
        'datetime_now': datetime_now,
    }
    return render(request, 'exam13.html', context)


def exam14(request, word, num1, num2):
    if word == '올라프1':
        result = True
    else:
        result = False
    context = {
        'result': result,
        'num1' : num1,
        'num2' : float(num2),
    }
    #return render(request, 'exam14.html', context)
    return render(request, 'exam14_1.html', context)

def exam15(request):
    return render(request, 'exam15.html')


def exam16(request):
    print(request.GET.get('message'))
    msg_list = ['안녕', '방가방가', '하이']
    message = request.GET.get('message')
    context = {
        'message': message,
        'msg_list': msg_list,
    }
    return render(request, 'exam16.html', context)


def exam17(request):
    return render(request, 'exam17.html')


def exam18(request):
    name = request.GET.get('name')
    numbers = range(1, 46)
    pick = sorted(random.sample(numbers, 6))
    context = {
        'name': name,
        'pick': pick,
    }
    return render(request, 'exam18.html', context)

def exam19(request) :
    dt = datetime.now()
    context = {'current_date' : dt}
    return render(request, 'exam19.html', context)
