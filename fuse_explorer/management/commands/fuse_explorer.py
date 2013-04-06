# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import datetime

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Yiiiiip, yip yip yip yip")
