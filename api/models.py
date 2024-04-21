from django.db import models


class Circuit(models.Model):
    circuitId = models.AutoField(primary_key=True)
    circuitRef = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    lat = models.FloatField()
    lng = models.FloatField()
    alt = models.IntegerField()
    url = models.URLField()


class Constructor(models.Model):
    constructorId = models.AutoField(primary_key=True)
    constructorRef = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    url = models.URLField()


class Driver(models.Model):
    driverId = models.AutoField(primary_key=True)
    driverRef = models.CharField(max_length=255)
    number = models.IntegerField()
    code = models.CharField(max_length=255)
    forename = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    dob = models.DateField()
    nationality = models.CharField(max_length=255)
    url = models.URLField()


class Race(models.Model):
    raceId = models.AutoField(primary_key=True)
    year = models.IntegerField()
    round = models.IntegerField()
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    url = models.URLField()
    fp1_date = models.DateField()
    fp1_time = models.TimeField()
    fp2_date = models.DateField()
    fp2_time = models.TimeField()
    fp3_date = models.DateField()
    fp3_time = models.TimeField()
    quali_date = models.DateField()
    quali_time = models.TimeField()
    sprint_date = models.DateField()
    sprint_time = models.TimeField()


class Qualifying(models.Model):
    qualifyId = models.AutoField(primary_key=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    constructor = models.ForeignKey(Constructor, on_delete=models.CASCADE)
    number = models.IntegerField()
    position = models.IntegerField()
    q1 = models.DurationField()
    q2 = models.DurationField()
    q3 = models.DurationField()


class Season(models.Model):
    year = models.IntegerField(primary_key=True)
    url = models.URLField()


class Status(models.Model):
    statusId = models.AutoField(primary_key=True)
    status = models.CharField(max_length=255)


class Result(models.Model):
    resultId = models.AutoField(primary_key=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    constructor = models.ForeignKey(Constructor, on_delete=models.CASCADE)
    number = models.IntegerField()
    grid = models.IntegerField()
    position = models.IntegerField()
    positionText = models.CharField(max_length=255)
    positionOrder = models.IntegerField()
    points = models.IntegerField()


class ConstructorResult(models.Model):
    constructorResultId = models.AutoField(primary_key=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    constructor = models.ForeignKey(Constructor, on_delete=models.CASCADE)
    points = models.IntegerField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)


class ConstructorStanding(models.Model):
    constructorStandingId = models.AutoField(primary_key=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    constructor = models.ForeignKey(Constructor, on_delete=models.CASCADE)
    points = models.IntegerField()
    position = models.IntegerField()
    positionText = models.CharField(max_length=255)
    wins = models.IntegerField()


class DriverStanding(models.Model):
    driverStandingId = models.AutoField(primary_key=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    points = models.IntegerField()
    position = models.IntegerField()
    positionText = models.CharField(max_length=255)
    wins = models.IntegerField()


class LapTimes(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    lap = models.IntegerField()
    position = models.IntegerField()
    time = models.DurationField()
    milliseconds = models.IntegerField()


class PitStops(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    stop = models.IntegerField()
    lap = models.IntegerField()
    time = models.DurationField()
    duration = models.DurationField()
    milliseconds = models.IntegerField()


class SprintResult(models.Model):
    resultId = models.AutoField(primary_key=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    constructor = models.ForeignKey(Constructor, on_delete=models.CASCADE)
    number = models.IntegerField()
    grid = models.IntegerField()
    position = models.IntegerField()
    positionText = models.CharField(max_length=255)
    positionOrder = models.IntegerField()
    points = models.IntegerField()