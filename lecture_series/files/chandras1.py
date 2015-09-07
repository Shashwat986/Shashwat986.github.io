# Comparisons can be chained!
1 < 2 < 3  # => True
2 < 3 < 2  # => False

1j*1j == -1

# math vs cmath

# Strings are created with " or '
"This is a string."
'This is also a string.'


# A string can be treated like a list of characters
"This is a string"[0]  # => 'T'

#'==' vs 'is'
None is None  # => True
1 is 1  # => True
[1] is [1]  # => False

# None, 0, and empty strings/lists all evaluate to False.
# All other values are True
bool(0)  # => False
bool("")  # => False

"yahoo!" if 3 > 2 else "no!"

li = []
li.append(1)
li.append(2)
li.append(3)
li.append(4)
li.insert(0,100)
li.pop()

li[-1]
li[1:3]
li[::-1]
del li[2]

1 in li
len(li)

# Tuples are like lists but are immutable.
tup = (1, 2, 3)
d, e, f = 4, 5, 6
e, d = d, e # Neatest swap

# Dictionaries store mappings
empty_dict = {}
filled_dict = {"one": 1, "two": 2, "three": 3}
filled_dict.keys()
filled_dict.values()
filled_dict.get("four", 4)

some_set = set([1, 2, 2, 3, 4])
filled_set = {1, 2, 2, 3, 4}
filled_set.add(5)
filled_set | other_set
filled_set & other_set
{1, 2, 3, 4} - {2, 3, 5}

if True:
	print("Hello")
elif 1==1:
	print("Bye")
else:
	print("Huh")

for animal in ["dog", "cat", "mouse"]:
    print("{} is a mammal".format(animal))

def add(x, y=0):
    print("x is %s and y is %s" % (x, y))
    return x + y    # Return values with a return statement

add(y=6, x=5)
add(5, 6)
add(1)


def create_adder(x):
    def adder(y):
        return x + y
    return adder

