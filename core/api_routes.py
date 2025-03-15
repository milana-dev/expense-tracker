from django.urls import path, include

urlpatterns = [
    path('users/', include('users.api.urls')),
    path('expenses/', include('expenses.api.urls'))
]
