from django.db import models

# Create your models here.

class rekap(models.Model):
    title = models.CharField(max_length=100)
    number_of_page =models.IntegerField()
    publish_date = models.DateField()
    quantity = models.IntegerField()
    
    def _str_(self):
        return self.title



        # /Erekap/list