from django.db import models

# Create your models here.
class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question
    
class ResultModel(models.Model):
    percent = models.FloatField()
    time = models.IntegerField()
    correct = models.FloatField()
    wrong = models.FloatField() 
    total = models.FloatField()
    score = models.FloatField()

    def __str__(self):
        return self.score