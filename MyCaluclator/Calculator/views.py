from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.
def home(requests):
    return render(requests,'Calculator/home.html')
def result(requests):
    op=requests.GET['operator']
    v3=requests.GET['value1']
    v4=requests.GET['value2']
    v1=float(v3)
    v2=float(v4)
    if(op=='+'):
        ans=v1+v2
    elif (op=='-'):
        ans=v1-v2
    elif(op=='*'):
        ans=v1*v2
    elif(op=='/'):
        ans=v1/v2
    return render(requests,'Calculator/result.html',{'answer':ans})
