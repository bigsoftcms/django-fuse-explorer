from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel

type_choices = (
    ("C", "Clothing"), ("H", "Homewares"), ("T", "Toys"),
)

class Item(TimeStampedModel):
    type = models.CharField(max_length=1, choices=type_choices)
    name = models.CharField(max_length=32)
    price = models.DecimalField(decimal_places=2, max_digits=12)

    def __unicode__(self):
        return self.name

class Order(TimeStampedModel):
    user = models.ForeignKey(User)
    paid = models.BooleanField(default=False)

class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    item = models.ForeignKey(Item)
    qty = models.SmallIntegerField(default=1)
