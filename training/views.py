
from django.shortcuts import render


def count_of_word(text):
    return len(text.split())

def about(request):
    return render(request, 'This is about page')

def home(request):
    return render(request, 'home.html')

def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    num_of_word = count_of_word(user_text)

    data = {'usertext': user_text,
            'reversedtext': reversed_text,
            'countofword': num_of_word
            }
    return render(request, 'reverse.html', data)