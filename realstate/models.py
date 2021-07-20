from django.db import models


class Developer(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='الأسم')
    address = models.CharField(max_length=255, null=True, verbose_name='العنوان')
    image = models.ImageField(null=True, blank=True, verbose_name='الشعار')

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='الأسم')
    details = models.TextField(null=True, verbose_name='التفاصيل')
    image = models.ImageField(null=True, blank=True, verbose_name='الشعار')

    def __str__(self):
        return self.name


class ProjectState(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='اسم الكوبوتد')
    description = models.CharField(max_length=255, null=True, verbose_name='عن الكوبوتد')
    logo = models.ImageField(verbose_name='لوجو الكوبوتد', null=True)
    developer = models.ForeignKey(Developer, null=True, blank=True, on_delete=models.CASCADE, verbose_name='المطور')
    price = models.IntegerField(null=True, blank=True, default=1500, verbose_name='السعر')
    location = models.ForeignKey(Location, null=True, blank=True, on_delete=models.CASCADE, verbose_name='الموفع')

    def __str__(self):
        return self.name


class PayRequest(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='اسم')
    email = models.CharField(max_length=255, null=True, verbose_name='البريد الألكترونى')
    phone = models.IntegerField(blank=True, null=True, verbose_name='الهاتف')

    def __str__(self):
        return self.name
