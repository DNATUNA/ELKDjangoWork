from django.conf.urls import url
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.http import JsonResponse

from aims import views
from django.contrib.auth.views import login, logout


urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/inference$', views.DetailInferenceView.as_view(), name='detail.inference'),
    url(r'^(?P<pk>\d+)/details', views.DetailDetailsView.as_view(), name='detail.details'),
    # path('v1/tasks/', views.tasks, name='tasks'),
    url(r'^login/$', login, {'template_name': 'aims/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'aims/logout.html'}, name='logout'),
    url(r'search/', views.search, name='search'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



