# Generated by Django 2.0 on 2018-06-18 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('score_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='take',
            name='score',
            field=models.IntegerField(default=0, null=True, verbose_name='分数'),
        ),
    ]
