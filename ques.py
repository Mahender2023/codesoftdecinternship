class telephonebillcharges:
    def __init__(self,num_calls):
        self.num_calls = num_calls
    def calculate_bills(self):
        base_charge = 200
        call_charge_1 = 0.6
        call_charge_2 = 0.5
        call_charge_3 = 0.4
    if self.num_calls <= 100:
        total_bill = base_charge
    elif 100 < self.num_calls <= 150:
        total_bill = base_charge + (self.num_calls-100)*call_charge_1
    elif 150 < self.num_calls <= 200:
        total_bill = base_charge+50*call_charge_1+(self.num_calls-150)*call_charge_2
    else:
        total_bill =  base_charge + 50 * call_charge_1 + 50*call_charge_2 + (self.num_calls - 200) * call_charge_3
user_input = input("enter the number of calls")
obj= telephonebillcharges(user_input)
print(obj.calculate_bills())