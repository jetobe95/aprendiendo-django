from django.shortcuts import render,HttpResponse
def index(req):
  return render(req,'index/index.html')
