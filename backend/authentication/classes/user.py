from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from authentication.models import User
from authentication.serializers import UserSerializer

class User_view(APIView):

    permission_classes=[AllowAny]

    def post(self, request):
        
        email = request.data.get('email')
        username = request.data.get('username')
        password = request.data.get('password')
        age = request.data.get('age')
        localisation = request.data.get('localisation')
        re_password = request.data.get('re_password')
        
        try:
            user = User.register(email, username, password, re_password, age, localisation)
        except Exception as e:
            return Response({'errors': e.args[0]})

        return Response({'success': 'User created successfully!'}, status=200)

    def get(self, request):
            
        token = request.COOKIES.get('jwt')

        user=User.get_user_from_token(token)

        if not user : return Response(status=401)

        data = {}
        data['user'] = UserSerializer(user).data
        data['success'] = 'User logged in successfully'


        return Response(data, status=200)


        