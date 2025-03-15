from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import UserProfil

from expenses.api.filters import RecordFilter

from expenses.models import (
    FinancialRecord,
    IncomeCategory,
    ExpenseCategory
    )

from .serializers import (
    ListIncomeCategorySerializer,
    ListExpenseCategorySerializer,
    CreateFinancialRecordSerializer, 
    UpdateFinancialRecordSerializer, 
    
)


class CreateRecordApiView(generics.CreateAPIView):
    queryset = FinancialRecord.objects.all()
    serializer_class = CreateFinancialRecordSerializer
    permission_classes = [IsAuthenticated]
    
    
    def create(self, request, *args, **kwargs):
        selected_user_id = request.data.get("user")  
        if selected_user_id:
            profile = UserProfil.objects.get(id=selected_user_id)
        else:
            profile = request.user 

        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            income_amount = serializer.validated_data.get("income_amount", 0)
            expense_amount = serializer.validated_data.get("expense_amount", 0)

            try:
                financial_record = FinancialRecord.objects.get(user=profile)
                balance = financial_record.income_amount - financial_record.expense_amount

                if balance == 0 and expense_amount > 0:
                    return Response({"message": "Xərc əməliyyatı həyata keçirilə bilməz, çünki balansınız sıfırdır!"}, status=status.HTTP_400_BAD_REQUEST)
                
                if balance < expense_amount:
                    return Response({"message": "Xərc əməliyyatı həyata keçirilə bilməz, balansınız xərcdən azdır!"}, status=status.HTTP_400_BAD_REQUEST)

                financial_record.income_amount += income_amount
                financial_record.expense_amount += expense_amount
                financial_record.save()

                return Response({"message": "Maliyyə rekordu uğurla yeniləndi!"}, status=status.HTTP_200_OK)

            except FinancialRecord.DoesNotExist:
                if expense_amount > 0:
                    return Response({"message": "Balansınız sıfır olduğu üçün xərc əməliyyatı edilə bilməz!"}, status=status.HTTP_400_BAD_REQUEST)

                serializer.save(user=profile) 
                return Response({"message": "Maliyyə rekordu uğurla yaradıldı!"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
class ListFinancialRecordAPIView(generics.ListAPIView):
    queryset = FinancialRecord.objects.select_related('user_profile', 'income_category', 'expense_category')
    serializer_class = CreateFinancialRecordSerializer
    filterset_class = RecordFilter
    
    
    



class UpdateFinancialRecordView(generics.UpdateAPIView):
    queryset = FinancialRecord.objects.all()
    serializer_class = UpdateFinancialRecordSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def put(self, request, *args, **kwargs):
        user = request.user
        new_income = request.data.get('income_amount')
        new_expense = request.data.get('expense_amount')

        try:
            financial_record = FinancialRecord.objects.get(user=user)
        except FinancialRecord.DoesNotExist:
            return Response({"message": "Maliyyə rekordu tapılmadı!"}, status=status.HTTP_404_NOT_FOUND)
        current_balance = financial_record.income_amount - financial_record.expense_amount
        
        if new_expense is not None and new_expense > current_balance:
            return Response({"message": "Xərc mövcud balansdan çox ola bilməz!"}, status=status.HTTP_400_BAD_REQUEST)

        if new_income is not None:
            financial_record.income_amount = new_income 
        if new_expense is not None:
            financial_record.expense_amount = new_expense  

        new_balance = financial_record.income_amount - financial_record.expense_amount
        financial_record.save()

        return Response({
            "username": user.username,
            "income_amount": financial_record.income_amount,
            "expense_amount": financial_record.expense_amount,
            "balance": new_balance,
            "message": "Maliyyə rekordu yeniləndi!"
        }, status=status.HTTP_200_OK)


