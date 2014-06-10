from django.contrib import admin
from ratlog.models import Rat, Weight, Cage, Water, Task, Session, Drug, Medication


# Register your models here.

#Rat
class CageInline(admin.StackedInline):
	model = Cage
	extra = 1


class RatAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['name', 'strain', 'date_of_birth', 'start_date', 'sex', 'protocol', 'comments']}),
	]
	inlines = [CageInline]
	
admin.site.register(Rat, RatAdmin)

#Weight
admin.site.register(Weight)
admin.site.register(Water)

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

#Surgery, Drugs, Medication
admin.site.register(Drug)
admin.site.register(Medication)

