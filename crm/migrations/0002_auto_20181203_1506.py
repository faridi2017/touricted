# Generated by Django 2.1.2 on 2018-12-03 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aspnetroles',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
