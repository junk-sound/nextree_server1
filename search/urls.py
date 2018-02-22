from django.urls import path
from search.views import (
    SearchAPIView,
)
app_name = 'search'
urlpatterns = [
    # example url: /search/
    path('', SearchAPIView.as_view(), name = 'search'),
]