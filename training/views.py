
from django.shortcuts import render

def about(request):
    return render(request, 'This is about page')

def home(request):
    return render(request, 'home.html')

def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    number_of_word = len(user_text.split())

    data = {'usertext': user_text,
            'reversedtext': reversed_text,
            'count_of_word': number_of_word
            }
    return render(request, 'reverse.html', data)