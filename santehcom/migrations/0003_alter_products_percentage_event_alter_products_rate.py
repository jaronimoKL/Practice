# Generated by Django 4.1.1 on 2022-10-07 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('santehcom', '0002_alter_crate_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='percentage_event',
            field=models.IntegerField(blank=True, verbose_name='Процент акции'),
        ),
        migrations.AlterField(
            model_name='products',
            name='rate',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='santehcom.rating'),
        ),
    ]