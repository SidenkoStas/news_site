from news import views
from django.urls import path
from news.views import HomeNews, NewsByCategory, ViewNews, CreateNews
# from django.views.decorators.cache import cache_page


app_name = "news"

urlpatterns = [
    # path("", index, name="index"),
    # path("category/<int:category_id>/", get_category, name="get_category"),
    # path("news/<int:news_id>/", view_news, name="view_news"),
    # path("news/add-news/", add_news, name="add_news"),
    path("contact/", views.contact, name="contact"),
    # path("", cache_page(60)(HomeNews.as_view()), name="index"),
    path("", HomeNews.as_view(), name="index"),
    path("category/<int:category_id>/", NewsByCategory.as_view(),
         name="get_category"),
    path("news/<int:pk>/", ViewNews.as_view(), name="view_news"),
    path("news/add-news/", CreateNews.as_view(), name="add_news"),
    path("register", views.register, name="register"),
    path("login", views.user_login, name="login"),
    path("logout", views.user_logout, name="logout"),
]
