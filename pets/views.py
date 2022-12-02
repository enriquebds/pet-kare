from rest_framework.views import APIView, Response, Request, status
from .serializers import PetSerializer
from pets.models import Pet

# Create your views here.
class PetView(APIView):
    def get(self, request: Request) -> Response:
        pets = Pet.objects.all()

        serializer = PetSerializer(pets, many=True)

        return Response(serializer.data)
    
    def post(self, request: Request) -> Response:
        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)