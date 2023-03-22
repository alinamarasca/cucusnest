import json
import requests
from behave import *
from helpers import helpers as h
from phonenumbers_db import phones as db

@given('I need landline number')
def step_impl(context):
    pass


@when('I send a GET request {country} {amount}')
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
          data = json.loads(db)["be"]
          # starts with +32
          prefix = "+" + data[0].get('prefix')
          assert str(n[:3]) == prefix, \
          print(n, f"Wrong prefix: expected prefix {prefix}, but got {n[:3]}")
          # has total 11 chars(+, 10 digits)
          assert len(n) == 11 , \
          print(n, f"Expected 11 char(including +), but got {len(n)}")
          # has valid Belgian area code
          available_codes = data[1].get('landlineAreaCode')
          # big Brussels 2, Antwerp 3, Liège 4 and Ghent 9 - len is 1, res len is 2
          if (n[3:4] == str(2) or n[3:4] == str(3) or n[3:4] == str(4) or n[3:4] == str(9)):
              area_code = n[3:4]
          else: area_code = n[3:5]
          if area_code in available_codes:
             area_code_exists = True
          assert area_code == True, \
          print(n, f"Landline area code is outside range")
          # if +324 => Landlines in Liège also never starts with 04 6x, 04 7x, 04 8x or 04 9x
          if(n[3:4] == str(4)):
              landline_within_range = False
              first_landline_digit = int(n[4:5])
              forbidden_first_landline_digits = [6, 7, 8, 9]
              if first_landline_digit in forbidden_first_landline_digits:
                landline_within_range = False
              assert landline_within_range == True, \
              print(n, f"Landlines in Liège also never starts with 04 6x, 04 7x, 04 8x or 04 9x")
