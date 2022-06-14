import django
from django.utils import version
from django.test import TestCase

# Create your tests here.
def version():
    print(django.VERSION)
    print(django.get_version())

