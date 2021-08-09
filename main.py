
import phonenumbers
from test import number

from phonenumbers import geocoder
ch_nmber =phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_nmber,"en"))

from phonenumbers import carrier
service_nmber=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_nmber,"en"))

"""import phonenumbers
from phonenumbers import geocoder
phone_number1=phonenumbers.parse("+919403122086")
print(geocoder.description_for_number(phone_number1,"en"))"""