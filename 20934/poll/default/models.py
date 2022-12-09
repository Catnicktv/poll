from django.db import models

# Create your models here.
class Poll(models.Model):
    subject = models.CharField(max_length=60)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{}: {}".format(self.id, self.subject)

class Option(models.Model):
    title = models.CharField(max_length=60)
    count = models.IntegerField(default=0)
    poll_id = models.IntegerField()

    def __str__(self):
        return "{}) {}".format(self.poll_id, self.title)

