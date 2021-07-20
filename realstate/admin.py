from django.contrib import admin
from .models import Developer, Location, ProjectState, PayRequest

admin.site.register(Developer)
admin.site.register(Location)
admin.site.register(ProjectState)
admin.site.register(PayRequest)
