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
    given_modulo = generated_bis[9:]
    assert h.match_modulos(number, given_modulo) == True
    # And if gender is known month is +40
    # And if gender is not known month is +20 
    if(not date):
      increase = 0
      if(isGenderKnown):
        increase = 40
      else: increase = 20

      input_month = date[5:7]

      month = generated_bis[2:4]
      assert int(month) - int(increase) == int(input_month)
  
    
  