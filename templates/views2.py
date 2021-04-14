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
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(fullcaps=="on"):
        analyzed = djtext.upper()
        params = {'purpose': 'CHANGED TO UPPERCASE', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (noncaps == "on"):
        analyzed = djtext.lower()
        params = {'purpose': 'changed to lowercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif titlecase == "on":
        analyzed = djtext.title()
        params = {'purpose': 'Title Case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra space remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (sentencecase == "on"):
        analyzed = djtext.capitalize()
        params = {'purpose': 'Sentence case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (altcase == "on"):
        analyzed = [ele.upper() if idx % 2 else ele.lower() for idx, ele in enumerate(djtext)]
        analyzed = "".join(analyzed)
        params = {'purpose': 'aLtErNaTiNg cAsE', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(charcount=="on"):
        analyzed = len(djtext)
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        return render(request,'analyze.html',params)

    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')

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