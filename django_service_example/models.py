from django.db import models

# Create your models here.

class Card(models.Model):
    last4 = models.CharField(max_length=4)

    def __str__(self):
        return "Card id: {}, last4: {}".format(self.id, self.last4)
