from django.forms import ModelForm
from apps.home.models import ExamAgency, Exam, Question, Category, Section, Subject, Topic, UserProfile


class ExamAgencyForm(ModelForm):     
    class Meta:
        model = ExamAgency
        fields = '__all__'


class CategoryForm(ModelForm):     
    class Meta:
        model = Category
        fields = '__all__'


class ExamForm(ModelForm):     
    class Meta:
        model = Exam
        fields = '__all__'

class UserProfileForm(ModelForm):     
    class Meta:
        model = UserProfile
        fields = '__all__'


class QuestionForm(ModelForm):     
    class Meta:
        model = Question
        fields = '__all__'

class TopicForm(ModelForm):     
    class Meta:
        model = Topic
        fields = '__all__'

class SectionForm(ModelForm):     
    class Meta:
        model = Section
        fields = '__all__'

class SubjectForm(ModelForm):     
    class Meta:
        model = Subject
        fields = '__all__'
