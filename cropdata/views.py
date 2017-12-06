from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from cropdata.models import *
from cropdata.fusioncharts import FusionCharts
from collections import OrderedDict

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

class temperatureDetail(APIView):

    def get(self, request):
        final = []
        res = Temperature.objects.all()
        for item in res:
            data = {}
            data['id'] = item.id
            data['district'] = item.district
            data['year'] = item.year
            data['january'] = item.january
            data['february'] = item.february
            data['march'] = item.march
            data['april'] = item.april
            data['may'] = item.may
            data['june'] = item.june
            data['july'] = item.july
            data['august'] = item.august
            data['september'] = item.september
            data['october'] = item.october
            data['november'] = item.november
            data['december'] = item.december
            final.append(data)
        print (final[10]['october'])
        # return Response(final, status=status.HTTP_200_OK)
        return render(request, 'temperature.html', {'temp_data':final})

class pressureDetail(APIView):

    def get(self, request):
        final = []
        res = Pressure.objects.filter()
        for item in res:
            data = {}
            data['id'] = item.id
            data['district'] = item.district
            data['year'] = item.year
            data['january'] = item.january
            data['february'] = item.february
            data['march'] = item.march
            data['april'] = item.april
            data['may'] = item.may
            data['june'] = item.june
            data['july'] = item.july
            data['august'] = item.august
            data['september'] = item.september
            data['october'] = item.october
            data['november'] = item.november
            data['december'] = item.december
            final.append(data)
        # return Response(final, status=status.HTTP_200_OK)
        return render(request, 'pressure.html', {'press_data':final})

    
class pressureChartApi(APIView):

    def get(self, request):
        final = []
        year = []
        district = request.GET.get('dis', None)
        yr = request.GET.get('year', None)
        print (district,yr)
        if yr == "ALL":
            res = Pressure.objects.filter(district = district).order_by('year')
        else:
            res = Pressure.objects.filter(district = district, year= yr).order_by('year')
        for item in res:    
            data = OrderedDict()
            year.append(item.year)
            data['january'] = item.january
            data['february'] = item.february
            data['march'] = item.march
            data['april'] = item.april
            data['may'] = item.may
            data['june'] = item.june
            data['july'] = item.july
            data['august'] = item.august
            data['sepetember'] = item.september
            data['october'] = item.october
            data['november'] = item.november
            data['december'] = item.december
            final.append(data.values())
        #print (final)
        temp = {'year':year, 'month': data.keys(), 'value': final}
        return Response({'alldata':temp}, status=status.HTTP_200_OK)

class pressureChart(APIView):

    def get(self, request):
        return render(request, 'pressurechart.html')


class pressdataPassing(APIView):
    def get(self, request):
        
        res1 = Pressure.objects.values_list('district', flat=True).distinct()
        res2 = Pressure.objects.values_list('year', flat=True).distinct()
        data = {'dist':res1, 'yr':res2}

        return Response({'pdata':data}, status=status.HTTP_200_OK)


class temperatureChartApi(APIView):

    def get(self, request):
        final = []
        year = []
        district = request.GET.get('dis', None)
        yr = request.GET.get('year', None)
        # print (yr)
        # print (district)
        if yr == "ALL":
            res = Temperature.objects.filter(district = district).order_by('year')
        else:
            res = Temperature.objects.filter(district = district, year= yr).order_by('year')
        
        for item in res:
            data = OrderedDict()
            year.append(item.year)
            data['january'] = item.january
            data['february'] = item.february
            data['march'] = item.march
            data['april'] = item.april
            data['may'] = item.may
            data['june'] = item.june
            data['july'] = item.july
            data['august'] = item.august
            data['sepetember'] = item.september
            data['october'] = item.october
            data['november'] = item.november
            data['december'] = item.december
            final.append(data.values())
        #print (final)
        temp = {'year':year, 'month': data.keys(), 'value': final}
        return Response({'alldata':temp}, status=status.HTTP_200_OK)
        # return Response({'all':x}, status=status.HTTP_200_OK)

class temperatureChart(APIView):

    def get(self, request):
        return render(request,'temperaturechart.html')


class tempdataPassing(APIView):
    def get(self, request):
        
        res1 = Temperature.objects.values_list('district', flat=True).distinct()
        res2 = Temperature.objects.values_list('year', flat=True).distinct()
        data = {'dist':res1, 'yr':res2}

        return Response({'tdata':data}, status=status.HTTP_200_OK)


