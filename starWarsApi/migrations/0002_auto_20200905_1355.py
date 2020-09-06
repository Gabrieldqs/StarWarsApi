# Generated by Django 2.2.15 on 2020-09-05 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starWarsApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('climate', models.CharField(max_length=100)),
                ('terrain', models.CharField(max_length=100)),
                ('films', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Car',
        ),
    ]