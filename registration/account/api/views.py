from account.api.serializer import RegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


class Register(APIView):
    def post(self,request):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data["response"] = "Registration Successfull!"
            data["username"] = account.username
            data["email"] = account.email
            
            refresh = RefreshToken.for_user(account)
            data["token"] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                }            
            
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        return Response(data,status=status.HTTP_201_CREATED)
