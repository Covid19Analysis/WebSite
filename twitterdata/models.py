from django.db import models

# Create your models here.

class aeg(models.Model):
    Gun = models.IntegerField()
    Begeni=models.IntegerField()
    Cevaplar=models.IntegerField()
    Retweet=models.IntegerField()
    Tweets_Skoru=models.IntegerField()
    Toplam_Tweet_Duygu=models.IntegerField()
    Negatif=models.IntegerField()
    Pozitif=models.IntegerField()
    Toplam_Tweet=models.IntegerField()
    
  
