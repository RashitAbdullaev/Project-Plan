# Generated by Django 4.0.2 on 2022-07-29 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0010_alter_plan_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='date',
        ),
        migrations.AddField(
            model_name='plan',
            name='date_guild',
            field=models.DateField(blank=True, null=True, verbose_name='Срок-бригодира'),
        ),
        migrations.AddField(
            model_name='plan',
            name='date_merchant',
            field=models.DateField(default='2022-03-10', verbose_name='Срок_коммерсанта'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plan',
            name='reserve',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='plan.reserve', verbose_name='Резерв'),
        ),
    ]