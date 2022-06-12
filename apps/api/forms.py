from .models import Task
from django import forms
from django.db import models 
from PIL import Image
class taskForm(forms.ModelForm):
    # task.widget.attrs['required'] = 'required'
    photo = models.ImageField(upload_to='media/images')


    # def save(self):
    #     super().save()

    #     img = Image.open(self.photo.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.photo.path)
    class Meta:
        model = Task
        fields = ["task", "shift", "type", "remarks", "priority_level", "mill", "time_incident", "photo", "location", 'created_date']
        widgets = {
            'task': forms.TextInput(attrs={'class': 'form-control', 'required':'required', 'placeholder': 'Task Name'}),
            'shift': forms.Select(choices=(('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening'), ('Daily', 'Daily')),attrs={'class': 'form-control','required':'required', 'placeholder': 'Select shift'}),
            'type': forms.Select(attrs={'class': 'form-control','required':'required', 'placeholder': 'Select type of task'}),
            'remarks': forms.TextInput(attrs={'class': 'form-control', 'required':'required', 'placeholder': 'Enter remarks'}),
            'priority_level': forms.Select(attrs={'class': 'form-control', 'required':'required','placeholder': 'Select the priority level of the task'}),
            'mill': forms.Select(attrs={'class': 'form-control', 'required':'required', 'placeholder': 'Select the mill'}),
            'time_incident': forms.DateTimeInput(attrs={'class': 'form-control',  'placeholder': 'Select the time of the incident happens'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control', 'required':'required', 'placeholder': 'Select the location'}),
        }



class assigneeForm(forms.ModelForm):

    class Meta:
        NAME_CHOICES = (
        ('Gervase Delmar Peck' , 'Gervase Delmar Peck'),
        ('Nirmala St John' ,'Nirmala Janeka St John'),
        ('Paulo Coelho' ,'Paulo Coelho'),
        ('Kole Marvyn Sharma' ,'Kole Marvyn Sharma'),
        ('Goh Yew King', 'Goh Yew King'),
        ('Aspen Isidora Polley', 'Aspen Isidora Polley'),
        ('Sid Jaron Hull' , 'Sid Jaron Hull'),
        ('Ahyani Siregar' , 'Ahyani Siregar'),
        ('George Siregar' , 'George Siregar'),
        ('Tony Eusoff' ,'Tony Eusoff'),
        ('Xu Rongmao' ,'Xu Rongmao'),
        ('Liliyana Natsir' ,'Liliyana Natsir'),
        ('Andrea Hirata' ,'Andrea Hirata'),
        ('Revalina Sayuthi Temat','Revalina Sayuthi Temat' )
        )
        model = Task
        fields = ["id","assigned_to", "comment", "due_date",'assigned_date', "progress"]
        widgets = {
            'assigned_to': forms.Select(attrs={'class': 'form-control', 'required':'required', 'placeholder': 'PIC Name', "label":"Person In Charge"},
            choices=NAME_CHOICES),
            'comment': forms.Textarea(attrs={'class': 'form-control','required':'required', 'placeholder': 'Enter some comments here', 'rows': 3}),
            'due_date': forms.DateTimeInput(attrs={'class': 'form-control','required':'required', 'placeholder': 'Select due date for the task'}),
        }

        # queryset=ScenarioArea.objects.distinct('scenarioAreaName'), empty_label="Placeholder"