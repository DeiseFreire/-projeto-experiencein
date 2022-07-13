#from django.urls import path, re_path
from django.urls import path, re_path, include
from perfis import views
from rest_framework.authtoken import views as auth_views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('perfis', views.PerfilViewsSet)


urlpatterns = [
	path('', include(router.urls)),
	path('perfil/', views.get_meu_perfil, name='perfil'),
	path('convites/', views.get_convites, name="convites"),
	path('convites/convidar/<int:convite_id>', views.convidar, name='convidar'),
	path('convites/aceitar/<int:convite_id>', views.aceitar, name='aceitar'),
	path('login/', auth_views.obtain_auth_token, name='login')
]

#urlpatterns = [
#	path('', views.index, name='index'),
#	path('perfis/<int:perfil_id>', views.exibir, name='exibir'),
#	re_path(r'^pefis/\d+$, views.exibir, name='perfis'),
#	path(route, view, kwargs=None, name=None, Pattern=None name='convidar'),
#	path('perfis/<int:perfil_id>/convidar', views.convidar, name='convidar'),
#	path('convite/<int:convite_id>/aceitar', views.aceitar, name='aceitar')
#]
