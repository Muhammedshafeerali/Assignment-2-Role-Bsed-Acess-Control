# Generated by Django 3.1.5 on 2021-01-14 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Supportteam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': [('can_manage_clients', 'Can Manage Clients')],
            },
        ),
        migrations.CreateModel(
            name='Superadmin',
            fields=[
                ('supportteam_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.supportteam')),
            ],
            options={
                'permissions': [('can_view_revenue', 'Can View Revenue'), ('can_view_app_usage', 'Can app Usage')],
            },
            bases=('app.supportteam',),
        ),
    ]
