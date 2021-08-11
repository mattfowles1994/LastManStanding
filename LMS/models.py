from django.db import models

# Create your models here.
class Gameweek(models.Model):
    home_team = models.CharField(max_length=20)
    away_team = models.CharField(max_length=20)
    result = models.CharField(max_length=1, blank=True, null=True)
    score = models.CharField(max_length=5, blank=True, null=True)
    date= models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)

class Choice(models.Model):
    user_id = models.IntegerField()
    gameweek_id = models.ForeignKey("Gameweek", on_delete=models.CASCADE)

    Choices = [
        ('Home', 'Home'),
        ('Away', 'Away')
    ]
    chosen_result = models.CharField(
        max_length=4,
        choices=Choices
        )