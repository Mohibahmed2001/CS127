#Mohib Ahmed
#June 27,2023
#mohib.ahmed79@myhunter.cuny.edu
#We create and function and use if else statments

def computeFare(zone, ticketType):
     """
     Takes as two parameters: the zone and the ticket type.
     Returns the LIRR Transit fare, as follows:

     If the zone is 1 and the ticket type is "peak", the fare is 8.75.
     If the zone is 1 and the ticket type is "off-peak", the fare is 6.25.
     If the zone is 2 or 3 and the ticket type is "peak", the fare is 10.25.
     If the zone is 2 or 3 and the ticket type is "off-peak", the fare is 7.50.
     If the zone is 4 and the ticket type is "peak", the fare is 12.00.
     If the zone is 4 and the ticket type is "off-peak", the fare is 8.75.
     If the zone is 5, 6, or 7 and the ticket type is "peak", the fare is 13.50.
     If the zone is 5, 6, or 7 and the ticket type is "off-peak", the fare is 9.75.
     If the zone is greater than 8, return a negative number (since your calculator does not handle inputs that high).
     """
     
     fare = 0
     if ticketType == "peak":
         if zone == 1:
             fare = 8.75
         if zone == 2:
             fare = 10.25
         if zone == 3:
             fare = 10.25
         if zone == 4:
             fare = 12
         if zone == 5:
             fare = 13.5
         if zone == 6:
             fare = 13.5
         if zone == 7:
             fare = 13.5
         if zone >= 8:
             fare = -2
     elif ticketType == "off-peak":
         if zone == 1:
             fare = 6.25
         if zone == 2:
             fare = 7.5
         if zone == 3:
             fare = 7.5
         if zone == 4:
             fare = 8.75
         if zone == 5:
             fare = 9
         if zone == 6:
             fare = 9
         if zone == 7:
             fare = 9
         if zone >= 8:
             fare = -2
             
            

     return(fare)

def main():
     z = int(input('Enter the number of zones: '))
     t = input('Enter the ticket type (peak/off-peak): ').lower()
     fare = computeFare(z,t)
     print('The fare is', fare)

#Allow script to be run directly:
if __name__ == "__main__":
     main()
