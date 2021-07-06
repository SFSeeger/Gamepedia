from django.contrib import admin
from .models import Game, Engine, Publisher, Developer, Plattform, Genre

# Register your models here.
admin.site.register(Game)
admin.site.register(Engine)
admin.site.register(Publisher)
admin.site.register(Developer)
admin.site.register(Plattform)
admin.site.register(Genre)
