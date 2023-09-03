from django.urls import path
from .views import BlogListView, BlogDetaillView


urlpatterns = [
    path('post/', BlogListView.as_view()),
    path('post/<post_slug>/', BlogDetaillView.as_view()),

]