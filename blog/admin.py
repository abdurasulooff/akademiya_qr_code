from django.contrib import admin
from .models import (
    Fakultet,
    Kafedra,
    Teacher,
    Items,
)

admin.site.register(Fakultet)
admin.site.register(Kafedra)
admin.site.register(Teacher)
admin.site.register(Items)
