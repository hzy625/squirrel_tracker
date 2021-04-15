from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from traceback import print_exc
import datetime
from squirrel.models import Squirrel
from tqdm import tqdm
from django_pandas.io import read_frame

class Command(BaseCommand):
    """
    create a export command
    """
    help = 'export_squirrel_data'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='filepath')
    
    def handle(self, *args, **kwargs):
        path = kwargs['file']
        data = Squirrel.objects.all()
        try:
            df = read_frame(data)
            df.to_csv(path, index=False, encoding='UTF-8')
            print('success')
        except:
            print_exc()
