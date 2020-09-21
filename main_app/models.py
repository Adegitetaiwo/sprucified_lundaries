from django.db import models

# Create your models here.
class customerTestimony(models.Model):
    full_name = models.CharField(max_length=190)
    passport = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None)
    testimony = models.TextField()

    def __str__(self):
        return '{} Testimony. '.format(self.full_name)
    

    class Meta:
        verbose_name_plural = 'Customer Testimony'

class fourImageGallary(models.Model):
    image_file_name = models.CharField(max_length=150)
    image = models.ImageField(
        upload_to='images', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.image_file_name
    
    class Meta:
        verbose_name_plural = '[Gallary] Four Image Gallary'
    
    
class set_frequently_asked_question(models.Model):
    question = models.CharField(max_length=350)
    answer = models.TextField()

    def __str__(self):
        return self.question
    class Meta:
        verbose_name_plural = 'Set Frequently Asked Question'
