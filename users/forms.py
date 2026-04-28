from dataclasses import fields
from logging import PlaceHolder
from multiprocessing.sharedctypes import Value
from random import choices
from turtle import onclick
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from django.forms import (formset_factory, modelformset_factory)
from .models import *
from crispy_forms.layout import Div, Layout, Field, Row, Button
from crispy_forms.helper import FormHelper




class EducationInformationForm(forms.ModelForm):

    degree_nmae = (
        ("",'Choose degree'),
        ("Phd", "Phd"),
        ("MS", "MS"),
        ("BSc", "BSc"),
        ("HSC", "HSC"),
        ("SSC", "SSC"),
    )

    degree= forms.ChoiceField(choices= degree_nmae, label="Degree",)
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

class SpouseInformationForm(forms.ModelForm):
    spouse_name= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Spouse Name'}), label="", required=False)
    spouse_home_district = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Home District"}), label="", required=False)
    spouse_occupation= forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Occupation"}), label="", required=False)
    spouse_designation= forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Designation"}), label="", required=False)
    spouse_org_name= forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Org Name"}), label="", required=False)
    spouse_org_address= forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Org Address"}), label="", required=False)
    spouse_cell_no= forms.CharField(widget=forms.NumberInput(attrs={'placeholder': "Cell No"}), label="", required=False)
    
    class Meta:
        model = SpouseInformation
        fields= ["spouse_name", "spouse_home_district", "spouse_occupation", "spouse_designation", "spouse_org_name", "spouse_org_address","spouse_cell_no"]
        labels ={
            "spouse_name": 'Spouse Name',
            "spouse_home_district": "Home District",
            "spouse_occupation": "Occupation",
            "spouse_designation":"Designation",
            "spouse_org_name": "Org Name",
            "spouse_org_address": "Org Address",
            "spouse_cell_no": "Cell No",
        }

    def __init__(self, *args, **kwargs): 
        super(SpouseInformationForm, self).__init__(*args, **kwargs) 

        self.helper= FormHelper()
        self.helper.form_id= "id-entryfprm"
        self.helper.form_class= "form-inline"
        self.helper.layout= Layout(
            Div(
                Div("spouse_name", css_class='col-6 col-lg-3'),
                Div("spouse_home_district", css_class='col-6 col-md-3'),
                Div("spouse_occupation",  css_class='col-5 col-md-3'),
                Div("spouse_designation",  css_class='col-md-3'),
                # Div("spouse_org_name",  css_class='col-md-3'),
                # Div("spouse_org_address",  css_class='col-md-3'),
                # Div("spouse_cell_no", css_class='col-md-3'),
            css_class="row"
            ),
            Div(
                Div("spouse_org_name",  css_class='col-md-3'),
                Div("spouse_org_address",  css_class='col-md-3'),
                Div("spouse_cell_no", css_class='col-md-3'),
            css_class="row mt-3"
            )
        )

class ChildrenInformationForm(forms.ModelForm):
    C_Gender = (
        ("",'Choose gender'),
        ("Male", "Male"),
        ("Female", "Female"),
        ("others", "Others")
    )

    clild_name= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Child Name'}), label='Child Name', required=False)
    clild_gerder = forms.ChoiceField(choices= C_Gender, label="Gender", required=False)
    clild_birthDate= forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.widgets.DateInput(format='%Y%m%d', attrs={'placeholder': "Select BirthDate", 'type': "date"}), label="BirthDate", required=False, )
    clild_BirthPlace= forms.CharField(widget=forms.TextInput(attrs={'placeholder': "(Country/District)"}), label="BirthPlace", required=False)
    clild_Remarks= forms.CharField(widget=forms.TextInput(attrs={'placeholder': "enter your remarks"}), label="Remarks", required=False)

    class Meta:
        model = ChildrenInformation
        fields= ["clild_name", "clild_gerder", "clild_birthDate", "clild_BirthPlace", "clild_Remarks", ]
        labels ={
            "clild_name": 'Child Name',
            "clild_gerder": "Gender",
            "clild_birthDate": "Select BirthDate",
            "clild_BirthPlace":"BirthPlace (Country/District)",
            "clild_Remarks": "Remarks",
            
        }

    def __init__(self, *args, **kwargs): 
        super(ChildrenInformationForm, self).__init__(*args, **kwargs) 

        # self.fields["clild_birthDate"].widget.attrs['class']= "datepicker7"
        self.helper= FormHelper()
        self.helper.form_id= "id-entryform"
        self.helper.form_class= "form-inline"
        self.helper.layout= Layout(
            Div(
                Div("clild_name", css_class='col-6 col-lg-2'),
                Div("clild_gerder", css_class='col-6 col-md-2'),
                Div("clild_birthDate",  css_class='col-5 col-md-2'),
                Div("clild_BirthPlace",  css_class='col-md-3'),
                Div("clild_Remarks",  css_class='col-md-3'),
                
            css_class="row"
            )
        )


