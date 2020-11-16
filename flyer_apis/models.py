from django.db import models


class FlyerDetail(models.Model):
	id 				= models.CharField(max_length=50, null=False, blank=False, unique=True, primary_key=True)
	client_id 		= models.IntegerField(null=False)
	company_name	= models.CharField(max_length= 20, null= False, blank= False)
	creators_name	= models.CharField(max_length=20)
	email_id		= models.EmailField(max_length=30, null=False, blank=False)
	phone_no		= models.IntegerField(null=False, blank=False)
	content			= models.TextField(null=False, blank=False)
	image			= models.ImageField(upload_to='image/pic', height_field= None, width_field= None)

	db_table = "flyer_details"