from django.contrib import admin
from ratlog.models import Rat, Weight, Water, Task, Session, Medication, Vital


# Register your models here.
admin.site.register(Rat)
admin.site.register(Weight)


admin.site.register(Task)

class WaterInline(admin.StackedInline):
	model = Water
	extra = 1

class SessionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,  {'fields': ['rat', 'date', 'length']}),
		('Behavior',  {'fields': ['task', 'task_learned', 'motivation', 			'comments']}),		
	]
	inlines = [WaterInline]
	list_display = ('rat', 'task','date')
	list_filter = ['date']
	search_fields = ['rat__name', 'rat__id', 'task__name', 'task__maze_name']
	
admin.site.register(Session, SessionAdmin)


