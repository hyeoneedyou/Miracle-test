# Generated by Django 3.2.5 on 2021-07-20 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0004_auto_20210720_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certify',
            name='goal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certifys', to='health.health'),
        ),
    ]
