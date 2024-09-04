# Generated by Django 5.1.1 on 2024-09-04 08:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=128)),
                ('rodzaj', models.TextField()),
                ('ilosc', models.IntegerField()),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='viewer.genre')),
            ],
        ),
    ]
