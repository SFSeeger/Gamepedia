# Generated by Django 3.0.7 on 2020-06-29 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0003_auto_20200629_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='name',
        ),
        migrations.RemoveField(
            model_name='plattform',
            name='name',
        ),
    ]