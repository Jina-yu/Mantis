from django.shortcuts import render

# Create your views here.

def mentoring(request):
    return render(request, "mentoring.html")
    
def event(request):
    return render(request, "event.html")

def event_detail(request):
    return render(request, "event_detail1.html")

def event_up(request):
    return render(request, "event_up.html")

def event_re(request):
    return render(request, "event_re.html")

def lecture(request):
    return render(request, "lecture.html")    

def class1(request):
    return render(request, "class1.html")

def class1_play(request):
    return render(request, "class1_play.html")

def mentor(request):
    return render(request, "mentor.html")