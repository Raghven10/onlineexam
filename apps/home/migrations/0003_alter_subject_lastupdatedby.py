# Generated by Django 3.2.6 on 2021-12-14 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211214_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='lastUpdatedBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.user'),
        ),
    ]