# Generated by Django 4.1.3 on 2023-01-25 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='globales',
            name='id',
        ),
        migrations.AlterField(
            model_name='globales',
            name='nombre',
            field=models.CharField(max_length=500, primary_key=True, serialize=False),
        ),
    ]