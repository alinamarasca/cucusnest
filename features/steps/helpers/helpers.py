
def calc_amount(some_amount):
   return "&amount=" + str(some_amount) if some_amount !='' else 1

def calc_date(date):
   return "&date=" + str(date) if len(date) < 1 else None

def find_modulo(generated_bis):
    return  97 - int((generated_bis[:9])) % 97

def match_modulos(number, given_modulo):
   calculated_modulo = 97 - int(number) % 97
   matches = str(given_modulo).lstrip("0") == str(calculated_modulo)
   print("modulos", str(given_modulo).lstrip("0"), str(calculated_modulo))
   if (not matches):
    print(number, '2' + number, given_modulo)
    matches = match_modulos('2' + number, given_modulo=given_modulo)
   return matches
