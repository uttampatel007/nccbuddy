from django import forms

from .models import Comment, PostReport, Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title','content','image']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['comment']

class ReportPostForm(forms.ModelForm):
	class Meta:
		model = PostReport
		fields = ['reason']