from django.db import models
from django.urls import reverse

# Create your models here.
class Data(models.Model):
    Coin = models.CharField(max_length=50)
    Ticker = models.CharField(max_length=50)
    Entry_price = models.IntegerField()
    Exit_price = models.IntegerField()
    Quantity = models.IntegerField()
    Take_profit = models.IntegerField()
    Stop_loss = models.IntegerField()
    Return_on_investment = models.IntegerField()
    Entry_date = models.DateField()
    Exit_date = models.DateField()
    Holding_period = models.IntegerField()
    Result = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Coin
    
    