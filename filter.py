import django_filters
from django_filters import RangeFilter,DateTimeFromToRangeFilter
from .models import *


class MessageFilter(django_filters.FilterSet):
   
    range = RangeFilter(field_name='receiver_phone')
    # daterange = DateTimeFromToRangeFilter(field_name="date_send")

    class Meta:
        model = Message
        fields = []
        
        
    
