"""
" trafficMonitor/management/commands/rebuild.py
" Contributing Authors:
"    Bretton Murphy (Visgence, Inc)
"
" (c) 2012 Visgence, Inc.
"""

#system imports
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
import os

#local imports

class Command(BaseCommand):

    def handle(self, *args, **options):
        baseDir = os.path.dirname(os.path.abspath(os.sys.modules[settings.SETTINGS_MODULE].__file__))

        try:
            db_name = settings.DATABASES['default']['NAME']
            print "Found database with the name '%s' inside the settings." % db_name
        except KeyError:
            print "Could not automatically determine any database name."
        else:
            try:
                print "Attempting to remove database with the name '%s'." % db_name
                os.remove(baseDir + "/" + db_name)
                print "Database removed successfully."
            except OSError:
                print 'Database with name "%s" does not exist at project root. Going to create a new one.' % str(db_name)

        call_command('setup', interactive=True)
