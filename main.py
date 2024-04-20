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
