from masstable import Table

# print first 5 elements from AME03
print Table('AME2003').head()

# Calculate the root mean squared error of Moller, et al.
# Atomic Data and Nuclear Data Tables, 59(1995), 185-351.
  
print Table('FRDM95').rmse(relative_to='AME2003')


# Calculate the root mean squared error of Moller, et al.
# Atomic Data and Nuclear Data Tables, 59(1995), 185-351. 

def test_AME2003_has_right_length():
    assert len(Table('AME2003')) == 3180