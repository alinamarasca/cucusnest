import requests
from behave import *
from helpers import helpers as h


@given('I request')
def step_impl(context, ) :
     pass

@when("I send request {isGenderKnown} {isDateOfBirthKnown} {amount} {date}")
def step_impl(context, isGenderKnown, isDateOfBirthKnown, amount, date) :
       baseUrl = "https://bug6wxr929.execute-api.eu-west-1.amazonaws.com/Prod/bis?"
       gender = "isGenderKnown=" + isGenderKnown
       dob = "&isBirthdateKnown=" + isDateOfBirthKnown
       date = None if date else "&date=" + str(date)
       amount = None if int(amount) <=1 else "&amount=" + str(amount)
       url = f"{baseUrl}{gender}{dob}{date}{amount}"
       headers = {'Content-type': "application/json"} 
       context.response = requests.get(url, headers=headers)


@then ("response is valid for the {date} and {isGenderKnown}")
def step_impl(context, date, isGenderKnown):
    re =context.response.json()['bis'][0]

    # And response consists of 11 digits
    assert len(re) == 11, \
    f"Expected length response length is 11, but received {len(re)}"
    
    # And the last 2 digits are modulo of first 9 digits divided by 97
    a = int((re[9:])) % 97
    m = int((re[9:]))
    assert int(a) == int(m)
        

    
    # And if gender is known month is +40
    # And if gender is not known month is +20 
    if(not date):
      increase = 0
      if(isGenderKnown):
        increase = 40
      else: increase = 20

      input_month = date[5:7]

      month = re[2:4]
      # print(re, int(month), int(increase) , int(input_month))
      assert int(month) - int(increase) == int(input_month)
      
    
  