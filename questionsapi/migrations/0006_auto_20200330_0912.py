# Generated by Django 3.0.4 on 2020-03-30 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionsapi', '0001_initial'),
    ]
    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='subjectname',
            field=models.CharField(max_length=30),
        ),
    ]