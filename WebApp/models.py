from django.db import models
from django.db.models.fields.json import JSONField
from django_mysql.models import ListCharField
from django.db.models.fields import *
from django.utils.importlib import import_module
# Create your models here.

class Email(models.Model):
    headers = JSONField()
    email_to = ListCharField(base_field=EmailField())
    email_from = EmailField()
    bcc = ListCharField(base_field=EmailField())
    cc = ListCharField(base_field=EmailField())
    subject = CharField()
    raw_email = JSONField()wajyhggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg