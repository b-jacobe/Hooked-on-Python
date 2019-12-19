"""
8_10_magicians.py

Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by adding
the phrase the Great to each magician’s name. Call show_magicians() to
see that the list has actually been modified.

Created: 2-12-19
@author: Brian Jacobe

"""

def show_magicians(magician):
    m_list = []
    for mage in magician:
        title = mage.title()
        m_list.append(title)
    return m_list

def make_great(magician):
    g_list = []
    for mage in magician:
        mage = "the Great " + mage
        g_list.append(mage)
    return g_list

m_list = ["harry potter", "yen sid", "gandalf"]
g_list = make_great(m_list)

print(show_magicians(g_list))