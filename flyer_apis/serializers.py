from rest_framework import serializers
from .models import FlyerDetail

class FlyerDetailSerializer(serializers.ModelSerializer):


	image = serializers.ImageField(max_length=None, use_url=True)

	class Meta:
		model = FlyerDetail
		fields = ['id', 'client_id', 'company_name', 'creators_name', 'email_id', 'phone_no', 'content', 'image']
