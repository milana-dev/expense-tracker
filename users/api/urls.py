from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import RegisterAPIView, UserLoginView, LogoutView


urlpatterns = [
    path('register/' , RegisterAPIView.as_view(), name='register'),
    path('login/' , UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]


# {
#     "email": "meryem_vldov@mail.ru",
#     "phone": "+994 332 2677"
# }
# "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyMDM0ODg2LCJpYXQiOjE3NDIwMzQ1ODYsImp0aSI6ImUyNTE2YTkzMWI4NDQ5YWE5Yzc2MGFkMmIyZmRiMGM4IiwidXNlcl9pZCI6OX0.dYs0F9Hlddr4ubKRI7zXAyL_xRHc6yDtkVLpB9ScmKM",
    # "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0MjEyMDk4NiwiaWF0IjoxNzQyMDM0NTg2LCJqdGkiOiJkMGEzODUwOTZiMmI0NTk3OGRkMjVkODM0MzRiMDVlZCIsInVzZXJfaWQiOjl9.TDk65nsUg6h3_91AAjR0f5J5vEIFCU4vRsvB54hbjBM"
# }
