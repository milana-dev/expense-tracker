from rest_framework import serializers
from users.models import UserProfil
from users.api.serializers import UserProfilSerializer

from ..models import IncomeCategory,ExpenseCategory, FinancialRecord


class ListIncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = ('id', 'name')


class ListExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = ('id', 'name')


class CreateFinancialRecordSerializer(serializers.ModelSerializer):
    # user = UserProfilSerializer()
    income_category = ListIncomeCategorySerializer()
    expense_category = ListExpenseCategorySerializer()
    balance = serializers.SerializerMethodField()
    
    class Meta:
        model = FinancialRecord
        fields = '__all__'
        
    def get_balance(self, obj):
        income = obj.income_amount if obj.income_amount is not None else 0
        expense = obj.expense_amount if obj.expense_amount is not None else 0
        return income - expense
    


class UpdateFinancialRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialRecord
        fields = ['income_amount', 'expense_amount']
        
    def update(self, instance, validated_data):
        instance.income_amount = validated_data.get('income_amount', instance.income_amount)
        instance.expense_amount = validated_data.get('expense_amount', instance.expense_amount)
        
        instance.save()
        return instance