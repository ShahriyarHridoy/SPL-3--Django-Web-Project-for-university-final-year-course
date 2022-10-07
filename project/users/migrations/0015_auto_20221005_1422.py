# Generated by Django 3.2.9 on 2022-10-05 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0014_rename_educationinformationmodel_educationinformation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract_info',
            name='personal_info',
        ),
        migrations.RemoveField(
            model_name='joining_info',
            name='personal_info',
        ),
        migrations.AddField(
            model_name='contract_info',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='joining_info',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='educationinformation',
            name='personal_info',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
