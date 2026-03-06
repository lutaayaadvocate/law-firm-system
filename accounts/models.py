from django.db import models


class Transaction(models.Model):
    TYPE_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    description = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    date = models.DateField()
    case_reference = models.CharField(max_length=100, blank=True, null=True)

    def _str_(self):
        return f"{self.client_name} - {self.amount}"

from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[
        ('admin', 'Admin'),
        ('accounts', 'Accounts Staff'),
        ('staff', 'Staff'),
    ])

    def _str_(self):
        return self.user.username