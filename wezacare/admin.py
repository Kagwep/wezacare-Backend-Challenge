from django.contrib import admin
from .models import CustomUser,Question,Answer

# Register  models here.


admin.site.register(CustomUser)
admin.site.register(Question)
admin.site.register(Answer)
