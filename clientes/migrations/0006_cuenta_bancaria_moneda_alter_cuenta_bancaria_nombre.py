# Generated by Django 5.0.4 on 2024-05-26 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_cuenta_bancaria'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuenta_bancaria',
            name='moneda',
            field=models.CharField(choices=[('Bs', 'Bolivares'), ('$', 'Dolares')], default='Bs', max_length=4),
        ),
        migrations.AlterField(
            model_name='cuenta_bancaria',
            name='nombre',
            field=models.CharField(max_length=256),
        ),
    ]
