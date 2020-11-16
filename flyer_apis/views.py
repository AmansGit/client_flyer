# from django.shortcuts import render, get_object_or_404, render_to_http_response
from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework.decorators import action

# REST FRAMEWORK
from rest_framework import status
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import authentication, permissions

from django.contrib.auth.models import User

import json

from .models import FlyerDetail
from .serializers import FlyerDetailSerializer
import requests as request


#	endpoint for image input
# class Flyer(APIView):

# 	# authentication_classes = [authentication.TokenAuthentication]	#We have to do ID authentications
# 	# permission_classes = [permissions.IsAdminUser]					# just for Admin user
	
# 	def __init__(self, id):
# 		print("id:", id)
# 		pass

# 	def get(self, id):
# 		print("get method")
# 		pass

# 	#/flyer/:pk
# 	def retrieve(self,id):
# 		print("retrieve method")
# 		response = {}
# 		query = pk
# 		qs = FlyerDetail.objects.filter(id=pk)
# 		if qs is None:
# 			status_code = 400
# 			return HttpResponseBadRequest('Invalid refernce ID', status=status_code)

# 		else:
# 			response = {
# 				'Company Name': qs.company_name,
# 				'Created by': qs.creators_name,
# 				'Email-id': qs.email_id,
# 				'Phone': qs.phone_no,
# 				'Content': qs.content
# 			}
# 			json_data = json.dumps(response)
# 			return HttpResponse(json_data, content_type= 'application/json')


# 	# def post(self):
# 	# 	print("post method")
# 	# 	response = {}
# 	# 	body = request.body
# 	# 	data = request.data
# 	# 	print("body: ", body)
# 	# 	print("data: ", data)
# 	# 	if not is_json(data):
# 	# 		return self.render_to_http_response(json.dumps({
# 	# 			'msg': 'Not valid json data'
# 	# 			}), status=400)
# 	# 	# strdata = json.loads(request.body)
# 	# 	# form
# 	# 	# response = {
# 	# 	# 	'Company Name'	: body.company_name,
# 	# 	# 	'Creator Name'	: body.creators_name,
# 	# 	# 	'Emaid'			: body.email_id,
# 	# 	# 	'Phone No'		: body.phone_no,
# 	# 	# 	'Content'		: body.content,
# 	# 	# 	# 'Image'			: body.image,
# 	# 	# }
# 	# 	return HttpResponse(json.dumps(response), content_type='application/json')


class FlyerViewSet(ModelViewSet):
	queryset = FlyerDetail.objects.all()
	serializer_class=FlyerDetailSerializer
	@action(methods=['POST'], detail=True)
	def create_flyer(self, request):
		response = {}
		flyer_json = json.loads(request.body)
		company_name = flyer_json['company_name']
		creators_name = flyer_json['creators_name']
		email_id = flyer_json['email_id']
		phone_no = flyer_json['phone_no']
		content = flyer_json['content']

		if not is_json(data):
			return self.render_to_http_response(json.dumps({
				'msg': 'Not valid json data'
				}), status=400)

		flyer_qs = FlyerDetail(company_name=company_name, creators_name=creators_name,
						 email_id=email_id, phone_no=phone_no, content=content)
	
		try:
			flyer_qs.save()
			response = json.dumps({
				'Success': "Your data is stored"
				})
		except:
			response = json.dumps({
				'Error': "Something went wrong"
				})
		return HttpResponse(response, content_type='application/json')


class FlyerGetSet(ModelViewSet):
	@action(methods=['GET'], detail=True)
	def retrieve_flyer(self,id):
		print("retrieve method")
		response = {}
		query = pk
		qs = FlyerDetail.objects.filter(id=pk)
		if qs is None:
			status_code = 400
			return HttpResponseBadRequest('Invalid refernce ID', status=status_code)

		else:
			response = {
				'Company Name': qs.company_name,
				'Created by': qs.creators_name,
				'Email-id': qs.email_id,
				'Phone': qs.phone_no,
				'Content': qs.content
			}
			json_data = json.dumps(response)
			return HttpResponse(json_data, content_type= 'application/json')

