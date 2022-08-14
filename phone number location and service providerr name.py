import phonenumbers
from test import number #here is another file named test  where a number is imported
from phonenumbers import geocoder # geocoder is  a built in function in phonenumbers

ch_number = phonenumbers.parse(number, "ch") #  here the number is stored
print(geocoder.description_for_number(ch_number, "en")) #allows you to take your customers'
                                                        # and create a map of their locations

from  phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))
