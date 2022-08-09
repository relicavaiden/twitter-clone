# Generated by Django 4.0.6 on 2022-08-08 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.IntegerField(blank=True, default=0, verbose_name='like'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(db_index=True, max_length=14, verbose_name='Name'),
        ),
    ]
