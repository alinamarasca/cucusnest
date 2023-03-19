import requests
from behave import *


@given('I request BIS')
def step_impl(context, ) :
     pass

@when("I send a GET request {isGenderKnown} {isDateOfBirthKnown} {amount} {date}")
def step_impl(context, isGenderKnown, isDateOfBirthKnown, amount, date) :
       baseUrl = "https://bug6wxr929.execute-api.eu-west-1.amazonaws.com/Prod/bis?"
       gender = "isGenderKnown=" + isGenderKnown
       dob = "&isBirthdateKnown=" + isDateOfBirthKnown
       date = None if date else "&date=" + str(date)
       amount = None if int(amount) <=1 else "&amount=" + str(amount)
       url = f"{baseUrl}{gender}{dob}{date}{amount}"
       headers = {'Content-type': "application/json"} 
       context.response = requests.get(url, headers=headers)


@then ("the response status code should be 200")
def step_impl(context):
      assert context.response.status_code == 200
    
  