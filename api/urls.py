# Here we're using urls directly from API rather than from API_Project/urls.py

from django.urls import path
#from .views import article_list, article_details  (function based)
#from .views import ArticleList, ArticleDetails     (class based)
from .views import ArticleList, ArticleDetails #mixins

urlpatterns = [
    #path for mixins
    path('articles/', ArticleList.as_view()),
    path('articles/<int:id>/', ArticleDetails.as_view())

    #path for class based operations
    # path('articles/', ArticleList.as_view()),
    # path('articles/<int:id>/', ArticleDetails.as_view())

    #path for function based ops
    # path('articles/', article_list),
    # path('articles/<int:pk>', article_details)
]
