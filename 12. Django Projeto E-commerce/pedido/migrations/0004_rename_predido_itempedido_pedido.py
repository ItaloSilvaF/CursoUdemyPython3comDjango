# Generated by Django 4.1.4 on 2023-01-04 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_pedido_qtd_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itempedido',
            old_name='predido',
            new_name='pedido',
        ),
    ]