class TraningInformationForm(forms.ModelForm):
    T_type = (
        ("",'Choose'),
        ("Local", "Local"),
        ("Foreign", "Foreign"),
    )

    traning_type= forms.ChoiceField(choices= T_type, label='',)
    traning_title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Traning Name'}), label='',)
    traning_institution= forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Institution Name"}), label="",)
    traning_country= forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Country Name"}), label="", )
    traning_start_date= forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.widgets.DateInput(format='%Y%m%d', attrs={'placeholder': "Select Start Date", 'type': "date"}), label="")
    traning_end_date= forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.widgets.DateInput(format='%Y%m%d', attrs={'placeholder': "Select End Date", 'type': "date"}), label="")
    traning_grade= forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Grade Value"}), label="", )
    traning_position= forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Position"}), label="", )

    class Meta:
        model = TraningInformation
        fields= ["traning_type", "traning_title", "traning_institution", "traning_country", "traning_start_date", "traning_end_date", "traning_grade", "traning_position" ]
        # labels ={
        #     "traning_type": 'Traning Type',
        #     "traning_title": "Traning Name",
        #     "traning_institution": "Institution Name",
        #     "traning_country":"Country Name",
        #     "traning_start_date": "Start Date", 
        #     "traning_end_date": "End Date",
        #     "traning_grade": "Grade",
        #     "traning_position":"Position",

        # }

    def __init__(self, *args, **kwargs): 
        super(TraningInformationForm, self).__init__(*args, **kwargs) 
        self.helper= FormHelper()
        self.helper.form_id= "id-entryform"
        self.helper.form_class= "form-inline"
        self.helper.layout= Layout(
            Div(
                Div("traning_type", css_class='form-group col-lg-1'),
                Div("traning_title", css_class=' col-md-3'),
                Div("traning_institution",  css_class='col-md-2'),
                Div("traning_country",  css_class='col-md-2'),
                Div("traning_start_date",  css_class='col-md-1'),
                Div("traning_end_date",  css_class='col-md-1'),
                Div("traning_grade",  css_class='col-md-1'),
                Div("traning_position",  css_class='col-md-1'),
                
            css_class="row"
            )
        )


class PostingInformationForm(forms.ModelForm):

    p_designation= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Designation'}), label='',)
    p_office = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Office'}), label='',)
    p_district= forms.CharField(widget=forms.TextInput(attrs={'placeholder': "District Name"}), label="",)
    p_upazila= forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Upazila Name"}), label="", )
    p_form_date= forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.widgets.DateInput(format='%Y%m%d', attrs={'placeholder': "Select Start Date", 'type': "date"}), label="")
    p_to_date= forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.widgets.DateInput(format='%Y%m%d', attrs={'placeholder': "Select End Date", 'type': "date"}), label="", required=False)
    p_till_today= forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Grade Value"}), label="", )
    

    class Meta:
        model = PostingInformation
        fields= ["p_designation", "p_office", "p_district", "p_upazila", "p_form_date", "p_to_date", "p_till_today", ]

    def __init__(self, *args, **kwargs): 
        super(PostingInformationForm, self).__init__(*args, **kwargs) 
        self.helper= FormHelper()
        self.helper.form_id= "id-entryform"
        self.helper.form_class= "form-inline"
        self.helper.layout= Layout(
            Div(
                Div("p_designation", css_class=' col-lg-2'),
                Div("p_office", css_class=' col-md-3'),
                Div("p_district",  css_class='col-md-2'),
                Div("p_upazila",  css_class='col-md-2'),
                Div("p_form_date",  css_class='col-md-1'),
                Div("p_to_date",  css_class='col-md-1'),
                Div("p_till_today",  css_class='col-md-1'),
                
            css_class="row"
            )
        )


