from django.shortcuts import render

# Create your views here.
def begin_numbers(request)->render:
    template_='begin_numbers.html'
    context={}
    return render(request,template_,context=context)

def begin_uppercase_letters(request)->render:
    template_='begin_uppercase_letters.html'
    context={}
    return render(request,template_,context=context)