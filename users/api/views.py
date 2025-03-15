from  rest_framework import generics
from .serializers import RegisterSerializer, LoginSerializer
from users.models import UserProfil
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken



class RegisterAPIView(generics.CreateAPIView):
    queryset = UserProfil.objects.all()
    serializer_class = RegisterSerializer
    
    def create(self, request, *args, **kwargs):
        phone = request.data.get('phone')
        email = request.data.get('email')
        
        if UserProfil.objects.filter(phone=phone).exists():
            return Response({"error": "Telefon nömrəsi artıq mövcuddur!", "redirect_url": "/api/v1/users/login/"}, status=status.HTTP_400_BAD_REQUEST)
        if UserProfil.objects.filter(email=email).exists():
            return Response({"error": "Email artıq mövcuddur!"}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)




class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        phone = request.data.get('phone')
        
        user = UserProfil.objects.filter(email=email, phone=phone).first()
        
        if user:
            refresh = RefreshToken.for_user(user)
            
            return Response({
                "message": "Giriş uğurlu oldu",
                "user_id": user.id,
                "access_token": str(refresh.access_token), 
                "refresh_token": str(refresh) 
            })
        return Response({"error": "Yanlış email və ya telefon nömrəsi"}, status=status.HTTP_400_BAD_REQUEST)






class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        phone = request.data.get('phone')
        user = UserProfil.objects.filter(email=email, phone=phone).first()
        
        if user:
            try:
                refresh_token = request.data.get('refresh')
                token = RefreshToken(refresh_token)
                token.blacklist()
                
                return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"error": "Invalid email or phone number"}, status=status.HTTP_400_BAD_REQUEST)

    
    
