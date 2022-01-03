# -*- encoding: utf-8 -*-

from django import template
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views.generic import FormView

from apps.home.forms import CategoryForm, ExamForm, ExamAgencyForm, QuestionForm, SectionForm, SubjectForm, TopicForm, UserProfileForm

from .models import Exam, Question, ExamAgency, Category, Section, Subject, Topic


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def exam(request):
    context = {'segment': 'exam'}
    
    return render(request, "home/exam.html", context)


@login_required(login_url="/login/")
def agencies(request):
    context = {'segment': 'agencies'}
    form = ExamAgencyForm(request.POST or None)      
    if request.method == "POST":  
        print('Entered POST method...')
        if form.is_valid():  
            print('Form is valid...')
            try:  
                print('Try to save Form ..')
                form.save()                 
                return redirect('agencies')
            except:  
                msg = "Sorry, Form was not saved!"
        else:
            print('Form is not valid...exiting')
            msg = 'Error validating the form'
            return redirect('agencies')

    else: 
        print('Fetching all categories...')  
        msg = '..fetching all categories'
        form = ExamAgencyForm()          
        questions = ExamAgency.objects.all()       
        context = {'agencies': agencies, 'form':form, 'msg':msg}
        
    return render(request, "home/exam_agency.html", context)

@login_required(login_url="/login/")
def topics(request):
    context = {'segment': 'topics'}
    form = TopicForm(request.POST or None)      
    if request.method == "POST":  
        print('Entered POST method...')
        if form.is_valid():  
            print('Form is valid...')
            try:  
                print('Try to save Form ..')
                form.save()                 
                return redirect('topics')
            except:  
                msg = "Sorry, Form was not saved!"
        else:
            print('Form is not valid...exiting')
            print(form.errors.as_text)
            msg = 'Error validating the form'

            return redirect('topics')

    else: 
        print('Fetching all topics...')         
        form = TopicForm()          
        topics = Topic.objects.all() 
        subjects = Subject.objects.all() 
        sections = Section.objects.all()      
        context = {'topics': topics, 'form':form, 'sections': sections,'subjects':subjects, 'segment':'topics'}
        
    return render(request, "home/topics.html", context)



@login_required(login_url="/login/")
def delete_topic(request,id):
    topic = Topic.objects.get(pk=id)
    topic.delete()
    msg = 'Deleted Successfully.'       

    return redirect('topics')

@login_required(login_url="/login/")
def get_sections_by_subject_id(request, id):  
    
    data = serializers.serialize('json', Section.objects.filter(subject = id))         
    
    return JsonResponse(data, safe=False)


@login_required(login_url="/login/")
def get_topics(request, id):  
    
    data = serializers.serialize('json', Topic.objects.filter(section = id))         
    
    return JsonResponse(data, safe=False)



@login_required(login_url="/login/")
def subjects(request):
    context = {'segment': 'subjects'}
    form = SubjectForm(request.POST or None)      
    if request.method == "POST":  
        print('Entered POST method...')
        if form.is_valid():  
            print('Form is valid...')
            try:  
                print('Try to save Form ..')
                form.save()                 
                return redirect('subjects')
            except:  
                msg = "Sorry, Form was not saved!"
        else:
            print('Form is not valid...exiting')
            msg = 'Error validating the form'
            return redirect('subjects')

    else: 
        print('Fetching all subjects...')  
       
        form = SubjectForm()          
        subjects = Subject.objects.all()       
        context = {'subjects': subjects, 'form':form}
        
    return render(request, "home/subjects.html", context)

@login_required(login_url="/login/")
def delete_subject(request,id):
    subject = Subject.objects.get(pk=id)
    subject.delete()
    msg = 'Deleted Successfully.'       

    return redirect('subjects')

