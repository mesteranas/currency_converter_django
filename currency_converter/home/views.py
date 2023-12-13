from . import google_currency
from django.shortcuts import render

# Create your views here.
def home_(r):
    return render(r,"home.html")
def currency(r):
    result=""
    if r.method=="POST":
        result=google_currency.convert(r.POST["From"],r.POST["To"],int(r.POST["Value"]))
    return render(r,"currency.html",{"currencies":google_currency.CODES.items(),"Result":str(result)})
def Contect(r):
    return render(r,"contect.html")
def about(r):
    return render(r,"about.html")