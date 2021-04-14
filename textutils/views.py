#I have created this file - Shyam Makwana
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('textdata','default')

    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    noncaps = request.POST.get('noncaps', 'off')
    titlecase = request.POST.get('titlecase', 'off')
    sentencecase = request.POST.get('sentencecase', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    altcase = request.POST.get('altcase', 'off')

    purpose = ""
    flag=0
    analyzed = ""

    if removepunc == "on":
        flag=1
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        purpose = purpose + 'Removed Punctuations '
        djtext = analyzed

    if (noncaps == "on"):
        flag = 1
        analyzed = djtext.lower()
        purpose = purpose + 'changed to lowercase '
        djtext = analyzed

    if(fullcaps=="on"):
        flag = 1
        analyzed = djtext.upper()
        purpose = purpose + 'CHANGED TO UPPERCASE '
        djtext = analyzed

    if titlecase == "on":
        flag = 1
        analyzed = djtext.title()
        purpose = purpose + 'Title Case '
        djtext = analyzed

    if (sentencecase == "on"):
        flag = 1
        analyzed = djtext.capitalize()
        purpose = purpose + 'Sentence case '
        djtext = analyzed

    if (altcase == "on"):
        flag = 1
        analyzed = [ele.upper() if idx % 2 else ele.lower() for idx, ele in enumerate(djtext)]
        analyzed = "".join(analyzed)
        purpose = purpose + 'aLtErNaTiNg cAsE '
        djtext = analyzed

    if (newlineremover == "on"):
        flag = 1
        analyzed = djtext.replace('\n','')
        # for char in djtext:
        #     if char != "\n" and char != "\r":
        #         analyzed = analyzed + char
        purpose = purpose + 'Removed NewLines '
        djtext = analyzed
        print(djtext)

    if (extraspaceremover == "on"):
        flag = 1
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        purpose = purpose + 'Extra space remover '
        djtext = analyzed

    if(flag==0):
        return HttpResponse('Error! Select any Utils')

    else :
        params = {'purpose': purpose, 'analyzed_text': djtext}
        return render(request, 'analyze.html', params)


def website(request):
    s='''<h2>Navigation Bar <br> </h2>
    <h2><a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
    <a href="https://www.facebook.com/"> Facebook </a> <br>
    <a href="https://www.flipkart.com/"> Flipkart </a> <br>
    <a href="https://www.hindustantimes.com/"> News </a> <br>
    <a href="https://www.google.com/"> Google </a> <br></h2>'''
    return HttpResponse(s)

# def capfirst(request):
#     return HttpResponse("Capitalize First")
#
# def newlineremove(request):
#     return HttpResponse("New Line Remove")
#
# def spaceremove(request):
#     return HttpResponse("Space Remover")
#
# def charcount(request):
#     return HttpResponse("Char Count")