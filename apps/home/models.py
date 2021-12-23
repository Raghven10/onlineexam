# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):    
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    about_me = models.CharField(max_length=500)
    job_position = models.CharField(max_length=50)
    job_company = models.CharField(max_length=50)
    lastUpdatedOn = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    lastUpdatedBy = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

class ExamAgency(models.Model):
    agency_name = models.CharField(max_length=50)
    agency_description = models.CharField(max_length=50)
    lastUpdatedOn = models.DateTimeField(auto_now_add=True)
    lastUpdatedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 

class Category(models.Model):
    category_name = models.CharField(max_length=250)
    category_description = models.CharField(max_length=250)
    lastUpdatedOn = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    lastUpdatedBy = models.ForeignKey(User, on_delete = models.CASCADE,blank=True, null=True) 

class Subject(models.Model):
    subject_code= models.CharField(max_length=10)
    subject_name = models.CharField(max_length=50)
    subject_description = models.CharField(max_length=50)
    lastUpdatedOn = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    lastUpdatedBy = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

class Section(models.Model): 
    section_code= models.CharField(max_length=10)   
    section_name = models.CharField(max_length=250)
    section_description = models.CharField(max_length=250)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    lastUpdatedOn = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    lastUpdatedBy = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

class Topic(models.Model):    
    topic_name = models.CharField(max_length=50)
    topic_description = models.CharField(max_length=50)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    lastUpdatedOn = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    lastUpdatedBy = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

class Exam(models.Model):
    exam_name = models.CharField(max_length=50)
    exam_date = models.DateField()
    exam_category = models.CharField(max_length=50)
    exam_agency = models.ForeignKey(ExamAgency, on_delete=models.CASCADE)
    lastUpdatedOn = models.DateTimeField(auto_now_add=True)
    lastUpdatedBy = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) 

class Question(models.Model):     
    question = models.CharField(max_length=5000)
    correct_answer = models.CharField(max_length=5000)
    explaination = models.CharField(max_length=10000, blank=True, null=True)
    exam_ref = models.CharField(max_length=5000, blank=True, null=True)
    question_type = models.CharField(max_length=50) # MULTIPLE-CHOICE / FILL IN THE BLANKS / DESCRIPTIVE
    option1 = models.CharField(max_length=250, blank=True, null=True)
    option2 = models.CharField(max_length=250, blank=True, null=True)
    option3 = models.CharField(max_length=250, blank=True, null=True)
    option4 = models.CharField(max_length=250, blank=True, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    
    lastUpdatedOn = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    lastUpdatedBy = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)




    

    
