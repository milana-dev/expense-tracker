from django.contrib import admin

from .models import (
    ExpenseCategory, 
    IncomeCategory,
    FinancialRecord
)

admin.site.register(ExpenseCategory)
admin.site.register(IncomeCategory)

admin.site.register(FinancialRecord)
class FinancialRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'income_category', 'income_amount', 'expense_category', 'expense_amount', 'balance', 'date')
    search_fields = ('user_username', 'about')  
    list_filter = ('income_category', 'expense_category', 'date')  
    
    def balance(self, obj):
        return obj.income_amount - obj.expense_amount
    balance.admin_order_field = 'income_amount' 
    balance.short_description = 'Balans' 
