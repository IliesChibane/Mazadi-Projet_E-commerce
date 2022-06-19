from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from authentication.models import User
from django.shortcuts import render

class Login_view(APIView):

    permission_classes=[AllowAny]

    def post(self, request):
        
        email = request.data.get('email')
        password = request.data.get('password')
        for d in request.data:
            print(d)

        token = User.get_token(email, password)

        if not token : 
            return render(request, 'index2.html')

        response = Response(status=200)
        response.data={'success':'Login successful'}
        response.set_cookie(key='jwt', value=token, httponly=True)

        return render(request, 'index2.html')