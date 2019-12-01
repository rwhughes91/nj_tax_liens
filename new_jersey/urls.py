from django.urls import path

from . import views

app_name = "new_jersey"
urlpatterns = [
    path('', views.home, name='home'),
    path('lien_search', views.lien_search, name="lien_search"),
    path('lien/<int:lien_id>', views.lien_detail, name="lien_detail"),
]
