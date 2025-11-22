from django.db import models
from django.utils.text import slugify

# Create your models here.
class Service(models.Model): #tabloları oluşturmak için python class ı oluşturduk
    title = models.CharField(max_length=100) #bunu tablo olarak düşün title burda sütun olarak CharField veri türü max_length kısıtlama olarak kullanıldı
    description = models.TextField()  ##uzun olableceği için Textfield yapttık
    icon_class = models.CharField(max_length=50) #icon için icon class ı ekledik
    is_featured = models.BooleanField(default=False) #bazıları anasayfada görünmesini isteyebiliriz  bazılarını istemeiyebilirz bu yüzden boolean oluşturduk
    slug = models.SlugField(unique=True,blank=True) #her hizmetin benzersiz bir slug ı olmalı

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Service,self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['title']