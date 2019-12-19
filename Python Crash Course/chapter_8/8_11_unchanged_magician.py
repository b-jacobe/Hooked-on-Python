"""
8_11_unchanged_magicians.py

Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original
names and one list with the Great added to each magician’s name.

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
g_list = make_great(m_list[:])

print(show_magicians(g_list))
print(show_magicians(m_list))