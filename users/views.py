from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm,ReportUserForm
from blog.models import Post, Notification
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!\
                            You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    context = {'form': form}
    template_name = 'users/register.html'
    
    return render(request, template_name, context)


# @login_required
def profile(request,username=None):
    report_form = ReportUserForm()
    user =  get_object_or_404(User,username=username)
    post_list = Post.objects.filter(author=user).order_by('-id')
    post_count = post_list.count()
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 4)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)    
    
    context = {
        'report_form':report_form,
        'posts':posts,
        'user_id':user,
        'post_count':post_count,
    }
    template_name = 'users/profile.html'

    return render(request, template_name, context)

@login_required
def updateProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile',username=request.user.username)
        else:
            messages.error(request, f'Username already exists or in use!')
            return redirect('profile-update')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form,
        }
        template_name = 'users/update_profile.html'

        return render(request, template_name, context)


@login_required
def userFollowUnfollow(request,pk=None):
    current_user = request.user
    other_user = User.objects.get(pk=pk)

    if other_user not in current_user.profile.follows.all():
        current_user.profile.follows.add(other_user)
        other_user.profile.followers.add(current_user)
        
        notify = Notification.objects.create(sender=current_user,receiver=other_user,action="started following you.")

    else:
        current_user.profile.follows.remove(other_user)
        other_user.profile.followers.remove(current_user)
    return redirect('profile',username=other_user.username)


@login_required
def  change_password(request):
    if request.method == 'POST':
        form  =  PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile',username=request.user.username)
        else:
            return redirect('change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request, 'users/change_password.html',args)