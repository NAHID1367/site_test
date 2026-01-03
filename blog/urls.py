from  django.urls import path
from .views import blog_view, single_view, test, blog_category

app_name = 'blog'

urlpatterns = [
    path('', blog_view,name='index'),
    path('test/',test,name='test'),
    path('<int:pid>',single_view,name='single'),
    path('category/<str:cat_name>',blog_view,name='category'),
    path('author/<str:author_username>', blog_view,name='author'),
    #path('post/<int:pid>',test,name='test'),
    #path('<str:name>/<str:family_name>/<int:age>',test,name='test'),
]