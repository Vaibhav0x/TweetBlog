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
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            
            # Log in the user, specifying the backend explicitly
            login(request, user, backend='tweet.backends.EmailOrUsernameBackend')

            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
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

def faq_list(request):
    faqs = [
        {'question': 'What is RweetBlog?', 'answer': 'RweetBlog is a micro-blogging platform where users can post short tweets with images and thoughts.'},
        {'question': 'How do I create an account?', 'answer': 'Click on the "Register" button on the top right corner and fill in your details.'},
        {'question': 'Is RweetBlog free to use?', 'answer': 'Yes, RweetBlog is completely free to use.'},
        {'question': 'Can I edit a Rweet after posting?', 'answer': 'Yes, you can edit your post after posting on Rweetblog.'},
        {'question':'Can I delete a rweet after posting?','answer':'Yes, you can delete your rweet if you want to delete.'},
        {'question':'Can I reset my password after register the account','answer':'Yes, you can reset your password using reset password button and check the mail and click on mail link and reset the password details'},
        # Add more as needed
    ]
    return render(request,'faq.html',{'faqs': faqs})

def about_page(request):
    return render(request,'about.html')

def pricing_view(request):
    pricing_plans = [
        {
            'title': 'Free',
            'price': '0',
            'features': [
                'Create Rweets',
                'Upload 1 image per post',
                'Basic user support'
            ],
        },
        {
            'title': 'Pro',
            'price': '5',
            'features': [
                'Unlimited Rweets',
                'Upload up to 3 images per post',
                'Priority support',
            ],
        },
        {
            'title': 'Premium',
            'price': '10',
            'features': [
                'All Pro features',
                'Schedule Rweets',
                'Advanced analytics',
            ],
        }
    ]
    return render(request, 'pricing.html', {'plans': pricing_plans})

def features_view(request):
    features = [
        {'title': 'Post Rweets', 'description': 'Share short, impactful messages with your followers.'},
        {'title': 'Image Uploads', 'description': 'Attach images to your Rweets to express yourself visually.'},
        {'title': 'User Profiles', 'description': 'Create and customize your profile for others to discover.'},
        {'title': 'Particular User View', 'description': 'To view all the rweets but only update, delete your rweets.'},
        {'title': 'Rest Password', 'description': 'Reset your password using gmail link.'},
        {'title': 'Responsive Design', 'description': 'Enjoy a seamless experience on both desktop and mobile.'},
    ]
    return render(request, 'features.html', {'features': features})