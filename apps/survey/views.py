from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'survey/index.html')

def result(request):
    if 'num' not in request.session:
        request.session['num'] = 0
    request.session['num'] += 1
    
    return render(request, 'survey/result.html')

def process(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['lang'] = request.POST['lang']
        request.session['comment'] = request.POST['comment']
    return redirect('/result')

# Create your views here.
def back(request):
    return redirect('/')