from django.urls import path
from . import views

# start with blog
urlpatterns = [
    # https://localhost:8000/blog/
    path('', views.blog_list, name="blog_list"),
    # http://localhost:8000/blog/pk
    path('<int:blog_pk>', views.blog_detail, name="blog_detail"),
    # http://localhost:8000/blog/type/pk
    path('type/<int:blog_type_pk>', views.blogs_with_type, name="blogs_with_type"),
    path('date/<int:year>/<int:month>', views.blogs_with_date, name="blogs_with_date"),
]
