from django.urls import path
from .views import index, rubric_bbs, BbCreateView, set_language  # добавил set_language


urlpatterns = [
    path('', index, name='index'),
    path('<int:rubric_id>/', rubric_bbs, name='rubric_bbs'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('setlang/<str:language>/', set_language, name='set_language'),  # НОВЫЙ ПУТЬ
]