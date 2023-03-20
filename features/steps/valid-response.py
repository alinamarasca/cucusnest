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
    date = h.calc_date(date)
    amount = h.calc_amount(amount)
    
    url = f"{baseUrl}{gender}{dob}{date}{amount}"
    print(url)

    headers = {'Content-type': "application/json"} 
    context.response = requests.get(url, headers=headers)


@then ("response is valid for the {date} and {isGenderKnown}")
def step_impl(context, date, isGenderKnown):
    print(context.response)
    generated_bis = context.response.json()['bis'][0]

    # And response consists of 11 digits
    assert len(generated_bis) == 11, \
    f"Expected length response length is 11, but received {len(generated_bis)}"
    
    # And the last 2 digits are modulo of first 9 digits divided by 97
    number = generated_bis[:9]
    print(number)
    given_modulo = generated_bis[9:]
    matches = False
    calculated_modulo = 97 - int(number) % 97
    matches = str(given_modulo).lstrip("0") == str(calculated_modulo)
    print(matches)
    if (not matches):
        number = str(2) + generated_bis[:9]
    calculated_modulo = 97 - int(number) % 97
    matches = str(given_modulo) == str(calculated_modulo)
    print(matches)
    print(str(given_modulo), str(calculated_modulo), generated_bis)
    assert  str(given_modulo).lstrip("0") == str(calculated_modulo)
    
    # And if gender is known month is +40
    # And if gender is not known month is +20 
    if(not date):
      increase = 0
      if(isGenderKnown):
        increase = 40
      else: increase = 20

      input_month = date[5:7]

      month = re[2:4]
      print(re, int(month), int(increase) , int(input_month))
      assert int(month) - int(increase) == int(input_month)
      
    
  