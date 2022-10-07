import email
from pyexpat import model
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import EducationInformationForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import *
import datetime

from multiprocessing import AuthenticationError
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, force_text 
from django.core.mail import EmailMessage
from django import forms
from django.core.files.storage import FileSystemStorage

# from .tokens import account_activation_token

from django.http import HttpResponse  
from django.contrib.auth import login, authenticate, logout 
from django.views import View 
from django.forms import formset_factory




# ...
# def activate(request, uidb64, token):
#     return redirect('homepage')
# ...
# ...
# def activateEmail(request, user, to_email):
#     mail_subject = 'Activate your user account.'
#     message = render_to_string('template_activate_account.html', {
#         'user': user.username,
#         'domain': get_current_site(request).domain,
#         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#         'token': account_activation_token.make_token(user),
#         'protocol': 'https' if request.is_secure() else 'http'
#     })
#     email = EmailMessage(mail_subject, message, to=[to_email])
#     if email.send():
#         messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
#             received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
#     else:
#         messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')
# ...

# ...
# def activate(request, uidb64, token):
#     Users = User()
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = Users.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, Users.DoesNotExist):
#         user = None

#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()

#         messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
#         return redirect('users/login.html')
#     else:
#         messages.error(request, 'Activation link is invalid!')
    
#     return redirect('users/home.html')
# ...



def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             username = form.cleaned_data.get('username')
#             # to get the domain of the current site  
#             current_site = get_current_site(request)  
#             mail_subject =  'Activation link has been sent to your email id'
#             # messages.success(request, f'Hi {username}, your account was created successfully')
#             # return redirect('home')

#             message = render_to_string('template_activate_account.html', {  
#                 'user': user,  
#                 'domain': current_site.domain,  
#                 'uid':urlsafe_base64_encode(force_bytes(user.pk)), 
#                 'token':account_activation_token.make_token(user),  
#             })  
#             to_email = form.cleaned_data.get('email')  
#             email = EmailMessage(  
#                         mail_subject, message, to=[to_email]  
#             )  
#             email.send()  
#             return HttpResponse('Please confirm your email address to complete the registration')   

#     else:
#         form = UserCreationForm()

#     return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')

# class LoginForm(AuthenticationForm):
#     def __init__(self,  *args, **kwargs) -> None:
#         super(LoginForm, self).__init__( *args, **kwargs)

#         username = UsernameField(widget= forms.TextInput(
#             attrs={'class':'input', 'placeholder':'" Your Username"', 'id':'username'}
#         ))
#         password = forms.CharField(widget= forms.PasswordInput(
#             attrs={'class':'input', 'placeholder':'Your password', 'id':'password1'}
#         ))


