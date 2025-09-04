from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path("scrape/", views.run_scraper, name="run_scraper"),
]