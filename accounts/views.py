from django.shortcuts import render
from django.db.models import Sum
from .models import Transaction
from datetime import datetime

def finance_dashboard(request):

    total_income = Transaction.objects.filter(
        transaction_type="income"
    ).aggregate(Sum("amount"))["amount__sum"] or 0

    total_expense = Transaction.objects.filter(
        transaction_type="expense"
    ).aggregate(Sum("amount"))["amount__sum"] or 0

    balance = total_income - total_expense

    current_month = datetime.now().month

    monthly_transactions = Transaction.objects.filter(
        date__month=current_month
    )

    context = {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
        "monthly_transactions": monthly_transactions
    }

    return render(request, "accounts/dashboard.html", context)