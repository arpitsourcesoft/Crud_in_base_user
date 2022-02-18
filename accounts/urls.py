from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name = 'index'), 
    path('home/', views.home),  
    path('showformdata', views.showformdata),
    path('signup/', views.showformdata, name = 'signup'),
    path('login/', views.user_login, name= 'login'),
    path('detail<int:pk>', views.show_user, name= 'detail'),
    
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
]