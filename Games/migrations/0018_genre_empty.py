# Generated by Django 3.0.7 on 2020-07-14 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0017_auto_20200714_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='empty',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
