import requests
import json

""" This program acts as a currency converter.  You start by telling it your source currency, and then target currency.
 Next you tell it how much source currency you have.  The program returns the amount of converted target currency """

conv_rates = {}
input_list = ['usd', 'eur']


def update_conv_rates(base_currency):
    """ This function creates a nested dictionary update to the conv_rates dict.  The outer dict is the source currency
    and the inner dict is the target currency with exchange rate """

    global conv_rates

    url = ('http://www.floatrates.com/daily/' + base_currency + '.json')
    r = requests.get(url)
    var = r.json()

    working_dict = {}
    # Build the inner dictionary
    for i in var:
        key = {str(i)}
        value = (var[i]['rate'])

        new_dict = dict.fromkeys(key, value)
        working_dict.update(new_dict)

    # Build the outer dictionary
    key2 = {str(base_currency)}
    value2 = working_dict
    nested_dict = dict.fromkeys(key2, value2)

    # Update the conversion dictionary
    conv_rates.update(nested_dict)


""" Main Body Of Program """
source_currency = input()
update_conv_rates(source_currency)

while True:
    target_currency = input()
    if target_currency == "":
        break
    source_amt = input()
    print('Checking the cache...')

    if target_currency.lower() in input_list:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        input_list.append(target_currency.lower())

    target_amount = round(float(source_amt) * float(conv_rates[source_currency][target_currency]), 2)
    print(f'You received {target_amount} {target_currency.upper()}.')

