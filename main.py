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
