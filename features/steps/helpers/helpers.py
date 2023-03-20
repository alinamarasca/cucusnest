
# [on_true] if [expression] else [on_false] 

def calc_amount(some_amount):
   return "&amount=" + str(some_amount) if some_amount !='' else 1

def calc_date(date):
   return "&date=" + str(date) if len(date) < 1 else None

def find_modulo(generated_bis):
    return  97 - int((generated_bis[:9])) % 97

def calc_expected_modulo(generated_bis):
   number = generated_bis[:9]
   given_modulo = generated_bis[9:]
   matches = False
   calculated_modulo = 97 - int(number) % 97
   print(generated_bis, number, given_modulo, calculated_modulo )
   matches = str(given_modulo).lstrip("0") == str(calculated_modulo)
   print(matches)
   if (not matches):
      number = str(2) + generated_bis[:9]
   calculated_modulo = 97 - int(number) % 97
   print(generated_bis, number, given_modulo, calculated_modulo )
   matches = str(given_modulo).lstrip("0") == str(calculated_modulo)
   print(matches)

   return matches
   

# if calculated modulo true = exit
#if calculated modulo false = calc with 2 before number, if this true 

#    return matches


#     year = date[:4] 
#     number = generated_bis[:9]

# if(not date):
#     if int(year) >= 2000:
#         number = '2' + number
#     return 97 - int(number) % 97


    # if(gender_known):
    #     current_month = int(number[2:4]) + 40
    # else:
    #     current_month = int(number[2:4]) + 20

# print(find_modulo("68301029177"))

print(calc_expected_modulo("83471758408"))
print("------------------------")
# print(calc_expected_modulo("87301059773"))
