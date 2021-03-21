from app import db, Puppy

# Create 
my_puppy = Puppy('Rufus', 9)
db.session.add(my_puppy)
db.session.commit()

# Read
all_puppies = Puppy.query.all() # List of pupies in db
print(all_puppies)

# Select by id
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

# Filters (SQL codes)
puppy_frakie = Puppy.query.filter_by(name='Frankie')
print(puppy_frakie.all())

# Update 
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

# Delete 
second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()

# All puppy

all_puppies = Puppy.query.all()
print(all_puppies)
