# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question, Order

import json
#import http.client
import httplib
#import urllib.parse
from urlparse import urlparse
import sys
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# change these to your server and credentials
Url = 'http://twlatestga.unitysandbox.com/Unity/UnityService.svc'

# Replace "web20" with your Unity application name
Appname      = 'VigliettaPeter.Peter.TestApp'

# Replace the following with your Unity service credentials
Svc_username = 'Vigli-43bb-Peter-test'
Svc_password = 'V#8L#eTt@P6t%rp1t%Rt2St@Pp1Bb6'

# valid EHR username, used along with token in each Magic call
# (see Sandboxes page of developer portal for current values)
Ehr_username = 'jmedici'
Ehr_password = 'password01'

# *******************************************************************************************************
# * NAME:        UnityHelloWorld.py
# *
# * DESCRIPTION: Example Python application code to illustrate basic usage of Unity with Allscripts
# *              TouchWorks/Professional EHR.
# *
# * Unpublished (c) 2015 Allscripts Healthcare Solutions, Inc. and/or its affiliates. All Rights Reserved.
# *
# * This software has been provided pursuant to a License Agreement, with Allscripts Healthcare Solutions,
# * Inc. and/or its affiliates, containing restrictions on its use. This software contains valuable trade
# * secrets and proprietary information of Allscripts Healthcare Solutions, Inc. and/or its affiliates
# * and is protected by trade secret and copyright law. This software may not be copied or distributed
# * in any form or medium, disclosed to any third parties, or used in any manner not provided for in
# * said License Agreement except with prior written authorization from Allscripts Healthcare Solutions,
# * Inc. and/or its affiliates. Notice to U.S. Government Users: This software is "Commercial Computer
# * Software."
# *
# * This is example code, not meant for production use.
# *******************************************************************************************************


# build Magic action JSON string
def buildjson(action, appname, ehruserid, patientid, unitytoken,
              param1='', param2='', param3='', param4='', param5='', param6='', data=''):
    return json.dumps({'Action': action,
                       'Appname': appname,
                       'AppUserID': ehruserid,
                       'PatientID': patientid,
                       'Token': unitytoken,
                       'Parameter1': param1, 'Parameter2': param2, 'Parameter3': param3,
                       'Parameter4': param4, 'Parameter5': param5, 'Parameter6': param6,
                       'Data': data})

# post action JSON to MagicJson endpoint, get JSON in return
def unityaction(jsonstr):

    u = urlparse(Url)
    if (u.scheme == 'http'):
        conn = httplib.HTTPConnection(u.hostname)
    elif (u.scheme == 'https'):
        conn = httplib.HTTPSConnection(u.hostname)

    conn.request('POST', '/Unity/UnityService.svc/json/MagicJson',
             jsonstr,
             {'Content-Type': 'application/json'})
    resp = conn.getresponse( )
    retjson = resp.read( ).decode( )
    conn.close( )
    return retjson

# get Unity security token from GetToken endpoint
def gettoken(username, password):
    u = urlparse(Url)
    if (u.scheme == 'http'):
        conn = httplib.HTTPConnection(u.hostname)
    elif (u.scheme == 'https'):
        conn = httplib.HTTPSConnection(u.hostname)
    
    conn.request('POST', '/Unity/UnityService.svc/json/GetToken',
             json.dumps({'Username': username, 'Password': password}),
             {'Content-Type': 'application/json'})
    response = conn.getresponse( )
    t = response.read( ).decode( )
    conn.close( )
    return t

#BELOW ARE THE UNITY CALLS TO GET A TOKEN, THEN AUTHENTICATE THE EHR USER, THEN CALL GET ORDERS. 
#THEY ARE ALL COMMENTED OUT SO THAT YOU CAN RUN THE SERVER TO TEST YOUR APP. 

'''
# Get Unity security token
token = gettoken(Svc_username, Svc_password)
print('Using Unity security token: ' + token)


# Authenticate EHR user before calling other Magic actions
jsonstr = buildjson('GetUserAuthentication', Appname, Ehr_username, '', token, Ehr_password)
unity_output = unityaction(jsonstr)

# Uncomment to display full GetUserAuthentication output
# print('Output from GetUserAuthentication: ')
# print(json.dumps(json.loads(unity_output), indent=4, separators=(',', ': ')))
# print( )


# AUTHENTICATE EHR USER (Look for ValidUser = YES)
json_dict = json.loads(unity_output)
valid_user = json_dict[0]['getuserauthenticationinfo'][0]['ValidUser']
if (valid_user == 'YES'):
	print('EHR user is valid.')
else:
	print('EHR user is invalid: ' + json_dict[0]['getuserauthenticationinfo'][0]['ErrorMessage'])

print( )


# Call GetOrders 
jsonstr = buildjson('GetOrders', Appname, Ehr_username, 39, token, '', '', 'active')
unity_output = unityaction(jsonstr)

callOutput = json.loads(unity_output)
print callOutput

dataReturned = callOutput[0]

orderData = dataReturned['getordersinfo']


def dummyView(xxx):
    return HttpResponse('falcon')
   

'''




#Save the orders into SQLite db
'''
def saveOrders():
    for i in orderData:
      o = Order(order_number = i["ordernumber"], orderable_name = i["orderable"], orderable_code = i["ordercode"])
      o.save()          

saveOrders()
'''





#HERE IS WHERE MY ACTUAL APP STARTS


def Quirklist(request):
  order_list = Order.objects.all
  context = {'ordersInTemplate': order_list}
  return render(request, 'unityapp/index.html', context)
