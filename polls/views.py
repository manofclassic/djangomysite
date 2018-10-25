from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question, Choice


def data(request, email, number):
    value = request.GET['user_name']
    return HttpResponse(value + email + str(number))


def vote(request):
    choice = request.POST['choice']
    c = Choice.objects.get(pk=choice)


def detail(request, id):
    question =Question.objects.get(id=id)
    return render(request, 'polls/detail.html', {'item':question})


def add_question(request):
    text = request.POST['text']

    # q = Question(
    #     question_text = text,
    #     pub_date-timezone.now()
    # q.save()
    return HttpResponse('입력완료')


def index(request):
    list = Question.objects.all()
    return render(
        request,
        'polls/index.html',
        {'question':list})


def result(request,id):
    question = Question.objects.get(pk=id)
    return render(request,'polls/result.html', {'question':question})
