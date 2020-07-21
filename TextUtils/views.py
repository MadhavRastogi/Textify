# created by me - Madhav

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")


def analyze(request):
    #get text from user

    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlremover = request.POST.get('newlremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    analyzlen = ""

    if removepunc == "on" or fullcaps == "on" or newlremover == "on" or charcounter == "on":
        if removepunc == 'on':
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char
            djtext = analyzed
            analyzed = ""

        if fullcaps == "on":
            for char in djtext:
                analyzed = analyzed + char.upper()
            djtext = analyzed
            analyzed = ""

        if newlremover == "on":
            for char in djtext:
                if char != "\n" and char != "\r":
                    analyzed = analyzed + char
            djtext = analyzed

        if charcounter == "on":
            analyzlen = len(djtext)

        params = {'purpose': 'Result', 'analyzed_text': djtext, 'noc': analyzlen}
        return render(request, 'analyze.html', params)

    else:
        params = {'purpose': 'Please select an operation and try again', 'analyzed_text': djtext, 'noc': analyzlen}
        return render(request, 'analyze.html', params)
