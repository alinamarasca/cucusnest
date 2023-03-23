
import requests
from behave import *
from helpers import helpers as h
from phonenumbers_db import phones as db

@given('I need landline number')
def step_impl(context):
    pass


@when('Request {country} {amount}')
def step_impl(context, country, amount):
    baseUrl = "https://bug6wxr929.execute-api.eu-west-1.amazonaws.com/Prod//telephone?"
    country = "country=" + country
    amount = "&amount=" + str(amount)
    url = f"{baseUrl}{country}{amount}"
    headers = {'Content-type': "application/json"} 
    context.response = requests.get(url, headers=headers)
    pass


@then('I receive {amount} of valid landline number for {country}')
def step_impl(context, amount, country):
    generated_data = context.response.json()['phoneNumber']
    # print(generated_data)
    for n in generated_data:
        if (country == "Belgium"):
          data = h.get_data(db, "be")
          # starts with +32
          prefix = data[0].get('prefix')
          assert str(n[:3]) == prefix, \
          print(n, f"Wrong prefix: expected prefix {prefix}, but got {n[:3]}")
          # has total 11 chars(+, 10 digits)
          assert len(n) == 11 , \
          print(n, f"Expected 11 char(including +), but got {len(n)}")
          # has valid Belgian area code
          area_code_exists = False
          available_codes = data[1].get('landlineAreaCode')
          area_code = h.be_area_code_from_number(n)
          if int(area_code) in available_codes:
             area_code_exists = True
          assert area_code_exists == True, \
          print(n, f"Landline area code {area_code} is outside range")
          # if +324 => Landlines in Liège also never starts with 04 6x, 04 7x, 04 8x or 04 9x
          if(n[3:4] == str(4)):
            landline_within_range = h.liege_landline_exceptions(n)
            assert landline_within_range == True, \
            print(n, f"Landlines in Liège also never starts with 04 6x, 04 7x, 04 8x or 04 9x")
 