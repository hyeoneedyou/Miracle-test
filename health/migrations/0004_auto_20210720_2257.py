# Generated by Django 3.2.5 on 2021-07-20 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_auto_20210720_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certify',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='health',
            name='created',
            field=models.DateTimeField(),
        ),
    ]
