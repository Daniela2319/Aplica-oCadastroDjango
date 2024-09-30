from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from cursos.models import Curso
from rest_api.serializers import CursoModelSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def hello_world(request):
  if request.method == 'POST':
    return Response({'message': f'HEllo World!, {request.data.get("name")}'})
  return Response({'hello': 'world Api'})

class CursoModelViewSet(ModelViewSet):
  queryset = Curso.objects.all() #conjunto de busca queryset
  serializer_class = CursoModelSerializer #serializador