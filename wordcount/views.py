from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    the_text = request.GET['fulltext']
    print (the_text)

    l = the_text.split()
    c = len(l)

    wordcountdic = {}
    
    for word in l:
        if word in wordcountdic:
            wordcountdic[word] += 1
        else:
            wordcountdic[word] = 1

    sort = sorted(wordcountdic.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', 
    {'fulltext': the_text, 'thecount': c , 'dic': sort})
