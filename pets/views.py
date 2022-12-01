from rest_framework.views import APIView, Response, Request, status

# Create your views here.
class PetView(APIView):
    def get(self, request: Request) -> Response:
        ...

    
    def post(self, request: Request) -> Response:
        ...