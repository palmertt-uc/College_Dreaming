from django.db import models


# Create your models here.
class Earnings(models.Model):
    earningid = models.AutoField(db_column='EarningId', primary_key=True)  # Field name made lowercase.
    opeid = models.CharField(db_column='OPEID', max_length=15)  # Field name made lowercase.
    degree_level = models.CharField(db_column='Degree_Level', max_length=2, blank=True, null=True)  # Field name made lowercase.
    oneyear50pct = models.FloatField(db_column='OneYear50Pct', blank=True, null=True)  # Field name made lowercase.
    fiveyear50pct = models.FloatField(db_column='FiveYear50Pct', blank=True, null=True)  # Field name made lowercase.
    tenyear50pct = models.FloatField(db_column='TenYear50Pct', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Earnings'

    def __str__(self):
        return "Earning: " + str(self.earningid)


class Crime(models.Model):
    crimeid = models.AutoField(db_column='CrimeId', primary_key=True)  # Field name made lowercase.
    msa = models.CharField(db_column='MSA', max_length=150)  # Field name made lowercase.
    violentcrimes = models.FloatField(db_column='ViolentCrimes', blank=True, null=True)  # Field name made lowercase.
    propertycrimes = models.FloatField(db_column='PropertyCrimes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Crime'

    def __str__(self):
        return "Crime: " + self.msa


class Climate(models.Model):
    climateid = models.AutoField(db_column='ClimateId', primary_key=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude')  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude')  # Field name made lowercase.
    mintemp = models.FloatField(db_column='MinTemp')  # Field name made lowercase.
    avgtemp = models.FloatField(db_column='AvgTemp')  # Field name made lowercase.
    maxtemp = models.FloatField(db_column='MaxTemp')  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Climate'

    def __str__(self):
        return "Climate Zipcode: " + self.zipcode


class Cities(models.Model):
    cityid = models.AutoField(db_column='CityId', primary_key=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=2)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=2)  # Field name made lowercase.
    bars = models.IntegerField(db_column='Bars', blank=True, null=True)  # Field name made lowercase.
    crimeid = models.ForeignKey('Crime', models.DO_NOTHING, db_column='CrimeId', blank=True, null=True)  # Field name made lowercase.

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
    climateid = models.ForeignKey(Climate, models.DO_NOTHING, db_column='ClimateId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Institutions'
        ordering = ['maincampus']

    def __str__(self):
        return self.instname

    @property
    def institution_url(self):
        if self.insturl == 'NULL':
            return 'Not Reported'
        else:
            return self.insturl

    @property
    def main_campus(self):
        if ord(self.maincampus) == 1:
            return 'Yes'
        else:
            return 'No'

    @property
    def highest_degree(self):
        if self.highestdegree == '0':
            return 'Highest Degree Offered: Not Reported'
        elif self.highestdegree == '1':
            return 'Highest Degree Offered: Associate Degree'
        elif self.highestdegree == '2':
            return "Highest Degree Offered: Bachelor's Degree"
        elif self.highestdegree == '3':
            return "Highest Degree Offered: Master's Degree"
        elif self.highestdegree == '4':
            return 'Highest Degree Offered: Doctorate Degree'

    @property
    def predominant_degree(self):
        if self.predominantdegrees == '0':
            return 'Predominant Degree: Not Reported'
        elif self.predominantdegrees == '1':
            return 'Predominant Degree: Associate Degree'
        elif self.predominantdegrees == '2':
            return "Predominant Degree: Bachelor's Degree"
        elif self.predominantdegrees == '3':
            return "Predominant Degree: Master's Degree"
        elif self.predominantdegrees == '4':
            return 'Predominant Degree: Doctorate Degree'


class Admissions(models.Model):
    admissionid = models.AutoField(db_column='AdmissionId', primary_key=True)  # Field name made lowercase.
    institutionid = models.ForeignKey('Institutions', models.DO_NOTHING,
                                      db_column='InstitutionId')  # Field name made lowercase.
    admission_rate_overall = models.FloatField(blank=True, null=True)
    admission_rate_by_ope_id = models.FloatField(blank=True, null=True)
    sat_scores_25th_percentile_critical_reading = models.FloatField(blank=True, null=True)
    sat_scores_75th_percentile_critical_reading = models.FloatField(blank=True, null=True)
    sat_scores_25th_percentile_math = models.FloatField(blank=True, null=True)
    sat_scores_75th_percentile_math = models.FloatField(blank=True, null=True)
    sat_scores_25th_percentile_writing = models.FloatField(blank=True, null=True)
    sat_scores_75th_percentile_writing = models.FloatField(blank=True, null=True)
    sat_scores_midpoint_critical_reading = models.FloatField(blank=True, null=True)
    sat_scores_midpoint_math = models.FloatField(blank=True, null=True)
    sat_scores_midpoint_writing = models.FloatField(blank=True, null=True)
    act_scores_25th_percentile_cumulative = models.FloatField(blank=True, null=True)
    act_scores_75th_percentile_cumulative = models.FloatField(blank=True, null=True)
    act_scores_25th_percentile_english = models.FloatField(blank=True, null=True)
    act_scores_75th_percentile_english = models.FloatField(blank=True, null=True)
    act_scores_25th_percentile_math = models.FloatField(blank=True, null=True)
    act_scores_75th_percentile_math = models.FloatField(blank=True, null=True)
    act_scores_25th_percentile_writing = models.FloatField(blank=True, null=True)
    act_scores_75th_percentile_writing = models.FloatField(blank=True, null=True)
    act_scores_midpoint_cumulative = models.FloatField(blank=True, null=True)
    act_scores_midpoint_english = models.FloatField(blank=True, null=True)
    act_scores_midpoint_math = models.FloatField(blank=True, null=True)
    act_scores_midpoint_writing = models.FloatField(blank=True, null=True)
    sat_scores_average_overall = models.FloatField(blank=True, null=True)
    sat_scores_average_by_ope_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Admissions'

    def __str__(self):
        return self.institutionid.instname + ' - Admission'

    @property
    def admission_rate(self):
        if self.admission_rate_overall == 0:
            return 'Not Reported'
        else:
            return '{:.1%}'.format(self.admission_rate_overall)

    @property
    def average_sat_score(self):
        if self.sat_scores_average_overall == 0:
            return 'Not Reported'
        else:
            return round(self.sat_scores_average_overall)

    @property
    def average_act_score(self):
        if self.act_scores_midpoint_cumulative == 0:
            return 'Not Reported'
        else:
            return round(self.act_scores_midpoint_cumulative)


class Completionrates(models.Model):
    completionrateid = models.AutoField(db_column='CompletionRateId', primary_key=True)  # Field name made lowercase.
    institutionid = models.ForeignKey('Institutions', models.DO_NOTHING,
                                      db_column='InstitutionId')  # Field name made lowercase.
    completion_rate_4yr_150_white = models.FloatField(blank=True, null=True)
    completion_rate_4yr_150_black = models.FloatField(blank=True, null=True)
    completion_rate_4yr_150_hispanic = models.FloatField(blank=True, null=True)
    completion_rate_4yr_150_asian = models.FloatField(blank=True, null=True)
    completion_rate_4yr_150_aian = models.FloatField(blank=True, null=True)
    completion_rate_4yr_150_nhpi = models.FloatField(blank=True, null=True)
    completion_rate_4yr_150_2ormore = models.FloatField(blank=True, null=True)
    completion_rate_4yr_150_nonresident_alien = models.FloatField(blank=True, null=True)
    completion_rate_4yr_150_race_unknown = models.FloatField(blank=True, null=True)
    completion_rate_l4yr_150_white = models.FloatField(blank=True, null=True)
    completion_rate_l4yr_150_black = models.FloatField(blank=True, null=True)
    completion_rate_l4yr_150_hispanic = models.FloatField(blank=True, null=True)
    completion_rate_l4yr_150_asian = models.FloatField(blank=True, null=True)
    completion_rate_l4yr_150_aian = models.FloatField(blank=True, null=True)
    completion_rate_l4yr_150_nhpi = models.FloatField(blank=True, null=True)
    completion_rate_l4yr_150_2ormore = models.FloatField(blank=True, null=True)
    completion_rate_l4yr_150_nonresident_alien = models.FloatField(blank=True, null=True)
    completion_rate_l4yr_150_race_unknown = models.FloatField(blank=True, null=True)
    completion_rate_4yr_200nt = models.FloatField(blank=True, null=True)
    completion_rate_less_than_4yr_200nt = models.FloatField(blank=True, null=True)
    completion_rate_4yr_150nt = models.FloatField(blank=True, null=True)
    completion_rate_less_than_4yr_150 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CompletionRates'

    def __str__(self):
        return self.institutionid.instname + ' - Completion Rate'

    @property
    def total_4year_completion_rate(self):
        if self.completion_rate_4yr_150nt == 0:
            return 'Not Reported'
        else:
            return '{:.1%}'.format(self.completion_rate_4yr_150nt)


class Costs(models.Model):
    costsid = models.AutoField(db_column='CostsId', primary_key=True)  # Field name made lowercase.
    institutionid = models.ForeignKey('Institutions', models.DO_NOTHING,
                                      db_column='InstitutionId')  # Field name made lowercase.
    avg_net_price_public = models.FloatField(blank=True, null=True)
    avg_net_price_private = models.FloatField(blank=True, null=True)
    net_price_public_by_income_level_0_to_30000 = models.FloatField(blank=True, null=True)
    net_price_public_by_income_level_30001_to_48000 = models.FloatField(blank=True, null=True)
    net_price_public_by_income_level_48001_to_75000 = models.FloatField(blank=True, null=True)
    net_price_public_by_income_level_75001_to_110000 = models.FloatField(blank=True, null=True)
    net_price_public_by_income_level_110001_to_plus = models.FloatField(blank=True, null=True)
    net_price_private_by_income_level_0_to_30000 = models.FloatField(blank=True, null=True)
    net_price_private_by_income_level_30001_to_48000 = models.FloatField(blank=True, null=True)
    net_price_private_by_income_level_48001_to_75000 = models.FloatField(blank=True, null=True)
    net_price_private_by_income_level_75001_to_110000 = models.FloatField(blank=True, null=True)
    net_price_private_by_income_level_110001_to_plus = models.FloatField(blank=True, null=True)
    net_price_public_by_income_level_0_to_48000 = models.FloatField(blank=True, null=True)
    net_price_private_by_income_level_0_to_48000 = models.FloatField(blank=True, null=True)
    net_price_public_by_income_level_30001_to_75000 = models.FloatField(blank=True, null=True)
    net_price_private_by_income_level_30001_to_75000 = models.FloatField(blank=True, null=True)
    net_price_public_by_income_level_75000_to_plus = models.FloatField(blank=True, null=True)
    net_price_private_by_income_level_75000_to_plus = models.FloatField(blank=True, null=True)
    attendance_academic_year = models.FloatField(blank=True, null=True)
    attendance_program_year = models.FloatField(blank=True, null=True)
    tuition_in_state = models.FloatField(blank=True, null=True)
    tuition_out_of_state = models.FloatField(blank=True, null=True)
    tuition_program_year = models.FloatField(blank=True, null=True)
    instructional_expenditure_per_fte = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Costs'

    def __str__(self):
        return self.institutionid.instname + ' - Cost'

    @property
    def in_state_tuition(self):
        if self.tuition_in_state == 0:
            return 'Not Reported'
        else:
            return '${:,.2f}'.format(self.tuition_in_state)

    @property
    def out_state_tuition(self):
        if self.tuition_out_of_state == 0:
            return 'Not Reported'
        else:
            return '${:,.2f}'.format(self.tuition_out_of_state)


class Institutiontypes(models.Model):
    institutiontypeid = models.AutoField(db_column='InstitutionTypeId', primary_key=True)  # Field name made lowercase.
    institutionid = models.ForeignKey('Institutions', models.DO_NOTHING,
                                      db_column='InstitutionId')  # Field name made lowercase.
    ccbasic = models.IntegerField(db_column='CCBASIC', blank=True, null=True)  # Field name made lowercase.
    ccugprof = models.IntegerField(db_column='CCUGPROF', blank=True, null=True)  # Field name made lowercase.
    ccsizset = models.IntegerField(db_column='CCSIZSET', blank=True, null=True)  # Field name made lowercase.
    hbcu = models.TextField(db_column='HBCU', blank=True,
                            null=True)  # Field name made lowercase. This field type is a guess.
    pbi = models.TextField(db_column='PBI', blank=True,
                           null=True)  # Field name made lowercase. This field type is a guess.
    annhi = models.TextField(db_column='ANNHI', blank=True,
                             null=True)  # Field name made lowercase. This field type is a guess.
    tribal = models.TextField(db_column='TRIBAL', blank=True,
                              null=True)  # Field name made lowercase. This field type is a guess.
    aanapii = models.TextField(db_column='AANAPII', blank=True,
                               null=True)  # Field name made lowercase. This field type is a guess.
    hsi = models.TextField(db_column='HSI', blank=True,
                           null=True)  # Field name made lowercase. This field type is a guess.
    nanti = models.TextField(db_column='NANTI', blank=True,
                             null=True)  # Field name made lowercase. This field type is a guess.
    menonly = models.TextField(db_column='MENONLY', blank=True,
                               null=True)  # Field name made lowercase. This field type is a guess.
    womenonly = models.TextField(db_column='WOMENONLY', blank=True,
                                 null=True)  # Field name made lowercase. This field type is a guess.
    relaffil = models.IntegerField(db_column='RELAFFIL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InstitutionTypes'

    def __str__(self):
        return self.institutionid.instname + ' - Institution Type'

    @property
    def institution_type(self):
        if ord(self.hbcu) == 1:
            return 'Historically Black Institution'
        elif ord(self.pbi) == 1:
            return 'Predominately Black Institution'
        elif ord(self.annhi) == 1:
            return 'Alaskan Native or Native Hawaiian-Serving Institution'
        elif ord(self.hsi) == 1:
            return 'Hispanic-Serving Institution'
        elif ord(self.nanti) == 1:
            return 'Native American Non-Tribal Institution'
        elif ord(self.menonly) == 1:
            return 'Men Only Institution'
        elif ord(self.womenonly) == 1:
            return 'Women Only Institution'
        elif self.relaffil > 0:
            return 'Religious Institution'
        else:
            'Not Reported'


class Majors(models.Model):
    majorid = models.AutoField(db_column='MajorId', primary_key=True)  # Field name made lowercase.
    institutionid = models.ForeignKey(Institutions, models.DO_NOTHING,
                                      db_column='InstitutionId')  # Field name made lowercase.
    agriculture = models.FloatField(blank=True, null=True)
    resources = models.FloatField(blank=True, null=True)
    architecture = models.FloatField(blank=True, null=True)
    ethnic_cultural_gender = models.FloatField(blank=True, null=True)
    communication = models.FloatField(blank=True, null=True)
    communications_technology = models.FloatField(blank=True, null=True)
    computer = models.FloatField(blank=True, null=True)
    personal_culinary = models.FloatField(blank=True, null=True)
    education = models.FloatField(blank=True, null=True)
    engineering = models.FloatField(blank=True, null=True)
    engineering_technology = models.FloatField(blank=True, null=True)
    language = models.FloatField(blank=True, null=True)
    family_consumer_science = models.FloatField(blank=True, null=True)
    legal = models.FloatField(blank=True, null=True)
    english = models.FloatField(blank=True, null=True)
    humanities = models.FloatField(blank=True, null=True)
    library = models.FloatField(blank=True, null=True)
    biological = models.FloatField(blank=True, null=True)
    mathematics = models.FloatField(blank=True, null=True)
    military = models.FloatField(blank=True, null=True)
    multidiscipline = models.FloatField(blank=True, null=True)
    parks_recreation_fitness = models.FloatField(blank=True, null=True)
    philosophy_religious = models.FloatField(blank=True, null=True)
    theology_religious_vocation = models.FloatField(blank=True, null=True)
    physical_science = models.FloatField(blank=True, null=True)
    science_technology = models.FloatField(blank=True, null=True)
    psychology = models.FloatField(blank=True, null=True)
    security_law_enforcement = models.FloatField(blank=True, null=True)
    public_administration_social_service = models.FloatField(blank=True, null=True)
    social_science = models.FloatField(blank=True, null=True)
    construction = models.FloatField(blank=True, null=True)
    mechanic_repair_technology = models.FloatField(blank=True, null=True)
    precision_production = models.FloatField(blank=True, null=True)
    transportation = models.FloatField(blank=True, null=True)
    visual_performing = models.FloatField(blank=True, null=True)
    health = models.FloatField(blank=True, null=True)
    business_marketing = models.FloatField(blank=True, null=True)
    history = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Majors'

    def __str__(self):
        return self.institutionid.instname + ' - Majors'

    @property
    def history_percentage(self):
        return '{:.1%}'.format(self.history)

    @property
    def business_marketing_percentage(self):
        return '{:.1%}'.format(self.business_marketing)

    @property
    def health_percentage(self):
        return '{:.1%}'.format(self.health)

    @property
    def visual_performing_percentage(self):
        return '{:.1%}'.format(self.visual_performing)

    @property
    def transportation_percentage(self):
        return '{:.1%}'.format(self.transportation)

    @property
    def precision_production_percentage(self):
        return '{:.1%}'.format(self.precision_production)

    @property
    def mechanic_repair_technology_percentage(self):
        return '{:.1%}'.format(self.mechanic_repair_technology)

    @property
    def construction_percentage(self):
        return '{:.1%}'.format(self.construction)

    @property
    def social_science_percentage(self):
        return '{:.1%}'.format(self.social_science)

    @property
    def public_administration_social_service_percentage(self):
        return '{:.1%}'.format(self.public_administration_social_service)

    @property
    def security_law_enforcement_percentage(self):
        return '{:.1%}'.format(self.security_law_enforcement)

    @property
    def psychology_percentage(self):
        return '{:.1%}'.format(self.psychology)

    @property
    def science_technology_percentage(self):
        return '{:.1%}'.format(self.science_technology)

    @property
    def physical_science_percentage(self):
        return '{:.1%}'.format(self.physical_science)

    @property
    def theology_religious_vocation_percentage(self):
        return '{:.1%}'.format(self.theology_religious_vocation)

    @property
    def philosophy_religious_percentage(self):
        return '{:.1%}'.format(self.philosophy_religious)

    @property
    def parks_recreation_fitness_percentage(self):
        return '{:.1%}'.format(self.parks_recreation_fitness)

    @property
    def multidiscipline_percentage(self):
        return '{:.1%}'.format(self.multidiscipline)

    @property
    def military_percentage(self):
        return '{:.1%}'.format(self.military)

    @property
    def mathematics_percentage(self):
        return '{:.1%}'.format(self.mathematics)

    @property
    def biological_percentage(self):
        return '{:.1%}'.format(self.biological)

    @property
    def library_percentage(self):
        return '{:.1%}'.format(self.library)

    @property
    def humanities_percentage(self):
        return '{:.1%}'.format(self.humanities)

    @property
    def english_percentage(self):
        return '{:.1%}'.format(self.english)

    @property
    def legal_percentage(self):
        return '{:.1%}'.format(self.legal)

    @property
    def family_consumer_science_percentage(self):
        return '{:.1%}'.format(self.family_consumer_science)

    @property
    def agriculture_percentage(self):
        return '{:.1%}'.format(self.agriculture)

    @property
    def resources_percentage(self):
        return '{:.1%}'.format(self.resources)

    @property
    def architecture_percentage(self):
        return '{:.1%}'.format(self.architecture)

    @property
    def ethnic_cultural_gender_percentage(self):
        return '{:.1%}'.format(self.ethnic_cultural_gender)

    @property
    def communication_percentage(self):
        return '{:.1%}'.format(self.communication)

    @property
    def communications_technology_percentage(self):
        return '{:.1%}'.format(self.communications_technology)

    @property
    def computer_percentage(self):
        return '{:.1%}'.format(self.computer)

    @property
    def personal_culinary_percentage(self):
        return '{:.1%}'.format(self.personal_culinary)

    @property
    def education_percentage(self):
        return '{:.1%}'.format(self.education)

    @property
    def engineering_percentage(self):
        return '{:.1%}'.format(self.engineering)

    @property
    def engineering_technology_percentage(self):
        return '{:.1%}'.format(self.engineering_technology)

    @property
    def language_percentage(self):
        return '{:.1%}'.format(self.language)


class Programs(models.Model):
    programsid = models.AutoField(db_column='ProgramsId', primary_key=True)  # Field name made lowercase.
    institutionid = models.ForeignKey(Institutions, models.DO_NOTHING,
                                      db_column='InstitutionId')  # Field name made lowercase.
    program_certificate_lt_1_yr_agriculture = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_agriculture = models.IntegerField(blank=True, null=True)
    program_assoc_agriculture = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_agriculture = models.IntegerField(blank=True, null=True)
    program_bachelors_agriculture = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_resources = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_resources = models.IntegerField(blank=True, null=True)
    program_assoc_resources = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_resources = models.IntegerField(blank=True, null=True)
    program_bachelors_resources = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_architecture = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_architecture = models.IntegerField(blank=True, null=True)
    program_assoc_architecture = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_architecture = models.IntegerField(blank=True, null=True)
    program_bachelors_architecture = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_ethnic_cultural_gender = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_ethnic_cultural_gender = models.IntegerField(blank=True, null=True)
    program_assoc_ethnic_cultural_gender = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_ethnic_cultural_gender = models.IntegerField(blank=True, null=True)
    program_bachelors_ethnic_cultural_gender = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_communication = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_communication = models.IntegerField(blank=True, null=True)
    program_assoc_communication = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_communication = models.IntegerField(blank=True, null=True)
    program_bachelors_communication = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_communications_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_communications_technology = models.IntegerField(blank=True, null=True)
    program_assoc_communications_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_communications_technology = models.IntegerField(blank=True, null=True)
    program_bachelors_communications_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_computer = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_computer = models.IntegerField(blank=True, null=True)
    program_assoc_computer = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_computer = models.IntegerField(blank=True, null=True)
    program_bachelors_computer = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_personal_culinary = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_personal_culinary = models.IntegerField(blank=True, null=True)
    program_assoc_personal_culinary = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_personal_culinary = models.IntegerField(blank=True, null=True)
    program_bachelors_personal_culinary = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_education = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_education = models.IntegerField(blank=True, null=True)
    program_assoc_education = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_education = models.IntegerField(blank=True, null=True)
    program_bachelors_education = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_engineering = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_engineering = models.IntegerField(blank=True, null=True)
    program_assoc_engineering = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_engineering = models.IntegerField(blank=True, null=True)
    program_bachelors_engineering = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_engineering_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_engineering_technology = models.IntegerField(blank=True, null=True)
    program_assoc_engineering_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_engineering_technology = models.IntegerField(blank=True, null=True)
    program_bachelors_engineering_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_language = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_language = models.IntegerField(blank=True, null=True)
    program_assoc_language = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_language = models.IntegerField(blank=True, null=True)
    program_bachelors_language = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_family_consumer_science = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_family_consumer_science = models.IntegerField(blank=True, null=True)
    program_assoc_family_consumer_science = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_family_consumer_science = models.IntegerField(blank=True, null=True)
    program_bachelors_family_consumer_science = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_legal = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_legal = models.IntegerField(blank=True, null=True)
    program_assoc_legal = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_legal = models.IntegerField(blank=True, null=True)
    program_bachelors_legal = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_english = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_english = models.IntegerField(blank=True, null=True)
    program_assoc_english = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_english = models.IntegerField(blank=True, null=True)
    program_bachelors_english = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_humanities = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_humanities = models.IntegerField(blank=True, null=True)
    program_assoc_humanities = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_humanities = models.IntegerField(blank=True, null=True)
    program_bachelors_humanities = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_library = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_library = models.IntegerField(blank=True, null=True)
    program_assoc_library = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_library = models.IntegerField(blank=True, null=True)
    program_bachelors_library = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_biological = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_biological = models.IntegerField(blank=True, null=True)
    program_assoc_biological = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_biological = models.IntegerField(blank=True, null=True)
    program_bachelors_biological = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_mathematics = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_mathematics = models.IntegerField(blank=True, null=True)
    program_assoc_mathematics = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_mathematics = models.IntegerField(blank=True, null=True)
    program_bachelors_mathematics = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_military = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_military = models.IntegerField(blank=True, null=True)
    program_assoc_military = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_military = models.IntegerField(blank=True, null=True)
    program_bachelors_military = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_multidiscipline = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_multidiscipline = models.IntegerField(blank=True, null=True)
    program_assoc_multidiscipline = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_multidiscipline = models.IntegerField(blank=True, null=True)
    program_bachelors_multidiscipline = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_parks_recreation_fitness = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_parks_recreation_fitness = models.IntegerField(blank=True, null=True)
    program_assoc_parks_recreation_fitness = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_parks_recreation_fitness = models.IntegerField(blank=True, null=True)
    program_bachelors_parks_recreation_fitness = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_philosophy_religious = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_philosophy_religious = models.IntegerField(blank=True, null=True)
    program_assoc_philosophy_religious = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_philosophy_religious = models.IntegerField(blank=True, null=True)
    program_bachelors_philosophy_religious = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_theology_religious_vocation = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_theology_religious_vocation = models.IntegerField(blank=True, null=True)
    program_assoc_theology_religious_vocation = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_theology_religious_vocation = models.IntegerField(blank=True, null=True)
    program_bachelors_theology_religious_vocation = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_physical_science = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_physical_science = models.IntegerField(blank=True, null=True)
    program_assoc_physical_science = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_physical_science = models.IntegerField(blank=True, null=True)
    program_bachelors_physical_science = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_science_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_science_technology = models.IntegerField(blank=True, null=True)
    program_assoc_science_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_science_technology = models.IntegerField(blank=True, null=True)
    program_bachelors_science_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_psychology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_psychology = models.IntegerField(blank=True, null=True)
    program_assoc_psychology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_psychology = models.IntegerField(blank=True, null=True)
    program_bachelors_psychology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_security_law_enforcement = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_security_law_enforcement = models.IntegerField(blank=True, null=True)
    program_assoc_security_law_enforcement = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_security_law_enforcement = models.IntegerField(blank=True, null=True)
    program_bachelors_security_law_enforcement = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_public_administration_social_service = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_public_administration_social_service = models.IntegerField(blank=True, null=True)
    program_assoc_public_administration_social_service = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_public_administration_social_service = models.IntegerField(blank=True, null=True)
    program_bachelors_public_administration_social_service = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_social_science = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_social_science = models.IntegerField(blank=True, null=True)
    program_assoc_social_science = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_social_science = models.IntegerField(blank=True, null=True)
    program_bachelors_social_science = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_construction = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_construction = models.IntegerField(blank=True, null=True)
    program_assoc_construction = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_construction = models.IntegerField(blank=True, null=True)
    program_bachelors_construction = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_mechanic_repair_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_mechanic_repair_technology = models.IntegerField(blank=True, null=True)
    program_assoc_mechanic_repair_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_mechanic_repair_technology = models.IntegerField(blank=True, null=True)
    program_bachelors_mechanic_repair_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_precision_production = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_precision_production = models.IntegerField(blank=True, null=True)
    program_assoc_precision_production = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_precision_production = models.IntegerField(blank=True, null=True)
    program_bachelors_precision_production = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_transportation = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_transportation = models.IntegerField(blank=True, null=True)
    program_assoc_transportation = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_transportation = models.IntegerField(blank=True, null=True)
    program_bachelors_transportation = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_visual_performing = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_visual_performing = models.IntegerField(blank=True, null=True)
    program_assoc_visual_performing = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_visual_performing = models.IntegerField(blank=True, null=True)
    program_bachelors_visual_performing = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_health = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_health = models.IntegerField(blank=True, null=True)
    program_assoc_health = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_health = models.IntegerField(blank=True, null=True)
    program_bachelors_health = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_business_marketing = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_business_marketing = models.IntegerField(blank=True, null=True)
    program_assoc_business_marketing = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_business_marketing = models.IntegerField(blank=True, null=True)
    program_bachelors_business_marketing = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_history = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_history = models.IntegerField(blank=True, null=True)
    program_assoc_history = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_history = models.IntegerField(blank=True, null=True)
    program_bachelors_history = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Programs'

    def __str__(self):
        return self.institutionid.instname + ' - ProgramID'


class Undergraduates(models.Model):
    undergraduateid = models.AutoField(db_column='UndergraduateId', primary_key=True)  # Field name made lowercase.
    institutionid = models.ForeignKey(Institutions, models.DO_NOTHING,
                                      db_column='InstitutionId')  # Field name made lowercase.
    enrollment_degree_seeking = models.FloatField(blank=True, null=True)
    demographics_white = models.FloatField(blank=True, null=True)
    demographics_black = models.FloatField(blank=True, null=True)
    demographics_hispanic = models.FloatField(blank=True, null=True)
    demographics_ai_an = models.FloatField(blank=True, null=True)
    demographics_asian = models.FloatField(blank=True, null=True)
    demographics_nhpi = models.FloatField(blank=True, null=True)
    demographics_multiracial = models.FloatField(blank=True, null=True)
    demographics_non_resident_alien = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Undergraduates'

    def __str__(self):
        return self.institutionid.instname + ' - Undergraduates'

    @property
    def check_demographics_equals_zero(self):
        if self.demographics_nhpi == 0 and self.demographics_asian == 0 and self.demographics_non_resident_alien == 0 \
                and self.demographics_multiracial == 0 and self.demographics_ai_an == 0 and \
                self.demographics_black == 0 and self.demographics_hispanic == 0 \
                and self.demographics_white == 0:
            return 0

    @property
    def check_demographics_is_none(self):
        if self.demographics_nhpi is None or self.demographics_asian is None or self.demographics_non_resident_alien is None \
                or self.demographics_multiracial is None or self.demographics_ai_an is None or \
                self.demographics_black is None or self.demographics_hispanic is None \
                or self.demographics_white is None:
            return 0

    @property
    def undergraduate_students(self):
        if self.enrollment_degree_seeking == 0:
            return 'Not Reported'
        return '{:,.0f}'.format(self.enrollment_degree_seeking)

    @property
    def american_indian_alaskan_native(self):
        if self.demographics_ai_an == 0:
            return '0%'
        else:
            return '{:.1%}'.format(self.demographics_ai_an)

    @property
    def white_students(self):
        if self.demographics_white == 0:
            return '0%'
        else:
            return '{:.1%}'.format(self.demographics_white)

    @property
    def black_students(self):
        if self.demographics_black == 0:
            return '0%'
        else:
            return '{:.1%}'.format(self.demographics_black)

    @property
    def hispanic_students(self):
        if self.demographics_hispanic == 0:
            return '0%'
        else:
            return '{:.1%}'.format(self.demographics_hispanic)

    @property
    def asian_students(self):
        if self.demographics_asian == 0:
            return '0%'
        else:
            return '{:.1%}'.format(self.demographics_asian)

    @property
    def pacific_islander_students(self):
        if self.demographics_nhpi == 0:
            return '0%'
        else:
            return '{:.1%}'.format(self.demographics_nhpi)

    @property
    def multiracial_students(self):
        if self.demographics_multiracial == 0:
            return '0%'
        else:
            return '{:.1%}'.format(self.demographics_multiracial)

    @property
    def non_resident_students(self):
        if self.demographics_non_resident_alien == 0:
            return 'Not Reported/0%'
        else:
            return '{:.1%}'.format(self.demographics_non_resident_alien)
