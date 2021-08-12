from django.db import models

# Create your models here.
class Team(models.Model):
    fpl_id = models.SmallIntegerField(primary_key=True)
    short_name = models.CharField(max_length=20)
    long_name = models.CharField(max_length=30)

class Gameweek(models.Model):
    gameweek_id = models.SmallIntegerField(default=0)
    home_team = models.ForeignKey("team", related_name='home_team', on_delete=models.CASCADE)
    away_team = models.ForeignKey("team", related_name='away_team', on_delete=models.CASCADE)
    result = models.CharField(max_length=1, blank=True, null=True)
    score = models.CharField(max_length=5, blank=True, null=True)
    date= models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    finished = models.BooleanField(default=False)



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