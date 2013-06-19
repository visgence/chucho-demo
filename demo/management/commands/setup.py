'''
' trafficMonitor/management/commands.setup.py
' Contributing Authors:
'    Jeremiah Davis (Visgence, Inc)
'    Bretton Murphy (Visgence, Inc)
'
' (c) 2013 Visgence, Inc.
'''

# System Imports
from django.core.management import call_command
from django.core.management.base import BaseCommand
from settings import APP_PATH
import git
import sys
import os

# local imports


class Command(BaseCommand):
    help = 'Runs syncdb, git submodule, and sets up an admin user.'

    def handle(self, *args, **options):

        # Make sure we have the current submodules
        # sys.stdout.write('Updating git-submodules...')
        # sys.stdout.flush()
        # repo = git.Repo(os.path.relpath(os.pardir, APP_PATH))
        # repo.submodule_update(to_latest_revision=False)

        call_command('syncdb', interactive=False)
        #call_command('migrate')

        # ORDER OF FIXTURES MATTERS!! Some have dependencies on others.
        print "Loading fixtures..."
        fixtures = [
            [
                "demo/fixtures/users.json"
            ]
        ]

        # Load fixtures
        for apps in fixtures:
            for fixture in apps:
                call_command('loaddata', fixture, verbosity=1)
        print "Done"
