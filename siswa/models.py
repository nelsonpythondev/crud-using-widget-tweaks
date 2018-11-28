from django.db import models
from datetime import datetime

class Siswa(models.Model):
    name = models.CharField(max_length=200)
    male = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    created_at = models.DateField(default=datetime.utcnow)
