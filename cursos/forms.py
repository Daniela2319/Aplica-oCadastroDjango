from django import forms
from cursos.models import Curso

class CursoForm(forms.ModelForm):
  class Meta:
    model = Curso
    fields = ('titulo', 'nivel', 'data_do_curso', 'carga_horaria', 'descricao')