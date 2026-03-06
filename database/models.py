from django.db import models

class Draft(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    file = models.FileField(upload_to='templates/')
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title