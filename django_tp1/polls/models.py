from django.db import models
from django.utils import timezone
import datetime

class Question (models.Model):
    question_text = models.CharField (max_length = 200)
    publication_date = models.DateTimeField ('date published')
    
    def published_this_week ( self ):
        if self.publication_date >= (timezone.now() - datetime.timedelta( days =7)):
            return True
        else:
            return False
        
    def __str__ ( self ):
        return self.question_text

class Choice (models.Model):
    question = models.ForeignKey (Question, on_delete = models.CASCADE)
    text_choice = models.CharField(max_length = 200)

    number_of_votes = models.IntegerField()


    def __str__ ( self ):
        return self.text_choice