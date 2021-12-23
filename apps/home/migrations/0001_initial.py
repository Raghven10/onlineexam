# Generated by Django 3.2.6 on 2021-12-14 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=50)),
                ('exam_date', models.DateField()),
                ('exam_category', models.CharField(max_length=50)),
                ('lastUpdatedOn', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_code', models.CharField(max_length=10)),
                ('section_name', models.CharField(max_length=50)),
                ('section_description', models.CharField(max_length=250)),
                ('lastUpdatedOn', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=50)),
                ('topic_description', models.CharField(max_length=50)),
                ('lastUpdatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('lastUpdatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.section')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(max_length=10)),
                ('subject_name', models.CharField(max_length=50)),
                ('subject_description', models.CharField(max_length=50)),
                ('lastUpdatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('lastUpdatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user')),
            ],
        ),
        migrations.AddField(
            model_name='section',
            name='lastUpdatedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user'),
        ),
        migrations.AddField(
            model_name='section',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subject'),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.DateTimeField()),
                ('correct_answer', models.CharField(max_length=250)),
                ('question_type', models.CharField(max_length=50)),
                ('option1', models.CharField(blank=True, max_length=250, null=True)),
                ('option2', models.CharField(blank=True, max_length=250, null=True)),
                ('option3', models.CharField(blank=True, max_length=250, null=True)),
                ('option4', models.CharField(blank=True, max_length=250, null=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now_add=True)),
                ('exam_asked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.exam')),
                ('lastUpdatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user')),
            ],
        ),
        migrations.CreateModel(
            name='ExamAgency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_name', models.CharField(max_length=50)),
                ('agency_description', models.CharField(max_length=50)),
                ('lastUpdatedOn', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.user')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='exam_agency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.examagency'),
        ),
        migrations.AddField(
            model_name='exam',
            name='lastUpdatedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user'),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=250)),
                ('category_description', models.CharField(max_length=250)),
                ('lastUpdatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('lastUpdatedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.user')),
            ],
        ),
    ]