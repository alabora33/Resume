from django.contrib import admin
from core.models import *
# Register your models here.

@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']

    class Meta:
        model = GeneralSetting

@admin.register(ImageSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'file', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'file']
    list_editable = ['description', 'file']

    class Meta:
        model = ImageSetting

@admin.register(Skill)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name', 'percentage', 'updated_date', 'created_date']
    search_fields = ['name']
    list_editable = ['order', 'name', 'percentage']

    class Meta:
        model = Skill

@admin.register(Experience)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id','company_name', 'job_title', 'job_location', 'images', 'start_date', 'end_date']
    search_fields = ['company_name', 'job_title', 'job_location']
    list_editable = ['company_name', 'job_title', 'job_location', 'images', 'start_date', 'end_date']

    class Meta:
        model = Experience

@admin.register(Education)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id','school_name', 'edu_level', 'school_location', 'departmant', 'score', 'logos','start_date', 'end_date']
    search_fields = ['school_name', 'edu_level', 'school_location']
    list_editable = ['school_name', 'edu_level', 'school_location', 'departmant', 'score', 'logos', 'start_date', 'end_date']

    class Meta:
        model = Education

@admin.register(SocialMedia)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id','order', 'link', 'icon','updated_date', 'created_date']
    search_fields = [ 'link', 'icon']
    list_editable = ['order', 'link', 'icon']

    class Meta:
        model = SocialMedia