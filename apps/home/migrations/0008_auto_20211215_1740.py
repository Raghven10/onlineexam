# Generated by Django 3.2.6 on 2021-12-15 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20211215_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=5000),
        ),
    ]
