from django.urls import path #importa as lista das urls
from cursos.views import criar_curso #importa as views do app

app_name = 'Cursos'
urlpatterns = [
  path('criar_curso/', criar_curso, name='criar_curso')
]