# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from restapi.models import *
from django.db.models import Q
# from easy_pdf.views import PDFTemplateView
# from easy_pdf import *

# Create your views here.
def registration(request):
    return render_to_response('registration.html')

class dataDetail(APIView):

    def get(self, request):
        data = dict()
        data = {'name':'ubuntu', 'os':'linux', 'type': 'opensource'}
        return Response(data, status=status.HTTP_200_OK)


class userDetail(APIView):

    def get(self, request):
        #data = dict()
        #data = {'name':'sumit', 'gender':'male', 'age': '21'}
        final = []
        res = Info.objects.all()
        for item in res:
            data = {}
            data['id'] = item.id
            data['first_name'] = item.first_name
            data['last_name'] = item.last_name
            data['age'] = item.age
            data['address'] = item.address
            data['salary'] = item.salary
            final.append(data)
        #return Response(final, status=status.HTTP_200_OK)
        return render(request, 'userdetail.html', {'data':final, 'text':"This is User Table"})




class userQuery(APIView):

    def get(self, request):
        final = []
        name = request.GET.get('name', '')
        res = Info.objects.filter(Q(first_name__contains=name) | Q(last_name__contains=name))
        for item in res:
            data = {}
            data['id'] = item.id
            data['first_name'] = item.first_name
            data['last_name'] = item.last_name
            data['age'] = item.age
            data['address'] = item.address
            data['salary'] = item.salary
            final.append(data)
        #return Response(final, status=status.HTTP_200_OK)
        return render(request, 'usersearch.html', {'data':final, 'text':"This is User Table"})

class dataPassing(APIView):
	def get(self,request):
		data = list()
		data = ['UBU', 'MIN', 'DEB', 'LOL']
		return Response(data, status=status.HTTP_200_OK) 

class submitResult(APIView):
    def post(self,request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        address = request.POST['address']
        salary = request.POST['salary']

        print (first_name)
        print (age)
        # res = Info.objects.all()
        # for item in res:
        #     print (item.name)
        #     print (item.age)
        q = Info(first_name=first_name, last_name=last_name, age=age, address=address, salary=salary)
        q.save()
        print ("xxxxxxxxxxxxxxxxxxxxx")
        #return Response({'username':name, 'password':age}, status=status.HTTP_200_OK) 
        #return Response("Success!!", status=status.HTTP_200_OK)
        return HttpResponseRedirect("/userdetail/")

class cropData(APIView):

    def get(self, request):
        final = []
        res = Cropdata.objects.all()
        for item in res:
            data = {}
            data['id'] = item.id
            data['state'] = item.state
            data['district'] = item.district
            data['year'] = item.year
            data['season'] = item.season
            data['crop'] = item.crop
            data['production'] = item.production
            data['productivity'] = item.productivity
            final.append(data)
        # return Response(final, status=status.HTTP_200_OK)
        return render(request, 'cropdetail.html', {'crop_data':final, 'text':"This is Crop production details of Tamilnadu state from year 1997 to 2016"})

# class InvoicePDFView(PDFTemplateView):
#     template_name = "userdetail.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         myinstance = get_object_or_404(MyModel, pk=context['pk'])
#         context['myinstance'] = myinstance
#         return context
class imageStore(APIView):
    def get(self, request):
        res = Img.objects.filter(id = '1')
        # res1 = Img.objects.values_list('path', flat=True).distinct()
        print (res)
        return render(request, 'image.html', {'path': res}) 