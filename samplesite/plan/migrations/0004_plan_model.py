# Generated by Django 4.0.2 on 2022-07-04 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_alter_reserve_options_alter_product_product_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plan.model_product', verbose_name='Модели'),
        ),
    ]