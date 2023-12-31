# Generated by Django 4.2.4 on 2023-08-25 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('descricao', models.TextField()),
                ('aprovada', models.BooleanField(default=False)),
            ],
        ),
    ]
