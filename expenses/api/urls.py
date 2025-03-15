from django.urls import path
from . import views as expense_views



urlpatterns = [
    path('create/', expense_views.CreateRecordApiView.as_view()),
    path('all/', expense_views.ListFinancialRecordAPIView.as_view()),
    path('update/<int:pk>/', expense_views.UpdateFinancialRecordView.as_view()),    
]
