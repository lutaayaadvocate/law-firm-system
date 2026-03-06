from django.db import models

class LibraryDocument(models.Model):
    CATEGORY_CHOICES = [
        ('precedent', 'Precedent'),
        ('law', 'Law'),
    ]

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    document = models.FileField(upload_to='library/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title