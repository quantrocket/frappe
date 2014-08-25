#This file mainly exists to allow python setup.py test to work.
import os
import sys
os.environ["DJANGO_SETTINGS_MODULE"] = "recommendation.default_settings"
test_dir = os.path.dirname(__file__)
sys.path.insert(0, test_dir)

from django.test.utils import get_runner
from django.conf import settings


def test_suit():
    test_runner = get_runner(settings)
    failures = test_runner([], verbosity=1, interactive=True)
    sys.exit(failures)