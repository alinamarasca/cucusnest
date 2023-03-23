import requests
from behave import *
from helpers import helpers as h
from countries_phoneNumber_db import countries

@given('I send a GET request to API')
def step_impl(context, ) :
    pass

@when("I request data for {link_name} {response_name}")
def step_impl(context, link_name, response_name):
    baseUrl = "https://bug6wxr929.execute-api.eu-west-1.amazonaws.com/Prod//"
    url = ""
    min_limit = 99
    max_limit = 102
    i = min_limit
    if link_name == 'lorem':
        while i < max_limit:
            url = f"{baseUrl}{link_name}?lettersOnly=true&length={i}"
            headers = {'Content-type': "application/json"}
            context.response = requests.get(url, headers=headers)
            dd = context.response.json()
            requested_amount = i
            i += 1
            assert len(dd[response_name]) == requested_amount, \
            f"Expected {requested_amount}, but received {len(dd[response_name])}: {dd[response_name]}"
    elif link_name == 'telephone':
        for c in countries:
            country = c
            while i < max_limit:
                url = f"{baseUrl}{link_name}?country={country}&amount={i}"
                headers = {'Content-type': "application/json"}
                context.response = requests.get(url, headers=headers)
                dd = context.response.json()
                requested_amount = i
                i += 1
                if(requested_amount > 100 and len(dd[response_name]) > 100):
                    raise ValueError("API should return maximum 100 values, but was requested {requested_amount} and returned", {len(dd[response_name])})
            else: 
                assert len(dd[response_name]) == requested_amount, \
                f"Expected {requested_amount}, but received {len(dd[response_name])}: {dd[response_name]}"
    else:
        while i < max_limit:
            url = f"{baseUrl}{link_name}?amount={i}"
            headers = {'Content-type': "application/json"}
            context.response = requests.get(url, headers=headers)
            dd = context.response.json()
            requested_amount = i
            i += 1
            if(requested_amount > 100 and len(dd[response_name]) > 100):
                raise ValueError("API should return maximum 100 values, but was requested {requested_amount} and returned", {len(dd[response_name])})
            assert len(dd[response_name]) == requested_amount, \
            f"Expected {requested_amount}, but received {len(dd[response_name])}: {dd[response_name]}"
   

@then ("I receive adequate response")
def step_impl(context):
   assert 1 == 2,\
   print("done")
  
    
  