from django_tables2 import tables
from django_tables2.utils import A
from .models import *
from django.utils.html import format_html

class SquirrelTable(tables.Table):
    """
    定义Modeltable
    https://django-tables2.readthedocs.io/en/latest/pages/table-data.html#table-data
    """
    detail = tables.columns.LinkColumn('update', args=[A('pk')], orderable=False, empty_values=(), verbose_name='Action')
    def render_detail(self):
        return 'detail'
   
    
    class Meta:
        model = Squirrel # 指定模型
        fields = ('unique_squirrel_id', 'date', 'detail', )
        attrs = {"class": "table table-striped text-center"} 
        template_name = 'django_tables2/bootstrap.html'