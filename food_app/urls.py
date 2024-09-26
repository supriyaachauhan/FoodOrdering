from django.contrib import admin
from django.urls import path
from food_app.views import *

urlpatterns = [
    path('', admin.site.urls),
]