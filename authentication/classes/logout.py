from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

class Logout_view(APIView):

    permission_classes=[AllowAny]

    def get(self, request):
        
        response = Response(status=200)
        response.delete_cookie(key='jwt')

        return response