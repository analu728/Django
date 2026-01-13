from django.db import models

class Aula(models.Model):
    disciplina= models.CharField(max_length=50)
    professor= models.CharField(max_length=120)
    horario= models.DateTimeField()
    def __str__(self):
        return f'{self.disciplina} - {self.professor}'