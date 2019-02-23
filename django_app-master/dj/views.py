from django.shortcuts import render

from django.template import loader

from .models import Question

# Create your views here.
from django.http import HttpResponseNotFound
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

questionare = {
    'test_one': [
        'Huh?',
        'Seriously?',
        'Do you?',
        'Would you?'
    ],
    'test_two': [
        "Sure?"
        "Okay?"
        "Right?"
        "Correct?"
    ],
    'test_three': [
        "Why?"
        "How?"
        "When?"
        "Was?"
    ]
}
# Create your views here.
def test_one(request,*args):
     if request.GET:
        name = request.GET["name"]
        if name in questionare.keys():
            return HttpResponse(questionare[name][0]+"  "+questionare[name][1]+"  "+questionare[name][2]+"   "+questionare[name][3])
        else:
            return HttpResponseNotFound("Name Error,try again")

def test_two(request,*args):
    obj = Question()
    if(request.GET):
            user = request.GET["name"]
            obj = Question.objects.get(id=user)
            return HttpResponse(obj.questions)
    return HttpResponse("Welcome to test_two ")



def test_three(request):
    obj=Question()
    #if request.method=="GET":
    if request.method=='POST':
        h=request.POST["name"]
        obj=Question.objects.get(id=h)
        return render(request,"index.html",{"tag": obj}) 
    return render(request,"index.html",{"tag": obj})