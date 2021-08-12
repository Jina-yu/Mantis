from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def signup(request):
    return render(request, "signup.html")

def login(request):
    return render(request, "login.html")

def mypage(request):
    return render(request, "mypage.html")

def myinfo_re(request):
    return render(request, "myinfo_re.html")

def myinfo_up(request):
    return render(request, "myinfo_up.html")

def myclass(request):
    return render(request, "myclass.html")

def cash(request):
    return render(request, "cash.html")

def cash_check(request):
    return render(request,"cash_check.html")

def certification(reqeust):
    return render(reqeust, "certification.html")

def certification_check(request):
    return render(request,"certification_check.html")