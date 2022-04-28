from django.db import models


# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100, default='test')
    points = models.IntegerField()
    league_position = models.IntegerField()
    salary = models.IntegerField()
    record = models.CharField(max_length=100)
    stadium = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Players(models.Model):
    name = models.CharField('Name of player', max_length=200)
    team = models.ForeignKey(Team, blank=True, null=True, on_delete=models.CASCADE)
    age = models.IntegerField()
    number = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    position = models.CharField(max_length=45)
    shots_attempted = models.IntegerField()
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()
    saves = models.IntegerField()

    def __str__(self):
        return self.name


class Coach(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, blank=True, null=True, on_delete=models.CASCADE)
    age = models.IntegerField()
    all_time_record = models.CharField(max_length=100)
    season_record = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Game(models.Model):
    score = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    time = models.DateTimeField()

