amount=int(input("Enter the amount:"))
notes=[2000, 500, 100, 50, 20, 10]

for note in notes:
    if amount >= note:
        count = amount // note
        amount = amount % note
        print(note,'x',count) 