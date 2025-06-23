from django.contrib.auth.models import User
from django.db import models
from django.forms import forms
from django.utils import timezone
from django.urls import reverse



class Category(models.Model):
    objects = None
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)



class News(models.Model):



    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"


    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')

    # news classi bilan category classini bog'laymiz'
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    upload_time = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=2,

                              choices=Status.choices,
                              default=Status.Draft)

    view_count = models.IntegerField(default=1)
    # PUBLISHED - NASHR QILINGANDAGI HOLAT
    # DRAFT - QORALAMA



# newsni published qilinganlarini chiqarish uchun

    object = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ["-publish_time"] #4 3 2 1 yangilik chiqishi ['publish_time'] 1 2 3 4

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_detail_page", args=[self.slug])

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.email


# class SubsicriptionForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharFiled()
#     email = forms.EmailField()


class Comment(models.Model):
    news = models.ForeignKey(News,
                             on_delete=models.CASCADE,
                             related_name="comments")
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="comments")
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering= ['created_time']

    def __str__(self):
        return f"Comment- {self.body} by {self.user}"