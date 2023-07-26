#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. What does an empty dictionary&#39;s code look like?

"""

In Python, an empty dictionary is represented by curly braces {}. Here's what the code for an
empty dictionary looks like:


empty_dict = {}



This creates a new dictionary called empty_dict that doesn't contain any key-value pairs and is 
essentially empty. You can add elements to the dictionary by assigning values to specific keys.
For example:


empty_dict['key1'] = 'value1'
empty_dict['key2'] = 'value2'
This would result in empty_dict containing two key-value pairs:


{'key1': 'value1', 'key2': 'value2'}


"""


# In[2]:


# 2. What is the value of a dictionary value with the key &#39;foo&#39; and the value 42?

"""The value associated with the key 'foo' in the dictionary is 42. In Python, a dictionary is a 
collection of key-value pairs, where each key is unique, and each key is associated with a specific 
value. When you define a dictionary like this:
"""

my_dict = {'foo': 42}
value_of_foo = my_dict['foo']
print(value_of_foo) 


# In[3]:


# 3. What is the most significant distinction between a dictionary and a list?

"""
The most significant distinction between a dictionary and a list in Python is how they store and access data:

Data Storage:

List: A list is an ordered collection of elements. It maintains the order of elements based on their position in t
he list. Elements in a list are accessed by their index, which starts from 0 for the first element.


Dictionary: A dictionary is an unordered collection of key-value pairs. It stores data as key-value pairs
, where each key is unique and maps to a specific value. The order of elements is not guaranteed in a dictionary.


Accessing Elements:

List: In a list, you access elements by their numerical index. For example, to access the first element in a list, you 
use my_list[0].

Dictionary: In a dictionary, you access elements by their unique keys. For example, if you have a key 'name', you can
access its corresponding value using my_dict['name'].


Keyed Data Structure:

List: A list does not require keys to access elements, and the elements are usually of the same type 
(although Python allows for heterogeneous lists).

Dictionary: A dictionary is a collection of key-value pairs, making it ideal for associating data with 
specific keys. The keys can be of any immutable type (e.g., strings, integers, tuples), and the values 
can be of any data type.

Here's an example to illustrate the difference:


# List example
my_list = [10, 20, 30, 40, 50]
print(my_list[2])  # Output: 30

# Dictionary example
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict['age'])  # Output: 30
In summary, a list is used to store an ordered collection of elements accessed by their index, while a
dictionary is used to store an unordered collection of key-value pairs accessed by their unique keys. 
Choosing between a list and a dictionary depends on the specific requirements and the way you need to 
organize and access your data.


"""


# In[4]:


# 4. What happens if you try to access spam[&#39;foo&#39;] if spam is {&#39;bar&#39;: 100}?

spam = {'bar': 100}

if 'foo' in spam:
    value = spam['foo']
    print(value)
else:
    print("'foo' key does not exist in the dictionary.")


# In[5]:


# 5. If a dictionary is stored in spam, what is the difference between the expressions &#39;cat&#39; in spam and
#39;cat&#39; in spam.keys()?

# cat in spam
spam = {'cat': 5, 'dog': 3, 'fish': 2}
print('cat' in spam)  # Output: True
print('bird' in spam)  # Output: False



# cat in spam.keys()

spam = {'cat': 5, 'dog': 3, 'fish': 2}
print('cat' in spam.keys())  # Output: True
print('bird' in spam.keys())  # Output: False


# In[6]:


# 6. If a dictionary is stored in spam, what is the difference between the expressions &#39;cat&#39; in spam and
#39;cat&#39; in spam.values()?

# cat in spam
spam = {'cat': 5, 'dog': 3, 'fish': 2}
print('cat' in spam)  # Output: True
print('bird' in spam)  # Output: False

# cat in spam.values()
spam = {'cat': 5, 'dog': 3, 'fish': 2}
print('cat' in spam.values())  # Output: False
print(5 in spam.values())      # Output: True


# In[7]:


# 7. What is a shortcut for the following code?
# if &#39;color&#39; not in spam:
# spam[&#39;color&#39;] = &#39;black&#39;


spam.setdefault('color', 'black')


# In[8]:


# 8. How do you &quot;pretty print&quot; dictionary values using which module and function?

import pprint

my_dict = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York',
    'hobbies': ['reading', 'hiking', 'cooking'],
    'contact': {
        'email': 'john.doe@example.com',
        'phone': '123-456-7890'
    }
}

pprint.pprint(my_dict)


# In[ ]:




