from django.urls import path
import blog.views

urlpatterns = [
    path('', blog.views.blog, name='blog'),
    path('<int:blog_id>/', blog.views.detail, name='detail')
]