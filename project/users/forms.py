from dataclasses import fields
from logging import PlaceHolder
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from django.forms import (formset_factory, modelformset_factory)
from .models import *
from crispy_forms.layout import Div, Layout, Field, Row
from crispy_forms.helper import FormHelper




class EducationInformationForm(forms.ModelForm):
    degree= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Degree'}), label="",)
    r_department = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Group/Department"}), label="")
    board_university= forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Board/University"}), label="")
    passing_year= forms.CharField(widget=forms.NumberInput(attrs={'placeholder': "Passing Year"}), label="")
    result= forms.CharField(widget=forms.NumberInput(attrs={'placeholder': "Result"}), label="")
    distinction= forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Distinction"}), label="")
    class Meta:
        model = EducationInformation
        fields= ["degree", "r_department", "board_university", "passing_year", "result", "distinction",]
        labels ={
            "degree": "Degree",
            "r_department": "Group/Department",
            "board_university": "Board/University",
            "passing_year": "Passing Year",
            "result": "Result",
            "distinction": "Distinction",
        }

    def __init__(self, *args, **kwargs): 
        super(EducationInformationForm, self).__init__(*args, **kwargs) 

        self.helper= FormHelper()
        self.helper.form_id= "id-entryfprm"
        self.helper.form_class= "form-inline"
        self.helper.layout= Layout(
            Div(
                Div("degree", css_class='col-6 col-lg-2'),
                Div("r_department", css_class='col-6 col-md-2'),
                Div("board_university",  css_class='col-5 col-md-2'),
                Div("passing_year",  css_class='col-md-2'),
                Div("result",  css_class='col-md-2'),
                Div("distinction",  css_class='col-md-2'),
            css_class="row"
            )
        )
    
    

            # Div(
            #     Div(Field("degree", placeHolder='Degree'), css_class='col-md-2'),
            #     Div(Field("r_department", placeHolder="Group/Department"), css_class='col-md-2'),
            #     Div(Field("board_university", placeHolder="Board/University"), css_class='col-md-2'),
            #     Div(Field("passing_year", placeHolder="Passing Year"), css_class='col-md-2'),
            #     Div(Field("result", placeHolder="Result"), css_class='col-md-2'),
            #     Div(Field("distinction", placeHolder="Distinction"), css_class='col-md-2'),
            # css_class="row"
            # )
        

        # self.fields['degree'].widget.attrs.update({ 
        #     'id': "degree",
        #     'name': "degree",
        #     'type': "text",
        #     'class': "form-control",
        #     'placeholder': "Degree",
        #     'required': 'required', 
        #     })
        # self.fields["r_department"].widget.attrs.update({ 
        #     'id': "r_department",
        #     'name': "r_department",
        #     'type': "text",
        #     'class': "form-control",
        #     'placeholder': "Group/Department",
        #     'required': 'required', 
        #     })
        # self.fields["board_university"].widget.attrs.update({ 
        #     'id': "board_university",
        #     'name': "board_university",
        #     'type': "text",
        #     'class': "form-control",
        #     'placeholder': "Board/University",
        #     'required': 'required',
        #     })
        # self.fields["passing_year"].widget.attrs.update({ 
        #     'id': "datepicker6",
        #     'name': "passing_year",
        #     'type': "number",
        #     'class': "form-control",
        #     'placeholder': "Passing Year",
        #     'required': 'required',
        #     })
        # self.fields["result"].widget.attrs.update({ 
        #     'id': "result",
        #     'name': "result",
        #     'type': "text",
        #     'class': "form-control",
        #     'placeholder': "Result",
        #     'required': 'required', 
        #     })
        # self.fields["distinction"].widget.attrs.update({ 
        #     'id': "distinction",
        #     'name': "distinction",
        #     'type': "text",
        #     'class': "form-control",
        #     'placeholder': "Distinction",
        #     'required': 'required',
        #     })
        # comment////

        # widgets = {

        #     'degree': forms.TextInput(attrs={
        #         'id': "degree",
        #         'name': "degree",
        #         'type': "text",
        #         'class': "form-control",
        #         'placeholder': "Degree",
        #         'required': 'required',
        #         }
        #     ),

        #     "r_department": forms.TextInput(attrs={
        #         'id': "r_department",
        #         'name': "r_department",
        #         'type': "text",
        #         'class': "form-control",
        #         'placeholder': "Group/Department",
        #         'required': 'required',
        #         }
        #     ),

        #     "board_university": forms.TextInput(attrs={
        #         'id': "board_university",
        #         'name': "board_university",
        #         'type': "text",
        #         'class': "form-control",
        #         'placeholder': "Board/University",
        #         'required': 'required',
        #         }
        #     ),

        #     "passing_year": forms.TextInput(attrs={
        #         'id': "datepicker6",
        #         'name': "passing_year",
        #         'type': "number",
        #         'class': "form-control",
        #         'placeholder': "Passing Year",
        #         'required': 'required',
        #         }
        #     ),

        #     "result": forms.TextInput(attrs={
        #         'id': "result",
        #         'name': "result",
        #         'type': "text",
        #         'class': "form-control",
        #         'placeholder': "Result",
        #         'required': 'required',
        #         }
        #     ),

        #     "distinction": forms.TextInput(attrs={
        #         'id': "distinction",
        #         'name': "distinction",
        #         'type': "text",
        #         'class': "form-control",
        #         'placeholder': "Distinction",
        #         'required': 'required',
        #         }
        #     ),
        # }

        # comment////



