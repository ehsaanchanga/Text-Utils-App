from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    #GET THE TEXT
    return render(request,'index.html')
def analyze(request):
    #check checqbox value
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')



   # check which checkbox is on
    if removepunc == "on":

        punctuations='''!()-[]{};:'"\,<>.?#$%/@^&*'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed + char
        params={'purpose':'removed punctuations','analyzed_text':analyzed}
        djtext=analyzed
        
    if(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params={'purpose':'changed to uppercase','analyzed_text':analyzed}
        djtext=analyzed
        
    
    if(newlineremover=='on'):
         analyzed=""
         for char in djtext:
             if char!="\n" and char!="\r":
                analyzed = analyzed + char
         params={'purpose':'removed newlines','analyzed_text':analyzed}
         djtext=analyzed
         

    if(extraspaceremover=='on'):
         analyzed=""
         for index,char in enumerate(djtext):
             if not(djtext[index]==" " and djtext[index+1]==" "):
                  analyzed = analyzed + char
         params={'purpose':'removed extra spaces','analyzed_text':analyzed}
         djtext=analyzed
         

    if(charcount=='on'):
         params={'purpose':'NO of characters','analyzed_text':len(djtext)}
         
    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on" and charcount!="on"):
        return HttpResponse(" please select any operation")

    return render(request,'analyze.html',params)
    
    