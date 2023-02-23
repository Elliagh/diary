from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h2>hello world</h2>')

def add_task(request):
    return HttpResponse('<h3>Добавить задачу</h2>')

def get_result(request):
    return HttpResponse('<h2>Получить сводку</h2>')

def clear_tasks(request):
    return HttpResponse('<h2>Очистить список</h2>')

def delete_task(request):
    return HttpResponse('<h2>Удалить задачу</h2>')
