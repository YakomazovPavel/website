from django.shortcuts import render


def indexA(request):
    return render(request, 'home_page/indexA.html')
    
    
def indexB(request):
    return render(request, 'home_page/indexB.html')
    
    
def indexC(request):
    return render(request, 'home_page/indexC.html')

