# Generated by Django 4.1.1 on 2022-10-16 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('santehcom', '0009_alter_products_image_alter_score_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='rate',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='santehcom.rating'),
        ),
    ]
