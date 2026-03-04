from django.urls import path
from .views import CursosAPIView, CursoAPIView, AvaliacoesAPIView, AvaliacaoAPIView, AvaliacaoViewSet, CursoViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('Avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>', CursoAPIView.as_view(), name='curso'),

    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacao/<int:avaliacao_pk>', AvaliacaoAPIView.as_view(), name='curso_avaliacao'),

    path('avaliacoes/<int:avaliacao_pk>', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes<int:pk>/', AvaliacaoAPIView.as_view(), name='avaliacao')

]
