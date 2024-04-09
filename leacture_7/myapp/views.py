from django.shortcuts import render

# Create your views here.
def learn_java(request):
    data={
        'course_name':'Java',
        'price':'1200'
    }
    return render(request,'myapp/home.html',data)
