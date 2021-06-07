from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)

    def __str__(self):
        return self.name
