from django.shortcuts import render

# Create your views here.
def do_code_1(request):
    return render(request,'myapp/myapp_1.html',{
        'title':'do coding form start',
        'language':'java'
    })

def do_code_2(request):
    return render(request,'myapp/myapp_2.html',{
        'title':'do coding form end',
        'language':'python'
    })
