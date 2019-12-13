import django_tables2 as tables
from .models import Entries_ion_frac, Entries_flux_ps

class constraintTable(tables.Table):
    class Meta:
        model = Entries_ion_frac
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("dictionary_tag","redshift", "ion_frac", "err_up", "err_down", "err_up2", "err_down2", "upper_lim", "lower_lim", "description", "reference")

class flux_psTable(tables.Table):
	class Meta:
		model = Entries_flux_ps
		template_name = "django_tables2/bootstrap-responsive.html"
		fields = ("dictionary_tag", "redshift", "ks", "flux_ps", "err_up", "err_down", "err_up2", "err_down2", "upper_lim", "lower_lim", "description", "reference")