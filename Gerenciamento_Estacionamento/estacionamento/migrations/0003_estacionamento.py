from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamento', '0002_estacionamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='estacionamento',
            name='valor_pagamento',
            field=models.FloatField(default=0),
        ),
    ]
