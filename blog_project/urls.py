from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views

admin.site.site_header = settings.ADMIN_SITE_HEADER


urlpatterns = [
    path('admin/site/', admin.site.urls), 
    path('', include('blog.urls', namespace='blog')), 
    path('account/register/', user_views.register, name='register'),
    path('account/profile-update/',user_views.updateProfile,name='profile-update'),
    path('account/follow-unfollow/<int:pk>/',user_views.userFollowUnfollow,name="follow-unfollow"),
    path('account/password-change/', user_views.change_password, name='change-password'),

    path('account/login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'), 
    path('account/logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),  
    path('account/password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),  
    path('account/password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),  
    path('account/password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),  
    path('account/password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),  
    path('account/community/', include('footer.urls', namespace='community')),
    path('<str:username>/', user_views.profile, name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'footer.views.error_404_view'