locations = [(12.9716, 77.5946)]
user_latitude = float(input("enter latitude: "))
user_longitude = float(input("enter longitude: "))

new_location = (user_latitude, user_longitude)

if new_location in locations:
    print("Location already exists")
else:
    locations.append(new_location)
print(locations)