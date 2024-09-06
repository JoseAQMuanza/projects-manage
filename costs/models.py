from django.db import models

class Project(models.Model):  
  id_project = models.AutoField(primary_key=True)
  name = models.TextField(max_length=30, null=False)
  budget = models.TextField(max_length=15, null=False)
  categories = models.TextField(max_length=30, null=False)

  def __str__(self):
    return self.name
  
class Service(models.Model):
  project = models.ForeignKey(Project, related_name='service', on_delete=models.CASCADE, null=False)  
  name = models.CharField(max_length=30, null=False)
  cost = models.TextField(max_length=15, null=False)  
  description = models.TextField(max_length=100, null=False)

  def __str__(self):
    return self.name
