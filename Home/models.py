from django.db import models

# Contact Form Model
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} <{self.email}>"

# Skill Model
class Skill(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}: {self.percentage}%"

# Experience Model
class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"

# Education Model
class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.degree} from {self.institution}"

# Project Model
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField()

    def __str__(self):
        return self.title

# Service Model
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# Testimonial Model
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"Testimonial from {self.name}"

# Social Link Model
class SocialLink(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.name
