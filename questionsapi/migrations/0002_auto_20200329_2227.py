# Generated by Django 3.0.4 on 2020-03-30 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionsapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='questions',
            table='Questions',
        ),
        migrations.AlterModelTable(
            name='subjects',
            table='Subjects',
        ),
    ]
