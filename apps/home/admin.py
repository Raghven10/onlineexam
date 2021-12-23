from django.contrib import admin
from django.contrib.auth.models import User

from apps.home.models import ExamAgency, Exam, Question, Category, Section, Subject, Topic, UserProfile

admin.site.register(ExamAgency)

admin.site.register(Category)

admin.site.register(Exam)

admin.site.register(Question)

admin.site.register(Topic)

admin.site.register(Section)

admin.site.register(Subject)

admin.site.register(UserProfile)