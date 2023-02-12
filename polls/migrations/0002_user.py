# Generated by Django 4.1.5 on 2023-02-05 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nombre del usuario')),
                ('age', models.IntegerField()),
                ('birthday', models.DateField()),
            ],
        ),
    ]