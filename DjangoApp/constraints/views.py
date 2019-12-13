# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django_tables2 import SingleTableView
from .models import Entries_ion_frac, Entries_flux_ps
from .tables import constraintTable, flux_psTable
from .filters import ion_fracFilter

class EntriesListView(SingleTableView):
    model = Entries_ion_frac
    table_class = constraintTable
    template_name = 'Entries.html'

class flux_psListView(SingleTableView):
	model = Entries_flux_ps
	table_class = flux_psTable
	template_name = 'Entries.html'
	

def constraints_list(request):
	filter = ion_fracFilter(request.GET, queryset = Entries_ion_frac.object.all())
	return render(request, 'Entries_filter.html', {'filter' : filter})
