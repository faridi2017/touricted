# Generated by Django 2.1.2 on 2018-12-03 09:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aspnetroles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'aspnetroles',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Aspnetusers',
            fields=[
                ('userid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=256, unique=True)),
                ('passwordhash', models.CharField(blank=True, max_length=128, null=True)),
                ('securitystamp', models.CharField(blank=True, max_length=256, null=True)),
                ('email', models.CharField(blank=True, max_length=256, null=True)),
                ('emailconfirmed', models.BooleanField()),
                ('phonenumber', models.CharField(blank=True, max_length=15, null=True)),
                ('phonenumberconfirmed', models.BooleanField()),
                ('twofactorenabled', models.BooleanField()),
                ('lockoutenddateutc', models.DateTimeField(blank=True, null=True)),
                ('lockoutenabled', models.BooleanField()),
                ('accessfailedcount', models.IntegerField()),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=30)),
                ('createddatetime', models.DateTimeField()),
                ('companyid', models.IntegerField(blank=True, null=True)),
                ('roleid', models.CharField(blank=True, max_length=10, null=True)),
                ('projectid', models.IntegerField(blank=True, null=True)),
                ('token', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'aspnetusers',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('attendanceid', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.CharField(max_length=100)),
                ('distancein', models.FloatField()),
                ('attendence', models.BooleanField(default=False)),
                ('datein', models.DateTimeField(blank=True, null=True)),
                ('dateout', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('distanceout', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'attendance',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('companyid', models.AutoField(primary_key=True, serialize=False)),
                ('companyname', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=70, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('companyaddress', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('contactpersonname', models.CharField(max_length=50)),
                ('contactphone', models.CharField(max_length=10)),
                ('contactemail', models.CharField(max_length=100)),
                ('activatedtill', models.DateTimeField()),
                ('isactivated', models.BooleanField()),
                ('logopath', models.TextField(blank=True, null=True)),
                ('companytype', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'company',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Companytype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'companytype',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('documentid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('projectid', models.CharField(max_length=20)),
                ('link', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'document',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Integrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourceid', models.IntegerField(blank=True, null=True)),
                ('integrationkey', models.CharField(blank=True, max_length=50, null=True)),
                ('integrationvalue', models.CharField(blank=True, max_length=500, null=True)),
                ('companyid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'integrations',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Jobruns',
            fields=[
                ('jobrunid', models.AutoField(primary_key=True, serialize=False)),
                ('startdate', models.DateTimeField()),
                ('enddate', models.DateTimeField()),
                ('noofleads', models.IntegerField()),
                ('errormessage', models.TextField(blank=True, null=True)),
                ('companyid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'jobruns',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Kwdelhi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=100, null=True)),
                ('lastname', models.CharField(blank=True, max_length=100, null=True)),
                ('emailaddress', models.CharField(blank=True, max_length=100, null=True)),
                ('telephonenumber', models.CharField(blank=True, max_length=100, null=True)),
                ('comments', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'kwdelhi',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Leaditems',
            fields=[
                ('leaditemid', models.AutoField(primary_key=True, serialize=False)),
                ('leadid', models.IntegerField(blank=True, null=True)),
                ('queryremarks', models.CharField(blank=True, max_length=200, null=True)),
                ('typeofproperty', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('rangefrom', models.IntegerField(blank=True, null=True)),
                ('rangeto', models.IntegerField(blank=True, null=True)),
                ('cmpctlabel', models.TextField(blank=True, null=True)),
                ('receivedon', models.DateTimeField(blank=True, null=True)),
                ('projname', models.CharField(blank=True, max_length=100, null=True)),
                ('assignedto', models.CharField(blank=True, max_length=128, null=True)),
                ('builderinterest', models.BooleanField(blank=True, null=True)),
                ('statusid', models.IntegerField(blank=True, null=True)),
                ('statusdate', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'leaditems',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('leadid', models.AutoField(primary_key=True, serialize=False)),
                ('createuserid', models.CharField(blank=True, max_length=128, null=True)),
                ('createdatetimeoffset', models.DateTimeField(blank=True, null=True)),
                ('edituserid', models.CharField(blank=True, max_length=128, null=True)),
                ('editdatetimeoffset', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=80, null=True)),
                ('phonenumber', models.CharField(blank=True, max_length=14, null=True)),
                ('isassigned', models.BooleanField(default=False)),
                ('companyid', models.IntegerField(blank=True, null=True)),
                ('cmpctlabel', models.TextField(blank=True, null=True)),
                ('receivedon', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('id', models.CharField(blank=True, max_length=150, null=True)),
                ('projectname', models.CharField(blank=True, max_length=256, null=True)),
                ('city', models.CharField(blank=True, max_length=256, null=True)),
                ('locality', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'leads',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Leadstatus',
            fields=[
                ('statusid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'leadstatus',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('locationid', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.CharField(max_length=100)),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('longitude', models.CharField(max_length=100)),
                ('lattitude', models.CharField(max_length=100)),
                ('companyid', models.IntegerField()),
                ('lastupdated', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'location',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('projectid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('longitude', models.CharField(blank=True, max_length=100, null=True)),
                ('lattitude', models.CharField(blank=True, max_length=100, null=True)),
                ('companyid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'project',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Recording',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'recording',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Recordings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leadid', models.IntegerField()),
                ('name', models.CharField(max_length=250)),
                ('createdatetime', models.DateTimeField()),
                ('createdby', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'recordings',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Refreshtokens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('clientid', models.CharField(max_length=50)),
                ('issuedutc', models.DateTimeField()),
                ('expiresutc', models.DateTimeField()),
                ('protectedticket', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'refreshtokens',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sourcetypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'sourcetypes',
                'managed': True,
            },
        ),
    ]
