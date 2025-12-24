from  django.urls import path
from .views import blog_view, single_view, test

app_name = 'blog'

urlpatterns = [
    path('', blog_view,name='index'),
    path('<int:pid>',single_view,name='single'),
    #path('post/<int:pid>',test,name='test'),
    #path('<str:name>/<str:family_name>/<int:age>',test,name='test'),
]