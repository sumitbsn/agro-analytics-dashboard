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
import restapi.views
from restapi import views as v
from cropdata import views as c
import cropdata.views
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect, HttpResponse

# handler404 = 'views.my_404_view'
# handler404 = 'mysite.views.my_custom_page_not_found_view'

urlpatterns = [

    url(r'^admin/', admin.site.urls),
	url(r'^datadetail/$', restapi.views.dataDetail.as_view(), name='this gives user data'),
	url(r'^userdetail/$', restapi.views.userDetail.as_view(), name='this gives user data'),
    url(r'^usersearch/$', restapi.views.userQuery.as_view(), name='this search and gives user data'),
    url(r'^datapassing/$', restapi.views.dataPassing.as_view(), name='pass the data'),
    url(r'^submit_result/$', restapi.views.submitResult.as_view(), name='show result'),
    url(r'^registration/$',v.registration, name='registration page'),
    # url(r'^crop_data/$', restapi.views.cropData.as_view(), name='crop production details page'),
    url(r'^cropdatadetail/$', cropdata.views.cropdataDetail.as_view(), name='crop production details page'),
    
    url(r'^tamilnadu/district/temperaturedetail/$', cropdata.views.temperatureDetail.as_view(), name='temperature details page'),
    url(r'^tamilnadu/district/pressuredetail/$', c.pressureDetail.as_view(), name='pressure details page'),

    url(r'^pressurechart/$', cropdata.views.pressureChart.as_view(), name='Pressure Chart'),
    url(r'^pressurechartapi/$', cropdata.views.pressureChartApi.as_view(), name='Pressure Chart Api'),
    url(r'^pressdatapassing/$', cropdata.views.pressdataPassing.as_view(), name= 'pressure data passing api' ),
    
    url(r'^temperaturechartapi/$', cropdata.views.temperatureChartApi.as_view(), name='Temperature Chart Api'),
    url(r'^temperaturechart/$', cropdata.views.temperatureChart.as_view(), name='Temperature Chart'),
    url(r'^tempdatapassing/$', cropdata.views.tempdataPassing.as_view(), name= 'temperature data passing api' ),
    
    url(r'^cropdataapi/$', cropdata.views.cropdataApi.as_view(), name='Crop Data Api'),
    url(r'^cropdata/$', cropdata.views.CropData.as_view(), name='Crop Data'),

    url(r'^temperaturetableapi/$', cropdata.views.temperature_table_Api.as_view(), name='Temperature Table Api'),
    url(r'^temperaturetable/$', cropdata.views.temperatureTable.as_view(), name='Temperature Table'),

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
]
