# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.core.management.base import BaseCommand
from fuse_explorer.django_filesystem import DjangoFS
import os

class Command(BaseCommand):
    args = '[mountpoint]'
    help = 'Mount a filesystem view of the current project.'

    def handle(self, *args, **options):
        mountpoint = args[0] if args else os.path.abspath("fuse_explorer")
        fs = DjangoFS()
        fs.flags = 0
        fs.multithreaded = 0
        fs.fuse_args.mountpoint = mountpoint
        if 'verbosity' in options and int(options['verbosity']) > 1:
            fs.fuse_args.setmod('foreground')
#            fs.fuse_args.setmod('debug')
        self.stdout.write("Mouting on %s... " % mountpoint)
        fs.main()