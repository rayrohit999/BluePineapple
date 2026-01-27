'''
Write a function to calculate electricity bill.
'''
def calculateElectricityBill(unit_consumed: int) -> int:
    '''
    Takes unit consumed as input and returns electricity bill.
        Parameter:
            unit_consumed ( int ): unit consumed by customer in this month
        Returns:
            Calculated elctricity bill for this month
        Raises:
            ValueError: If unit_consumed is negative number
    '''
    if unit_consumed < 0:
        raise ValueError
    total_bill = 0

    # Slab 1 (0 - 50)unit 5 rupees per unit
    if unit_consumed > 50:
        total_bill += 50 * 5
        unit_consumed -= 50
        # Slab 2 (51 - 100)unit 7 rupees per unit
        if unit_consumed > 50:
            total_bill += 50 * 7
            unit_consumed -= 50
            # Slab 3 ( more than 100)units 10 rupees per unit
            if unit_consumed:
                total_bill += unit_consumed * 10
        else:
            total_bill += unit_consumed * 7
    else:
        total_bill += unit_consumed * 5
    return total_bill

if __name__ == "__main__":
    try:
        unit_consumed = int(input("Enter unit consumed in this month: "))
        bill = calculateElectricityBill(unit_consumed)
        print("Electricity bill for this month is : ", bill)
    except ValueError as e:
        print("Error: wrong value enterd for unit consumed")