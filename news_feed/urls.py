from django.urls import path


from .views import (
    news_list,
    news_detail,
    # homePageView,
    HomePageView,
    # contactPageView,
    ContactPageView,
    page404View,
    LocalPageView,
    XorijPageView,
    SportPageView,
    TechnologyPageView,
    NewsDeleteView,
    NewsUpdateView,
    NewsCreateView,
    admin_page_view,
    SearchResultList,


)

urlpatterns =[
    # path('', homePageView, name = 'home_page' ),
    path('', HomePageView.as_view(), name='home_page'),
    path('news/all/', news_list, name='all_news_list'),
    path("news/create/", NewsCreateView.as_view(), name="news_create"),
    path("news/<slug:news>/", news_detail, name = "news_detail_page"),
    path("news/<slug>/edit/", NewsUpdateView.as_view(), name="news_update"),
    path("news/<slug>/delete/", NewsDeleteView.as_view(), name="news_delete"),


    # path("contact-us/", contactPageView, name="contact_page"),
    path('contact-us/', ContactPageView.as_view(), name="contact_page"),
    path('local/', LocalPageView.as_view(), name = "local_page"),
    path("xorij/", XorijPageView.as_view(), name= "xorij_page"),
    path("sport/", SportPageView.as_view(), name="sport_page"),
    path("technology/", TechnologyPageView.as_view(), name="technology_page"),
    path("404/", page404View, name = "404_page"),
    path("adminpage/", admin_page_view, name="admin_page"),
    path('searchresult/', SearchResultList.as_view(), name="search_results"),


]