EducationInformationFormset = modelformset_factory (
    EducationInformation,
    fields= ("degree", "r_department", "board_university", "passing_year", "result", "distinction",),
    extra=1,
    widgets = {
        'degree': forms.TextInput(attrs={
            'id': "degree",
            'name': "degree",
            'type': "text",
            'class': "form-control",
            'placeholder': "Degree",
            'required': 'required',
            }
        ),

        "r_department": forms.TextInput(attrs={
            'id': "r_department",
            'name': "r_department",
            'type': "text",
            'class': "form-control",
            'placeholder': "Group/Department",
            'required': 'required',
            }
        ),

        "board_university": forms.TextInput(attrs={
            'id': "board_university",
            'name': "board_university",
            'type': "text",
            'class': "form-control",
            'placeholder': "Board/University",
           'required': 'required',
            }
        ),

        "passing_year": forms.TextInput(attrs={
            'id': "datepicker6",
            'name': "passing_year",
            'type': "number",
            'class': "form-control",
            'placeholder': "Passing Year",
            'required': 'required',
            }
        ),

        "result": forms.TextInput(attrs={
            'id': "result",
            'name': "result",
            'type': "number",
            'class': "form-control",
            'placeholder': "Result",
            'required': 'required',
            }
        ),

        "distinction": forms.TextInput(attrs={
            'id': "distinction",
            'name': "distinction",
            'type': "text",
            'class': "form-control",
            'placeholder': "Distinction",
            'required': 'required',
            }
        ),
    }
)


class UserRegisterForm(UserCreationForm): 
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['username'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'username', 
            'id':'username', 
            'type':'text', 
            'placeholder':'Your Name', 
            'maxlength': '16', 
            'minlength': '6', 
            }) 
        self.fields['email'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'email', 
            'id':'email', 
            'type':'email', 
            'placeholder':'Enter your email', 
            }) 
        self.fields['password1'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'password1', 
            'id':'password1', 
            'type':'password', 
            'placeholder':'password', 
            'maxlength':'22',  
            'minlength':'8' 
            }) 
        self.fields['password2'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'password2', 
            'id':'password2', 
            'type':'password', 
            'placeholder':'password', 
            'maxlength':'22',  
            'minlength':'8' 
            }) 
 
 
    username = forms.CharField(max_length=20, label=False) 
    email = forms.EmailField(max_length=100) 
 
    class Meta: 
        model = User 
        fields = ('username', 'email', 'password1', 'password2', )


class UserLoginForm(AuthenticationForm): 
    def __init__(self, *args, **kwargs): 
        super(UserLoginForm, self).__init__(*args, **kwargs) 
        self.fields['username'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'username', 
            'id':'username', 
            'type':'text', 
            'placeholder':'Your Name', 
            'maxlength': '16', 
            'minlength': '6', 
            }) 
        
        self.fields['password'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'password', 
            'id':'password', 
            'type':'password', 
            'placeholder':'password', 
            'maxlength':'22',  
            'minlength':'8' 
            }) 
       
 
 
    # username = forms.CharField(max_length=20, label=False) 
    # email = forms.EmailField(max_length=100) 
 
    # class Meta: 
    #     model = User 
    #     fields = ('username', 'password',  )


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField(required= True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user

# class PersonalInformationForm(forms.Form):
#     employee_id = forms.IntegerField(unique=True, max_length=30)
#     employee_name = forms.TextField(max_length=47)
#     email= forms.EmailField(max_length=20)
#     father_name = forms.TextField(max_length=255)
#     mother_name = forms.DateTimeField(auto_now_add=True)
#     birth_date = forms.DateField()
#     home_district = forms.TextField(max_length=255)
#     gender = forms.TextField(max_length=50)
#     religion = forms.TextField(max_length=255)
#     national_ID  = forms.IntegerField(max_length=255)
#     passport = forms.TextField(max_length=255)
#     driving_licence = forms.TextField(max_length=50)
#     gpf_cpf  = forms.IntegerField(max_length=100)
#     mobile = forms.IntegerField(max_length= 11)
#     blood_group= forms.TextField(max_length=3)
#     marital_status = forms.TextField(max_length=20)


# comment//////