from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

def operation(request):
    num1=int(request.GET['num1'])
    num2=int(request.GET['num2'])

    if request.GET['op']=='plus':
        re=num1+num2
    elif request.GET['op']=='minus':
        re=abs(num1-num2)
    elif request.GET['op']=='mul':
        re=num1*num2
    elif request.GET['op']=='divide':
        re=num1/num2
    return render(request,'index.html',{'result':re})
