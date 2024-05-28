from django.contrib import admin
from django.apps import apps

# Register your models here.
models = apps.get_app_config("clientes").get_models()
for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
