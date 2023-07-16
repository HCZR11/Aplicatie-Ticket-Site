# Generated by Django 3.2.19 on 2023-07-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eveniment',
            name='status',
            field=models.CharField(choices=[('1', 'To Do'), ('2', 'In Progress'), ('3', 'In Review'), ('4', 'Done')], default=('1', 'To Do'), max_length=25),
        ),
    ]
