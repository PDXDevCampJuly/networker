from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

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
		return "[{}] {}-{} {}".format(self.user_extension.id, self.user_extension.username, self.user_extension.first_name, self.user_extension.last_name)

class SkillCategory(models.Model):
	""" Helper table for User_Skill """
	skill_category = models.CharField(max_length=20)

	def __str__(self):
		return self.skill_category

class UserSkill(models.Model):
	""" Sub-table for the User: Skill """
	user_id = models.ForeignKey(NetworkerUser)
	skill_category_id = models.ForeignKey(SkillCategory)
	skill_description = models.TextField(max_length=255, blank=True)

	def __str__(self):
		return "{}, {} ({})".format(self.user_id, self.skill_description, self.skill_category_id)

class AddressCategory(models.Model):
	""" Helper table for User_Address """
	address_category = models.CharField(max_length=10)

	def __str__(self):
		return self.address_category

class UserAddress(models.Model):
	""" Sub-table for the User: Address """
	user_id = models.ForeignKey(NetworkerUser)
	address_category_id = models.ForeignKey(AddressCategory)
	street_address_1 = models.CharField(max_length=50)
	street_address_2 = models.CharField(max_length=50, blank=True)
	city_town = models.CharField(max_length=50)
	state_province = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	postal_code = models.CharField(max_length=25)
	latitude_api = models.FloatField()
	longitude_api = models.FloatField()

	def __str__(self):
		return "{}, {}, {}, {} ({})".format(self.user_id, self.street_address_1, self.postal_code, self.country, self.address_category_id)

class EmailCategory(models.Model):
	""" Helper table for User_Email """
	email_category = models.CharField(max_length=10)

	def __str__(self):
		return self.email_category

class UserEmail(models.Model):
	""" Sub-table for the User: Email """
	user_id = models.ForeignKey(NetworkerUser)
	email_category_id = models.ForeignKey(EmailCategory)
	email = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return "{}, {} ({}) ".format(self.user_id, self.email, self.email_category_id, )

class PhoneCategory(models.Model):
	""" Helper table for User_Phone """
	phone_category = models.CharField(max_length=10)

	def __str__(self):
		return self.phone_category

class UserPhone(models.Model):
	""" Sub-table for the User: Phone """
	user_id = models.ForeignKey(NetworkerUser)
	phone_category_id = models.ForeignKey(PhoneCategory)
	# country_code = models.PositiveSmallIntegerField(blank=True)
	phone_number = PhoneNumberField()

	def __str__(self):
		return "{}, {} ({})".format(self.user_id, self.phone_number, self.phone_category_id)

class SocialMediaCategory(models.Model):
	""" Helper table for User_Social_Media """
	social_media_category = models.CharField(max_length=50)

	def __str__(self):
		return self.social_media_category

class UserSocialMedia(models.Model):
	""" Sub-table for the User: Social Media """
	user_id = models.ForeignKey(NetworkerUser)
	social_media_category_id = models.ForeignKey(SocialMediaCategory)
	social_media_url = models.URLField(blank=True)

	def __str__(self):
		return "{}, {} ({})".format(self.user_id, self.social_media_url, self.social_media_category_id)

class JobCategory(models.Model):
	""" Helper table for User_Job """
	job_category = models.CharField(max_length=50)

	def __str__(self):
		return self.job_category

class UserJob(models.Model):
	""" Sub-table for the User: Job """
	user_id = models.ForeignKey(NetworkerUser)
	job_category_id = models.ForeignKey(JobCategory)
	job_description = models.TextField(max_length=255, blank=True)
	company_name = models.CharField(max_length=50, blank=True)
	company_state_province = models.CharField(max_length=50, blank=True)
	company_country = models.CharField(max_length=50, blank=True)
	is_current = models.BooleanField(default=True)
	company_year_started = models.DateField(default=timezone.now)
	company_year_ended = models.DateField(default=timezone.now)

	def __str__(self):
		return "{}, {}, current={} [{}]".format(self.user_id, self.company_name, self.is_current, self.job_category_id) 

class EducationCategory(models.Model):
	""" Helper table for User_Education """
	education_category = models.CharField(max_length=50)

	def __str__(self):
		return self.education_category

class UserEducation(models.Model):
	""" Sub-table for the User: Education """
	user_id = models.ForeignKey(NetworkerUser)
	education_category_id = models.ForeignKey(EducationCategory)
	education_description = models.TextField(max_length=255, blank=True)
	school_name = models.CharField(max_length=255, blank=True)
	is_completed = models.BooleanField(default=False)
	school_year_started = models.DateField(default=timezone.now)
	school_year_ended = models.DateField(default=timezone.now)

	def __str__(self):
		return "{}, {}, passed={} ({})".format(self.user_id, self.school_name, self.is_completed, self.education_category_id) 












