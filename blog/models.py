# Third party imports.
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill,Transpose
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True,unique=True,max_length=111)
    content =  models.TextField()
    image =  models.ImageField(upload_to='post_images')
    image_thumbnail = ImageSpecField(source='image',
                                      processors=[ 
                                        Transpose(),
                                        ResizeToFill(1000, 500)
                                        ],
                                      format='JPEG',
                                      options={'quality': 70})

    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes',blank=True)
    tagged_users = models.ManyToManyField(User, related_name='tagged_users',blank=True)

    @property
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

            
    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'slug': self.slug})

    def whatsapp_share_url(self):
        url = "https://wa.me/?text=http%3A//nccbuddy.com"+self.get_absolute_url()
        return url

    def facebook_share_url(self):
        url = "https://www.facebook.com/sharer/sharer.php?u=http%3A//nccbuddy.com"+self.get_absolute_url()
        return url

    def twitter_share_url(self):
        url = "https://twitter.com/intent/tweet?text=http%3A//nccbuddy.com"+self.get_absolute_url()
        return url
        

REASON = [
    
    ('SPAM','SPAM'),
    ('INAPPROPRIATE','INAPPROPRIATE'),
    
]


class PostReport(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reason = models.CharField(max_length=10,choices=REASON)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_reported = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.post.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment

class Notification(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User,on_delete=models.CASCADE, related_name='receiver')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    action = models.CharField(max_length=50, blank=True)
    read = models.BooleanField(default=False)    
    timestamp = models.DateTimeField(default=timezone.now)


# SIGNALS
@receiver(post_save,sender=Post)
def post_mentioned_notify(sender, instance, *args, **kwargs):
    sender = User.objects.get(pk=instance.author.pk)
    post = Post.objects.get(pk=instance.pk)
    string = instance.content
    poss_users = [i  for i in string.split() if i.startswith("@")]
    poss_users_list = []
    for user in poss_users:
        poss_users_list.append(user[1:])

    for username in poss_users_list:
        try:
            get_user = User.objects.get(username=username)
        except:
            continue
        if get_user in instance.tagged_users.all():
            continue
        elif get_user == sender:
            continue
        else:
            instance.tagged_users.add(get_user)
            notify = Notification.objects.create(sender=sender,receiver=get_user,post=post,action="mentioned you in post")


@receiver(post_save,sender=Comment)
def comment_added_notify(sender, instance, *args, **kwargs):
    sender = User.objects.get(pk=instance.author.pk)
    post = Post.objects.get(pk=instance.post.pk)
    receiver = User.objects.get(pk=instance.post.author.pk)
    if receiver == sender:
        pass
    else:
        notify = Notification.objects.create(sender=sender,receiver=receiver,post=post,action="commented on your post")


@receiver(pre_save,sender=Post)
def sulg_generator(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)