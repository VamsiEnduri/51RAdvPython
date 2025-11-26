from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"home.html")

def todos(request):
    return render(request,"todo.html")
def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")    
# def home(request):
#     return HttpResponse("this is homeview")
# def about(request):
#     return HttpResponse("this is about view")    

# def contact(request):
#     return HttpResponse("this is contact view") 
