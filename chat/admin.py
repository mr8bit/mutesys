from django.contrib import admin
from .models import Room,QA


admin.site.register(
    Room,
    list_display=["id", "title", "staff_only"],
    list_display_links=["id", "title"],
)
admin.site.register(QA)
