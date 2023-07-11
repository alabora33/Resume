from django.db import models

# Create your models here.
#django dan inherite ettiğimiz modelimizi nesne olarak tanımlıyoruz. Database deki bir tablo olduğunu belirtmiş oluyoruz
#field ler yani exceldeki sütunlar gibi bunları belirtiyoruz
class GeneralSetting(models.Model):
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
#name kısmı örnek oalrak About Me yazısı içindeki uzun yazılar da parameter de belirtilir
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='Updated Date',
        help_text = ''
    )
#tüm tablolarda olacak ve auto_now ile veriyi her güncellediğimizde otomatik olarak updated_date de update edilecek
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date',
        help_text = ''
    )
#auto_now_add de veriyi her güncellediğinde değilde yaratıldığında 1 kere güncelliyor sadece

    def __str__(self):
        return f'General Setting: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)

class ImageSetting(models.Model):
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
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='Updated Date',
        help_text=''
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date',
        help_text=''
    )

    def __str__(self):
        return f'Image Setting: {self.name}'

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ('name',)
