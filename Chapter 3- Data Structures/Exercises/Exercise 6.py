guests = ['Mr. & Mrs. Akbar' , 'Mr. & Mrs. Ali' , 'Mr. & Mrs. Rizwan']

name = guests[0].title()
print(name +", you are invited to family get together.")

name = guests[1].title()
print(name +", you are invited to family get together.")

name = guests[2].title()
print(name +", you are invited to family get together.")

name = guests[0].title()
print("\nSorry, " + name +" Can't make it to the family get together")

# Mr. & Mrs. Akbar can't make it to the get together lets invite Mr. & Mrs. Bilal
del(guests[0])
guests.insert(0,'Mr. & Mrs. Bilal')

# Print the invitations again.
name = guests[0].title()
print("\n" + name + ",you are invited to family get together.")

name = guests[1].title()
print(name +", you are invited to family get together.")

name = guests[2].title()
print(name +", you are invited to family get together.")

# The table wont arrive on time!
print("\nSorry, we can only invite two families on get together.")

name = guests.pop()
print("sorry, " + name.title() + " there's no room at the table.")

# There should be two families left. Let's invite them.
name = guests[0].title()
print(name + ", you are invited to family get together.")

name = guests[1].title()
print(name + ", you are invited to family get together.")