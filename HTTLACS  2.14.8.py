#You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours. At
#what time does the alarm go off? (Hint: you could count on your fingers, but this is not
#what we’re after. If you are tempted to count on your fingers, change the 51 to 5100.)
#8. Write a Python program to solve the general version of the above problem. Ask the user
#for the time now (in hours), and ask for the number of hours to wait. Your program
#should output what the time will be on the clock when the alarm goes off.

time_now = int(input("What is the time now in whole hours, between 1 and 24? "))
wait_time = int(input("How many hours from now should an alarm go off? "))
alarm_time = (time_now + wait_time) % 24
print(alarm_time)
