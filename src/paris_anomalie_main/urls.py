from django.contrib import admin
from django.urls import path, include
from .views import index, questions                # PAGE ACCUEIL INDEX

urlpatterns = [
    path('admin/', admin.site.urls),            # PAGE ADMIN
    path('', index, name='index'),              # PAGE ACCUEIL
    path('q<str:num_question>/', questions),    # AFFICHAGE DE MES 3 URLS QUESTIONS
]


