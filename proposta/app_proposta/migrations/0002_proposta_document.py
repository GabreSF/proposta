# Generated by Django 4.2.4 on 2023-08-25 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_proposta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposta',
            name='document',
            field=models.CharField(default='N/A', max_length=50),
            preserve_default=False,
        ),
    ]