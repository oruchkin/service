# Generated by Django 4.1.3 on 2022-11-27 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='headers',
            field=models.JSONField(blank=True, null=True, verbose_name='headers'),
        ),
    ]
