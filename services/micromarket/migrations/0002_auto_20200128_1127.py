# Generated by Django 2.2.7 on 2020-01-28 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('micromarket', '0001_initial'),
        ('wharehouse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instalation',
            name='capex',
            field=models.ManyToManyField(to='wharehouse.Capex', verbose_name='capex'),
        ),
        migrations.AddField(
            model_name='instalation',
            name='checkout',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='micromarket.Checkout', verbose_name='Serviço de Autopagamento'),
        ),
        migrations.AddField(
            model_name='instalation',
            name='planogram',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wharehouse.Planogram', verbose_name='Planograma'),
        ),
        migrations.AddField(
            model_name='checkout',
            name='capex',
            field=models.ManyToManyField(to='wharehouse.Capex', verbose_name='Capex'),
        ),
    ]
