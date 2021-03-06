# Generated by Django 3.0.4 on 2020-04-19 13:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasurehunt', '0006_score_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_number', models.IntegerField()),
                ('numuser', models.IntegerField(default=0)),
                ('accuracy', models.FloatField(default=0)),
                ('wrong', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='score',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
