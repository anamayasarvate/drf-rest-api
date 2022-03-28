from math import perm
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.generics import ListAPIView
from api.models import Library
from api.serializers import LibrarySerializer

class LibraryView(ModelViewSet):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()
    permission_classes = (permissions.AllowAny,)

@api_view(['GET',])
@permission_classes([permissions.AllowAny,])
def library_list_view(request):
    if request.method == 'GET':
        serializer = LibrarySerializer(Library.objects.all(), many=True)
        return Response(serializer.data)

@api_view(['POST',])
@permission_classes([permissions.IsAuthenticated,])
def library_create_view(request):
    if request.method == "POST":
        serializer = LibrarySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'incorrect data sent for posting'})

@api_view(['GET',])
@permission_classes([permissions.AllowAny,])
def library_detail_view(request, pk):
    if request.method == 'GET':
        library = get_object_or_404(Library, pk =pk)
        serializer = LibrarySerializer(library)
        return Response(serializer.data)

@api_view(['PUT',])
@permission_classes([permissions.IsAuthenticated,])
def library_update_view(request, pk):
    if request.method == "PUT":
        library = get_object_or_404(Library, pk =pk)
        serializer = LibrarySerializer(library, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'incorrect data sent for updating'})

@api_view(['DELETE',])
@permission_classes([permissions.IsAuthenticated,])
def library_delete_view(request, pk):
    if request.method == "DELETE":
        library = get_object_or_404(Library, pk =pk)
        library.delete()
        message = {'success': 'DELETED!'}
        return Response(message ,status = status.HTTP_200_OK)


class LibraryListView(ListAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = (permissions.AllowAny,)
