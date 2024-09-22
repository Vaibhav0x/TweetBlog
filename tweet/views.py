from django.shortcuts import render
from .models import Tweet
from django.db.models import Q
from .forms import TweetForm,UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

def index(request):
    return render(request,'index.html')


# all tweet list
def tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})

#create tweets
@login_required
def tweet_create(request):
    if request.method=='POST':
        form=TweetForm(request.POST,request.FILES)
        if form.is_valid():
         tweet=form.save(commit=False)
         tweet.user=request.user
         tweet.save() 
         return redirect('tweet_list')  
    else:
        form=TweetForm()
    return render(request,'tweet_form.html',{'form':form})

# edit tweet
@login_required
def tweet_edit(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=='POST':
        form=TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form=TweetForm(instance=tweet)
    return render(request,'tweet_form.html',{'form':form})

# delete tweet
@login_required
def tweet_delete(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=='POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})


#register the user
def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form=UserRegistrationForm()

    return render(request,'registration/register.html',{'form':form})

def search_tweets(request):
    query = request.GET.get('q', '')
    tweets=[]
    if query:
        tweets = Tweet.objects.filter(
            Q(text__icontains=query) | Q(user__username__icontains=query)
          )  # Filter based on the search query on text or username
    else:
        tweets=[]
        tweets = Tweet.objects.all()

    return render(request, 'search_results.html', {'tweets': tweets, 'query': query})

def redirect_to_tweet_list(request, unmatched):
    # Redirect to the tweet list page
    return redirect('tweet_list')