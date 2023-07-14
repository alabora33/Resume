from django.shortcuts import render, redirect, get_object_or_404
from core.models import GeneralSetting, ImageSetting,Skill,Experience,Education,SocialMedia,Document


def layout(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_description = GeneralSetting.objects.get(name='site_description').parameter
    home_banner_title = GeneralSetting.objects.get(name='home_banner_title').parameter
    home_banner_description = GeneralSetting.objects.get(name='home_banner_description').parameter
    home_banner_name = GeneralSetting.objects.get(name='home_banner_name').parameter
    about_myself_footer = GeneralSetting.objects.get(name='about_myself_footer').parameter
    about_myself_welcome = GeneralSetting.objects.get(name='about_myself_welcome').parameter


    #Images
    header_logo = ImageSetting.objects.get(name='header_logo').file
    home_banner_image = ImageSetting.objects.get(name='home_banner_image').file
    site_favicon = ImageSetting.objects.get(name='site_favicon').file

    #SocialMedia
    socialmedia = SocialMedia.objects.all()

    #Documents
    documents = Document.objects.all()

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'about_myself_footer': about_myself_footer,
        'about_myself_welcome': about_myself_welcome,
        'header_logo': header_logo,
        'home_banner_image': home_banner_image,
        'site_favicon': site_favicon,
        'socialmedia': socialmedia,
        'documents': documents,
    }
    return context

# Create your views here.
def index(request):

    #Skills
    skills = Skill.objects.all()
    # .order_by('order') order veya neye göre web de sıralıcaksak onu yazarız default u admin sayfasındaki

    #Experiences
    experiences = Experience.objects.all()

    #Educations
    educations = Education.objects.all()


    context={
        'skills':skills,
        'experiences':experiences,
        'educations':educations,
    }
    return render(request,'index.html',context=context)

def redirect_urls(request, slug):
    doc = get_object_or_404(Document, slug=slug)
    return  redirect(doc.file.url)
