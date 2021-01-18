from django.db import models
from django.contrib.auth.models import  AbstractUser

# Create your models here.

class Supportteam(models.Model):
   
    class Meta:
        permissions=[('can_manage_clients','Can Manage Clients')]

class Superadmin(Supportteam):
    
    class Meta:
        permissions=[('can_view_revenue','Can View Revenue'),
                    ('can_view_app_usage','Can app Usage'),
                    ('add_permission','Add Permission')]

