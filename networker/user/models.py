from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class NetworkerUser(models.Model):
	""" Main table for User """

	# default Django User
	# --------------------------
	# username, password, email, first_name, last_name
	
	# User extended
	# --------------------------
	user_extension = models.OneToOneField(User)
	relationship_to_group = models.CharField(max_length=50)
	profile_image = models.ImageField(upload_to='static/images', height_field=None, width_field=None, max_length=100)
	date_of_birth = models.DateField()

	def __str__(self):
		return self.user_extension.first_name + " " + self.user_extension.last_name

class SkillCategory(models.Model):
	""" Helper table for User_Skill """
	skill_category = models.CharField(max_length=20)

class UserSkill(models.Model):
	""" Sub-table for the User: Skill """
	user_id = models.ForeignKey(NetworkerUser)
	skill_category_id = models.ForeignKey(SkillCategory)
	skill_description = models.TextField(max_length=255, blank=True)

class AddressCategory(models.Model):
	""" Helper table for User_Address """
	address_category = models.CharField(max_length=10)

class UserAddress(models.Model):
	""" Sub-table for the User: Address """
	user_id = models.ForeignKey(NetworkerUser)
	address_category_id = models.ForeignKey(AddressCategory)
	street_address_1 = models.CharField(max_length=50)
	street_address_2 = models.CharField(max_length=50)
	city_town = models.CharField(max_length=50)
	state_province = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	postal_code = models.CharField(max_length=25)
	latitude_api = models.CharField(max_length=50)
	longitude_api = models.CharField(max_length=50)

class EmailCategory(models.Model):
	""" Helper table for User_Email """
	email_category = models.CharField(max_length=10)

class UserEmail(models.Model):
	""" Sub-table for the User: Email """
	user_id = models.ForeignKey(NetworkerUser)
	email_category_id = models.ForeignKey(EmailCategory)
	email = models.CharField(max_length=50, blank=True)

class PhoneCategory(models.Model):
	""" Helper table for User_Phone """
	phone_category = models.CharField(max_length=10)

class UserPhone(models.Model):
	""" Sub-table for the User: Phone """
	user_id = models.ForeignKey(NetworkerUser)
	phone_category_id = models.ForeignKey(PhoneCategory)
	country_code = models.PositiveSmallIntegerField(blank=True)
	phone_number = models.PositiveSmallIntegerField(blank=True)

class SocialMediaCategory(models.Model):
	""" Helper table for User_Social_Media """
	social_media_category = models.CharField(max_length=50)

class UserSocialMedia(models.Model):
	""" Sub-table for the User: Social Media """
	user_id = models.ForeignKey(NetworkerUser)
	social_media_category_id = models.ForeignKey(SocialMediaCategory)
	social_media_url = models.URLField(blank=True)

class JobCategory(models.Model):
	""" Helper table for User_Job """
	job_category = models.CharField(max_length=50)

class UserJob(models.Model):
	""" Sub-table for the User: Job """
	user_id = models.ForeignKey(NetworkerUser)
	job_category_id = models.ForeignKey(JobCategory)
	job_description = models.TextField(max_length=255, blank=True)
	company_name = models.CharField(max_length=50, blank=True)
	company_state_province = models.CharField(max_length=50, blank=True)
	company_country = models.CharField(max_length=50, blank=True)
	company_year_started = models.DateField(blank=True)
	company_year_ended = models.DateField(blank=True)

class EducationCategory(models.Model):
	""" Helper table for User_Education """
	education_category = models.CharField(max_length=50)

class UserEducation(models.Model):
	""" Sub-table for the User: Education """
	user_id = models.ForeignKey(NetworkerUser)
	education_category_id = models.ForeignKey(EducationCategory)
	education_description = models.TextField(max_length=255, blank=True)
	school_name = models.CharField(max_length=255, blank=True)
	graduation_status = models.BooleanField(default=False)
	school_year_started = models.DateField(blank=True)
	school_year_ended = models.DateField(blank=True)












