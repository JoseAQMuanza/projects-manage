# Generated by Django 4.2.15 on 2024-09-04 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costs', '0005_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='budget',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='service',
            name='cost',
            field=models.IntegerField(),
        ),
    ]
