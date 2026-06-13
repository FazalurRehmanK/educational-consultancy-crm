from django.contrib import admin
from django.urls import path
from core import views  # <-- We import your new views file here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.public_dashboard, name='dashboard'),  # <-- The empty '' means the home page!
]