class PromotionInformationForm(forms.ModelForm):

    Pro_nature = (
        ("",'Choose'),
        ("Regular", "Regular"),
        ("Selection Garde", "Selection Garde"),
        ("Sr. Grade", "Sr. Grade"),
        ("Natural", "Natural"),
    )

    pro_designation= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Designation'}), label='',)
    pro_nature = forms.ChoiceField(choices= Pro_nature, label='',)
    pro_promotion_date= forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.widgets.DateInput(format='%Y%m%d', attrs={'placeholder': "Select Promotion Date", 'type': "date"}), label="")
    pro_order_no= forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Order No."}), label="", )
    pro_order_date= forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.widgets.DateInput(format='%Y%m%d', attrs={'placeholder': "Select Order Date", 'type': "date"}), label="")
    pro_remarks= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Remarks'}), label='',)
    
    

    class Meta:
        model = PromotionInformatrion
        fields= ["pro_designation", "pro_nature", "pro_promotion_date", "pro_order_no", "pro_order_date", "pro_remarks", ]

    def __init__(self, *args, **kwargs): 
        super(PromotionInformationForm, self).__init__(*args, **kwargs) 
        self.helper= FormHelper()
        self.helper.form_id= "id-entryform"
        self.helper.form_class= "form-inline"
        self.helper.layout= Layout(
            Div(
                Div("pro_designation", css_class=' col-lg-2'),
                Div("pro_nature", css_class=' col-md-2'),
                Div("pro_promotion_date",  css_class='col-md-2'),
                Div("pro_order_no",  css_class='col-md-2'),
                Div("pro_order_date",  css_class='col-md-2'),
                Div("pro_remarks",  css_class='col-md-2'),
                
                
            css_class="row"
            )
        )

class AchievementInformationForm(forms.ModelForm):

    Achive_type = (
        ("",'Choose Type'),
        ("Journal Artical", "Journal Artical"),
        ("Conference Proceeding", "Conference Proceeding"),
        ("Developed Process", "Developed Process"),
        ("Patent", "Patent"),
        ("Books","Books/Books Chapters"),
        ("Award/Grant","Award/Grant")
    )

    achievement_type = forms.ChoiceField(choices= Achive_type, label='',)
    achievement_year= forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.widgets.DateInput(format='%Y%m%d', attrs={'placeholder': "Select Promotion Date", 'type': "date"}), label="")
    achievement_description= forms.CharField(widget=forms.TextInput(attrs={'placeholder': "achievement information"}), label="", )
    
    
    

    class Meta:
        model = AchievementInformation
        fields= ["achievement_type", "achievement_year", "achievement_description",]

    def __init__(self, *args, **kwargs): 
        super(AchievementInformationForm, self).__init__(*args, **kwargs) 
        self.helper= FormHelper()
        self.helper.form_id= "id-entryform"
        self.helper.form_class= "form-inline"
        self.helper.layout= Layout(
            Div(
                Div("achievement_type", css_class=' col-lg-3'),
                Div("achievement_year", css_class=' col-md-2'),
                Div("achievement_description",  css_class='col-md-7 row-2'),
                
                
                
            css_class="row"
            )
        )

class LeaveInformationForm(forms.ModelForm):

    L_type = (
        ("",'Choose Type'),
        ("Leave", "Leave"),
        ("Deputation", "Deputation"),
        
    )

    leave_type = forms.ChoiceField(choices= L_type, label='Type',)
    leave_form= forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.widgets.DateInput(format='%Y%m%d', attrs={'placeholder': "Select Promotion Date", 'type': "date"}), label="From")
    leave_to= forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.widgets.DateInput(format='%Y%m%d', attrs={'placeholder': "Select Promotion Date", 'type': "date"}), label="To")
    leave_description= forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Leave description"}), label="Description", )

    class Meta:
        model = LeaveInformation
        fields= ["leave_type", "leave_form", "leave_to", "leave_description",]

    def __init__(self, *args, **kwargs): 
        super(LeaveInformationForm, self).__init__(*args, **kwargs) 
        self.helper= FormHelper()
        self.helper.form_id= "id-entryform"
        self.helper.form_class= "form-inline"
        self.helper.layout= Layout(
            Div(
                Div("leave_type", css_class=' col-lg-2'),
                Div("leave_form", css_class=' col-md-2'),
                Div("leave_to", css_class=' col-md-2'),
                Div("leave_description",  css_class='col-md-5 row-2'),
                
                
                
            css_class="row"
            )
        )

