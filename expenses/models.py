from django.db import models
from users.models import UserProfil

class IncomeCategory(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'income'
        verbose_name_plural = 'Incomes'


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'expense'
        verbose_name_plural = 'expenses'
        

class FinancialRecord(models.Model):
    user = models.OneToOneField(UserProfil, on_delete=models.CASCADE)
    income_category = models.ForeignKey(IncomeCategory,on_delete=models.CASCADE,null=False, blank=False)
    income_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    expense_category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, blank=False, null=False)
    expense_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    about = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'financial record'
        verbose_name_plural = 'financial records'