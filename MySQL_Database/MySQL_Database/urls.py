"""
URL configuration for MySQL_Database project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from MySQL_CRUD import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"), #localhost:8000
    path('insert/',views.insert),
    path('update/<int:id>',views.update),
    path('view/<int:id>',views.view),
    path('delete_selected/', views.delete_selected, name='delete_selected'),
]
