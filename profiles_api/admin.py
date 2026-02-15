from django.contrib import admin

from profiles_api import models

## registers your model with the Django admin site, allowing it to be managed through the built-in admin interface.
admin.site.register(models.UserProfile)

