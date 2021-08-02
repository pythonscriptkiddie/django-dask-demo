import sys
import os
DJANGO_SETTINGS_MODULE='demo.settings'
#settings.configure()
import django

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path)
django.setup()
