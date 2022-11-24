def describe_city(city,country='Chile'):
   """Describe a city"""
   msg = f"{city.title()} is in {country.title()}."
   print(msg)

describe_city('santiago')
describe_city('reykjavik' , 'iceland')
describe_city('punta arenas') 