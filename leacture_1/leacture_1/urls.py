"""
URL configuration for leacture_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from course import views as course_view
from fees import views as fees_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',course_view.index),
    path('learndj/',course_view.learn_django),
    path('learn_py/',course_view.learn_python),
    path('fees_django/',fees_view.django_fees),
    path('fees_python/',fees_view.python_fees)
]
