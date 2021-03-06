from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from cropdata.models import *
from collections import OrderedDict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.template import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.conf import settings
import operator
from functools import reduce
from django.db.models import Q
from django.template.loader import get_template 
import os


class cropdataDetail(APIView):

    def get(self, request):
        page = request.GET.get('page', 1)
        final = []
        res = Cropdata.objects.all()

        
        paginator = Paginator(res, 500)
        try:
            res1 = paginator.page(page)
        except PageNotAnInteger:
            res1 = paginator.page(1)
        except EmptyPage:
            res1 = paginator.page(paginator.num_pages)


        # for item in res1:
        #     data = {}
        #     data['id'] = item.id
        #     data['state'] = item.state
        #     data['district'] = item.district
        #     data['year'] = item.year
        #     data['season'] = item.season
        #     data['crop'] = item.crop
        #     data['production'] = item.production
        #     data['productivity'] = item.productivity
        #     final.append(data)
        # return Response(final, status=status.HTTP_200_OK)
        return render(request, 'cropdetail.html', {'crop_data':res1, 'text':"This is Crop production details of Tamilnadu state from year 1997 to 2016"})

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
        # print (final[10]['october'])
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
            data['september'] = item.september
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

class rainfallChartApi(APIView):

    def get(self, request):
        final = []
        year = []
        district = request.GET.get('dis', None)
        yr = request.GET.get('year', None)
        # print (yr)
        # print (district)
        if yr == "ALL":
            res = Rainfall.objects.filter(district = district).order_by('year')
        else:
            res = Rainfall.objects.filter(district = district, year= yr).order_by('year')
        
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

class rainfallChart(APIView):

    def get(self, request):
        return render(request,'rainfallchart.html')


class rainfalldataPassing(APIView):
    def get(self, request):
        
        res1 = Rainfall.objects.values_list('district', flat=True).distinct()
        res2 = Rainfall.objects.values_list('year', flat=True).distinct()
        data = {'dist':res1, 'yr':res2}

        return Response({'rdata':data}, status=status.HTTP_200_OK)


class cropdataApi(APIView):

    def get(self, request):
        ret_dict = {'list': [], 'config': {'has_prev': None, 'has_next': None, 'cur_page': None, 'total_pages': None}}        

        count_per_page    = request.GET.get('count', 15) 
        page_number       = request.GET.get('page', 1)
        year              = request.GET.get('year', None)        
        district          = request.GET.get('district', None)
        season            = request.GET.get('season', None)
        crop              = request.GET.get('crop', None)
        treated_obj_list  = Cropdata.objects.all().values('id', 
                                                        'state',
                                                        'district',
                                                        'year',
                                                        'season',
                                                        'crop',
                                                        'production',
                                                        'productivity').order_by('id')
        

        if year is not None and year != 'ALL':
            treated_obj_list = treated_obj_list.filter(year=year)
        if district is not None and district != 'ALL':
            treated_obj_list = treated_obj_list.filter(district=district)
        if season is not None and season != 'ALL':
            treated_obj_list = treated_obj_list.filter(season=season)
        if crop is not None and crop != 'ALL':
            treated_obj_list = treated_obj_list.filter(crop=crop)


        paginator         = Paginator(treated_obj_list, count_per_page)
        try:
            corr_id_list  = paginator.page(page_number)
        except PageNotAnInteger:
            corr_id_list  = paginator.page(1)
        except EmptyPage:
            corr_id_list  = paginator.page(paginator.num_pages)

        ret_dict['config']['has_prev']      = corr_id_list.has_previous()
        ret_dict['config']['has_next']      = corr_id_list.has_next()
        ret_dict['config']['cur_page']      = corr_id_list.number
        ret_dict['config']['total_pages']   = corr_id_list.paginator.num_pages

        # today   = datetime.datetime.today()

        for row in corr_id_list:
            temp_dict = {
                        'sample_info' : {
                                        'id':                          row['id'],
                                        'state':                       row['state'],
                                        'district':                    row['district'], 
                                        'year':                        row['year'],
                                        'season':                      row['season'],
                                        'crop':                        row['crop'], 
                                        'production':                  row['production'],
                                        'productivity':                row['productivity']
                                    }
            }
            ret_dict['list'].append(temp_dict)

        res1 = Cropdata.objects.values_list('district', flat=True).distinct()
        res2 = Cropdata.objects.values_list('year', flat=True).distinct().order_by('year')
        res3 = Cropdata.objects.values_list('season', flat=True).distinct()
        res4 = Cropdata.objects.values_list('crop', flat=True).distinct()

        ret_dict['district'] = sorted(res1)
        ret_dict['year'] = sorted(res2)
        ret_dict['season'] = sorted(res3)
        ret_dict['crop'] = sorted(res4)


        return Response(ret_dict, status=status.HTTP_200_OK)

        
