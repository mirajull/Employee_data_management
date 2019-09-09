from django.db import models
from django.db import connection, connections
import json
import datetime
import urllib
from sqlserver_ado.fields import LegacyDateField, LegacyDateTimeField
from sqlserver_ado.fields import DateField, DateTimeField, TimeField
from django.db import models
from django.db import connection, connections
from django.urls import reverse,reverse_lazy


class Person(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)
