import django_filters

from expenses.models import FinancialRecord, IncomeCategory, ExpenseCategory

class RecordFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(field_name='date', lookup_expr='exact', label='Tarix')
    # balans = django_filters.NumberFilter(field_name='user__profile__balans', lookup_expr='exact', label='Balans')
    income_category = django_filters.NumberFilter(field_name='income_category__id', lookup_expr='icontains', label='Gəlir Kateqoriyası')
    expense_category = django_filters.NumberFilter(field_name='expense_category__id', lookup_expr='icontains', label='Xərc Kateqoriyası')

    class Meta:
        model = FinancialRecord
        fields = ['date', 'income_category', 'expense_category']





#  filterin qalib, update qalib, swagger qalib, login,register, logout qalib


    