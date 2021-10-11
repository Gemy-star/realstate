from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='الأسم')
    price = models.TextField(null=True, verbose_name='التفاصيل')
    image = models.ImageField(null=True, blank=True, verbose_name='الشعار')
    category = models.ForeignKey(Category, on_delete=models.CASCADE , null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    products = models.ManyToManyField(Product , null=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.quantity)


class PayRequest(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='اسم')
    email = models.CharField(max_length=255, null=True, verbose_name='البريد الألكترونى')
    phone = models.IntegerField(blank=True, null=True, verbose_name='الهاتف')
    order = models.OneToOneField(Order , on_delete=models.CASCADE , null=True)

    def __str__(self):
        return self.name
