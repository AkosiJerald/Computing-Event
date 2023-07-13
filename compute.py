#declare your variables  and value
rate_per_day = 15000 #rate of the day
sound_system = 4500 #sound system fee
stage_dec = 3000 #stage decoration fee
catering = 35000 #catering fee
EVAT = .12 #added tax

#Get the number of days from the user
num_ofdays = float(input("Enter number of days: "))


#Computation or formula

#compute amount by adding rate per day and number of days
amount = rate_per_day * num_ofdays

#compute total amount by adding amout, sound system, stage decoration and catering
total_amount = amount + sound_system + stage_dec + catering

#get tax by multiplying total amount and evat
tax = total_amount * EVAT

#get bill by adding the total amount and tax
bill = total_amount + tax

#Print tha output or total computation
print("Bill: ", bill)
