{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#  Python Tutorial"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Introduction"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Python is a great general-purpose programming language on its own, but with the help of a few popular libraries (numpy, scipy, matplotlib) it becomes a powerful environment for scientific computing and data engineering.\n",
    "\n",
    "We expect that many of you will have some experience with Python and numpy; for the rest of you, this section will serve as a quick crash course both on the Python programming language and on the use of Python for scientific computing.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this tutorial, we will cover:\n",
    "\n",
    "* Basic Python: Basic data types (Containers, Lists, Dictionaries, Sets, Tuples), Functions, Classes\n",
    "* Numpy: Arrays, Array indexing, Datatypes, Array math, Broadcasting\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Basics of Python"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Python is a high-level, dynamically typed multiparadigm programming language. Python code is often said to be almost like pseudocode, since it allows you to express very powerful ideas in very few lines of code while being very readable. As an example, here is an implementation of the classic quicksort algorithm in Python:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Basic data types"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Numbers"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Integers and floats work as you would expect from other languages:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3 <class 'int'>\n"
     ]
    }
   ],
   "source": [
    "x = 3\n",
    "print (x, type(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "3\n",
      "8\n",
      "16\n"
     ]
    }
   ],
   "source": [
    "print (x + 1)   # Addition;\n",
    "print (x - 1)   # Subtraction;\n",
    "print (x * 2)   # Multiplication;\n",
    "print (x ** 2)  # Exponentiation;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "x += 1\n",
    "print (x)  # Prints \"4\"\n",
    "x *= 2\n",
    "print (x)  # Prints \"8\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'float'>\n",
      "2.5 3.5 5.0 6.25\n"
     ]
    }
   ],
   "source": [
    "y = 2.5\n",
    "print (type(y)) # Prints \"<type 'float'>\"\n",
    "print (y, y + 1, y * 2, y ** 2) # Prints \"2.5 3.5 5.0 6.25\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Note that unlike many languages, Python does not have unary increment (x++) or decrement (x--) operators.\n",
    "\n",
    "Python also has built-in types for long integers and complex numbers; you can find all of the details in the [documentation](https://docs.python.org/2/library/stdtypes.html#numeric-types-int-float-long-complex)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Booleans"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Python implements all of the usual operators for Boolean logic, but uses English words rather than symbols (`&&`, `||`, etc.):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'bool'>\n"
     ]
    }
   ],
   "source": [
    "t, f = True, False\n",
    "print (type(t)) # Prints \"<type 'bool'>\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now we let's look at the operations:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "print (t and f) # Logical AND;\n",
    "print (t or f)  # Logical OR;\n",
    "print (not t)   # Logical NOT;\n",
    "print (t != f)  # Logical XOR;"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Strings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello 5\n"
     ]
    }
   ],
   "source": [
    "hello = 'hello'   # String literals can use single quotes\n",
    "world = \"world\"   # or double quotes; it does not matter.\n",
    "print (hello, len(hello))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello world\n"
     ]
    }
   ],
   "source": [
    "hw = hello + ' ' + world  # String concatenation\n",
    "print (hw)  # prints \"hello world\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello world 12\n"
     ]
    }
   ],
   "source": [
    "hw12 = '%s %s %d' % (hello, world, 12)  # sprintf style string formatting\n",
    "print (hw12)  # prints \"hello world 12\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "String objects have a bunch of useful methods; for example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n",
      "HELLO\n",
      "  hello\n",
      " hello \n",
      "he(ell)(ell)o\n",
      "world\n"
     ]
    }
   ],
   "source": [
    "s = \"hello\"\n",
    "print (s.capitalize())  # Capitalize a string; prints \"Hello\"\n",
    "print (s.upper())       # Convert a string to uppercase; prints \"HELLO\"\n",
    "print (s.rjust(7))      # Right-justify a string, padding with spaces; prints \"  hello\"\n",
    "print (s.center(7))     # Center a string, padding with spaces; prints \" hello \"\n",
    "print (s.replace('l', '(ell)'))  # Replace all instances of one substring with another;\n",
    "                               # prints \"he(ell)(ell)o\"\n",
    "print ('  world '.strip())  # Strip leading and trailing whitespace; prints \"world\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can find a list of all string methods in the [documentation](https://docs.python.org/2/library/stdtypes.html#string-methods)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Containers"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Python includes several built-in container types: lists, dictionaries, sets, and tuples."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Lists"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A list is the Python equivalent of an array, but is resizeable and can contain elements of different types:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 1, 2] 2\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "xs = [3, 1, 2]   # Create a list\n",
    "print (xs, xs[2])\n",
    "print (xs[-1])     # Negative indices count from the end of the list; prints \"2\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 1, 'foo']\n"
     ]
    }
   ],
   "source": [
    "xs[2] = 'foo'    # Lists can contain elements of different types\n",
    "print (xs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 1, 'foo', 'bar']\n"
     ]
    }
   ],
   "source": [
    "xs.append('bar') # Add a new element to the end of the list\n",
    "print (xs)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "bar [3, 1, 'foo']\n"
     ]
    }
   ],
   "source": [
    "x = xs.pop()     # Remove and return the last element of the list\n",
    "print (x, xs) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As usual, you can find all the gory details about lists in the [documentation](https://docs.python.org/2/tutorial/datastructures.html#more-on-lists)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Slicing"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In addition to accessing list elements one at a time, Python provides concise syntax to access sublists; this is known as slicing:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5]\n",
      "[3, 4]\n",
      "[3, 4, 5]\n",
      "[1, 2]\n",
      "[1, 2, 3, 4, 5]\n",
      "[1, 2, 3, 4]\n",
      "[1, 2, 8, 9, 5]\n"
     ]
    }
   ],
   "source": [
    "nums = [1, 2, 3, 4, 5]    \n",
    "print (nums)         # Prints \"[0, 1, 2, 3, 4]\"\n",
    "print (nums[2:4])    # Get a slice from index 2 to 4 (exclusive); prints \"[2, 3]\"\n",
    "print (nums[2:])     # Get a slice from index 2 to the end; prints \"[2, 3, 4]\"\n",
    "print (nums[:2])     # Get a slice from the start to index 2 (exclusive); prints \"[0, 1]\"\n",
    "print (nums[:])      # Get a slice of the whole list; prints [\"0, 1, 2, 3, 4]\"\n",
    "print (nums[:-1])    # Slice indices can be negative; prints [\"0, 1, 2, 3]\"\n",
    "nums[2:4] = [8, 9] # Assign a new sublist to a slice\n",
    "print (nums)         # Prints \"[0, 1, 8, 9, 4]\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Loops"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can loop over the elements of a list like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cat\n",
      "dog\n",
      "monkey\n"
     ]
    }
   ],
   "source": [
    "animals = ['cat', 'dog', 'monkey']\n",
    "for animal in animals:\n",
    "    print (animal)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If you want access to the index of each element within the body of a loop, use the built-in `enumerate` function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "#1: cat\n",
      "#2: dog\n",
      "#3: monkey\n"
     ]
    }
   ],
   "source": [
    "animals = ['cat', 'dog', 'monkey']\n",
    "for idx, animal in enumerate(animals):\n",
    "    print ('#%d: %s' % (idx + 1, animal))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### List comprehensions:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "When programming, frequently we want to transform one type of data into another. As a simple example, consider the following code that computes square numbers:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 4, 9, 16]\n"
     ]
    }
   ],
   "source": [
    "nums = [0, 1, 2, 3, 4]\n",
    "squares = []\n",
    "for x in nums:\n",
    "    squares.append(x ** 2)\n",
    "print (squares)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can make this code simpler using a list comprehension:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 4, 9, 16]\n"
     ]
    }
   ],
   "source": [
    "nums = [0, 1, 2, 3, 4]\n",
    "squares = [x ** 2 for x in nums]\n",
    "print (squares)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "List comprehensions can also contain conditions:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 4, 16]\n"
     ]
    }
   ],
   "source": [
    "nums = [0, 1, 2, 3, 4]\n",
    "even_squares = [x ** 2 for x in nums if x % 2 == 0]\n",
    "print (even_squares)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Dictionaries"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A dictionary stores (key, value) pairs, similar to a `Map` in Java or an object in Javascript. You can use it like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cute\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "d = {'cat': 'cute', 'dog': 'furry'}  # Create a new dictionary with some data\n",
    "print (d['cat'])       # Get an entry from a dictionary; prints \"cute\"\n",
    "print ('cat' in d)     # Check if a dictionary has a given key; prints \"True\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "wet\n"
     ]
    }
   ],
   "source": [
    "d['fish'] = 'wet'    # Set an entry in a dictionary\n",
    "print (d['fish'])      # Prints \"wet\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'monkey'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-29-2de793f9c766>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mprint\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0md\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'monkey'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m  \u001b[1;31m# KeyError: 'monkey' not a key of d\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m: 'monkey'"
     ]
    }
   ],
   "source": [
    "print (d['monkey'])  # KeyError: 'monkey' not a key of d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "N/A\n",
      "wet\n"
     ]
    }
   ],
   "source": [
    "print (d.get('monkey', 'N/A'))  # Get an element with a default; prints \"N/A\"\n",
    "print (d.get('fish', 'N/A'))    # Get an element with a default; prints \"wet\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "N/A\n"
     ]
    }
   ],
   "source": [
    "del d['fish']        # Remove an element from a dictionary\n",
    "print (d.get('fish', 'N/A')) # \"fish\" is no longer a key; prints \"N/A\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can find all you need to know about dictionaries in the [documentation](https://docs.python.org/2/library/stdtypes.html#dict)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It is easy to iterate over the keys in a dictionary:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A person has 2 legs\n",
      "A cat has 4 legs\n",
      "A spider has 8 legs\n"
     ]
    }
   ],
   "source": [
    "d = {'person': 2, 'cat': 4, 'spider': 8}\n",
    "for animal in d:\n",
    "    legs = d[animal]\n",
    "    print ('A %s has %d legs' % (animal, legs))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If you want access to keys and their corresponding values, use the iteritems method:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A person has 2 legs\n",
      "A cat has 4 legs\n",
      "A spider has 8 legs\n"
     ]
    }
   ],
   "source": [
    "d = {'person': 2, 'cat': 4, 'spider': 8}\n",
    "for animal, legs in d.items():\n",
    "    print ('A %s has %d legs' % (animal, legs))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Dictionary comprehensions: These are similar to list comprehensions, but allow you to easily construct dictionaries. For example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{0: 0, 2: 4, 4: 16}\n"
     ]
    }
   ],
   "source": [
    "nums = [0, 1, 2, 3, 4]\n",
    "even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}\n",
    "print (even_num_to_square)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Sets"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A set is an unordered collection of distinct elements. As a simple example, consider the following:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "animals = {'cat', 'dog'}\n",
    "print ('cat' in animals)   # Check if an element is in a set; prints \"True\"\n",
    "print ('fish' in animals)  # prints \"False\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "animals.add('fish')      # Add an element to a set\n",
    "print ('fish' in animals)\n",
    "print (len(animals))       # Number of elements in a set;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "animals.add('cat')       # Adding an element that is already in the set does nothing\n",
    "print (len(animals))       \n",
    "animals.remove('cat')    # Remove an element from a set\n",
    "print (len(animals))       "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "_Loops_: Iterating over a set has the same syntax as iterating over a list; however since sets are unordered, you cannot make assumptions about the order in which you visit the elements of the set:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "#1: fish\n",
      "#2: dog\n",
      "#3: cat\n"
     ]
    }
   ],
   "source": [
    "animals = {'cat', 'dog', 'fish'}\n",
    "for idx, animal in enumerate(animals):\n",
    "    print ('#%d: %s' % (idx + 1, animal))\n",
    "# Prints \"#1: fish\", \"#2: dog\", \"#3: cat\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Set comprehensions: Like lists and dictionaries, we can easily construct sets using set comprehensions:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{0, 1, 2, 3, 4, 5}\n"
     ]
    }
   ],
   "source": [
    "from math import sqrt\n",
    "print ({int(sqrt(x)) for x in range(30)})"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Tuples"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A tuple is an (immutable) ordered list of values. A tuple is in many ways similar to a list; one of the most important differences is that tuples can be used as keys in dictionaries and as elements of sets, while lists cannot. Here is a trivial example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'tuple'>\n",
      "5\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "d = {(x, x + 1): x for x in range(10)}  # Create a dictionary with tuple keys\n",
    "t = (5, 6)       # Create a tuple\n",
    "print (type(t))\n",
    "print (d[t])       \n",
    "print (d[(1, 2)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'tuple' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-42-c8aeb8cd20ae>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mt\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: 'tuple' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "t[0] = 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Functions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Python functions are defined using the `def` keyword. For example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "negative\n",
      "zero\n",
      "positive\n"
     ]
    }
   ],
   "source": [
    "def sign(x):\n",
    "    if x > 0:\n",
    "        return 'positive'\n",
    "    elif x < 0:\n",
    "        return 'negative'\n",
    "    else:\n",
    "        return 'zero'\n",
    "\n",
    "for x in [-1, 0, 1]:\n",
    "    print (sign(x))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We will often define functions to take optional keyword arguments, like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, Bob!\n",
      "HELLO, FRED\n"
     ]
    }
   ],
   "source": [
    "def hello(name, loud=False):\n",
    "    if loud:\n",
    "        print ('HELLO, %s' % name.upper())\n",
    "    else:\n",
    "        print ('Hello, %s!' % name)\n",
    "\n",
    "hello('Bob')\n",
    "hello('Fred', loud=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Classes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The syntax for defining classes in Python is straightforward:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, Fred\n",
      "HELLO, FRED!\n"
     ]
    }
   ],
   "source": [
    "class Greeter:\n",
    "\n",
    "    # Constructor\n",
    "    def __init__(self, name):\n",
    "        self.name = name  # Create an instance variable\n",
    "\n",
    "    # Instance method\n",
    "    def greet(self, loud=False):\n",
    "        if loud:\n",
    "            print ('HELLO, %s!' % self.name.upper())\n",
    "        else:\n",
    "            print ('Hello, %s' % self.name)\n",
    "\n",
    "g = Greeter('Fred')  # Construct an instance of the Greeter class\n",
    "g.greet()            # Call an instance method; prints \"Hello, Fred\"\n",
    "g.greet(loud=True)   # Call an instance method; prints \"HELLO, FRED!\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Programming exercise\n",
    "Problem: Write a function: Given a two list of ints, create a third list such that should contain only odd numbers from the first list and even numbers from the second list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# example input: list1: [10, 20, 23, 11, 17], list2: [13, 43, 24, 36, 12]\n",
    "# example output: [23, 11, 17, 24, 36, 12]\n",
    "def merge_lists(listOne, listTwo):\n",
    "    # write your code here\n",
    "\n",
    "# test your function\n",
    "list1 = [10, 20, 23, 11, 17]\n",
    "list2 = [13, 43, 24, 36, 12]\n",
    "print(merge_lists(list1, list2))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Numpy"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Numpy is the core library for scientific computing in Python. It provides a high-performance multidimensional array object, and tools for working with these arrays. If you are already familiar with MATLAB, you might find this [tutorial](http://wiki.scipy.org/NumPy_for_Matlab_Users) useful to get started with Numpy."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "To use Numpy, we first need to import the `numpy` package:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Arrays"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A numpy array is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers. The number of dimensions is the rank of the array; the shape of an array is a tuple of integers giving the size of the array along each dimension."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can initialize numpy arrays from nested Python lists, and access elements using square brackets:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'numpy.ndarray'> (3,) 1 2 3\n",
      "[5 2 3]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3])  # Create a rank 1 array\n",
    "print (type(a), a.shape, a[0], a[1], a[2])\n",
    "a[0] = 5                 # Change an element of the array\n",
    "print (a)                  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3]\n",
      " [4 5 6]]\n"
     ]
    }
   ],
   "source": [
    "b = np.array([[1,2,3],[4,5,6]])   # Create a rank 2 array\n",
    "print (b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(2, 3)\n",
      "1 2 4\n"
     ]
    }
   ],
   "source": [
    "print (b.shape)                   \n",
    "print (b[0, 0], b[0, 1], b[1, 0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Numpy also provides many functions to create arrays:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0. 0.]\n",
      " [0. 0.]]\n"
     ]
    }
   ],
   "source": [
    "a = np.zeros((2,2))  # Create an array of all zeros\n",
    "print (a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1. 1.]]\n"
     ]
    }
   ],
   "source": [
    "b = np.ones((1,2))   # Create an array of all ones\n",
    "print (b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[7 7]\n",
      " [7 7]]\n"
     ]
    }
   ],
   "source": [
    "c = np.full((2,2), 7) # Create a constant array\n",
    "print (c) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1. 0.]\n",
      " [0. 1.]]\n"
     ]
    }
   ],
   "source": [
    "d = np.eye(2)        # Create a 2x2 identity matrix\n",
    "print (d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.34399879 0.36689494]\n",
      " [0.31923691 0.23037697]]\n"
     ]
    }
   ],
   "source": [
    "e = np.random.random((2,2)) # Create an array filled with random values\n",
    "print (e)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Array indexing"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Numpy offers several ways to index into arrays."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Slicing: Similar to Python lists, numpy arrays can be sliced. Since arrays may be multidimensional, you must specify a slice for each dimension of the array:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[2 3]\n",
      " [6 7]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Create the following rank 2 array with shape (3, 4)\n",
    "# [[ 1  2  3  4]\n",
    "#  [ 5  6  7  8]\n",
    "#  [ 9 10 11 12]]\n",
    "a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])\n",
    "\n",
    "# Use slicing to pull out the subarray consisting of the first 2 rows\n",
    "# and columns 1 and 2; b is the following array of shape (2, 2):\n",
    "# [[2 3]\n",
    "#  [6 7]]\n",
    "b = a[:2, 1:3]\n",
    "print (b)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A slice of an array is a view into the same data, so modifying it will modify the original array."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "77\n"
     ]
    }
   ],
   "source": [
    "print (a[0, 1])  \n",
    "b[0, 0] = 77    # b[0, 0] is the same piece of data as a[0, 1]\n",
    "print (a[0, 1]) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can also mix integer indexing with slice indexing. However, doing so will yield an array of lower rank than the original array. Note that this is quite different from the way that MATLAB handles array slicing:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  2  3  4]\n",
      " [ 5  6  7  8]\n",
      " [ 9 10 11 12]]\n"
     ]
    }
   ],
   "source": [
    "# Create the following rank 2 array with shape (3, 4)\n",
    "a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])\n",
    "print (a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Two ways of accessing the data in the middle row of the array.\n",
    "Mixing integer indexing with slices yields an array of lower rank,\n",
    "while using only slices yields an array of the same rank as the\n",
    "original array:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5 6 7 8] (4,)\n",
      "[[5 6 7 8]] (1, 4)\n",
      "[[5 6 7 8]] (1, 4)\n",
      "[5 7]\n"
     ]
    }
   ],
   "source": [
    "row_r1 = a[1, :]    # Rank 1 view of the second row of a  \n",
    "row_r2 = a[1:2, :]  # Rank 2 view of the second row of a\n",
    "row_r3 = a[[1], :]  # Rank 2 view of the second row of a\n",
    "print (row_r1, row_r1.shape) \n",
    "print (row_r2, row_r2.shape)\n",
    "print (row_r3, row_r3.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You could slice array with strides."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 3]\n",
      "[[ 1  2  3  4]\n",
      " [ 9 10 11 12]]\n"
     ]
    }
   ],
   "source": [
    "print(a[0, ::2]) # first we choose the first row of array a. Then we slice cols with stride 2.\n",
    "print(a[::2, :]) # slice rows with stride 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You could use reshape function to modify the shape of array. The following code reshape the array with shape (3, 4) to (2, 6) and (1, 12)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  2  3  4  5  6]\n",
      " [ 7  8  9 10 11 12]]\n",
      "[[ 1  2  3  4  5  6  7  8  9 10 11 12]]\n"
     ]
    }
   ],
   "source": [
    "print(a.reshape((2, 6)))\n",
    "print(a.reshape((1, -1))) # in reshape function, -1 means numpy will automatically compute the remaining dimensions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 2  6 10] (3,)\n",
      "\n",
      "[[ 2]\n",
      " [ 6]\n",
      " [10]] (3, 1)\n"
     ]
    }
   ],
   "source": [
    "# We can make the same distinction when accessing columns of an array:\n",
    "col_r1 = a[:, 1]\n",
    "col_r2 = a[:, 1:2]\n",
    "print (col_r1, col_r1.shape)\n",
    "print ()\n",
    "print (col_r2, col_r2.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Integer array indexing: When you index into numpy arrays using slicing, the resulting array view will always be a subarray of the original array. In contrast, integer array indexing allows you to construct arbitrary arrays using the data from another array. Here is an example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 4 5]\n",
      "[1 4 5]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([[1,2], [3, 4], [5, 6]])\n",
    "\n",
    "# An example of integer array indexing.\n",
    "# The returned array will have shape (3,) and \n",
    "print (a[[0, 1, 2], [0, 1, 0]])\n",
    "\n",
    "# The above example of integer array indexing is equivalent to this:\n",
    "print (np.array([a[0, 0], a[1, 1], a[2, 0]]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2 2]\n",
      "[2 2]\n"
     ]
    }
   ],
   "source": [
    "# When using integer array indexing, you can reuse the same\n",
    "# element from the source array:\n",
    "print (a[[0, 0], [1, 1]])\n",
    "\n",
    "# Equivalent to the previous integer array indexing example\n",
    "print (np.array([a[0, 1], a[0, 1]]))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "One useful trick with integer array indexing is selecting or mutating one element from each row of a matrix:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  2  3]\n",
      " [ 4  5  6]\n",
      " [ 7  8  9]\n",
      " [10 11 12]]\n"
     ]
    }
   ],
   "source": [
    "# Create a new array from which we will select elements\n",
    "a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])\n",
    "print (a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 1  6  7 11]\n"
     ]
    }
   ],
   "source": [
    "# Create an array of indices\n",
    "b = np.array([0, 2, 0, 1])\n",
    "\n",
    "# Select one element from each row of a using the indices in b\n",
    "print (a[:, b])  # : means Prints \"[ 1  6  7 11]\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[21 12 13]\n",
      " [14 15 26]\n",
      " [27 18 19]\n",
      " [20 31 22]]\n"
     ]
    }
   ],
   "source": [
    "# Mutate one element from each row of a using the indices in b\n",
    "a[:, b] += 10\n",
    "print (a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Numpy provides many useful functions for performing computations on arrays; one of the most useful is `sum`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 235,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "[4 6]\n",
      "[3 7]\n"
     ]
    }
   ],
   "source": [
    "x = np.array([[1,2],[3,4]])\n",
    "\n",
    "print np.sum(x)  # Compute sum of all elements; prints \"10\"\n",
    "print np.sum(x, axis=0)  # Compute sum of each column; prints \"[4 6]\"\n",
    "print np.sum(x, axis=1)  # Compute sum of each row; prints \"[3 7]\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can find the full list of mathematical functions provided by numpy in the [documentation](http://docs.scipy.org/doc/numpy/reference/routines.math.html).\n",
    "\n",
    "Apart from computing mathematical functions using arrays, we frequently need to reshape or otherwise manipulate data in arrays. The simplest example of this type of operation is transposing a matrix; to transpose a matrix, simply use the T attribute of an array object:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Broadcasting"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Broadcasting is a powerful mechanism that allows numpy to work with arrays of different shapes when performing arithmetic operations. Frequently we have a smaller array and a larger array, and we want to use the smaller array multiple times to perform some operation on the larger array.\n",
    "\n",
    "For example, suppose that we want to add a constant vector to each row of a matrix. We could do it like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 238,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 2  2  4]\n",
      " [ 5  5  7]\n",
      " [ 8  8 10]\n",
      " [11 11 13]]\n"
     ]
    }
   ],
   "source": [
    "# We will add the vector v to each row of the matrix x,\n",
    "# storing the result in the matrix y\n",
    "x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])\n",
    "v = np.array([1, 0, 1])\n",
    "y = np.empty_like(x)   # Create an empty matrix with the same shape as x\n",
    "\n",
    "# Add the vector v to each row of the matrix x with an explicit loop\n",
    "for i in range(4):\n",
    "    y[i, :] = x[i, :] + v\n",
    "\n",
    "print (y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Numpy broadcasting allows us to perform this computation without actually creating multiple copies of v. Consider this version, using broadcasting:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 242,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 2  2  4]\n",
      " [ 5  5  7]\n",
      " [ 8  8 10]\n",
      " [11 11 13]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# We will add the vector v to each row of the matrix x,\n",
    "# storing the result in the matrix y\n",
    "x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])\n",
    "v = np.array([1, 0, 1])\n",
    "y = x + v  # Add v to each row of x using broadcasting\n",
    "print y"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The line `y = x + v` works even though `x` has shape `(4, 3)` and `v` has shape `(3,)` due to broadcasting; this line works as if v actually had shape `(4, 3)`, where each row was a copy of `v`, and the sum was performed elementwise.\n",
    "\n",
    "Broadcasting two arrays together follows these rules:\n",
    "\n",
    "1. If the arrays do not have the same rank, prepend the shape of the lower rank array with 1s until both shapes have the same length.\n",
    "2. The two arrays are said to be compatible in a dimension if they have the same size in the dimension, or if one of the arrays has size 1 in that dimension.\n",
    "3. The arrays can be broadcast together if they are compatible in all dimensions.\n",
    "4. After broadcasting, each array behaves as if it had shape equal to the elementwise maximum of shapes of the two input arrays.\n",
    "5. In any dimension where one array had size 1 and the other array had size greater than 1, the first array behaves as if it were copied along that dimension\n",
    "\n",
    "If this explanation does not make sense, try reading the explanation from the [documentation](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html) or this [explanation](http://wiki.scipy.org/EricsBroadcastingDoc).\n",
    "\n",
    "Functions that support broadcasting are known as universal functions. You can find the list of all universal functions in the [documentation](http://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs).\n",
    "\n",
    "Here are some applications of broadcasting:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 4  5]\n",
      " [ 8 10]\n",
      " [12 15]]\n"
     ]
    }
   ],
   "source": [
    "# Compute outer product of vectors\n",
    "v = np.array([1,2,3])  # v has shape (3,)\n",
    "w = np.array([4,5])    # w has shape (2,)\n",
    "# To compute an outer product, we first reshape v to be a column\n",
    "# vector of shape (3, 1); we can then broadcast it against w to yield\n",
    "# an output of shape (3, 2), which is the outer product of v and w:\n",
    "\n",
    "print (np.reshape(v, (3, 1)) * w)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 244,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[2 4 6]\n",
      " [5 7 9]]\n"
     ]
    }
   ],
   "source": [
    "# Add a vector to each row of a matrix\n",
    "x = np.array([[1,2,3], [4,5,6]])\n",
    "# x has shape (2, 3) and v has shape (3,) so they broadcast to (2, 3),\n",
    "# giving the following matrix:\n",
    "\n",
    "print (x + v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 245,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 5  6  7]\n",
      " [ 9 10 11]]\n"
     ]
    }
   ],
   "source": [
    "# Add a vector to each column of a matrix\n",
    "# x has shape (2, 3) and w has shape (2,).\n",
    "# If we transpose x then it has shape (3, 2) and can be broadcast\n",
    "# against w to yield a result of shape (3, 2); transposing this result\n",
    "# yields the final result of shape (2, 3) which is the matrix x with\n",
    "# the vector w added to each column. Gives the following matrix:\n",
    "\n",
    "print ((x.T + w).T)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 246,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 5  6  7]\n",
      " [ 9 10 11]]\n"
     ]
    }
   ],
   "source": [
    "# Another solution is to reshape w to be a row vector of shape (2, 1);\n",
    "# we can then broadcast it directly against x to produce the same\n",
    "# output.\n",
    "print (x + np.reshape(w, (2, 1)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 247,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 2  4  6]\n",
      " [ 8 10 12]]\n"
     ]
    }
   ],
   "source": [
    "# Multiply a matrix by a constant:\n",
    "# x has shape (2, 3). Numpy treats scalars as arrays of shape ();\n",
    "# these can be broadcast together to shape (2, 3), producing the\n",
    "# following array:\n",
    "print (x * 2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Programming exercise\n",
    "Problem: Write a function to create a 8x8 matrix and fill it with a checkerboard pattern."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Your function should ouput like this:\n",
    "# [[0 1 0 1 0 1 0 1]                                                      \n",
    "#  [1 0 1 0 1 0 1 0]                                                      \n",
    "#  [0 1 0 1 0 1 0 1]                                                      \n",
    "#  [1 0 1 0 1 0 1 0]                                                      \n",
    "#  [0 1 0 1 0 1 0 1]                                                      \n",
    "#  [1 0 1 0 1 0 1 0]                                                      \n",
    "#  [0 1 0 1 0 1 0 1]                                                      \n",
    "#  [1 0 1 0 1 0 1 0]]\n",
    "\n",
    "def checkerboard():\n",
    "    # write your code here\n",
    "\n",
    "\n",
    "print(checkboard())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This brief overview has touched on many of the important things that you need to know about numpy, but is far from complete. Check out the [numpy reference](http://docs.scipy.org/doc/numpy/reference/) to find out much more about numpy."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
