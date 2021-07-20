# Generated by Django 3.0 on 2021-05-07 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='الأسم')),
                ('address', models.CharField(max_length=255, null=True, verbose_name='العنوان')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='الشعار')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='الأسم')),
                ('details', models.CharField(max_length=255, null=True, verbose_name='التفاصيل')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='الشعار')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='اسم الكوبوتد')),
                ('description', models.CharField(max_length=255, null=True, verbose_name='عن الكوبوتد')),
                ('logo', models.ImageField(null=True, upload_to='', verbose_name='لوجو الكوبوتد')),
                ('price', models.IntegerField(blank=True, default=1500, null=True, verbose_name='السعر')),
                ('developer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='realstate.Developer', verbose_name='المطور')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='realstate.Location', verbose_name='الموفع')),
            ],
        ),
    ]
