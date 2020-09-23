from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def event(request):
    all_posts = [

    {
        'author':'James',
        'title':'Instagram Reel Actors',
        'content':'Hurry up for!!!! For more Fun',
        'date_posted':'Dec 24,2020 10:00 AM'

    },
    {
        'author':'Tom',
        'title':'FacebBook Live Session',
        'content':'Please Jion Us To more Details',
        'date_posted':'Dec 23,2020 1:00 PM'

    }
    ]
    
    data = {
       'posts':all_posts
    }
    return render(request,'events.html',data)