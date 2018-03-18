from django.db import models

# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=50 , unique=True)
    pincode = models.DecimalField(max_digits=6 , decimal_places=0)
    website = models.URLField(verbose_name="website")
    photo = models.FileField(upload_to="college" , blank=True)

    def __str__(self):
        return self.name
