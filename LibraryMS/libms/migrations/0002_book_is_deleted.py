# Generated by Django 4.0.6 on 2022-10-31 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_deleted',
            field=models.CharField(default='n', max_length=2),
        ),
    ]