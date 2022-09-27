user_input_length = input("Enter a length (whole number): ")
user_input_width = input("Enter a width (whole number): ")
user_input_price = input("Enter a price (number and decimal only): ")

length = int(user_input_length)
width = int(user_input_width)
price = float(user_input_price)

#calculation
total_footage = length * width
total_cost = total_footage * price

#display results
print("--------------------------")
print("length: ", length)
print("width: ", width)
print("total Footage: ", total_footage)
print("Total cost: ", total_cost)
