# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

'''
class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('My site admin')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('My administration')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Site administration')

admin_site = MyAdminSite()
'''

from django.contrib import admin
from . import models

admin.site.register(models.Entries_ion_frac)
admin.site.register(models.Entries_flux_ps)
admin.site.site_header = 'MPA Constraints Database'
admin.site.site_title = 'Constraint Database'
admin.site.index_title = 'Administration'