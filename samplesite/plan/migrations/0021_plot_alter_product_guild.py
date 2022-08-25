# Generated by Django 4.0.2 on 2022-08-24 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plan', '0020_remove_act_act_number_alter_act_act_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot_name', models.CharField(max_length=150, verbose_name='Название участка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Бригадир')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='guild',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='plan.plot', verbose_name='Участок'),
        ),
    ]