class OtherServiceInformationForm(forms.ModelForm):

    otherService_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Service Type"}), label="Service Type", )
    otherService_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "address"}), label="Address", )
    otherService_designation = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "designation"}), label="Designation", )
    otherService_form= forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.widgets.DateInput(format='%Y%m%d', attrs={'placeholder': "Select Promotion Date", 'type': "date"}), label="From")
    otherService_to= forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.widgets.DateInput(format='%Y%m%d', attrs={'placeholder': "Select Promotion Date", 'type': "date"}), label="To", required=False)

    class Meta:
        model = OtherServiceInformation
        fields= ["otherService_type", "otherService_address", "otherService_designation", "otherService_form",]

    def __init__(self, *args, **kwargs): 
        super(OtherServiceInformationForm, self).__init__(*args, **kwargs) 
        self.helper= FormHelper()
        self.helper.form_id= "id-entryform"
        self.helper.form_class= "form-inline"
        self.helper.layout= Layout(
            Div(
                Div("otherService_type", css_class=' col-lg-2'),
                Div("otherService_address", css_class=' col-md-4'),
                Div("otherService_designation", css_class=' col-md-2'),
                Div("otherService_form",  css_class='col-md-2'),
                Div("otherService_to",  css_class='col-md-2'),
                
                
                
            css_class="row"
            )
        )

class OtherActivitiesInformationForm(forms.ModelForm):

    otherActivities_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "activityType"}), label="Activity/Assignment Type", )
    otherActivities_role = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "role"}), label="Role", )
    otherActivities_form= forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.widgets.DateInput(format='%Y%m%d', attrs={'placeholder': "Select Promotion Date", 'type': "date"}), label="From")
    otherActivities_to= forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.widgets.DateInput(format='%Y%m%d', attrs={'placeholder': "Select Promotion Date", 'type': "date"}), label="To", required=False)  

    class Meta:
        model = OtherActivitiesInformation
        fields= ["otherActivities_type", "otherActivities_role", "otherActivities_form", "otherActivities_to",]

    def __init__(self, *args, **kwargs): 
        super(OtherActivitiesInformationForm, self).__init__(*args, **kwargs) 
        self.helper= FormHelper()
        self.helper.form_id= "id-entryform"
        self.helper.form_class= "form-inline"
        self.helper.layout= Layout(
            Div(
                Div("otherActivities_type", css_class=' col-lg-3'),
                Div("otherActivities_role", css_class=' col-md-3'),
                Div("otherActivities_form", css_class=' col-md-2'),
                Div("otherActivities_to",  css_class='col-md-2'),
                
                
                
            css_class="row"
            )
        )

class R_and_D_ProjectsInformationForm(forms.ModelForm):

    Project_type = (
        ("",'Choose'),
        ("R & D", "R & D"),
        ("EXT. grant-Special Allocation", "EXT. grant-Special Allocation"),
        ("EXT. grant-Foreign Allocation", "EXT. grant-Foreign Allocation"),
        
    )
    Project_status = (
        ("",'Choose'),
        ("Complete", "Complete"),
        ("Ongoing", "Ongoing"), 
    )

    r_and_d_Project_type= forms.ChoiceField(choices= Project_type, label='Project Type',)
    r_and_d_ProjectName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "project name"}), label="Project Name", )
    r_and_d_Project_role = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "role"}), label="Role in Project", )
    r_and_d_Project_status= forms.ChoiceField(choices= Project_status, label='Project Status',)
    r_and_d_Project_tenure= forms.CharField(widget=forms.TextInput(attrs={'placeholder': "E.g. 2020-2021"}), label="Tenure", )

    class Meta:
        model = R_and_D_ProjectsInformation
        fields= ["r_and_d_Project_type","r_and_d_ProjectName", "r_and_d_Project_role", "r_and_d_Project_status", "r_and_d_Project_tenure", ]

    def __init__(self, *args, **kwargs): 
        super(R_and_D_ProjectsInformationForm, self).__init__(*args, **kwargs) 
        self.helper= FormHelper()
        self.helper.form_id= "id-entryform"
        self.helper.form_class= "form-inline"
        self.helper.layout= Layout(
            Div(
                Div("r_and_d_Project_type", css_class=' col-lg-3'),
                Div("r_and_d_ProjectName", css_class=' col-md-3'),
                Div("r_and_d_Project_role", css_class=' col-md-2'),
                Div("r_and_d_Project_status", css_class=' col-md-2'),
                Div("r_and_d_Project_tenure", css_class=' col-md-2'),
                
                
                
                
            css_class="row"
            )
        )

