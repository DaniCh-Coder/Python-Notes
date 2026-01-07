# Convert kilometers to miles
def km_to_miles(km):
    miles = km * 0.621371
    return miles


# Convert miles to kilometers
def miles_to_km(miles):
    km = miles / 0.621371
    return km

# Example usage
if __name__ == "__main__":
    # Input from user from kilometers to miles
    print("Kilometers to Miles Conversion")
    kilometers = float(input("Enter distance in kilometers: "))
    miles = km_to_miles(kilometers)
    print(f"{kilometers} kilometers is equal to {miles} miles.")
    # Input from user from miles to kilometers
    print("\nMiles to Kilometers Conversion")
    miles_input = float(input("Enter distance in miles: "))
    kilometers = miles_to_km(miles_input)
    print(f"{miles_input} miles is equal to {kilometers} kilometers.")
    
