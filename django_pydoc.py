import os
import django
import pydoc

__author__ = "Tareq"

# Prepare Django before executing pydoc command
os.environ['DJANGO_SETTINGS_MODULE'] = 'cms_py.settings'
django.setup()

# Now executing pydoc
pydoc.cli()