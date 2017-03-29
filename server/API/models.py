from django.db import models

class Player(models.Model):
    nickname = models.CharField(max_length=20)
    firstName = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    position = models.ForeignKey('Position')
    password = models.CharField(max_length=30)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.nickname

class Position(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField(default=0)

    def __str__(self):
        return 'x='+str(self.x)+' y='+str(self.y)+' z='+str(self.z)

class Question(models.Model):
    questionText = models.CharField(max_length=100)
    answer1 = models.CharField(max_length=20)
    answer2 = models.CharField(max_length=20)
    answer3 = models.CharField(max_length=20)
    answer4 = models.CharField(max_length=20)
    CHOICES= (
        ('1',answer1),
        ('2', answer2),
        ('3', answer3),
        ('4', answer4),
    )
    rightAnswer= models.CharField(max_length=20, choices=CHOICES)
    position = models.ForeignKey('Position')
    rayon = models.FloatField(default=2)

    def __str__(self):
        return self.questionText