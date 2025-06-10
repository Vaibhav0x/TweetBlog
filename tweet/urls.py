from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('<int:tweet_id>/like/', views.toggle_like, name='toggle_like'),
    path('register/', views.register, name='register'),
    path('search/', views.search_tweets, name='search_tweets'),
    path('faq/', views.faq_list, name='faq'),
    path('about/',views.about_page,name='about_rweet'),
    path('pricing/', views.pricing_view, name='pricing_view'),
    path('features/',views.features_view,name='features_rweet'),
    
    # Catch-all pattern for any other URLs under /tweet/
    path('<path:unmatched>/', views.redirect_to_tweet_list),
]
