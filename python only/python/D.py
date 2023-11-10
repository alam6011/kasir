from phonenumbers import carrier, geocoder, timezone
mobileNo = input("masuukan nomor : ")
mobileNo = phonenumbers.parse(mobileNo)
#mendapatkan lokasi
print(timezone.time_zones_for_number (mobileNo))
#mendapatkan provider

print(carrier.name_for_number (mobileNo, "en"))
 #mendapatkan negara

print(geocoder.description_for_number (mobileNo, "en"))

 #validating a phone number

print("valid Mobile Number : ", phonenumbers.is_valid_number (mobileNo))


#checking possibility a number

print("checking possibility of number : ",phonenumbers.is_possible_number (mobilP))