@login_required(login_url="/login/")
def sections(request):
    context = {'segment': 'sections'}
    form = SectionForm(request.POST or None)      
    if request.method == "POST":  
        print('Entered POST method...')
        if form.is_valid():  
            print('Form is valid...')
            try:  
                print('Try to save Form ..')
                form.save()                 
                return redirect('sections')
            except:  
                msg = "Sorry, Form was not saved!"
        else:
            print('Form is not valid...exiting')
            msg = 'Error validating the form'
            print(form.errors.as_text)
            return redirect('sections')

    else: 
        print('Fetching all Sections...')  
       
        form = SectionForm()          
        sections = Section.objects.all()  
        subjects = Subject.objects.all()     
        
        context = {'sections': sections,'subjects':subjects, 'form':form, 'segment':'sections'}
        
    return render(request, "home/sections.html", context)



@login_required(login_url="/login/")
def delete_section(request,id):

    section = Section.objects.get(pk=id)
    section.delete()
    msg = 'Deleted Successfully.'       

    return redirect('sections')

@login_required(login_url="/login/")
def categories(request):
    context = {'segment': 'categories'}
    form = CategoryForm(request.POST or None)      
    if request.method == "POST":  
        print('Entered POST method...')
        if form.is_valid():  
            print('Form is valid...')
            try:  
                print('Try to save Form ..')
                
                form.save()                 
                return redirect('categories')
            except:  
                msg = "Sorry, Form was not saved!"
        else:
            print('Form is not valid...exiting')
            msg = 'Error validating the form'
            return redirect('categories')

    else: 
        print('Fetching all categories...')          
        form = CategoryForm()          
        categories = Category.objects.all()       
        context = {'categories': categories, 'form':form}        
    return render(request, "home/exam_category.html", context)


@login_required(login_url="/login/")
def delete_category(request,id):

    category = Category.objects.get(pk=id)
    category.delete()
    msg = 'Deleted Successfully.'       

    return redirect('categories')

@login_required(login_url="/login/")
def questions(request):
    
    form = QuestionForm(request.POST or None)      
    if request.method == "POST":  
        print('Entered POST method...')
        if form.is_valid():  
            print('Form is valid...')
            try:  
                print('Try to save Form ..')
                form.save()                 
                return redirect('questions')
            except:  
                msg = "Sorry, Form was not saved!"
        else:
            print('Form is not valid...exiting')
            msg = 'Error validating the form'
            return redirect('questions')

    else: 
        print('Fetching all questions...')  
        msg = '..fetching all questions'
        form = QuestionForm()          
        questions = Question.objects.all()       
        context = {'questions': questions, 'form':form, 'msg':msg, 'segment': 'question'}
        
    return render(request, "home/questions.html", context)


@login_required(login_url="/login/")
def new_question(request):
    
    form = QuestionForm(request.POST or None)      
    if request.method == "POST":  
        print('Entered POST method...')
        if form.is_valid():  
            print('Form is valid...')
            try:  
                print('Try to save Form ..')
                form.save()                 
                return redirect('new_question')
            except:  
                msg = "Sorry, Form was not saved!"
        else:
            print('Form is not valid...exiting')
            print(form.errors.as_text)
            msg = 'Error validating the form'

            return redirect('new_question')

    else: 
        print('Entering get question_form....')         
        form = QuestionForm()          
        subjects = Subject.objects.all()  
        categories = Category.objects.all()           
        context = {'form':form, 'subjects':subjects,'categories':categories, 'segment':'question'}
        
    return render(request, "home/add_question.html", context)

@login_required(login_url="/login/")
def update_profile(request):
    
    form = UserProfileForm(request.POST or None)      
    if request.method == "POST":  
        print('Entered POST method...')
        if form.is_valid():  
            print('Form is valid...')
            try:  
                print('Try to save Form ..')
                form.save()                 
                return redirect('update_profile')
            except:  
                msg = "Sorry, Form was not saved!"
        else:
            print('Form is not valid...exiting')
            print(form.errors.as_text)
            msg = 'Error validating the form'

            return redirect('update_profile')

    else: 
        print('Entering get profile_form....')         
        form = UserProfileForm()       
                 
        context = {'form':form,'segment':'profile'}
        
    return render(request, "home/profile.html", context)

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
