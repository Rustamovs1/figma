from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to="CategoryImg")

    def __str__(self):
        return self.name


class Banner(models.Model):
    img = models.ImageField(upload_to='BannerImg')
    title = models.CharField(max_length=255)
    text = models.TextField()


class News(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='NewsImg')
    description = models.TextField()
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)


class About(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    vidio = models.FileField(upload_to='AboutVidio')


class Information(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=25)
    fax = models.CharField(max_length=70)
    address = models.CharField(max_length=255)


class Team(models.Model):
    img = models.ImageField(upload_to='TeamImg')
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name


class Contact(models.Model):
    subject = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    explanation = models.TextField()
    file = models.FileField(upload_to='Contact', null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    explanation = models.TextField()
    img = models.ImageField(upload_to='PostIMG')


class PostVidio(models.Model):
    title = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    explanation = models.TextField()
    url = models.URLField()
    Profile = models.ForeignKey(User, on_delete=models.CASCADE)

