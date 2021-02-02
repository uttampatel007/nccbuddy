from django.urls import path

from .views import ProfileDetailView, UserCreateView, LoginView

app_name = "api"

urlpatterns = [
	path('profile/<int:pk>/',ProfileDetailView.as_view(), name="profile-details"),
	path('users/create/',UserCreateView.as_view(),name="user-create"),
	path('users/login/',LoginView.as_view(),name="user-login"),
]