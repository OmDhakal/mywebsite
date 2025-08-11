from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ContactMessage, Skill, Experience, Education, Project, Service, Testimonial, SocialLink

admin.site.register(ContactMessage)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.register(SocialLink)