@login_required()
def add_profile(request):
    educationInfo = EducationInformationForm(request.POST or None)
    educationInfo1 = EducationInformationForm()
    EducationInfoFormset = formset_factory(EducationInformationForm, extra=5)
    formset = EducationInfoFormset(request.POST or None)
    context={"formset": formset, "edu_Info_form": educationInfo}

    if request.method == "POST":

        if "personal_info_button" in request.POST and request.FILES["pro_pic"]:
            e_id = request.POST.get("employee_id")
            e_bd = request.POST.get("birth_date")
            # pro_pic1 = request.FILES.get("pro_pic")
            # pro_pic2 = request.FILES.get("profile-PicturePreview")
            pro_pic = request.FILES['pro_pic']
            fss = FileSystemStorage()
            pro_pic_file = fss.save(pro_pic.name, pro_pic)
            pro_pic_file_url = fss.url(pro_pic_file)

            signature_pic = request.FILES['signature_pic']
            fss1 = FileSystemStorage()
            signature_pic_file = fss1.save(signature_pic.name, signature_pic)
            signature_pic_url = fss.url(signature_pic_file)
            
            print(pro_pic)
            # print(pro_pic2)
            birth_date = datetime.datetime.strptime(request.POST.get("birth_date"), "%m/%d/%Y").strftime("%Y-%m-%d")
            print(birth_date)

            e_personal_info_model = Personal_info(
                e_unit = request.POST.get("e_unit"),
                e_division = request.POST.get("e_division"),
                employee_id=  request.POST.get("employee_id"),
                employee_name=  request.POST.get("employee_name"),
                email= request.POST.get("email"),
                father_name= request.POST.get("father_name"),
                mother_name= request.POST.get("mother_name"),
                birth_date= birth_date,
                home_district= request.POST.get("home_district"),
                gender =  request.POST.get("gender"),
                religion =  request.POST.get("religion"),
                national_ID  =  request.POST.get("national_ID"),
                passport =  request.POST.get("passport"),
                driving_licence =  request.POST.get("driving_licence"),
                gpf_cpf  =  request.POST.get("gpf_cpf"),
                phone =  request.POST.get("phone"),
                blood_group=  request.POST.get("blood_group"),
                marital_status =  request.POST.get("marital_status"),
                specialization =  request.POST.get("specialization"),
                pro_pic = pro_pic_file_url,
                signature_pic= signature_pic_url,
                )
            print(e_personal_info_model)
            e_personal_info_model.save()

        elif "contract_info_button" in request.POST:
            print(request.POST.get("present_address"))
            
            e_contract_info_model = Contract_info(
                present_address = request.POST.get("present_address"),
                parmanent_address = request.POST.get("parmanent_address"),
                emergency_name = request.POST.get("emergency_name"),
                present_post_office= request.POST.get("present_post_office"),
                parmanent_post_office = request.POST.get("parmanent_post_office"),
                emergency_relation= request.POST.get("emergency_relation"),
                present_police_station =  request.POST.get("present_police_station"),
                parmanent_police_station = request.POST.get("parmanent_police_station"),
                emergency_address=  request.POST.get("emergency_address"),
                present_district =  request.POST.get("present_district"),
                parmanent_district = request.POST.get("parmanent_district"),
                emergency_phone = request.POST.get("emergency_phone"),
                present_upazila =  request.POST.get("present_upazila"),
                parmanent_upazila = request.POST.get("parmanent_upazila"),
                emergency_cell_no = request.POST.get("emergency_cell_no"),
                present_tel_number = request.POST.get("present_tel_number"),
                parmanent_tel_number = request.POST.get("parmanent_tel_number"),
                emergency_email =  request.POST.get("emergency_email"),
            )
            print(e_contract_info_model)
            e_contract_info_model.save()

        elif "joining_info_button" in request.POST:

            joining_date = datetime.datetime.strptime(request.POST.get("joining_date"), "%m/%d/%Y").strftime("%Y-%m-%d")
            prl_date= datetime.datetime.strptime(request.POST.get("prl_date"), "%m/%d/%Y").strftime("%Y-%m-%d")
            conf_date = datetime.datetime.strptime(request.POST.get("conf_date"), "%m/%d/%Y").strftime("%Y-%m-%d")
            gazatted_date = datetime.datetime.strptime(request.POST.get("gazatted_date"), "%m/%d/%Y").strftime("%Y-%m-%d")
            edndorsement_date = datetime.datetime.strptime(request.POST.get("edndorsement_date"), "%m/%d/%Y").strftime("%Y-%m-%d")

            print(joining_date)

            e_joining_info_model = Joining_info(
                rank= request.POST.get("rank"),
                grade =  request.POST.get("grade"),
                designation=  request.POST.get("designation"),
                batch=  request.POST.get("batch"),
                workStation=  request.POST.get("workStation"),
                joining_date=  joining_date,
                office_name=   request.POST.get("office_name"),
                prl_date =  prl_date,
                department=  request.POST.get("department"),
                order_no_date= request.POST.get("order_no_date"),
                district=  request.POST.get("district"),
                conf_date= conf_date,
                upazila=   request.POST.get("upazila"),
                gazatted_date=  gazatted_date,
                job_nature=  request.POST.get("job_nature"),
                edndorsement_date=  edndorsement_date,
            )
            print(e_joining_info_model)
            e_joining_info_model.save()

        elif "education_info_button" in request.POST:
            # print(formset)
            if (formset.is_valid()):
                # educationInfo = EducationInformationForm(request.POST)
                if formset.is_valid() :
                    for form in formset:
                        print(form.cleaned_data.get("degree"))
                        print("####################")
                        if form.cleaned_data.get("degree") and form.cleaned_data.get("r_department") and form.cleaned_data.get("board_university") and form.cleaned_data.get("passing_year") and form.cleaned_data.get("result") and form.cleaned_data.get("distinction"):
                            # form.save()
                            EducationInformation(
                                degree= form.cleaned_data.get("degree"),
                                r_department= form.cleaned_data.get("r_department"),
                                board_university= form.cleaned_data.get("board_university"),
                                passing_year= form.cleaned_data.get("passing_year"),
                                result= form.cleaned_data.get("passing_year"),
                                distinction= form.cleaned_data.get("distinction"),
                            ).save()
                            messages.success(request, f'your Education Information was added successfully')

    elif request.method == "Get":
        # formset = EducationInformationForm(queryset=EducationInformation.objects.none())
        formset = EducationInformationForm(request.GET or None)


    return render(request, 'users/add-profile.html', context )