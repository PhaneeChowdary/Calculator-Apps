from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def submit(request):
    s = request.GET['query']
    print(s)
    try:
        ans = eval(s)
        mydict = {
            's' : s,
            'ans' : ans,
            'error': False,
            'result' : True
        }
        return render(request, 'home.html', context = mydict)
    except:
        mydict['error'] = True
        mydict['result'] = False
        return render(request, 'home.html', context = mydict)
