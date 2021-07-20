from django.db import models


class FAQ(models.Model):
    question = models.TextField(null=True, blank=True, verbose_name='السؤال')
    answer = models.TextField(null=True, blank=True, verbose_name='الأجابة')

    def __str__(self):
        return self.question


class Contact(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='الأسم')
    email = models.CharField(max_length=255, null=True, blank=True, verbose_name='البريد الألكترونى')
    subject = models.CharField(max_length=255, null=True, blank=True, verbose_name='عنوان الرسالة')
    message = models.TextField(null=True, blank=True, verbose_name='موضوع الرسالة')

    def __str__(self):
        return self.name
