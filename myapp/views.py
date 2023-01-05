#THIS is created by me
from django.http import HttpResponse
from django.shortcuts import render
def ragu(request):
    
    return render(request,"index.html",{"NAME":"SACHETAN","AGE":"18"})
def removpunc(request):
    text=request.POST.get('text','default')
    punc=request.POST.get('analyze','off')
    capital=request.POST.get('capital','off')
    space=request.POST.get('space','off')
    newline=request.POST.get('new','off')
    print(text)
    print(punc)
    print(capital)
    print(space)   
    print(newline) 
    janu=''
    if(punc=='on'or capital=='on'or space=='on'):
        if(punc=='on'):
            c='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
            for t in text:
                if t not in c:
                    janu=janu+t
            text=janu
        if(capital=='on'):
            janu=text.upper()
            text=janu
        if(newline=='on'):
            janu=''
            for char in text:
                if char!='\n' and char!='\r':
                    janu=janu+char
                    
            text=janu        
        if(space=="on"):
            janu=''
            for i,j in enumerate(text):
                if(not(text[i]==" "and text[i+1]==" ")):
                  janu=janu+j  
            text=janu 
            print(text)
    else:
        return HttpResponse('''<style>*{background-color:black;}</style><h1 style="text-align:center;background-color:black;color:red;padding:300px">ERROR</h1>''')
          
    return render(request,"analyse.html",{"nopanc":text})