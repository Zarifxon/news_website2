from http.client import HTTPResponse

from hitcount.views import HitCountMixin
from hitcount.utils import get_hitcount_model

from .utils import latin_to_cyrillic, cyrillic_to_latin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404


from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView

from .custom_permissions import OnlyLoggedSuperUser
from .forms import ContactForm, CommentForm
from .models import News, Category, Contact


# Create your views here.


def news_list(request):
    news_list = News.published.all()
    context ={
        "news_list":news_list
    }
    return render(request, 'news/news_list.html', context)



def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {}
    # Hitcount logis
    hit_count = get_hitcount_model().objects.get_for_object(news)
    hits = hit_count.hits
    hitcontext = context['hitcount'] = {'pk': hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits = hits + 1
        hitcontext['hit_counted'] = hit_count_response.hit_counted
        hitcontext['hit_message'] = hit_count_response.hit_message
        hitcontext['total_hits'] = hits

    # news.view_count = news.view_count +1
    # news.save()
    comments = news.comments.filter(active=True)
    comment_count = comments.count()
    news_comment = None
    if request.method=="POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.news=news
            new_comment.user= request.user
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {
        "news" : news,
        "comments":comments,
        "new_comment":news_comment,
        "comment_count":comment_count,
        "comment_form":comment_form
    }

    return render(request, 'news/news_detail.html', context)


# def homePageView(request):
#     local_news =News.objects.all().filter(category__name="Mahalliy").order_by("-publish_time")[1:6]
#     local_one = News.objects.all().filter(category__name="Mahalliy").order_by("-publish_time")[:1]
#     news_list = News.objects.all().filter(status=News.Status.Published).order_by("-publish_time")[:5]
#     categories = Category.objects.all()
#     context = {
#         "news_list": news_list,
#         "categories": categories,
#         "local_news": local_news,
#         "local_one":local_one,
#     }
#     return render(request, 'news/home.html', context)

class HomePageView(ListView):
    model = News
    template_name = "news/home.html"
    context_object_name= 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().filter(status=News.Status.Published).order_by("-publish_time")[:5]
        # mahalliy yangiliklar
        context['local_one'] = News.published.all().filter(category__name="Mahalliy").order_by("-publish_time")[:1]
        context['local_news'] = News.published.all().filter(category__name="Mahalliy").order_by("-publish_time")
        context['mahallliy_xabarlar'] = News.published.all().filter(category__name="Mahalliy").order_by("-publish_time")[:5]

        #xorij yangiliklari
        context["xorij_one"] = News.published.all().filter(category__name="Xorij").order_by("-publish_time")[:1]
        context["xorij_news"]= News.published.all().filter(category__name="Xorij").order_by("-publish_time")
        context['xorij_yangiliklari'] = News.published.all().filter(category__name="Xorij").order_by("-publish_time")[:5]

        #texnologiya yangiliklari
        context['texnologiya_one']= News.published.all().filter(category__name="Texnologiya").order_by("-publish_time")[:1]
        context['texnologiya_news']= News.published.all().filter(category__name="Texnologiya").order_by("-publish_time")
        context['texnologiya_yangiliklari']= News.published.all().filter(category__name="Texnologiya").order_by("-publish_time")[:5]

        #sport_yangiliklari
        context['sport_one'] = News.published.all().filter(category__name="Sport").order_by("-publish_time")[:1]
        context['sport_news'] = News.published.all().filter(category__name="Sport").order_by("-publish_time")
        context['sport_yangiliklari'] = News.published.all().filter(category__name="Sport").order_by("-publish_time")[:5]



        return context

# def contactPageView(request):
#     form = ContactForm(request.POST)
#     if request.method=="POST" and form.is_valid():
#         form.save()
#         return HTTPResponse("<h2> Biz bilan bog'langaningiz uchun rahmat </h2>")
#     context = {
#         "form": form
#     }
#     return render(request, 'news/contact.html', context)




class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            "form": form
        }
        return render(request, "news/contact.html", context)


    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method=="POST" and form.is_valid():
            form.save()
            return HTTPResponse("<h2> Biz bilan bog'langaningiz uchun rahmat </h2>")
        context = {
            "form":form
        }
        return render(request, "news/contact.html", context)


def page404View(request):
    context = {

    }
    return render(request, 'news/404.html', context)



class LocalPageView(ListView):
    model = News
    template_name = "news/mahalliy.html"
    context_object_name = "maxalliy_yangiliklar"


    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Mahalliy")
        return news

class XorijPageView(ListView):
    model = News
    template_name = "news/xorij.html"
    context_object_name = "xorij_yangiliklari"


    def get_queryset(self):
         news = self.model.published.all().filter(category__name="Xorij")
         return news


class SportPageView(ListView):
    model = News
    template_name = "news/sport.html"
    context_object_name = "sport_yangiliklari"

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Sport")
        return news

class TechnologyPageView(ListView):
    model = News
    template_name = "news/technology.html"
    context_object_name = "texnologiya_yangiliklari"

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Texnologiya")
        return news



class NewsUpdateView(OnlyLoggedSuperUser, UpdateView):
    model = News
    fields = ('title', 'body', 'image', 'category', 'status')
    template_name = 'crud/news_edit.html'


class NewsDeleteView(OnlyLoggedSuperUser, DeleteView):
    model = News
    template_name = 'crud/news_delete.html'
    success_url = reverse_lazy('home_page') #Yangilikni o'chirgandan so'ng home qaytadi

# genericview
class NewsCreateView(OnlyLoggedSuperUser, CreateView):
    model = News
    template_name = 'crud/news_create.html'
    fields = ('title', 'title_uz', 'title_en', 'title_ru', 'slug', 'body', 'body_uz', 'body_en', 'body_ru', 'image', 'category', 'status')

@login_required
@user_passes_test(lambda u:u.is_superuser)

def admin_page_view(request):
    admin_user = User.objects.filter(is_superuser=True)
    context = {
        "admin_user":admin_user
        }
    return render(request, "pages/admin_page.html", context)


class SearchResultList(ListView):
    model= News
    template_name = "news/search_results.html"
    context_object_name = "barcha_yangiliklar"



    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            latin = cyrillic_to_latin(query.lower())
            cyrillic = latin_to_cyrillic(query.lower())

            return News.object.filter(
                Q(title__icontains=query) |
                Q(body__icontains=query) |
                Q(title__icontains=latin) |
                Q(body__icontains=latin) |
                Q(title__icontains=cyrillic) |
                Q(body__icontains=cyrillic)
            )
        return News.object.none()
