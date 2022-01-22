# render: 파이썬 데이터 템플릿에 적용하여 HTML로 변환
# get_object_or_404: 404 오류 출력(요청한 페이지가 없는 경우)
from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    """
    pybo 목록 출력
    """
    # 질문 목록 데이터 '-create_date'는 작성일시 역순(게시물을 최신으로 확인)
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}

    # 'pybo/question_list.html' -> 템플릿 -> config/settings.py에 추가
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    # 오류를 404오류로 출력
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)