"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, handler404
from django.contrib import admin
from cropdata import views as c
import cropdata.views
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import views as auth_views
from django.conf.urls import include

# handler404 = 'views.my_404_view'
# handler404 = 'mysite.views.my_custom_page_not_found_view'

urlpatterns = [

    url(r'^meadmin/', admin.site.urls),

    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    url(r'^secret/', include(admin.site.urls)),

    # url(r'^cropdatadetail/$', cropdata.views.cropdataDetail.as_view(), name='crop production details page'),
    
    url(r'^tamilnadu/district/temperaturedetail/$', cropdata.views.temperatureDetail.as_view(), name='temperature details page'),
    url(r'^tamilnadu/district/pressuredetail/$', c.pressureDetail.as_view(), name='pressure details page'),

    url(r'^pressurechart/$', cropdata.views.pressureChart.as_view(), name='Pressure Chart'),
    url(r'^pressurechartapi/$', cropdata.views.pressureChartApi.as_view(), name='Pressure Chart Api'),
    url(r'^pressdatapassing/$', cropdata.views.pressdataPassing.as_view(), name= 'pressure data passing api' ),
    
    url(r'^temperaturechartapi/$', cropdata.views.temperatureChartApi.as_view(), name='Temperature Chart Api'),
    url(r'^temperaturechart/$', cropdata.views.temperatureChart.as_view(), name='Temperature Chart'),
    url(r'^tempdatapassing/$', cropdata.views.tempdataPassing.as_view(), name= 'temperature data passing api' ),

    url(r'^rainfallchartapi/$', cropdata.views.rainfallChartApi.as_view(), name='Rainfall Chart Api'),
    url(r'^rainfallchart/$', cropdata.views.rainfallChart.as_view(), name='Rainfall Chart'),
    url(r'^rainfalldatapassing/$', cropdata.views.rainfalldataPassing.as_view(), name= 'Rainfall data passing api' ),
    
    url(r'^cropdataapi/$', cropdata.views.cropdataApi.as_view(), name='Crop Data Api'),
    url(r'^cropdata/$', cropdata.views.CropData.as_view(), name='Crop Data'),

    url(r'^temperaturetableapi/$', cropdata.views.temperature_table_Api.as_view(), name='Temperature Table Api'),
    url(r'^temperaturetable/$', cropdata.views.temperatureTable.as_view(), name='Temperature Table'),

    url(r'^rainfalltableapi/$', cropdata.views.rainfall_table_Api.as_view(), name='Rainfall Table Api'),
    url(r'^rainfalltable/$', cropdata.views.rainfallTable.as_view(), name='Rainfall Table'),

    url(r'^pressuretableapi/$', cropdata.views.pressure_table_Api.as_view(), name='Pressure Table Api'),
    url(r'^pressuretable/$', cropdata.views.pressureTable.as_view(), name='Pressure Table'),


    # url(r'^cropdatapassing/$', cropdata.views.cropdataPassing.as_view(), name= 'Crop Data passing api' ),
    
    # url(r'^home/$', cropdata.views.Home.as_view(), name= 'Home page Api' ),
    # url(r'^invoice/$', restapi.views.InvoicePDFView.as_view(), name='invoice'),
    url(r'^signup/$', cropdata.views.Signup.as_view(), name= 'Signup page Api' ),
    url(r'^login/$', cropdata.views.Login.as_view(), name= 'Login page Api' ),
    url(r'^logout/$', c.logoutUser, name= 'Logout page Api' ),
    url(r'^submitsignupdetail/$', cropdata.views.submitSignupdetail.as_view(), name= 'Submit user signup details Api' ),
    url(r'^submitlogindetail/$', cropdata.views.submitLogindetail.as_view(), name= 'Submit user login details Api' ),
    # url(r'^image/$', restapi.views.imageStore.as_view(), name= 'image api'),
    url(r'^home/$', cropdata.views.BlogListView.as_view(), name='blog_list'),
    url(r'^home/(?P<pk>\w+)/$', cropdata.views.BlogDetailView.as_view(), name='blogs'),
    url(r'^blogsearch/$', cropdata.views.BlogSearchListView.as_view(), name='blog search list view'),
    url(r'^$', lambda r: HttpResponseRedirect('home/')),
    url(r'^aboutme/$', cropdata.views.aboutMe.as_view(), name= 'About Me api'),
    url(r'^blogpost/$', cropdata.views.blogPost.as_view(), name= 'Blog Post api'),
    url(r'^submitblogpost/$', cropdata.views.submitblogPost.as_view(), name= 'Blog Post submit api'),


    # url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
   
    
    # url(r'^', include('mysite.urls')),
    # url('^', include('django.contrib.auth.urls')),
    url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'password_reset_form.html'}, name='password_reset_form'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, {'template_name': 'password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, {'template_name': 'password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, {'template_name': 'password_reset_complete.html'}, name='password_reset_complete'),


    url(r'^submitcommentpost/$', cropdata.views.submitcommentPost.as_view(), name= 'Submit Comment api'),
    # url(r'^commentpost/$', cropdata.views.commentPost.as_view(), name= 'Comment api'),
]
