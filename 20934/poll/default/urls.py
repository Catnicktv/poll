from django.urls import path
# from .views import poll_list, PollList, PollView, PollVote, PollCreate
from .views import *

urlpatterns = [
    path('list/', poll_list),
    path('', PollList.as_view()),
    path('<int:pk>/', PollView.as_view()),
    path('option/<int:oid>/', PollVote.as_view()),
    path('create/', PollCreate.as_view()),
    path('<int:pk>/edit/', PollEdit.as_view()),
    path('<int:pk>/delete/', PollDelete.as_view()),
    path('<int:pk>/add/', OptionCreate.as_view()),
    path('option/<int:oid>/edit/', OptionEdit.as_view()), 
    path('option/<int:oid>/delete/', OptionDelete.as_view()),
]