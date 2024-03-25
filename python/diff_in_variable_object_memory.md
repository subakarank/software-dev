**Object Creation for Integers:**

- When you create an integer in Python, such as x = 5, Python creates an integer object to represent the value 5.
This object contains the actual value and any necessary metadata. Python manages this object internally, handling memory allocation and deallocation.

**Memory Allocation for Objects:**

- When Python creates an object, it allocates memory to store that object.
The amount of memory allocated depends on the type of object and the system architecture.
For integers, Python typically allocates a fixed amount of memory to store the integer value itself and any necessary metadata.

**References:**

- In Python, variables are references to objects.
When you assign a value to a variable, such as x = 5, x becomes a reference to the integer object representing the value 5. Similarly,
when you assign another variable y to the same value, like y = 5, y also becomes a reference to the same integer object.

**Sharing Memory vs. Sharing Objects:**

- When we say that x and y share the same object, it means they both point to the same location in memory where that integer object is stored.
They are essentially two names or labels referring to the same object. However, they are not the object itself. The object is the actual data stored in memory,
while x and y are references or labels pointing to that data.

So, when you change the value of x, like x = 10,
Python creates a new integer object representing the value 10 and updates the reference x to point to this new object.
However, it doesn't affect the reference y, which still points to the original object representing the value 5.


In summary, objects in Python are the actual data stored in memory, while references are labels or names that point to those objects.
Multiple references can point to the same object, allowing for variables to share data. However,
changing the value of one reference doesn't affect other references pointing to the same object.

Creation of Integer Object: When you assign a value to a variable, Python creates an object in memory to represent that value.
For integers within the range -5 to 256, Python preallocates these objects for performance reasons. Let's say you have the following code:

```
x = 5
y = 5
```

**Memory Allocation:**

- When you execute the above code, Python allocates memory for the integer object representing the value 5. 
Both x and y are then assigned references to this same object.

```
            +-------------+
  x ------> | Integer 5   |
            +-------------+
              ^
              |
  y ----------+

```

In this diagram:

x and y are references (or pointers) to the same integer object in memory.
The integer object contains the value 5.

**Changing Reference:**
If you were to change the reference of x to a different integer value, 
it would point to a different object in memory, but y would still point to the original 5 object:
```
x = 10
```
After this change, the diagram would look like this:

```
            +-------------+   +-------------+
  x ------> | Integer 10  |   | Integer 5   |
            +-------------+   +-------------+
                                  ^
                                  |
  y ------------------------------+

```

Now, x refers to a new integer object containing the value 10, while y still refers to the original integer object containing the value 5. There's no conflict because x and y are independent references to different objects in memory.

This separation of references and objects is fundamental to Python's memory management and allows for efficient memory usage and manipulation of objects.



