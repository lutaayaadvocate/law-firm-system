from django.db import models



class Client(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Matter(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Closed', 'Closed'),
        ('Pending', 'Pending'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    assigned_to = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    matter_number = models.CharField(max_length=50, unique=True)
    case_type = models.CharField(max_length=100)
    court = models.CharField(max_length=200, blank=True, null=True)
    opposing_party = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    filing_date = models.DateField(blank=True, null=True)
    next_hearing_date = models.DateField(blank=True, null=True)
    fees_agreed = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    notes = models.TextField(blank=True, null=True)

    def balance(self):
        return self.fees_agreed - self.amount_paid

    def __str__(self):
        return self.matter_number

class CourtDate(models.Model):
    matter = models.ForeignKey('Matter', on_delete=models.CASCADE, related_name='court_dates')
    court_name = models.CharField(max_length=255)
    hearing_date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    outcome = models.TextField(blank=True, null=True)

    def _str_(self):
        return f"{self.matter} - {self.hearing_date}"

