from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Players
from .models import Team
from .models import Coach
from .models import Game

admin.site.register(Game)
admin.site.register(Players)
admin.site.register(Team)
admin.site.register(Coach)

