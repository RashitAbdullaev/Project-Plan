# Generated by Django 4.0.2 on 2022-08-12 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0019_alter_product_expense_product_id_expense_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='act',
            name='act_number',
        ),
        migrations.AlterField(
            model_name='act',
            name='act_date',
            field=models.DateField(verbose_name='Дата сдачи'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='act',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plan.act', verbose_name='Акт'),
        ),
    ]
