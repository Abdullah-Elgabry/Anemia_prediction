from django.db import models


class PredResults(models.Model):

    Gender = models.FloatField()
    Hemoglobin = models.FloatField()
    MCH = models.FloatField()
    MCHC = models.FloatField()
    MCV  = models.FloatField(null=True,blank=True)
    prediction = models.CharField(max_length=30)
    
    def __str__(self):
        return self.prediction
