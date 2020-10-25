from django.db import models


# Create your models here.
class Institutions(models.Model):
    institutionid = models.AutoField(db_column='InstitutionId', primary_key=True)  # Field name made lowercase.
    unitid = models.CharField(db_column='UNITID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    opeid = models.CharField(db_column='OPEID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    opeid6 = models.CharField(db_column='OPEID6', max_length=20, blank=True, null=True)  # Field name made lowercase.
    instname = models.CharField(db_column='InstName', max_length=200)  # Field name made lowercase.
    accredagency = models.CharField(db_column='AccredAgency', max_length=200)  # Field name made lowercase.
    insturl = models.CharField(db_column='InstURL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pricecalcurl = models.CharField(db_column='PriceCalcURL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    statefips = models.CharField(db_column='StateFIPS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    maincampus = models.TextField(db_column='MainCampus', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    numberofbranches = models.CharField(db_column='NumberOfBranches', max_length=2, blank=True, null=True)  # Field name made lowercase.
    predominantdegrees = models.CharField(db_column='PredominantDegrees', max_length=1, blank=True, null=True)  # Field name made lowercase.
    highestdegree = models.CharField(db_column='HighestDegree', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ownership = models.CharField(db_column='Ownership', max_length=1, blank=True, null=True)  # Field name made lowercase.
    distanceonly = models.TextField(db_column='DistanceOnly', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    locale = models.CharField(db_column='Locale', max_length=10, blank=True, null=True)  # Field name made lowercase.
    zipcodeid = models.ForeignKey('Zipcodes', models.DO_NOTHING, db_column='ZipCodeId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Institutions'

    def __str__(self):
        return self.instname


class Cities(models.Model):
    cityid = models.AutoField(db_column='CityId', primary_key=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=2)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cities'

    def __str__(self):
        return self.city + ", " + self.state


class Zipcodes(models.Model):
    zipcodeid = models.AutoField(db_column='ZipCodeId', primary_key=True)  # Field name made lowercase.
    cityid = models.ForeignKey(Cities, models.DO_NOTHING, db_column='CityId')  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZipCodes'

    def __str__(self):
        return self.zipcode
