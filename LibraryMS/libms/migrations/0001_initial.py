# Generated by Django 4.0.6 on 2022-10-29 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookn', models.CharField(max_length=30)),
                ('authorn', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('type', models.CharField(max_length=30)),
            ],
        ),
    ]