class CropData(APIView):

    def get(self, request):
        return render(request,'cropdata.html')

class temperature_table_Api(APIView):

    def get(self, request):
        ret_dict = {'list': [], 'config': {'has_prev': None, 'has_next': None, 'cur_page': None, 'total_pages': None}}        

        count_per_page    = request.GET.get('count', 15) 
        page_number       = request.GET.get('page', 1)
        year              = request.GET.get('year', None)        
        district          = request.GET.get('district', None)

        treated_obj_list  = Temperature.objects.all().values('id', 
                                                        'district',
                                                        'year',
                                                        'january',
                                                        'february',
                                                        'march',
                                                        'april',
                                                        'may',
                                                        'june',
                                                        'july',
                                                        'august',
                                                        'september',
                                                        'october',
                                                        'november',
                                                        'december').order_by('id')
        

        if year is not None and year != 'ALL':
            treated_obj_list = treated_obj_list.filter(year=year)
        if district is not None and district != 'ALL':
            treated_obj_list = treated_obj_list.filter(district=district)


        paginator         = Paginator(treated_obj_list, count_per_page)
        try:
            corr_id_list  = paginator.page(page_number)
        except PageNotAnInteger:
            corr_id_list  = paginator.page(1)
        except EmptyPage:
            corr_id_list  = paginator.page(paginator.num_pages)

        ret_dict['config']['has_prev']      = corr_id_list.has_previous()
        ret_dict['config']['has_next']      = corr_id_list.has_next()
        ret_dict['config']['cur_page']      = corr_id_list.number
        ret_dict['config']['total_pages']   = corr_id_list.paginator.num_pages

        # today   = datetime.datetime.today()

        for row in corr_id_list:
            temp_dict = {
                        'sample_info' : {
                                        'id':                          row['id'],
                                        'district':                    row['district'], 
                                        'year':                        row['year'],
                                        'january':                     row['january'],
                                        'february':                    row['february'], 
                                        'march':                       row['march'],
                                        'april':                       row['april'],
                                        'may':                         row['may'],
                                        'june':                        row['june'],
                                        'july':                        row['july'],
                                        'august':                      row['august'],
                                        'september':                   row['september'],
                                        'october':                     row['october'],
                                        'november':                    row['november'],
                                        'december':                    row['december'],
                                    }
            }
            ret_dict['list'].append(temp_dict)

        res1 = Temperature.objects.values_list('district', flat=True).distinct()
        res2 = Temperature.objects.values_list('year', flat=True).distinct().order_by('year')

        ret_dict['district'] = sorted(res1)
        ret_dict['year'] = sorted(res2)

        return Response(ret_dict, status=status.HTTP_200_OK)

class temperatureTable(APIView):

    def get(self, request):
        return render(request,'temperature_table.html')


