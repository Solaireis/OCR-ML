# Import PassportEye
from passporteye import read_mrz

# Process image
mrz = read_mrz("Passport.jpg")

# Obtain image
mrz_data = mrz.to_dict()

print(mrz_data['country'])
print(mrz_data['names'])
print(mrz_data['surname'])
print(mrz_data['type'])


# Process image
mrz = read_mrz("passport2.png")

# Obtain image
mrz_data = mrz.to_dict()

print(mrz_data['country'])
print(mrz_data['names'])
print(mrz_data['surname'])
print(mrz_data['type'])


# Process image
mrz = read_mrz("passport69.jpg")
if mrz is None:
    print("No MRZ found")
    exit(1)

# Obtain image
mrz_data = mrz.to_dict()

print(mrz_data['country'])
print(mrz_data['names'])
print(mrz_data['surname'])
print(mrz_data['type'])