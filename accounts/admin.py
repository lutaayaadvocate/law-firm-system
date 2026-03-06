from django.contrib import admin
from django.db.models import Sum
from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):

    list_display = (
        'client_name',
        'description',
        'formatted_amount',
        'transaction_type',
        'date'
    )

    def formatted_amount(self, obj):
        return f"UGX {obj.amount:,.0f}"

    formatted_amount.short_description = "Amount"

    # SHOW TOTALS AT THE BOTTOM
    def changelist_view(self, request, extra_context=None):

        response = super().changelist_view(request, extra_context=extra_context)

        try:
            qs = response.context_data['cl'].queryset

            total_income = qs.filter(transaction_type='income').aggregate(
                total=Sum('amount')
            )['total'] or 0

            total_expense = qs.filter(transaction_type='expense').aggregate(
                total=Sum('amount')
            )['total'] or 0

            profit = total_income - total_expense

            response.context_data['summary'] = {
                'total_income': total_income,
                'total_expense': total_expense,
                'profit': profit
            }

        except:
            pass

        return response


admin.site.register(Transaction, TransactionAdmin)