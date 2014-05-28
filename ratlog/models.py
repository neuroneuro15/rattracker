from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

#Used to add a rat to the database
class Rat(models.Model):
	name = models.CharField(max_length=15)
	start_date = models.DateField('first day of handling')
	date_of_birth = models.DateField('Date of Birth')
	
	strain = models.CharField(max_length=30, default='Long Evans')
	
	SEX_CHOICES = (
		('M', 'Male'),
		('F', 'Female')
	)
	sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='M')
	
	protocol = models.CharField(max_length=50, blank=True)
	comments = models.CharField(max_length=200, blank=True)
	
	def __unicode__(self):
		return self.name

#Enter the Cage Number of the Rat	
class Cage(models.Model):
	rat = models.ForeignKey(Rat)
	date = models.DateField('When Transferred to Cage')
	cage = models.IntegerField()


### Behavior ###
class Task(models.Model):
	name = models.CharField(verbose_name='Name of Task',max_length = 100)
	maze_name = models.CharField(verbose_name='Name of Maze or Environment',max_length = 100)
	#TO BE ADDED LATER
	#paradigm_file = 
	#maze_image = 
	description = models.CharField(max_length=300, blank=True)
	
	def __unicode__(self):
		return "{0} in {1}".format(self.name,self.maze_name)


class Session(models.Model):
	rat = models.ForeignKey(Rat)	
	date = models.DateTimeField('Date of Behavioral Session',default=timezone.now())
	length = models.FloatField(verbose_name='Length of Behavioral Session (hours)')
	
	task = models.ForeignKey(Task)
	task_learned = models.BooleanField('Rat Appears to Have Learned the Task.')
	
	
	
	motivation = models.FloatField(verbose_name='How Motivated Did the Rat Seem? (Recc. Range: 0-10)')
	
	comments = models.CharField(max_length=200, blank=True)
	
	def __unicode__(self):
		return "{0}: {1} on {2}".format(self.rat, self.task, self.date)


#Enter the rat's weight	
class Weight(models.Model):
	session = models.ForeignKey(Session)
	weight = models.FloatField()
	
	
	comments = models.CharField(max_length=200, blank=True)
	
	def __unicode__(self):
		return '{0}: {1}g'.format(self.session, self.weight)


	
#Water Given to the Rat (If free, enter 1000ml)
class Water(models.Model):
	session = models.ForeignKey(Session)
	
	date = models.DateTimeField('Date Water Given',default=timezone.now())
	
	CONTEXT_CHOICES = (
		('Free', 'Free Water'),
		('Restriction', 'Set Amount/Time Water Given, for water restriction'),
		('Task', 'Given as Reward for Task'),
		('PostTask', 'Extra Water Given after Task is completed')
		
	)
	context = models.CharField(max_length=15, choices=CONTEXT_CHOICES)
	
	amount = models.FloatField(verbose_name='Water Amount (ml)',blank=True, null=True)
	time = models.IntegerField(
		verbose_name='Time that Water was Freely Given (minutes)',blank=True, null=True)
		
	def __unicode__(self):
		return "{0}: {1}".format(self.session,self.context)



### Surgery / Medical ###

#Rat's Medication, whenever Performed
class Drug(models.Model):
	name = models.CharField(max_length=70)
	purpose = models.CharField(max_length=100)
	comments = models.TextField()
	
	def __unicode__(self):
		return self.name

class Medication(models.Model):
	rat = models.ForeignKey(Rat)
	drug = models.ForeignKey(Drug)
	date = models.DateTimeField('Date Administered',default=timezone.now())
	dose = models.FloatField(verbose_name='Dose Given (ml)') 
	comments = models.TextField(blank=True)
	

	
#Rat Vitals, whenever Checked
class Vital(models.Model):
	rat = models.ForeignKey(Rat)
	date = models.DateTimeField('Date Checked',default=timezone.now())
	heart_rate = models.FloatField(verbose_name='Heart Rate (bpm)',blank=True, null=True)
	temperature = models.FloatField(verbose_name='Temperature (celsius)',blank=True, null=True)
	
	comments = models.CharField(max_length=200, blank=True)
	
	
	

