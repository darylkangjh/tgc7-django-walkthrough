from django.urls import path
import home.views


urlpatterns = [
    path('', home.views.welcome)
]