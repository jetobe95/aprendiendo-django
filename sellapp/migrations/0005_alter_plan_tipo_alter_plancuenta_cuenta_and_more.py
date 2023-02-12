# Generated by Django 4.1.5 on 2023-02-06 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sellapp', '0004_plan_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='tipo',
            field=models.CharField(choices=[('spotify', 'Spotify'), ('Netflix', 'Netflix'), ('Star plus', 'Star plus')], max_length=200),
        ),
        migrations.AlterField(
            model_name='plancuenta',
            name='cuenta',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='sellapp.cuenta'),
        ),
        migrations.AlterField(
            model_name='plancuenta',
            name='plan',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='sellapp.plan'),
        ),
    ]