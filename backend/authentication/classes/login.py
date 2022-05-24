from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from authentication.models import User

class Login_view(APIView):

    permission_classes=[AllowAny]

    def post(self, request):
        
        email = request.data.get('email')
        password = request.data.get('password')

        token = User.get_token(email, password)

        if not token : return Response(status=401)

        response = Response(status=200)
        response.data={'success':'Login successful'}
        response.set_cookie(key='jwt', value=token, httponly=True)

        return response