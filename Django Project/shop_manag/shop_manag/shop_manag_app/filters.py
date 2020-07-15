import django_filters
from .models import *
from django_filters import DateFilter

class Order_Filter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    #custom field name

    class Meta:
        model = Order
        fields = ['status', 'start_date', 'end_date','total']