class rainfall_table_Api(APIView):

    def get(self, request):
        ret_dict = {'list': [], 'config': {'has_prev': None, 'has_next': None, 'cur_page': None, 'total_pages': None}}        

        count_per_page    = request.GET.get('count', 15) 
        page_number       = request.GET.get('page', 1)
        year              = request.GET.get('year', None)        
        district          = request.GET.get('district', None)

        treated_obj_list  = Rainfall.objects.all().values('id', 
                                                        'district',
                                                        'year',
                                                        'january',
                                                        'february',
                                                        'march',
                                                        'april',
                                                        'may',
                                                        'june',
                                                        'july',
                                                        'august',
                                                        'september',
                                                        'october',
                                                        'november',
                                                        'december').order_by('id')
        

        if year is not None and year != 'ALL':
            treated_obj_list = treated_obj_list.filter(year=year)
        if district is not None and district != 'ALL':
            treated_obj_list = treated_obj_list.filter(district=district)


        paginator         = Paginator(treated_obj_list, count_per_page)
        try:
            corr_id_list  = paginator.page(page_number)
        except PageNotAnInteger:
            corr_id_list  = paginator.page(1)
        except EmptyPage:
            corr_id_list  = paginator.page(paginator.num_pages)

        ret_dict['config']['has_prev']      = corr_id_list.has_previous()
        ret_dict['config']['has_next']      = corr_id_list.has_next()
        ret_dict['config']['cur_page']      = corr_id_list.number
        ret_dict['config']['total_pages']   = corr_id_list.paginator.num_pages

        # today   = datetime.datetime.today()

        for row in corr_id_list:
            temp_dict = {
                        'sample_info' : {
                                        'id':                          row['id'],
                                        'district':                    row['district'], 
                                        'year':                        row['year'],
                                        'january':                     row['january'],
                                        'february':                    row['february'], 
                                        'march':                       row['march'],
                                        'april':                       row['april'],
                                        'may':                         row['may'],
                                        'june':                        row['june'],
                                        'july':                        row['july'],
                                        'august':                      row['august'],
                                        'september':                   row['september'],
                                        'october':                     row['october'],
                                        'november':                    row['november'],
                                        'december':                    row['december'],
                                    }
            }
            ret_dict['list'].append(temp_dict)

        res1 = Rainfall.objects.values_list('district', flat=True).distinct()
        res2 = Rainfall.objects.values_list('year', flat=True).distinct().order_by('year')

        ret_dict['district'] = sorted(res1)
        ret_dict['year'] = sorted(res2)

        return Response(ret_dict, status=status.HTTP_200_OK)

class rainfallTable(APIView):

    def get(self, request):
        return render(request,'rainfall_table.html')



class pressure_table_Api(APIView):

    def get(self, request):
        ret_dict = {'list': [], 'config': {'has_prev': None, 'has_next': None, 'cur_page': None, 'total_pages': None}}        

        count_per_page    = request.GET.get('count', 15) 
        page_number       = request.GET.get('page', 1)
        year              = request.GET.get('year', None)        
        district          = request.GET.get('district', None)

        treated_obj_list  = Pressure.objects.all().values('id', 
                                                        'district',
                                                        'year',
                                                        'january',
                                                        'february',
                                                        'march',
                                                        'april',
                                                        'may',
                                                        'june',
                                                        'july',
                                                        'august',
                                                        'september',
                                                        'october',
                                                        'november',
                                                        'december').order_by('id')
        

        if year is not None and year != 'ALL':
            treated_obj_list = treated_obj_list.filter(year=year)
        if district is not None and district != 'ALL':
            treated_obj_list = treated_obj_list.filter(district=district)


        paginator         = Paginator(treated_obj_list, count_per_page)
        try:
            corr_id_list  = paginator.page(page_number)
        except PageNotAnInteger:
            corr_id_list  = paginator.page(1)
        except EmptyPage:
            corr_id_list  = paginator.page(paginator.num_pages)

        ret_dict['config']['has_prev']      = corr_id_list.has_previous()
        ret_dict['config']['has_next']      = corr_id_list.has_next()
        ret_dict['config']['cur_page']      = corr_id_list.number
        ret_dict['config']['total_pages']   = corr_id_list.paginator.num_pages

        # today   = datetime.datetime.today()

        for row in corr_id_list:
            press_dict = {
                        'sample_info' : {
                                        'id':                          row['id'],
                                        'district':                    row['district'], 
                                        'year':                        row['year'],
                                        'january':                     row['january'],
                                        'february':                    row['february'], 
                                        'march':                       row['march'],
                                        'april':                       row['april'],
                                        'may':                         row['may'],
                                        'june':                        row['june'],
                                        'july':                        row['july'],
                                        'august':                      row['august'],
                                        'september':                   row['september'],
                                        'october':                     row['october'],
                                        'november':                    row['november'],
                                        'december':                    row['december'],
                                    }
            }
            ret_dict['list'].append(press_dict)

        res1 = Pressure.objects.values_list('district', flat=True).distinct()
        res2 = Pressure.objects.values_list('year', flat=True).distinct().order_by('year')

        ret_dict['district'] = sorted(res1)
        ret_dict['year'] = sorted(res2)

        return Response(ret_dict, status=status.HTTP_200_OK)

class pressureTable(APIView):

    def get(self, request):
        return render(request,'pressure_table.html')

