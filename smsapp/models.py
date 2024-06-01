from django.db import models
class StudentModel(models.Model):
	rno = models.IntegerField(primary_key = True)
	name = models.CharField(max_length=40)
	marks = models.IntegerField()
	
	def __str__(self):
		return self.name
