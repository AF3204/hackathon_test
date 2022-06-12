from pyexpat import model
from xml.etree.ElementTree import Comment
from django import forms
from numpy import require
from datetime import datetime
from .models import *
class taskForm(forms.Form):
    incidentName = forms.CharField(
        label="Incident Name",
        error_messages={'required': 'Please enter the task name'},
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter incident name",
                "class": "form-control"
            }
        ))

    type = forms.ChoiceField(
        label="Type",
        error_messages={'required': 'Please select the type of task'},
        required=True,
        choices=(('Activity', 'Activity'), ('Incident', 'Incident')),
        widget=forms.Select(
            attrs={
                "placeholder": "Enter incident name",
                "class": "form-control"
            }
        ))

    timeIncidentOccured = forms.DateTimeField(
        label= "Time of Incident Occured",
        input_formats=["%d/%m/%Y %H:%M"],
        
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1',
            'placeholder': 'Please select the time of incident occured.'
        })
    )
    shift = forms.ChoiceField(
        label="Shift",
        error_messages={'required': 'Please select the type of task'},
        # required=True,
        choices=(('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening'), ('Daily', 'Daily')),
        widget=forms.Select(
            attrs={
                "placeholder": "Select the shift",
                "class": "form-control"
            }
        ))

    mill = forms.ChoiceField(
        label="Mill",
        error_messages={'required': 'Please select the mill'},
        required=True,
        widget=forms.Select(
            attrs={
                "placeholder": "Select Mill",
                "class": "form-control"
            }
        ))

    location = forms.ChoiceField(
        label="Location",
        error_messages={'required': 'Please select the location'},
        required=True,
        choices=(('Fresh palm fruit bunch reception', 'Fresh palm fruit bunch reception'), ('Sterilization section', 'Sterilization section'), ('Threshing section', 'Threshing section'), ('Digesting and Pressing section', 'Digesting and Pressing section'), ('Oilclarification section', 'Oilclarification section'), ('Fiber separation section', 'Fiber separation section'), ('Palm kernel recovery section', 'Palm kernel recovery section'),
                 ('Engine room', 'Engine room'), ('Boiler house', 'Boiler house'), ('Water treatment', 'Water treatment'), ('Effluent treat plant', 'Effluent treat plant')),
        widget=forms.Select(
            attrs={
                "placeholder": "Select location",
                "class": "form-control"
            }
        ))

    remarks = forms.CharField(
        label="Remarks",
        required=True,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Enter remarks ",
                "class": "form-control",
                "rows":3
            }
        ))

    priorityLevel = forms.ChoiceField(
        label="Priority Level",
        error_messages={'required': 'Please select the priority level'},
        required=True,
        choices=(('Low', 'Low'), ('Moderate', 'Moderate'),
                 ('High', 'High'), ('Immediate', 'Immediate')),
        widget=forms.Select(
            attrs={
                "placeholder": "Select priority level",
                "class": "form-control"
            }
        ))

    imageUpload = forms.ImageField(
        label="Upload Image",
        required= False)
    
    
