# Name - Karthick Periasamy
# Roll No - iitp_aimltn_2602379
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")

temperatures = [28, 32, 35, 29, 31, 27, 30]

min_temp = temperatures[0]
max_temp = temperatures[0]

for temp in temperatures:
    if temp < min_temp:
        min_temp = temp
    if temp > max_temp:
        max_temp = temp

print("Minimum temperature:", min_temp)
print("Maximum temperature:", max_temp)

print("\n===== Task 2: Count Hot Days =====")

temperatures = [28, 32, 35, 29, 31, 27, 30]

temperatures = [28, 32, 35, 29, 31, 27, 30]

hot_days = 0

for temp in temperatures:
    if temp <= 30:
        continue   # Skip non-hot days
    
    hot_days += 1  # Count only hot days

print("Number of hot days:", hot_days)

print("\n===== Task 3: Alert System =====")

temperatures = [32, 35, 28, 40, 31, 29]

hot_days = 0

for day in range(len(temperatures)):
    temp = temperatures[day]
    
    if temp >= 40:
        print(f"Alert! Extreme temperature {temp}°C detected on Day {day + 1}")
        break
    
    if temp > 30:
        hot_days += 1

print("Hot Days before alert:", hot_days)