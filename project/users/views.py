import email
from pyexpat import model
from sys import prefix
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import AchievementInformationForm, ChildrenInformationForm, EducationInformationForm, LeaveInformationForm, OtherActivitiesInformationForm, OtherServiceInformationForm, PostingInformationForm, PromotionInformationForm, R_and_D_ProjectsInformationForm, ResearchInterestInformationForm, SpouseInformationForm, ThesisSupervisionInformationForm, TraningInformationForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import *
import datetime
from .scrap import paperScraping
from django.http import JsonResponse
import json
from users.models import Personal_info

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
from django.views.decorators.csrf import csrf_protect, csrf_exempt




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
def paper_response_json(request):
    # personalInfoList = Personal_info.objects.all
    # print(personalInfoList)
    
    current_user = request.user
    user_email= current_user.email   
    user_Name= Personal_info.objects.get(email=current_user.email).employee_name
    print(user_Name, user_email)
    responseP = paperScraping(user_Name, user_email)
    # testArr= []
    # arrValue= {
    #     "paperLink": 1,
    #     "paperName": 2,        
    #     "paperType": user_Name,
    #     "paperPublishDate": current_user.id,
    #     "paperDescription": current_user.email,
    # }
    # testArr.append(arrValue)
    # responseP= json.dumps(testArr, indent=4)
    # print(responseP)
    return JsonResponse(responseP, safe=False)


@login_required()
def add_profile(request):
    
    EducationInfoFormset = formset_factory(EducationInformationForm)
    edu_formset = EducationInfoFormset(request.POST if "education_info_button" in request.POST else None, prefix="education")

    SpouseInfoFormset = formset_factory(SpouseInformationForm)
    spouse_formset = SpouseInfoFormset(request.POST if "spouse_info_button" in request.POST else None, prefix="spouse")

    ChildrenInfoFormset = formset_factory(ChildrenInformationForm)
    children_formset = ChildrenInfoFormset(request.POST if "child_info_button" in request.POST else None, prefix="children")

    TraningInfoFormset = formset_factory(TraningInformationForm)
    traning_formset = TraningInfoFormset(request.POST if "traning_info_button" in request.POST else None, prefix="traning")

    PostingInfoFormset = formset_factory(PostingInformationForm)
    posting_formset= PostingInfoFormset(request.POST if "posting_info_button" in request.POST else None, prefix="posting")

    PromotionInfoFormset = formset_factory(PromotionInformationForm)
    promotion_formset= PromotionInfoFormset(request.POST if "promotion_info_button" in request.POST else None, prefix="promotion")

    AchievementInfoFormset= formset_factory(AchievementInformationForm)
    achievement_formset = AchievementInfoFormset(request.POST if "achievement_info_button" in request.POST else None, prefix="achievement")
    
    LeaveInfoFormset= formset_factory(LeaveInformationForm)
    leave_formset= LeaveInfoFormset(request.POST if "leave_info_button" in request.POST else None, prefix="leave")

    OtherServiceInfoFormset = formset_factory(OtherServiceInformationForm)
    otherService_formset = OtherServiceInfoFormset(request.POST if "otherService_info_button" in request.POST else None, prefix="otherService")

    OtherActivitiesInfoFormset = formset_factory(OtherActivitiesInformationForm)
    otherActivities_formset = OtherActivitiesInfoFormset(request.POST if "otherActivities_info_button" in request.POST else None, prefix="otherActivities")
    
    R_and_D_ProjectInfoFormset = formset_factory(R_and_D_ProjectsInformationForm)
    r_and_d_formset = R_and_D_ProjectInfoFormset(request.POST if "r_and_d_info_button" in request.POST else None, prefix="r_and_d")
    
    ThesisSupervisionInfoFormset = formset_factory(ThesisSupervisionInformationForm)
    thesisSupervision_formset = ThesisSupervisionInfoFormset(request.POST if "thesisSupervision_info_button" in request.POST else None, prefix="thesisSupervision")

    ResearchInterestInfoFormset = formset_factory(ResearchInterestInformationForm)
    researchInterest_formset = ResearchInterestInfoFormset(request.POST if "researchInterest_info_button" in request.POST else None, prefix="researchInterest")



    context={
        "edu_formset": edu_formset,
        "spouse_formset": spouse_formset,
        "children_formset": children_formset,
        "traning_formset":traning_formset,
        "posting_formset": posting_formset,
        "promotion_formset": promotion_formset,
        "achievement_formset": achievement_formset,
        "leave_formset": leave_formset,
        "otherService_formset": otherService_formset,
        "otherActivities_formset": otherActivities_formset,
        "r_and_d_formset": r_and_d_formset,
        "thesisSupervision_formset": thesisSupervision_formset,
        "researchInterest_formset": researchInterest_formset,
        

        }


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
                user = request.user,
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
                about_summary = request.POST.get("about_summary"),
                pro_pic = pro_pic_file_url,
                signature_pic= signature_pic_url,
                )
            print(e_personal_info_model)
            e_personal_info_model.save()

        elif "contract_info_button" in request.POST:
            print(request.POST.get("present_address"))
            
            e_contract_info_model = Contract_info(
                user = request.user,
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
                user = request.user,
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
            if (edu_formset.is_valid()):
                # educationInfo = EducationInformationForm(request.POST)
                if edu_formset.is_valid() :
                    # edu_len=len(edu_formset)
                    # print(edu_len)
                    # test= False
                    for form in edu_formset:
                    
                        if form.cleaned_data.get("degree") and form.cleaned_data.get("r_department") and form.cleaned_data.get("board_university") and form.cleaned_data.get("passing_year") and form.cleaned_data.get("result") and form.cleaned_data.get("distinction"):
                            # form.save()
                            EducationInformation(
                                user = request.user,
                                degree= form.cleaned_data.get("degree"),
                                r_department= form.cleaned_data.get("r_department"),
                                board_university= form.cleaned_data.get("board_university"),
                                passing_year= form.cleaned_data.get("passing_year"),
                                result= form.cleaned_data.get("passing_year"),
                                distinction= form.cleaned_data.get("distinction"),
                            ).save()
                            messages.success(request, f'your Education Information was added successfully')

        elif "spouse_info_button" in request.POST:
            # print(formset)
            if (spouse_formset.is_valid()):
                # educationInfo = EducationInformationForm(request.POST)
                for form1 in spouse_formset:
                    if form1.cleaned_data.get("spouse_name"):
                        # form.save()
                        SpouseInformation(
                            user = request.user,
                            spouse_name= form1.cleaned_data.get("spouse_name"),
                            spouse_home_district= form1.cleaned_data.get("spouse_home_district"),
                            spouse_occupation= form1.cleaned_data.get("spouse_occupation"),
                            spouse_designation= form1.cleaned_data.get("spouse_designation"),
                            spouse_org_name= form1.cleaned_data.get("spouse_org_name"),
                            spouse_org_address= form1.cleaned_data.get("spouse_org_address"),                                spouse_cell_no= form1.cleaned_data.get("spouse_cell_no"),
                        ).save()
                        messages.success(request, f'Your Spouse Information was added successfully')
                   
        elif "child_info_button" in request.POST:
            
            if (children_formset.is_valid()):
                # educationInfo = EducationInformationForm(request.POST)   
                print(children_formset)
                for form2 in children_formset:
                    print("#########################################")
                    # print(form)
                    print(form2.cleaned_data.get("clild_gerder"))
                    print(form2.cleaned_data.get("clild_birthDate"))
                    if form2.cleaned_data.get("clild_name") and form2.cleaned_data.get("clild_gerder") and form2.cleaned_data.get("clild_birthDate") and form2.cleaned_data.get("clild_BirthPlace"):
                        # form.save()
                        # child_birth_date = datetime.datetime.strptime(form2.cleaned_data.get("clild_birthDate"), "%m/%d/%Y").strftime("%Y-%m-%d")
                        print("&&&&&&&&&&&&&&&&&&&&&&&")
                        ChildrenInformation(
                            user = request.user,
                            clild_name= form2.cleaned_data.get("clild_name"),
                            clild_gerder= form2.cleaned_data.get("clild_gerder"),
                            # clild_birthDate= child_birth_date,
                            clild_birthDate=form2.cleaned_data.get("clild_birthDate"),
                            clild_BirthPlace= form2.cleaned_data.get("clild_BirthPlace"),
                            clild_Remarks= form2.cleaned_data.get("clild_Remarks"),
                                
                        ).save()
                        messages.success(request, f'Your Children Information was added successfully')

        elif "traning_info_button" in request.POST:
            
            if (traning_formset.is_valid()):
                # educationInfo = EducationInformationForm(request.POST)   
                print(traning_formset)
                for form in traning_formset:
                    print("#########################################")
                    # print(form)
                    print(form.cleaned_data.get("traning_type"))
                    print(form.cleaned_data.get("traning_title"))
                    if form.cleaned_data.get("traning_type") and form.cleaned_data.get("traning_title") and form.cleaned_data.get("traning_institution") and form.cleaned_data.get("traning_country"):
                        # form.save()
                        # child_birth_date = datetime.datetime.strptime(form2.cleaned_data.get("clild_birthDate"), "%m/%d/%Y").strftime("%Y-%m-%d")
                        print("&&&&&&&&&&&&&&&&&&&&&&&")
                        TraningInformation(
                            user= request.user,
                            traning_type= form.cleaned_data.get("traning_type"),
                            traning_title= form.cleaned_data.get("traning_title"),
                            traning_institution= form.cleaned_data.get("traning_institution"),
                            traning_country= form.cleaned_data.get("traning_country"),
                            traning_start_date= form.cleaned_data.get("traning_start_date"),
                            traning_end_date= form.cleaned_data.get("traning_end_date"),
                            traning_grade= form.cleaned_data.get("traning_grade"),
                            traning_position= form.cleaned_data.get("traning_position"),
                                
                        ).save()
                        messages.success(request, f'Your Traning Information was added successfully')

        elif "posting_info_button" in request.POST:
            
            if (posting_formset.is_valid()):
                # educationInfo = EducationInformationForm(request.POST)   
                print(posting_formset)
                for form in posting_formset:
                    print("#########################################")
                    # print(form)
                    print(form.cleaned_data.get("p_designation"))
                    print(form.cleaned_data.get("p_office"))
                    if form.cleaned_data.get("p_office") and form.cleaned_data.get("p_district") and form.cleaned_data.get("p_upazila") :
                        # form.save()
                        # child_birth_date = datetime.datetime.strptime(form2.cleaned_data.get("clild_birthDate"), "%m/%d/%Y").strftime("%Y-%m-%d")
                        print("&&&&&&&&&&&&&&&&&&&&&&&")
                        PostingInformation(
                            user= request.user,
                            p_designation= form.cleaned_data.get("p_designation"),
                            p_office= form.cleaned_data.get("p_office"),
                            p_district= form.cleaned_data.get("p_district"),
                            p_upazila= form.cleaned_data.get("p_upazila"),
                            p_form_date= form.cleaned_data.get("p_form_date"),
                            p_to_date= form.cleaned_data.get("p_to_date"),
                            p_till_today= form.cleaned_data.get("p_till_today"),
                            
                                
                        ).save()
                        messages.success(request, f'Your Posting Information was added successfully')

        elif "promotion_info_button" in request.POST:
            
            if (promotion_formset.is_valid()):
                # educationInfo = EducationInformationForm(request.POST)   
                print(promotion_formset)
                for form in promotion_formset:
                    print("#########################################")
                    # print(form)
                    print(form.cleaned_data.get("pro_designation"))
                    print(form.cleaned_data.get("pro_nature"))
                    if form.cleaned_data.get("pro_nature") and form.cleaned_data.get("pro_promotion_date") :
                        # form.save()
                        # child_birth_date = datetime.datetime.strptime(form2.cleaned_data.get("clild_birthDate"), "%m/%d/%Y").strftime("%Y-%m-%d")
                        print("&&&&&&&&&&&&&&&&&&&&&&&")
                        PromotionInformatrion(
                            user= request.user,
                            pro_designation= form.cleaned_data.get("pro_designation"),
                            pro_nature=  form.cleaned_data.get("pro_nature"),
                            pro_promotion_date=  form.cleaned_data.get("pro_promotion_date"),
                            pro_order_no=  form.cleaned_data.get("pro_order_no"),
                            pro_order_date=  form.cleaned_data.get("pro_order_date"),
                            pro_remarks=  form.cleaned_data.get("pro_remarks"),
                            
                                
                        ).save()
                        messages.success(request, f'Your Promotion Information was added successfully')

        elif "achievement_info_button" in request.POST:
            
            if (achievement_formset.is_valid()):
                # educationInfo = EducationInformationForm(request.POST)   
                print(achievement_formset)
                for form in achievement_formset:
                    print("#########################################")
                    # print(form)
                    print(form.cleaned_data.get("achievement_type"))
                    print(form.cleaned_data.get("achievement_year"))
                    print(form.cleaned_data.get("achievement_description"))
                    if form.cleaned_data.get("achievement_type") and form.cleaned_data.get("achievement_year") :
                        # form.save()
                        # child_birth_date = datetime.datetime.strptime(form2.cleaned_data.get("clild_birthDate"), "%m/%d/%Y").strftime("%Y-%m-%d")
                        print("&&&&&&&&&&&&&&&&&&&&&&&")
                        AchievementInformation(
                            user= request.user,
                            achievement_type= form.cleaned_data.get("achievement_type"),
                            achievement_year= form.cleaned_data.get("achievement_year"),
                            achievement_description=  form.cleaned_data.get("achievement_description"),
                            
                                
                        ).save()
                        messages.success(request, f'Your Achievement Information was added successfully')
        
        elif "leave_info_button" in request.POST:
            
            if (leave_formset.is_valid()):
                # educationInfo = EducationInformationForm(request.POST)   
                print(leave_formset)
                for form in leave_formset:
                    print("#########################################")
                    # print(form)
                    print(form.cleaned_data.get("leave_type"))
                    print(form.cleaned_data.get("leave_description"))
                    if form.cleaned_data.get("leave_type") and form.cleaned_data.get("leave_description") :
                        # form.save()
                        # child_birth_date = datetime.datetime.strptime(form2.cleaned_data.get("clild_birthDate"), "%m/%d/%Y").strftime("%Y-%m-%d")
                        print("&&&&&&&&&&&&&&&&&&&&&&&")
                        LeaveInformation(
                            user= request.user,
                            leave_type = form.cleaned_data.get("leave_type"),
                            leave_form= form.cleaned_data.get("leave_form"),
                            leave_to= form.cleaned_data.get("leave_to"),
                            leave_description= form.cleaned_data.get("leave_description"),
                            
                                
                        ).save()
                        messages.success(request, f'Your Leave/Deputation Information was added successfully')

        elif "otherService_info_button" in request.POST:
            
            if (otherService_formset.is_valid()):
                # educationInfo = EducationInformationForm(request.POST)   
                print(otherService_formset)
                for form in otherService_formset:
                    print("#########################################")
                    # print(form)
                    print(form.cleaned_data.get("otherService_type"))
                    print(form.cleaned_data.get("otherService_address"))
                    if form.cleaned_data.get("otherService_type") and form.cleaned_data.get("otherService_address") :
                        # form.save()
                        # child_birth_date = datetime.datetime.strptime(form2.cleaned_data.get("clild_birthDate"), "%m/%d/%Y").strftime("%Y-%m-%d")
                        print("&&&&&&&&&&&&&&&&&&&&&&&")
                        OtherServiceInformation(
                            user= request.user,
                            otherService_type = form.cleaned_data.get("otherService_type"),
                            otherService_address =  form.cleaned_data.get("otherService_address"),
                            otherService_designation =   form.cleaned_data.get("otherService_designation"),
                            otherService_form=  form.cleaned_data.get("otherService_form"),
                            otherService_to= form.cleaned_data.get("otherService_to"),
                            
                                
                        ).save()
                        messages.success(request, f'Your Former/Other Information was added successfully')

        elif "otherActivities_info_button" in request.POST:
            
            if (otherActivities_formset.is_valid()):
                # educationInfo = EducationInformationForm(request.POST)   
                print(otherActivities_formset)
                for form in otherActivities_formset:
                    print("#########################################")
                    # print(form)
                    print(form.cleaned_data.get("otherActivities_type"))
                    print(form.cleaned_data.get("otherActivities_role"))
                    if form.cleaned_data.get("otherActivities_type") and form.cleaned_data.get("otherActivities_role") :
                        # form.save()
                        # child_birth_date = datetime.datetime.strptime(form2.cleaned_data.get("clild_birthDate"), "%m/%d/%Y").strftime("%Y-%m-%d")
                        print("&&&&&&&&&&&&&&&&&&&&&&&")
                        OtherActivitiesInformation(
                            user= request.user,
                            otherActivities_type = form.cleaned_data.get("otherActivities_type"),
                            otherActivities_role= form.cleaned_data.get("otherActivities_role"),
                            otherActivities_form = form.cleaned_data.get("otherActivities_form"),
                            otherActivities_to=  form.cleaned_data.get("otherActivities_to"),
                            
                                
                        ).save()
                        messages.success(request, f'Your Other Activities/Assignment Information was added successfully')

        elif "r_and_d_formset_info_button" in request.POST:
            
            if (r_and_d_formset.is_valid()):
                # educationInfo = EducationInformationForm(request.POST)   
                print(r_and_d_formset)
                for form in r_and_d_formset:
                    print("#########################################")
                    # print(form)
                    print(form.cleaned_data.get("r_and_d_ProjectName"))
                    print(form.cleaned_data.get("r_and_d_Project_role"))
                    if form.cleaned_data.get("r_and_d_ProjectName") and form.cleaned_data.get("r_and_d_Project_role") :
                        
                        print("&&&&&&&&&&&&&&&&&&&&&&&")
                        R_and_D_ProjectsInformation(
                            user= request.user,
                            r_and_d_Project_type = form.cleaned_data.get("r_and_d_Project_type"),
                            r_and_d_ProjectName = form.cleaned_data.get("r_and_d_ProjectName"),
                            r_and_d_Project_role= form.cleaned_data.get("r_and_d_Project_role"),
                            r_and_d_Project_status = form.cleaned_data.get("r_and_d_Project_status"),
                            r_and_d_Project_tenure = form.cleaned_data.get("r_and_d_Project_tenure"),
                            
                                
                        ).save()
                        messages.success(request, f'Your R & D Projects Information was added successfully')

        elif "thesisSupervision_info_button" in request.POST:
            
            if (thesisSupervision_formset.is_valid()):
                # educationInfo = EducationInformationForm(request.POST)   
                print(thesisSupervision_formset)
                for form in thesisSupervision_formset:
                    print("#########################################")
                    # print(form)
                    print(form.cleaned_data.get("thesisSupervision_type"))
                    print(form.cleaned_data.get("thesisSupervision_supervisors"))
                    if form.cleaned_data.get("thesisSupervision_type") and form.cleaned_data.get("thesisSupervision_supervisors") :
                        # form.save()
                        # child_birth_date = datetime.datetime.strptime(form2.cleaned_data.get("clild_birthDate"), "%m/%d/%Y").strftime("%Y-%m-%d")
                        print("&&&&&&&&&&&&&&&&&&&&&&&")
                        ThesisSupervisionInformation(
                            user= request.user,
                            thesisSupervision_type = form.cleaned_data.get("thesisSupervision_type"),
                            thesisSupervision_supervisors = form.cleaned_data.get("thesisSupervision_supervisors"),
                            thesisSupervision_studentName = form.cleaned_data.get("thesisSupervision_studentName"),
                            thesisSupervision_studentSession =  form.cleaned_data.get("thesisSupervision_studentSession"),
                            thesisSupervision_thesisTitle = form.cleaned_data.get("thesisSupervision_thesisTitle"),
                                
                        ).save()
                        messages.success(request, f'Your Thesis Supervision Information was added successfully')

        elif "researchInterest_info_button" in request.POST:
            
            if (researchInterest_formset.is_valid()):
                # educationInfo = EducationInformationForm(request.POST)   
                print(researchInterest_formset)
                for form in researchInterest_formset:
                    print("#########################################")
                    # print(form)
                    print(form.cleaned_data.get("otherActivities_type"))
                    if form.cleaned_data.get("otherActivities_type")  :
                        
                        print("&&&&&&&&&&&&&&&&&&&&&&&")
                        ResearchInterestInformation(
                            user= request.user,
                            researchInterest_fields = form.cleaned_data.get("researchInterest_fields"),
                                
                        ).save()
                        messages.success(request, f'Your Research Interest Information was added successfully')



    elif request.method == "Get":
        # formset = EducationInformationForm(queryset=EducationInformation.objects.none())
        # edu_formset = EducationInformationForm(request.GET or None)
        # spouse_formset = SpouseInformationForm(request.GET or None)
        # children_formset = ChildrenInformationForm (request.GET or None)
        edu_formset = EducationInfoFormset(request.GET, prefix="education")
        spouse_formset = SpouseInfoFormset(request.GET, prefix="spouse")
        children_formset = ChildrenInfoFormset(request.GET, prefix="children")
        traning_formset = TraningInfoFormset(request.GET, prefix="traning")
        posting_formset = PostingInfoFormset(request.GET, prefix="posting")
        promotion_formset = PromotionInfoFormset(request.GET, prefix="promotion")
        achievement_formset = AchievementInfoFormset(request.GET, prefix="achievement")
        leave_formset= LeaveInfoFormset(request.GET, prefix="leave")
        otherService_formset = OtherServiceInfoFormset(request.GET, prefix="otherService")
        otherActivities_formset = OtherActivitiesInfoFormset(request.GET, prefix="otherActivities")
        r_and_d_formset = R_and_D_ProjectInfoFormset(request.GET , prefix="r_and_d")
        thesisSupervision_formset = ThesisSupervisionInfoFormset(request.GET, prefix="thesisSupervision")
        researchInterest_formset = ResearchInterestInfoFormset(request.GET, prefix="researchInterest")


    return render(request, 'users/add-profile.html', context)