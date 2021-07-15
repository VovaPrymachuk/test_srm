from django.db import models
from django.contrib.auth.models import Group


Group.add_to_class('description', models.CharField(max_length=200,null=True, blank=True))
