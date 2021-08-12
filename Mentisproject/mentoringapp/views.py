from django.shortcuts import render

# Create your views here.

def mentoring(request):
    return render(request, "mentoring.html")

def mentor(request):
    return render(request, "mentor.html")

def apply(request):
    return render(request, "apply.html")

def apply_check(request):
    return render(request, "apply_check.html")

def qna(request):
    return render(request, "qna.html")

def column(request):
    return render(request, "column.html")

def column_write(request):
    return render(request, "column_write.html")

def column_re(request):
    return render(request, "column_re.html")

def column_detail1(request):
    return render(request, "column_detail1.html") 
  

def column_coment_re(request):
    return render(request, "column_coment_re.html") 