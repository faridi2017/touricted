from django.db import models
import uuid


class Aspnetroles(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'aspnetroles'
        verbose_name_plural = "Aspnetroles"


class Aspnetusers(models.Model):
    userid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=256,unique=True)
    passwordhash = models.CharField(max_length=128, blank=True, null=True)
    securitystamp = models.CharField(max_length=256, blank=True, null=True)
    email = models.CharField(max_length=256, blank=True, null=True)
    emailconfirmed = models.NullBooleanField()
    phonenumber = models.CharField(max_length=15, blank=True, null=True)
    phonenumberconfirmed = models.BooleanField()
    twofactorenabled = models.NullBooleanField()
    lockoutenddateutc = models.DateTimeField(blank=True, null=True)
    lockoutenabled = models.NullBooleanField()
    accessfailedcount = models.IntegerField()
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    createddatetime = models.DateTimeField()
    companyid = models.IntegerField(blank=True, null=True)
    roleid = models.CharField(max_length=10, blank=True, null=True)
    projectid = models.IntegerField(blank=True, null=True)
    token = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aspnetusers'
        verbose_name_plural = "Aspnetusers"


class Agent(models.Model):
    agentid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=256,unique=True)
    passwordhash = models.CharField(max_length=128, blank=True, null=True)
    email = models.CharField(max_length=256, blank=True, null=True)
    emailconfirmed = models.NullBooleanField()
    phonenumber = models.CharField(max_length=15, blank=True, null=True)
    phonenumberconfirmed = models.BooleanField()
    name = models.CharField(max_length=20)
    companyname = models.CharField(max_length=256)
    createddatetime = models.DateTimeField(auto_now_add=True, blank=True)
    roleid = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent'
        verbose_name_plural = "Agent"


class Attendance(models.Model):
    attendanceid = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=100)
    distancein = models.FloatField()
    attendence = models.BooleanField(default=False)
    datein = models.DateTimeField(blank=True, null=True)
    dateout = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    distanceout = models.FloatField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'attendance'
        verbose_name_plural = "Attendance"


class Company(models.Model):
    companyid = models.AutoField(primary_key=True)
    companyname = models.CharField(max_length=100)
    email = models.EmailField(max_length=70,blank=True, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    companyaddress = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    contactpersonname = models.CharField(max_length=50)
    contactphone = models.CharField(max_length=10)
    contactemail = models.CharField(max_length=100)
    activatedtill = models.DateTimeField()
    isactivated = models.NullBooleanField()
    logopath = models.TextField(blank=True, null=True)
    companytype = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'
        verbose_name_plural = "Company"


class Companytype(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'companytype'

class Document(models.Model):
    documentid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    projectid = models.IntegerField()
    link = models.FileField()

    class Meta:
        managed = False
        db_table = 'document'
        verbose_name_plural = "Document"

class Profilepics(models.Model):
    username = models.CharField(primary_key=True,max_length=100)
    pics = models.ImageField()

    class Meta:
        managed = False
        db_table = 'profilepics'
        verbose_name_plural = "profilepics"


class Integrations(models.Model):
    sourceid = models.IntegerField(blank=True, null=True)
    integrationkey = models.CharField(max_length=50, blank=True, null=True)
    integrationvalue = models.CharField(max_length=500, blank=True, null=True)
    companyid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'integrations'


class Jobruns(models.Model):
    jobrunid = models.AutoField(primary_key=True)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    noofleads = models.IntegerField()
    errormessage = models.TextField(blank=True, null=True)
    companyid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobruns'


class Kwdelhi(models.Model):
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    emailaddress = models.CharField(max_length=100, blank=True, null=True)
    telephonenumber = models.CharField(max_length=100, blank=True, null=True)
    comments = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kwdelhi'


class Leaditems(models.Model):
    leaditemid = models.AutoField(primary_key=True)
    leadid = models.IntegerField(blank=True, null=True)
    queryremarks = models.CharField(max_length=200, blank=True, null=True)
    typeofproperty = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    rangefrom = models.IntegerField(blank=True, null=True)
    rangeto = models.IntegerField(blank=True, null=True)
    cmpctlabel = models.TextField(blank=True, null=True)
    receivedon = models.DateTimeField(blank=True, null=True)
    projname = models.CharField(max_length=100, blank=True, null=True)
    assignedto = models.CharField(max_length=128, blank=True, null=True)
    builderinterest = models.NullBooleanField()
    statusid = models.IntegerField(blank=True, null=True)
    statusdate = models.DateTimeField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'leaditems'
        verbose_name_plural = "Leaditems"


class Leads(models.Model):
    leadid = models.AutoField(primary_key=True)
    createuserid = models.CharField(max_length=128, blank=True, null=True)
    createdatetimeoffset = models.DateTimeField(blank=True, null=True)
    edituserid = models.CharField(max_length=128, blank=True, null=True)
    editdatetimeoffset = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    phonenumber = models.CharField(max_length=14, blank=True, null=True)
    isassigned = models.NullBooleanField(default=False)
    companyid = models.IntegerField(blank=True, null=True)
    cmpctlabel = models.TextField(blank=True, null=True)
    receivedon = models.DateTimeField(auto_now_add=True)
    statusid = models.IntegerField(blank=True, null=True)
    id = models.CharField(max_length=150, blank=True, null=True)
    projectname = models.CharField(max_length=256, blank=True, null=True)
    city = models.CharField(max_length=256, blank=True, null=True)
    locality = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leads'
        verbose_name_plural = "Leads"


class Leadstatus(models.Model):
    statusid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'leadstatus'
        verbose_name_plural = "Leadstatus"


class Location(models.Model):
    locationid = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=100)
    username = models.CharField(max_length=30, blank=True, null=True)
    longitude = models.CharField(max_length=100)
    lattitude = models.CharField(max_length=100)
    companyid = models.IntegerField()
    lastupdated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'


class Project(models.Model):
    projectid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)
    lattitude = models.CharField(max_length=100, blank=True, null=True)
    companyid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'
        verbose_name_plural = "Project"


class Recording(models.Model):
    record = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recording'


class Recordings(models.Model):
    leadid = models.IntegerField()
    name = models.CharField(max_length=250)
    createdatetime = models.DateTimeField()
    createdby = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'recordings'


class Refreshtokens(models.Model):
    subject = models.CharField(max_length=50)
    clientid = models.CharField(max_length=50)
    issuedutc = models.DateTimeField()
    expiresutc = models.DateTimeField()
    protectedticket = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'refreshtokens'


class Sourcetypes(models.Model):
    source = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sourcetypes'

# class Profileimage(models.Model):
#     username = models.CharField(primary_key=True, max_length=100)
#     userimage = models.BYT
#
#     class Meta:
#         managed = False
#         db_table = 'sprofileimage'
