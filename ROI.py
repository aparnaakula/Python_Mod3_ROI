class RoiCalc():

    def __init__(self, rent_income=0, expenses=0, cash_flow=0, ROI=0):
        self.rentincome = rent_income
        self.expenses_r = expenses
        self.cashflow = cash_flow
        self.roi = ROI

    def rent_income(self):
        self.rentincome = int(input('What is the monthly rental income for this property? '))

# Monthly expenses
    def expenses(self):
        tax = int(input('Please enter the monthly tax amount: '))
        insurance = int(input('Please enter the monthly insurance amount: '))
        utilitities = int(input('Please enter the monthly utilities amount: '))
        repairs = int(input('How much are you saving for repairs monthly? '))
        capEx = int(input('How much are you saving for CapEx monthly? '))
        prop_man = int(input('How much are you paying the property manager monthly? '))
        mortgage = int(input('What is your monthly mortgage cost?  '))
        self.expenses_r = tax + insurance + utilitities + repairs + capEx + prop_man + mortgage
        print("My Expenses: %s" %(self.expenses_r))
        
# Cash flow
    def cash_flow(self):
        self.cashflow = self.rentincome - self.expenses_r
        print("My cash flow: %s" % (self.cashflow))

# Annual Return of Investment
    def ROI(self):
        self.cashflow = self.cashflow * 12
        overall_investment = int(input("What was the total investment you made on this property? "))
        self.roi = (self.cashflow/overall_investment) * 100

        print(' The cash on cash ROI: ')
        print(str(self.roi) + '%')

    def quit(self):
        print("Thank you")
        return True
        
rentalProperty = RoiCalc()

def run():
    while True:
        response = input('1.Income\n2.Expenses\n3.Cashflow \n4.ROI \n5.Quit \nPlease pick:  ')
        if response.lower() == '1':
            rentalProperty.rent_income()
        elif response.lower() == '2':
            rentalProperty.expenses()
        elif response.lower() == '3':
            rentalProperty.cash_flow()
        elif response.lower() == '4':
            rentalProperty.ROI()
        elif response.lower() == '5':
            if rentalProperty.quit():
                break
        else:
            print('Please enter a valid option ')

run()

