# Generated by Django 4.1.1 on 2022-10-19 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('santehcom', '0013_alter_products_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='rate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='santehcom.rating', verbose_name='Оценка'),
        ),
    ]