class ThesisSupervisionInformationForm(forms.ModelForm):
    
    Thesis_type = (
        ("",'Choose Type'),
        ("M.Sc", "M.Sc"),
        ("M.Phil", "M.Phil"),
        ("PhD", "PhD"),
        ("Post. Doc", "Post. Doc"),
        
    )

    thesisSupervision_type = forms.ChoiceField(choices= Thesis_type, label='Thesis Type',)
    thesisSupervision_supervisors = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "supervisors name"}), label="Supervisors Name", )
    thesisSupervision_studentName= forms.CharField(widget=forms.TextInput(attrs={'placeholder': "student name"}), label="Student Name", )
    thesisSupervision_studentSession= forms.CharField(widget=forms.TextInput(attrs={'placeholder': "E.g. 2016-17"}), label="Student Session", )
    thesisSupervision_thesisTitle = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "enter thesis title"}), label="Thesis Title", )

    class Meta:
        model = ThesisSupervisionInformation
        fields= ["thesisSupervision_type", "thesisSupervision_supervisors", "thesisSupervision_studentName", "thesisSupervision_studentSession", "thesisSupervision_thesisTitle"]

    def __init__(self, *args, **kwargs): 
        super(ThesisSupervisionInformationForm, self).__init__(*args, **kwargs) 
        self.helper= FormHelper()
        self.helper.form_id= "id-entryform"
        self.helper.form_class= "form-inline"
        self.helper.layout= Layout(
            Div(
                Div("thesisSupervision_type", css_class='col-lg-2'),
                Div("thesisSupervision_supervisors", css_class='span4 col-md-3'),
                Div("thesisSupervision_studentName", css_class=' col-md-2'),
                Div("thesisSupervision_studentSession",  css_class='col-md-2'),
                Div("thesisSupervision_thesisTitle", css_class='col-md-3'),
                
                
            css_class="row"
            )
        )
    
class ResearchInterestInformationForm(forms.ModelForm):

    researchInterest_fields = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "interested fields name"}), label="", )
    

    class Meta:
        model = ResearchInterestInformation
        fields= ["researchInterest_fields", ]

    def __init__(self, *args, **kwargs): 
        super(ResearchInterestInformationForm, self).__init__(*args, **kwargs) 
        self.helper= FormHelper()
        self.helper.form_id= "id-entryform"
        self.helper.form_class= "form-inline"
        self.helper.layout= Layout(
            Div(
                
                Div("researchInterest_fields", css_class=' col-lg-10'),

            )
        )

        #     Div(
        #         Div(Field("degree", placeHolder='Degree'), css_class='col-md-2'),
        #         Div(Field("r_department", placeHolder="Group/Department"), css_class='col-md-2'),
        #         Div(Field("board_university", placeHolder="Board/University"), css_class='col-md-2'),
        #         Div(Field("passing_year", placeHolder="Passing Year"), css_class='col-md-2'),
        #         Div(Field("result", placeHolder="Result"), css_class='col-md-2'),
        #         Div(Field("distinction", placeHolder="Distinction"), css_class='col-md-2'),
        #     css_class="row"
        #     )
        # comment//////

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



# EducationInformationFormset = modelformset_factory (
#     EducationInformation,
#     fields= ("degree", "r_department", "board_university", "passing_year", "result", "distinction",),
#     extra=1,
#     widgets = {
#         'degree': forms.TextInput(attrs={
#             'id': "degree",
#             'name': "degree",
#             'type': "text",
#             'class': "form-control",
#             'placeholder': "Degree",
#             'required': 'required',
#             }
#         ),

#         "r_department": forms.TextInput(attrs={
#             'id': "r_department",
#             'name': "r_department",
#             'type': "text",
#             'class': "form-control",
#             'placeholder': "Group/Department",
#             'required': 'required',
#             }
#         ),

#         "board_university": forms.TextInput(attrs={
#             'id': "board_university",
#             'name': "board_university",
#             'type': "text",
#             'class': "form-control",
#             'placeholder': "Board/University",
#            'required': 'required',
#             }
#         ),

#         "passing_year": forms.TextInput(attrs={
#             'id': "datepicker6",
#             'name': "passing_year",
#             'type': "number",
#             'class': "form-control",
#             'placeholder': "Passing Year",
#             'required': 'required',
#             }
#         ),

#         "result": forms.TextInput(attrs={
#             'id': "result",
#             'name': "result",
#             'type': "number",
#             'class': "form-control",
#             'placeholder': "Result",
#             'required': 'required',
#             }
#         ),

#         "distinction": forms.TextInput(attrs={
#             'id': "distinction",
#             'name': "distinction",
#             'type': "text",
#             'class': "form-control",
#             'placeholder': "Distinction",
#             'required': 'required',
#             }
#         ),
#     }
# )

# #comment///////


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