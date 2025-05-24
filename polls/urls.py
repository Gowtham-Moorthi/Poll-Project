from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:poll_id>/', views.poll_detail, name='poll_detail'),
    path('<int:poll_id>/vote/', views.vote, name='vote'),
    path('<int:poll_id>/results/', views.results, name='results'),
    path('add_poll/', views.add_poll, name='add_poll'),
    path('<int:poll_id>/delete/', views.delete_poll, name='delete_poll'),
    path('<int:poll_id>/reset/', views.reset_poll, name='reset_poll'),
]
