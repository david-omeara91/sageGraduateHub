from django.contrib import admin
from .models import (Graduate, Event, Resource, ResourceCategory,
                     Mentor, Question, Answer, Advice)
# Register your models here.
admin.site.register(Graduate)
admin.site.register(Event)
admin.site.register(ResourceCategory)
admin.site.register(Resource)
admin.site.register(Mentor)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Advice)