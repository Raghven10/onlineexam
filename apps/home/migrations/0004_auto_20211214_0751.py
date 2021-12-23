# Generated by Django 3.2.6 on 2021-12-14 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_subject_lastupdatedby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='lastUpdatedBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.user'),
        ),
        migrations.AlterField(
            model_name='section',
            name='lastUpdatedBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.user'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='lastUpdatedBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.user'),
        ),
    ]
