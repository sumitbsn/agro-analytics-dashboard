from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from cropdata.models import *

class cropdataDetail(APIView):

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

