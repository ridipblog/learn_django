from django.urls import path
from . import views
urlpatterns = [
    path('do-code-1/', views.do_code_1),
    path('do-code-2/', views.do_code_2),
]
