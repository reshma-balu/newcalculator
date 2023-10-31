from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from operations.forms import OperationForm
class AdditionView():
    def get(self,request,*args,**kwargs):
        form=OperationForm()
        return render(request,"add.html",{"Form":form})

    def post(self,request,*args,**kwargs):
        form=OperationForm()
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            res=n1+n2
            return render(request,"add.html",{"result":res})
        else:
            return render(request,"add.html",{"Form":form})



