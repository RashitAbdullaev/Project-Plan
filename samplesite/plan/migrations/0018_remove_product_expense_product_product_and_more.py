# Generated by Django 4.0.2 on 2022-08-12 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0017_product_expense_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_expense_product',
            name='product',
        ),
        migrations.AddField(
            model_name='product_expense_product',
            name='product_one',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Продукция', to='plan.product', verbose_name='Продукция'),
        ),
    ]
