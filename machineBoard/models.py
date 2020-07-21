from django.db import models

# Create your models here.


class MaintainerTeam(models.Model):
    nameTeam = models.CharField(max_length=64)
    passwordTeam = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.nameTeam}'


class Defaillance(models.Model):
    CAUSE_CHOICE = (
        ('1', 'Accident imprévisible'),
        ('2', 'Cause intrinsèque detectable'),
        ('3', 'Cause intrinsèque non detectable'),
        ('4', 'Défaut d\'entretien'),
        ('5', 'Mauvaise intervention antérieure'),
        ('6', 'Mauvaise conduite'),
        ('7', 'Consignes non respectées'),
        ('8', 'Autres'),
    )
    ORIGINE_CHOICE = (
        ('1', 'Origine mécanique'),
        ('2', 'Origine électrique'),
        ('3', 'Origine électronique'),
        ('4', 'Origine hydraulique'),
    )
    GRAVITE_CHOICE = (
        ('1', 'CRITIQUE'),
        ('2', 'MAJEURE'),
        ('3', 'MINEURE'),
    )

    cause = models.CharField(max_length=64, null=True,
                             blank=True, choices=CAUSE_CHOICE)
    origine = models.CharField(
        max_length=32, null=True, blank=True, choices=ORIGINE_CHOICE)
    gravite = models.CharField(
        max_length=32, null=True, blank=True, choices=GRAVITE_CHOICE)

    def __str__(self):
        return f'Cause: {self.get_cause_display()}, \n Origine: {self.get_origine_display()}, \n Gravité: {self.get_gravite_display()}'


class InfoIntervention(models.Model):
    defaillanceList = models.ForeignKey(
        Defaillance, on_delete=models.SET_NULL, null=True)
    dateDefaillance = models.DateField()
    dateIntervention = models.DateField()
    maintainerTeam = models.ForeignKey(
        MaintainerTeam, on_delete=models.SET_NULL, null=True)
    durationIntervention = models.FloatField()
    dateServiceOn = models.DateField()

    def __str__(self):
        return f'Intervention ID: {self.id}'


class Machine(models.Model):
    machineName = models.CharField(max_length=64)
    infoInterventionAll = models.ManyToManyField(
        InfoIntervention, related_name="machine")

    def __str__(self):
        return f'{self.machineName}'
