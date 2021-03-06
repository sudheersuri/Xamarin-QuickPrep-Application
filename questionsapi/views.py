from django.shortcuts import render, redirect
from .models import Questions,subjects
from .forms import QCreate,SubCreate
from django.http import JsonResponse,HttpResponse
import json

def login(request):
    return render(request,'login.html')


def angulartest(request):
    return render(request,'angulartest.html')

def allsubjects(request):
    allsubs=subjects.objects.all()
    subs=[]
    for x in allsubs:
        subs.append({'subject':x.subjectname})
    return JsonResponse(subs,safe=False)

def editor(request):
    allquestions = Questions.objects.all()
    resarray=[]
    for x in allquestions:
        resarray.append({'id':x.id,'question':x.question,'answer':x.answer,'sid':x.subject_id})
    return render(request,'editor.html',{'res':resarray})


def subeditor(request):
    allsubs = subjects.objects.all()
    resarray=[]
    for x in allsubs:
        resarray.append({'id':x.id,'subject':x.subjectname})
    return render(request,'subeditor.html',{'res':resarray})

def editquestion(request):
    qid=request.POST["qid"]
    q=request.POST["q"]
    a=request.POST["a"]
    sid=request.POST["sid"]
    selected = Questions.objects.get(id=qid)
    selected.question=q
    selected.answer=a
    selected.subject_id=sid
    selected.save()
    return redirect('/questionsapi/editor/')

def editsubject(request):
    sid=request.POST["sid"]
    s=request.POST["s"]
    selected = subjects.objects.get(id=sid)
    selected.subjectname=s
    selected.save()
    return redirect('/questionsapi/subeditor/')


def checklogin(request):
    passgiven=request.POST["pass"]
    if(passgiven=="sudheer95"):
        subjectlist=[]
        allsubs=subjects.objects.all()
        for x in allsubs:
             subjectlist.append(x.subjectname)
        return render(request,'home.html',{'sub':subjectlist})
    else:
        return HttpResponse("Wrong Password")

def addtodb(request):
        subname=request.POST["subopts"]
        ques=request.POST["q"]
        ans=request.POST["a"]
        subobj=subjects.objects.get(subjectname=subname)
        quesobj=Questions.objects.create(question=ques,answer=ans,subject_id=subobj.id)
        allquestions = Questions.objects.all()
        resarray=[]
        for x in allquestions:
            resarray.append({'question':x.question,'answer':x.answer})
        return JsonResponse(resarray,safe=False)

def addsubname(request):
    subname=request.POST["subname"]
    sub=subjects.objects.create(subjectname=subname);
    return HttpResponse("Subject got added successfully")

def displayques(request):
    subname=request.GET["sub"]
    subid=subjects.objects.get(subjectname=subname)
    subquestions=Questions.objects.all().filter(subject_id=subid)
    qarr=[]
    for x in subquestions:
        qarr.append({'question':x.question,'answer':x.answer})
    return JsonResponse(qarr,safe=False)
