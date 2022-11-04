from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ArtistSerializer
from .models import Artist

# Create your views here.


class ArtistView(APIView):

    def get(self, request):
        serializer = ArtistSerializer(Artist.objects.all(), many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
