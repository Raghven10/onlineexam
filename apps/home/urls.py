# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

     # The Questions page
    path('questions', views.questions, name='questions'), 
     # The Questions page
    path('new_question', views.new_question, name='new_question'), 

     # The Subject page
    path('subjects', views.subjects, name='subjects'), 
    path('delete_subject/<int:id>', views.delete_subject, name='delete_subject'),  

     # The Section page
    path('sections', views.sections, name='sections'), 
    path('delete_section/<int:id>', views.delete_section, name='delete_section'),  
    path('get_sections/<int:id>', views.get_sections_by_subject_id, name='get_sections_by_subject_id'), 

     # The Topic page
    path('topics', views.topics, name='topics'), 
    path('delete_topic/<int:id>', views.delete_topic, name='delete_topic'),  
    path('get_topics/<int:id>', views.get_topics, name='get_topics'), 

     # The Categories page
    path('categories', views.categories, name='categories'), 
    path('delete_category/<int:id>', views.delete_category, name='delete_category'), 

    # The Profile page
    path('update_profile', views.update_profile, name='update_profile'), 

    path('agencies', views.agencies, name='agencies'), 


    path('exam', views.exam, name='exam'),  

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
