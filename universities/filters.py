import django_filters
from django.forms import TextInput

from .models import Institutions


class InstitutionFilter(django_filters.FilterSet):
    STATE_CHOICES = [('AL', 'AL'), ('AK', 'AK'), ('AZ', 'AZ'), ('AR', 'AR'), ('CA', 'CA'), ('CO', 'CO'),
                     ('CT', 'CT'), ('DE', 'DE'), ('FL', 'FL'), ('GA', 'GA'), ('HI', 'HI'), ('ID', 'ID'),
                     ('IL', 'IL'), ('IN', 'IN'), ('IA', 'IA'), ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'),
                     ('ME', 'ME'), ('MD', 'MD'), ('MA', 'MA'), ('MI', 'MI'), ('MN', 'MN'), ('MS', 'MS'),
                     ('MO', 'MO'), ('MT', 'MT'), ('NE', 'NE'), ('NV', 'NV'), ('NH', 'NH'), ('NJ', 'NJ'),
                     ('NM', 'NM'), ('NY', 'NY'), ('NC', 'NC'), ('ND', 'ND'), ('OH', 'OH'), ('OK', 'OK'),
                     ('OR', 'OR'), ('PA', 'PA'), ('RI', 'RI'), ('SC', 'SC'), ('SD', 'SD'), ('TN', 'TN'),
                     ('TX', 'TX'), ('UT', 'UT'), ('VT', 'VT'), ('VA', 'VA'), ('WA', 'WA'), ('WV', 'WV'),
                     ('WI', 'WI'), ('WY', 'WY')]

    institution_name = django_filters.CharFilter(field_name='instname', lookup_expr='icontains',
                                                 label='Institution Name',
                                                 widget=TextInput(attrs={'placeholder': 'Enter Name...'}))
    institution_city = django_filters.CharFilter(field_name='zipcodeid__cityid__city', lookup_expr='iexact',
                                                 label='City Name',
                                                 widget=TextInput(attrs={'placeholder': 'Enter City...'}))
    institution_state = django_filters.ChoiceFilter(field_name='zipcodeid__cityid__state', label='State',
                                                    choices=STATE_CHOICES)
    act_average = django_filters.NumberFilter(field_name='admissions__act_scores_midpoint_cumulative',
                                              label='ACT Score', lookup_expr='gt',
                                              widget=TextInput(attrs={'placeholder': 'Enter ACT Score...'}))
    sat_average = django_filters.NumberFilter(field_name='admissions__sat_scores_average_overall',
                                              label='SAT Score', lookup_expr='gt',
                                              widget=TextInput(attrs={'placeholder': 'Enter SAT Score...'}))

    class Meta:
        model = Institutions
        fields = ('institution_name', 'institution_city', 'institution_state', 'act_average',
                  'sat_average')
