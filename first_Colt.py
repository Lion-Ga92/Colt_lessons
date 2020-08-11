print("How many kms did you run today?")
miles_km = input()
miles = float(miles_km)/1.60934
miles = round(miles, 2)
print(f"your {miles_km} kms is equal to {miles} miles")
