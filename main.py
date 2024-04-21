if __name__ == "__main__":
  """
  Python provides another composite data type called a dictionary, which is similar to a list in that it is a collection of objects.

  Here's what you'll learn in this tutorial: You'll cover the basic characteristics of Python dictionaris and learn how to access and manage dictionary data.
  Once you have finished this tutorial, you should have a good sense of when a dictionary is the appropriate data type to use, and how to do so.

  Dictionaries and lists share the following characteristics:
  - Both are mutable.
  - Both are dynamic. They can grow and shrink as needed.
  - Both can be nested. A list can contain another list.
  A dictionary can contain another dictionary.
  A dictionary can also contain a list, and vice versa.

  Dictionaries differ from lists primary in how elements are accessed:
  - List elements are accessed by their position in the list, via indexing.
  - Dictionary elements are accessed via keys.
  """

  # Defining a Dictionary

  """
  Dictionaries are Python's implementation of a data structure that is more generally known as an associative array.
  A dictionary consist of a collection of key-value pairs.
  Each key-value pair maps the key to its associated value.

  You can define a dictionary by enclosing a comma-separated list of key-value pairs in curly braces ({}).
  A colon (:) separates each key from its associated value:

  The following defined a dictionary that mnaps a location to the name of its corresponding Major League Baseball team:
  """

  MLB_team = {
    "Colorado": "Rockies",
    "Boston": "Red Sox",
    "Minnesota": "Twins",
    "Milwaukee": "Brewers",
    "Seattle": "Mariners"
  }

  """
  You can also construct a dictionary with the built-in dict() function.
  The argument to dict() function should be a sequence of key-value pairs.
  A list of tuples works well for this
  """

  MLB_team = dict([
    ("Colorado", "Rockies"),
    ("Boston", "Red Sox"),
    ("Minnesota", "Twins"),
    ("Milwaukee", "Brewers"),
    ("Seattle", "Mariners")
  ])

  """
  If the key values are simple strings, they can be specificed as keyword arguments.
  So here is yet another way to define MLB_team:
  """

  MLB_team = dict(
    Colorado = "Rockies",
    Boston = "Red Sox",
    Minnesota = "Twins",
    Milwaukee = "Brewers",
    Seattle = "Mariners"
  )

  """
  Once you've defined a dictionary, you can display its contents, the sane as you can do for a list.
  All three of the definitions shown above appear as follows when displayed:
  """

  print(MLB_team)
  print(type(MLB_team))

  """
  The entries in the dictionary display in the order they were defined.
  But that is irrelevant when it comes to retrieving them.
  Dictionary elements are not accessed by numerical index:

  Perhaps you'd still like to sort your dictionary.
  If that's the case, then checkout Soring a Python Dictionary: Values, Keys and More.
  """

  # Accessing Dictonary Values

  """
  Of course, dictionary elements must be accessible somehow.
  If you don't get them by index, then how do you get them?

  A value is retrieved from a dictionary by specifying its corresponding key in square brackets ([]):
  """

  print(MLB_team["Minnesota"])
  print(MLB_team["Colorado"])

  """
  If you refer to a key that is not in the dictionary. Python raises an exception:

  Adding an entry to an exsting dictionary os simply a metter of assogning a new key and value:
  """

  MLB_team["Seattle"] = "Seahawks"
  print(MLB_team)

  """
  To delete an entry, use the del statement, specifying the key to delete
  """

  del MLB_team["Seattle"]
  print(MLB_team)

  # Dictionary Keys vs List Indices

  """
  You may have noticed that the interpreter raise the same exception, KeyError, when a dictionary is accessed with either an undefined key or by a numeric index:

  In fact, it's the same error.
  In the latter case, [1] looks like a numerical index, but it isn't.

  You will see later in this tutorial that an object of any immutable type can be used as a dictionary key.
  Accordingly, there is no reason you can't use integers:
  """

  d = { 0: "a", 1: "b", 2: "c", 3: "d" }
  print(d)
  print(d[0])
  print(d[2])

  """
  In the expression MLB_team[1], d[0] and d[2], the number in square brackets appear as though they might be indices.
  But they have nothing to do with the order of the items in the dictionary.
  Python is interpreting them as dictionary keys.
  If you define this same dictionary in reverse order, you still get the same value using the same keys:
  """

  d = { 3: "d", 2: "c", 1: "b", 0: "a" }
  print(d)
  print(d[0])
  print(d[2])

  """
  The syntax look similar, but you can't treat a dictionary like a list:
  """

  print(type(d))
  # d[-1]   # KeyError
  # d[0:2]  # TypeError
  # d.append("e") # AttributeError

  """
  Note: Although access to items in a dictionary does not depend on order, Python does guarantee that the order of items in a dictionary is preserved.
  When displayed, items will appear in the order they were defined, and iteration through the keys will occur in that order as well.
  Items added to a dictionary are added at the end.
  If items are deleted, the order of the remaining items is retained.
  """

  # Building a Dictionary Incrementally

  """
  Defining a dictionary using curly braces and a list of key-value pairs, as shown above, is fine id you know all the keys and values in advance.
  But what if you want to build a dictionary on the fly?

  You can start by creating an empty dictionary, which is specified by empty curly braces.
  Then you can add new keys and values one at a time:
  """

  person = {}
  print(type(person))

  person["fname"] = "Joe"
  person["lname"] = "Fonebone"
  person["age"] = 51
  person["spouse"] = "Edna"
  person["children"] = ["Ralph", "Betty", "Joey"]
  person["pets"] = { "dog": "Fido", "cat": "Sox" }

  print(person)
  print(person["fname"])
  print(person["age"])
  print(person["children"])

  """
  Retrieving the values in the sublist or subdictionary requires an addtional index or key:
  """

  print(person["children"][-1])
  print(person["pets"]["cat"])

  """
  This example exhibits another feature of dictionaries: the values contained in the dictionary don't need to be the same type.
  In person, some of the values are strings, one is an integer, one is a list, and one is another dictionary.

  Just as the values in a dictionary don't need to be of the same type, the keys don't either
  """

  foo = { 42: "aaa", 2.78: "bbb", True: "ccc" }
  print(foo)
  print(foo[42])
  print(foo[2.78])
  print(foo[True])

  """
  Here. one of the keys is integer, one is a flowt, and one is Boolean.
  It's not obvious how this would be useful, but you never know.

  Notice how versatile Python dictionaries are.
  In MLB_team, the same piece of information (the baseball team name) is kept for each of several different geographical locations.
  person, on the other hand, stores varying types of date for a single person.

  You can use dictionaries for a wide range purpose because there are so few limitations on the keys and values that are allowed.
  But there are some. Read on!
  """

  # Restrictions on Dictionary Keys

  """
  Almost any type of value can be used as a dictionary key in Python.
  You just saw this example, where integer, float, and Boolean objects are used as keys:
  """

  foo = { 42: "aaa", 2.78: "bbb", True: "ccc" }
  print(foo)

  """
  You can even use built-in objects like types and functions
  """

  d = { int: 1, float: 2, bool: 3 }
  print(d)
  print(d[float])

  d = { bin: 1, hex: 2, oct: 3 }
  print(d)
  print(d[oct])

  """
  However, there are a couple restrictions that dictionary key must abide by.

  First, a given key can appear in a dictionary only once.
  Duplicates keys are now allowed.
  A dictionary maps each key to a corresponding, so it doesn't make sense to map a particular key more than once.

  You saw above that when you assign a value to an already existing dictionary key, it does not add the key a second time, but replaces the existing value
  """

  MLB_team = {
    "Colorado": "Rockies",
    "Boston": "Red Sox",
    "Minnesota": "Twins",
    "Milwaukee": "Brewers",
    "Seattle": "Mariners"
  }
  print(MLB_team)
  MLB_team["Minnesota"] = "Timberwolves"
  print(MLB_team)

  """
  Similarly, if you specify a ket a second time duting the initial creation of a dictionary, the second occurrence will override the first:
  """

  MLB_team = {
    "Colorado": "Rockies",
    "Boston": "Red Sox",
    "Minnesota": "Timberwolves",
    "Milwaukee": "Brewers",
    "Seattle": "Mariners",
    "Minnesota": "Twins"
  }
  print(MLB_team)

  """
  Secondly, a dictionary key must be a type that immutable.
  You have already seen examples where several of the immutable types you are familiar with - integer, float, string and Boolean - have served as dictionary keys.

  A tuple can also be a dictionary key, because tuples are immutable:
  """

  d = { (1, 1): "a", (1, 2): "b", (2, 1): "c", (2, 2): "d" }
  print(d)
  print(d[(1, 1)])
  print(d[(2, 1)])

  """
  Recall from the discussion on tuples that one rationale for using a tuple instead of a list is that there are circumstances where an immutable type is required.
  This is one of them.

  However, neither a list nor another dictionary can serve as a dictionary key, because lists and dictionaries are mutablle
  """

  # d = { [1, 1]: "a", [1, 2]: "b", [2, 1]: "c", [2, 2]: "d" }
  # TypeError

  """
  Technical Note: Why does the error message say "unhashable"?

  Technically, it is not quite correct to say an object must be immutable to be used as a dictionary key.
  More precisely, an object must be hashable, which means it can be passed to a hash function.
  A hash function takes data or arbitrary size and maps it to a relatively simpler fixed-size value called a hash value (or simply hash), which is used for table lookup and comparison.

  Python's built-in hash() function returns the hash value for an object which is hashable, and raise an exception for an object which isn't:
  """

  print(hash("foo"))

  """
  All of the built-in immutable types you have learned about so far are hashable, and the mutable container types (lists and dictionaries) are not.
  So for present purposes, you can think of hashable and immutable as more oe less synonymous.

  In future tutorials, you will encounter mutable objects which are also hashable.
  """

  # Restrictions on Dictionary Values

  """
  By contrast, there are no restrictions on dictionary values.
  Literally none at all.
  A dictionary value can be any type of object Python supports, including mutable types like lists and dictionaries, and user-defined objects, which you will learn about in upcoming tutorials.

  There is also no restriction against a particular value appearing in a dictionary mutiple times:
  """

  d = { 0: "a", 1: "a", 2: "a", 3: "a" }
  print(d)
  print(d[0] == d[1] == d[2])
