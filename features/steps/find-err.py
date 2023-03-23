import requests
from behave import *
from helpers import helpers as h
from countries_phoneNumber_db import countries

API_BASE_URL = "https://bug6wxr929.execute-api.eu-west-1.amazonaws.com/Prod//"

@given('I send a GET request to API')
def step_impl(context, ) :
    pass

@when("I request data for {link_name} {response_name}")
def step_impl(context, link_name, response_name):
    url = ""
    i = 2227
    if link_name == 'lorem':
        limit = 2230
        while i < 2229:
            url = f"{API_BASE_URL}{link_name}?lettersOnly=true&length={i}"
            headers = {'Content-type': "application/json"}
            context.response = requests.get(url, headers=headers)
            dd = context.response.json()
            requested_amount = i
            i += 1
            if(requested_amount > 2230 and len(dd[response_name]) > 2230):
              raise ValueError(f"API should return maximum 2230 chars, but was requested:{ requested_amount } and returned: {len(dd[response_name])}. Url:{url}")
            assert len(dd[response_name]) == requested_amount, \
            f"Expected {requested_amount}, but received {len(dd[response_name])}: {dd[response_name]}"
    elif link_name == 'telephone':
        for c in countries:
            country = c
            while i < 105:
                url = f"{API_BASE_URL}{link_name}?country={country}&amount={i}"
                headers = {'Content-type': "application/json"}
                context.response = requests.get(url, headers=headers)
                dd = context.response.json()
                requested_amount = i
                i += 1
                if(requested_amount > 100 and len(dd[response_name]) > 100):
                    raise ValueError(f"API should return maximum 100 values, but was requested:{ requested_amount } and returned: {len(dd[response_name])}. Url:{url}")
            else: 
                assert len(dd[response_name]) == requested_amount, \
                f"Expected {requested_amount}, but received {len(dd[response_name])}: {dd[response_name]}"
    else:
        while i < 105:
            url = f"{API_BASE_URL}{link_name}?amount={i}"
            headers = {'Content-type': "application/json"}
            context.response = requests.get(url, headers=headers)
            dd = context.response.json()
            requested_amount = i
            i += 1
            if(requested_amount > 100 and len(dd[response_name]) > 100):
                raise ValueError(f"API should return maximum 100 values, but was requested:{ requested_amount } and returned: {len(dd[response_name])}. Url:{url}")
            assert len(dd[response_name]) == requested_amount, \
            f"Expected {requested_amount}, but received {len(dd[response_name])}: {dd[response_name]}"
   

@then ("I receive adequate response")
def step_impl(context):
   assert 1 == 2,\
   print("done")
  
    
  