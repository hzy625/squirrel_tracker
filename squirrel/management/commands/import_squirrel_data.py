from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from traceback import print_exc
import datetime
from squirrel.models import Squirrel
from tqdm import tqdm
class Command(BaseCommand):
    """
    create a import command
    """
    help = 'import_squirrel_data'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='filepath')
    
    def handle(self, *args, **kwargs):
        path = kwargs['file']
        try:
            Squirrel.objects.all().delete()
            df = pd.read_csv(path, header=0, encoding='UTF-8')
            columns = [
                'X', 'Y', 'Unique Squirrel ID','Shift', 'Date',
                'Age', 'Primary Fur Color', 'Location', 'Specific Location',
                'Running', 'Chasing', 'Climbing', 'Eating', 'Foraging', 'Other Activities',
                'Kuks', 'Quaas', 'Moans', 'Tail flags', 'Tail twitches', 'Approaches', 'Indifferent',
                'Runs from'
            ]
            df = df[columns]
            df['Date'] = df['Date'].apply(lambda x: datetime.datetime.strptime(str(x), '%m%d%Y').date())
            df = df.fillna('')
            for index, row in tqdm(df.iterrows()):
                try:
                    Squirrel.objects.update_or_create(
                        unique_squirrel_id=row['Unique Squirrel ID'],
                        latitude=row['Y'],
                        longitude=row['X'],
                        shift=row['Shift'],
                        date=row['Date'],
                        age=row['Age'],
                        primary_fur_color=row['Primary Fur Color'],
                        location=row['Location'],
                        specific_location=row['Specific Location'],
                        running=row['Running'],
                        chasing=row['Chasing'],
                        climbing=row['Climbing'],
                        eating=row['Eating'],
                        foraging=row['Foraging'],
                        other_activities=row['Other Activities'],
                        kuks=row['Kuks'],
                        quaas=row['Quaas'],
                        moans=row['Moans'],
                        tail_flags=row['Tail flags'],
                        tail_twitches=row['Tail twitches'],
                        approaches=row['Approaches'],
                        indifferent=row['Indifferent'],
                        runs_from=row['Runs from']
                    )
                except:
                    continue  
            print('insert ok!')
        except:
            print_exc()
