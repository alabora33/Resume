from django.db import models

# Create your models here.
#django dan inherite ettiğimiz modelimizi nesne olarak tanımlıyoruz. Database deki bir tablo olduğunu belirtmiş oluyoruz
#field ler yani exceldeki sütunlar gibi bunları belirtiyoruz
class GeneralSettings(models.Model):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True
    )
#name ile string olarak uzunluğu ve default olarak ismi aynı olacağını belirtiyoruz. Blank=True default da verilen boş veriyi kabul etmesini sağlar
    description = models.CharField(
        default='',
        max_length=254,
        blank=True
    )
#description ile bu name i nerde kullandık ve ne için kullanıyoruz onu belirtiyoruz
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True
    )
#name kısmı örnek oalrak About Me yazısı içindeki uzun yazılar da parameter de belirtilir
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True
    )
#tüm tablolarda olacak ve auto_now ile veriyi her güncellediğimizde otomatik olarak updated_date de update edilecek
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True
    )
#auto_now_add de veriyi her güncellediğinde değilde yaratıldığında 1 kere güncelliyor sadece
