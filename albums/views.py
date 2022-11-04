from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AlbumSerializer
from .models import Album
# Create your views here.


class AlbumView(APIView):

    def get(self, request):
        serializer = AlbumSerializer(Album.objects.all(), many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
