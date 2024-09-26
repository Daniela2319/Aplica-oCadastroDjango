from datetime import date
from django import forms
from cursos.models import Curso

class CursoForm(forms.ModelForm):
  def clean_data_do_curso(self):
    data_do_curso = self.cleaned_data['data_do_curso']
    hoje = date.today()
    if data_do_curso < hoje:
      raise forms.ValidationError('Não é possivel cadastrar um curso no Passado!')
    return data_do_curso
    
  class Meta:
    model = Curso
    fields = ('titulo', 'nivel', 'data_do_curso', 'carga_horaria', 'descricao')