class cropdataPassing(APIView):
    def get(self, request):
        
        res1 = Cropdata.objects.values_list('district', flat=True).distinct()
        res2 = Cropdata.objects.values_list('year', flat=True).distinct().order_by('year')
        res3 = Cropdata.objects.values_list('season', flat=True).distinct()
        res4 = Cropdata.objects.values_list('crop', flat=True).distinct()
        data = {'dist':res1, 'yr':res2, 'ssn': res3, 'crp':res4}

        return Response({'cdata':data}, status=status.HTTP_200_OK)



class Home(APIView):

    def get(self, request):
        return render(request,'home.html')

class Signup(APIView):

    def get(self, request):
        return render(request,'signup.html')

class Login(APIView):

    def get(self, request):
        status = request.GET.get('status', '')
        # {% if request.user.username %}
        return render(request,'login.html', {'status': status})

class submitSignupdetail(APIView):
    def post(self,request):
        Username = request.POST['username']
        Email = request.POST['email']
        Password = request.POST['password']

        # print (Username)
        user = User.objects.create_user(username=Username, email=Email, password=Password)
        
        #return Response({'username':name, 'password':age}, status=status.HTTP_200_OK) 
        # return Response("Success!!", status=status.HTTP_200_OK)
        return HttpResponseRedirect("/login/?status=Success")

class submitLogindetail(APIView):
    def post(self,request):

        try:
            username = request.POST.get('uname', '')
            password = request.POST.get('psw', '')

            # print (username)
            # print (password)
            
            user = authenticate(request, username = username, password = password)      

            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/home/")
            else:
                return HttpResponseRedirect("/login/")
                
        except Exception as e:
            print (e)


def logoutUser(request):
    logout(request)
    # return Response(status=status.HTTP_200_OK)
    return HttpResponseRedirect("/login/")

class BlogDetailView(DetailView):
    model = Blog
    template_name = os.path.join(settings.BASE_DIR, 'cropdata/templates/blog_details.html')
    paginate_by = getattr(settings, "BLOG_PAGINATION_COUNT", 10)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['recentPost'] = Blog.objects.order_by('entry_time')[:getattr(settings, "RECENT_POST_COUNT", 5)][::-1]

        final = []
        res = Comment.objects.all()

        context['auth'] = res

        return context

class BlogListView(ListView):
    model = Blog
    template_name = os.path.join(settings.BASE_DIR, 'cropdata/templates/blog_list.html')
    paginate_by = getattr(settings, "BLOG_PAGINATION_COUNT", 10)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['recentPost'] = Blog.objects.order_by('entry_time')[:getattr(settings, "RECENT_POST_COUNT", 5)][::-1]
        return context

def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


class BlogSearchListView(APIView):
    """
    Display a Blog List page filtered by the search query.
    """
    def get(self, request):
        query = self.request.GET.get('q')
        print(query)
        #return Response("success", status=status.HTTP_200_OK)

        recentPost = Blog.objects.order_by('entry_time')[:getattr(settings, "RECENT_POST_COUNT", 5)][::-1]
        page_obj = Blog.objects.filter(Q(title__icontains=query)  | Q(body__icontains=query)  ).order_by('entry_time')
        
        return render(request, 'blog_list.html', {'page_obj':page_obj, 'recentPost':recentPost})


class aboutMe(APIView):

    def get(self, request):
        return render(request,'aboutme.html')

class blogPost(APIView):
    def get(self, request):
        return render(request, 'blogpost.html')

class submitblogPost(APIView):
    def post(self,request):
        User = request.POST['user']
        Title = request.POST['title']
        Body = request.POST['body']
        Entry_time = request.POST['entry_time']
        print(Entry_time)
        print (User)
        q = Blog(user=User, title=Title, body=Body, entry_time=Entry_time)
        q.save()
        #return Response({'username':name, 'password':age}, status=status.HTTP_200_OK) 
        # return Response("Success!!", status=status.HTTP_200_OK)
        return HttpResponseRedirect("/home/")


class forgotPasswd(APIView):

    def get(self, request):
        return render(request,'forgotpasswd.html')


class submitcommentPost(APIView):
    def post(self,request):
        Author = request.POST['author']
        Text = request.POST['text']
        Blog_id = request.POST['blog_id']
        Blog_url = request.POST['blog_url']
        # print (Author)
        # print (Blog_url)

        q = Comment(author=Author, text=Text, blog_id=Blog_id)
        q.save()
        #return Response({'username':name, 'password':age}, status=status.HTTP_200_OK) 
        # return Response("Success!!", status=status.HTTP_200_OK)
        return HttpResponseRedirect(Blog_url)