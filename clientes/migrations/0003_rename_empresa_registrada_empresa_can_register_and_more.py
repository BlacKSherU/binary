# Generated by Django 5.0.4 on 2024-05-14 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_empresa_options_empresa_empresa_registrada'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='Empresa_registrada',
            new_name='can_register',
        ),
        migrations.AddField(
            model_name='empresa',
            name='is_registered',
            field=models.BooleanField(default=False),
        ),
    ]
