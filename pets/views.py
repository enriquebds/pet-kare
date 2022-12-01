from rest_framework.views import APIView, Response, Request, status
from .serializers import PetSerializer
from pets.models import Pet

# Create your views here.
class PetView(APIView):
    def get(self, request: Request) -> Response:
        ...

    
    def post(self, request: Request) -> Response:
        serializer = PetSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_404_NOT_FOUND)

        pet = Pet.objects.create(**serializer.validated_data)

        serializer = PetSerializer(pet)

        return Response(serializer.data, status.HTTP_201_CREATED)