total_bill = int(input("What is your total bill? "))
discount = int(input("How much discount are you getting? "))
additional_discount = input("Are you getting any additional discount/cashback? Y or N ")

bill_after_discount = 0

if additional_discount == "Y":
    add_discount = int(input("How much additional discount are you getting? "))
    bill_after_discount = discount * total_bill / 100
    print(f"Your total savings after additional discount is {bill_after_discount}")
    bill_before_additional_discount = total_bill - bill_after_discount
    print(f"Your current bill before additional discount is {bill_before_additional_discount}")
    total_discount_after_additional_discount = add_discount * bill_before_additional_discount / 100
    total_bill_after_all_discount = bill_before_additional_discount - total_discount_after_additional_discount
    print(f"Your absolute total is {total_bill_after_all_discount}")
    

else:
    bill_after_discount = discount * total_bill / 100
    print(f"You are saving {bill_after_discount}")
    total_bill_after_discount = total_bill - bill_after_discount
    print(f"Your total bill is {total_bill_after_discount}")
