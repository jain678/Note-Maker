from .models import Note
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status



class NoteAPIView(APIView):
    def get_object(self,pk):
        return Note.objects.get(pk=pk)

    def get(self, request,pk=None):
        
        if pk==None:
            data = Note.objects.all().order_by('-updated')
            serializer = NoteSerializer(data,many=True)
        else:
            data = self.get_object(pk)
            serializer = NoteSerializer(data)
        return Response(serializer.data)

        
    def post(self,request,format=None):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk,format=None):
        note = Note.objects.get(pk=pk)
        serializer = NoteSerializer(note,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        note = Note.objects.get(pk=pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)