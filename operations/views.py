from django.shortcuts import render

from django.views.generic import View
# Create your views here.

class AdditionView(View):
    def get(self,request, *args, **kwargs):
        return render(request, 'add.html')
    def post(self, request,*args, **kwargs):
        print(request.POST)
        n1 = request.POST.get("num1")
        n2 = request.POST.get("num2")
        result = int(n1)+ int(n2)
        print(result)
        return render(request,'add.html', {"data": result})
    
class SubractionView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'sub.html')
    def post(self,request, *args, **kwargs):
        n1 = request.POST.get("num1")
        n2 = request.POST.get("num2")
        result = int(n1)- int(n2)
        print(result)
        return render(request,'sub.html', {"data", result})
class DivisonView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'div.html')
    def post(self,request, *args, **kwargs):
        n1 = request.POST.get("num1")
        n2 = request.POST.get("num2")
        result = int(n1)// int(n2)
        print(result)
        return render(request,'div.html',{"data": result} )

class LeapyearView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'leapyear.html')
    def post(self, request, *args, **kwargs):
        result = ""
        year = int(request.POST.get("year"))
        if year %100 ==0 and year%400 == 0 or year%100!=0 and year%4 ==0:
            result = f"{year} is a leap year"
        else:
            result = f"{year} is not a leap year"
        return render(request, 'leapyear.html', {"data": result})
