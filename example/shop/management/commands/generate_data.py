from django.core.management.base import NoArgsCommand
from example.shop.models import Item, Order, OrderItem, type_choices
import random
import base64
import os
from django.contrib.auth.models import User
from datetime import datetime, timedelta

random_chars = lambda : base64.urlsafe_b64encode(os.urandom(5))

class Command(NoArgsCommand):
    help = "My shiny new management command."

    def handle_noargs(self, how_many=10, **options):
        print("Creating admin user...")
        User.objects.create_superuser("admin", "admin@example.com", "admin")

        print("Creating users...")
        users = [
            User.objects.create_user(random_chars())
            for _ in range(how_many)
        ]

        print("Creating items...")
        items = [
            Item.objects.create(
                type=random.choice(type_choices)[0],
                name=random_chars(), 
                price=random.gauss(random.choice((5, 10, 20)), 5)
            )
            for _ in range(how_many * 10)
        ]

        print("Creating orders...")
        orders = [
            Order.objects.create(
                user=random.choice(users),
                paid=random.choice((True, True, False)),
                created=datetime.now() - timedelta(days=random.triangular(0,180,0))
            )
            for _ in range(how_many * 100)
        ]

        print("Creating order items...")
        for order in orders:
            [
                OrderItem.objects.create(order=order, item=items[int(random.triangular(0,len(items),0))], qty=random.randint(1, 5))
                for _ in range(random.randint(1, 5))
            ]
