from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
def hello_world(request):
  if request.method == 'POST':
    return Response({'message': f'HEllo World!, {request.data.get("name")}'})
  return Response({'hello': 'world Api'})