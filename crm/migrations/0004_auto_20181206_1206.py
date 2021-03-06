# Generated by Django 2.1.2 on 2018-12-06 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20181203_1621'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leadstatus',
            options={'managed': True, 'verbose_name_plural': 'Leadstatus'},
        ),
        migrations.AlterField(
            model_name='aspnetusers',
            name='emailconfirmed',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='aspnetusers',
            name='lockoutenabled',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='aspnetusers',
            name='twofactorenabled',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='isactivated',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='leaditems',
            name='builderinterest',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='leads',
            name='isassigned',
            field=models.NullBooleanField(default=False),
        ),
    ]
