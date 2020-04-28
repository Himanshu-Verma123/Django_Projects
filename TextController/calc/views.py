
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request,"index.html")

def newpage(request):
    return render(request,"signup.html")
def analyze(request):
    #get the text
    djtext=request.POST.get('text','default')
    remove_punc=request.POST.get("remove_punc","off")
    fullcaps=request.POST.get("fullcaps","off")
    newlineremover=request.POST.get("newlineremover","off")
    extraspaceremover=request.POST.get("extraspaceremover","off")
    charcount=request.POST.get("charcount","off")
    #checkbox values
    analyzed=""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    #Check which checkbox is on!
    if remove_punc=="on":
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char

        params={"purpose":"Removed Punctuations","Analyzed_text":analyzed}
        #return render(request,'analyze.html',params)
        djtext=analyzed
    if(fullcaps=="on"):

        a=""
        for char in djtext:
            a=a+char.upper()
        params={"purpose":"Changed to uppercase","Analyzed_text":a}
        #return render(request,'analyze.html',params)
        djtext=a

    if(newlineremover=="on"):
        a=""
        for char in djtext:
            if char!="\n" and char!="\r":
                a=a+char
        params={"purpose":"Removed new line","Analyzed_text":a}
        #return render(request,'analyze.html',params)
        djtext=a
    if(extraspaceremover=="on"):
        a=""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                a=a+char    
        params={"purpose":"Removed new line","Analyzed_text":a}

        djtext=a
    if(charcount=="on"):
        d={}
        for index,char in enumerate(djtext):
            a=djtext.count(char) 
            d[char]=a
        params={"purpose":"character counter","Analyzed_text":d}
        
    if (remove_punc!="on") and (fullcaps!="on") and (newlineremover!="on") and (extraspaceremover!="on") and (charcount!="on"):
        return HttpResponse("""
        <h1>Please on any operation so Try again!</h>
        
        
        """)
    
    
    return render(request,'analyze.html',params)

    
        



        