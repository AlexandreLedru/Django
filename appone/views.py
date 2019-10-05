from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from appone.models import User


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))


def user_list(request):
    users = []
    for u in User.objects.all():
        users.append(u.username + " : " + u.password)

    body = '<br/>'.join(users)
    return HttpResponse(body)


def user_add(request, username, password):
    user = User(username=username, password=password)
    user.save()
    return HttpResponse("Song saved at id={}".format(user.pk))

# Create your views here.
