from django.urls import re_path as url, include
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.news_today, name='newsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$', views.past_days_news, name='pastNews'),
    url(r'search/', views.search_results, name='search_results'),
    url(r'article/<int:article_id>/', views.article, name='article'),
    url(r'new/article', views.new_article, name='new-article'),
    url(r'login/', auth_views.LoginView.as_view(), name='login'),
    url(r'logout/', auth_views.LogoutView.as_view(), name='logout'),
    url(r'ajax/newsletter/', views.newsletter, name='newsletter'),
    url(r'api/merch/', views.MerchList.as_view()),
    url(r'api-token-auth/', obtain_auth_token),
    url(r'api/merch/merch-id/(?P<pk>[0-9]+)/$', views.MerchDescription.as_view()),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),


    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
