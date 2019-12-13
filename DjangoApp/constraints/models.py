# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import date
import json
# Create your models here.

class Entries_ion_frac(models.Model):
	dictionary_tag = models.TextField()
	redshift = models.FloatField()
	ion_frac = models.CharField(max_length=2000, blank=True)
	err_up = models.CharField(max_length=2000, blank=True, null=True)
	err_down = models.CharField(max_length=2000, null=True, blank=True)
	err_up2 = models.CharField(max_length=2000, null=True, blank=True)
	err_down2 = models.CharField(max_length=2000, null=True, blank=True)
	upper_lim = models.CharField(max_length=2000, null=True, blank=True)
	lower_lim = models.CharField(max_length=2000, null=True, blank=True)
	reference = models.TextField(default = "this")
	description = models.TextField(default = "that")

	object = models.Manager()

	def __str__(self):
		return self.dictionary_tag + " " + str(self.redshift)
	
    
class Entries_flux_ps(models.Model):
	dictionary_tag = models.TextField()
	redshift = models.CharField(max_length=2000, blank=True)
	ks = models.CharField(max_length=2000, blank=True)
	flux_ps = models.CharField(max_length=2000, blank=True)
	err_up = models.CharField(max_length=2000, blank=True)
	err_down = models.CharField(max_length=2000, blank=True)
	err_up2 = models.CharField(max_length=2000, blank=True)
	err_down2 = models.CharField(max_length=2000, blank=True)
	upper_lim = models.CharField(max_length=2000, blank=True)
	lower_lim = models.CharField(max_length=2000, blank=True)
	reference = models.TextField(default = "this")
	description = models.TextField(default = "that")

	object = models.Manager()

	def __str__(self):
		return self.dictionary_tag + " " + str(self.redshift)