# Generated by Django 3.0.7 on 2020-07-15 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0019_remove_genre_empty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]