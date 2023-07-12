from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models



class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='Updated Date',
        help_text=''
    )
    # tüm tablolarda olacak ve auto_now ile veriyi her güncellediğimizde otomatik olarak updated_date de update edilecek
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date',
        help_text=''
    )
    # auto_now_add de veriyi her güncellediğinde değilde yaratıldığında 1 kere güncelliyor sadece
    class Meta:
        abstract=True


# Create your models here.
#django dan inherite ettiğimiz modelimizi nesne olarak tanımlıyoruz. Database deki bir tablo olduğunu belirtmiş oluyoruz
#field ler yani exceldeki sütunlar gibi bunları belirtiyoruz
class GeneralSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting'
    )
#name ile string olarak uzunluğu ve default olarak ismi aynı olacağını belirtiyoruz. Blank=True default da verilen boş veriyi kabul etmesini sağlar
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text = ''
    )
#description ile bu name i nerde kullandık ve ne için kullanıyoruz onu belirtiyoruz
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Parameter',
        help_text = ''
    )
#name kısmı örnek olarak About Me yazısı içindeki uzun yazılar da parameter de belirtilir

    def __str__(self):
        return f'General Setting: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)

class ImageSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting'
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text = ''
    )
    file = models.ImageField(
        default='',
        verbose_name='Image',
        help_text='',
        blank=True,
        upload_to='images/',
    )
    def __str__(self):
        return f'Image Setting: {self.name}'

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ('name',)

class Skill(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order'
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting'
    )
    percentage = models.IntegerField(
        default=50,
        verbose_name='Percentage',
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    def __str__(self):
        return f'Skill: {self.name}'

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ('order',)

class Experience(AbstractModel):
    company_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Company Name',
    )
    job_title = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Job Title',
    )
    job_location= models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Job Location',
    )
    images = models.ImageField(
        default='',
        verbose_name='Image',
        help_text='',
        blank=True,
        upload_to='images/',
    )
    start_date = models.DateField(
        verbose_name='Start Date'
    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name='End Date'
    )
    def __str__(self):
        return f'Experience: {self.company_name}'

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ('-start_date',)

class Education(AbstractModel):
    school_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='School Name',
    )
    edu_level = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Education Level',
    )
    school_location= models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='School Location',
    )
    departmant =models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Departmant',
    )
    score = models.FloatField(
        verbose_name='Score',
        default='',
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(4)]
    )
    logos = models.ImageField(
        default='',
        verbose_name='Image',
        help_text='',
        blank=True,
        upload_to='images/',
    )
    start_date = models.DateField(
        verbose_name='Start Date'
    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name='End Date'
    )
    def __str__(self):
        return f'Education: {self.school_name}'

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        ordering = ('-start_date',)

class SocialMedia(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order'
    )
    link = models.URLField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Link'
    )
    icon = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Icon'
    )
    def __str__(self):
        return f'Social Media: {self.link}'

    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'Social Media'
        ordering = ('order',)
