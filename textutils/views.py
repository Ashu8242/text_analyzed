from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse('Home')
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')

    if removepunc == 'on':
        # analyzed = djtext
        punctuations = '''!"#$%&'()*+,"-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (spaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char
            #     pass
            # else:
        params = {'purpose': 'Removed new spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (removepunc !='on' and fullcaps !='on' and newlineremover !='on' and spaceremover !='on'):
        return HttpResponse('Please select any operation , Try again!')
    return render(request,'analyze.html',params)


# def capfirst(request):
#     return HttpResponse('Capatalize First')
#
# def newlineremove(request):
#     return HttpResponse('Newline Remove First')
#
# def spaceremove(request):
#     return HttpResponse('Space Remover <a href = "/">back</a>')
#
# def charcount(request):
#     return HttpResponse('Charcount')
