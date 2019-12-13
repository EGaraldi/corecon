import django_filters

from .models import Entries_ion_frac
from .tables import constraintTable

class ion_fracFilter(django_filters.FilterSet):
	'''
	dictionary_tag = django_filters.CharFilter(lookup_expr='icontains')
	redshift_gt = django_filters.NumberFilter(name='redshift', lookup_expr='gt')
	redshift_lt = django_filters.NumberFilter(name='redshift', lookup_expr='lt')
	'''
	class Meta:
		model = Entries_ion_frac
		fields = {'dictionary_tag': ['icontains'],
				  'redshift': ['gt','lt'],
				 }