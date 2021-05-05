prin_amt = int(input("Enter principle amount : "))
rate = float(input("Enter rate of interest (in percent %) : "))
time = float(input("Enter time period : "))

si = prin_amt * rate * time /100
total_amt = si + prin_amt

print('Simple interest for the time of period is :',si)
print('Total amount for the time of period is :',total_amt)