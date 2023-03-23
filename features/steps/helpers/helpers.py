import json
# OVERALL

def test():
    available_data = ['bis', 'isnz', 'kbo', 'nihii', 'plates', 'polis', 'riziv', 'telephone', 'uuid']
    baseUrl = "https://bug6wxr929.execute-api.eu-west-1.amazonaws.com/Prod//"
    for item in available_data:
        for am in range(1,101):
          url = f"{baseUrl}{item}?amount={am}"


# def get_data(source, country):
#    return json.loads(source)[country]

# def be_area_code_from_number(n):
#    # big Brussels 2, Antwerp 3, Liège 4 and Ghent 9 - len is 1, res len is 2
#    if (n[3:4] == str(2) or n[3:4] == str(3) or n[3:4] == str(4) or n[3:4] == str(9)):
#       return n[3:4]
#    else:  return n[3:5]

# #BIS
# def calc_amount(some_amount):
#    return "&amount=" + str(some_amount) if some_amount !='' else 1

# def calc_date(date):
#    return "&date=" + str(date) if len(date) < 1 else None

# def find_modulo(generated_bis):
#     return  97 - int((generated_bis[:9])) % 97

# def match_modulos(number, given_modulo):
#    calculated_modulo = 97 - int(number) % 97
#    matches = str(given_modulo).lstrip("0") == str(calculated_modulo)
#    print("modulos", str(given_modulo).lstrip("0"), str(calculated_modulo))
#    if (not matches):
#     print(number, '2' + number, given_modulo)
#     matches = match_modulos('2' + number, given_modulo=given_modulo)
#    return matches
