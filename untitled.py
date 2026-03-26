# Module1

# 3.1 How many seconds are in an hour?
# There are 60 seconds in a minute and 60 minutes in an hour.
seconds_in_hour = 60 * 60
print("3.1 Answer:", seconds_in_hour)

# 3.2 Assign the result to seconds_per_hour
seconds_per_hour = seconds_in_hour
print("3.2 seconds_per_hour:", seconds_per_hour)

# 3.3 How many seconds are in a day?
# There are 24 hours in a day.
seconds_in_day = seconds_per_hour * 24
print("3.3 Answer:", seconds_in_day)

# 3.4 Assign seconds_per_day
seconds_per_day = seconds_in_day
print("3.4 seconds_per_day:", seconds_per_day)

# 3.5 Floating-point division
float_division = seconds_per_day / seconds_per_hour
print("3.5 Floating-point result:", float_division)

# 3.6 Integer division
int_division = seconds_per_day // seconds_per_hour
print("3.6 Integer division result:", int_division)

# Answer check for 3.6
print("3.6 Comparison:", "Yes, it matches except no .0")
