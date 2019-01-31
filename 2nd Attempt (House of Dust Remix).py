#!/usr/bin/env python
# coding: utf-8

# In[24]:


#!/usr/bin/python

# A House of Dust, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Alison Knowles & James Tenney, 1967
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 10 March 2015 to remove a duplicate value in "place".
# Updated 17 November 2015 to remove a near-duplicate value in "inhabitants".
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

material = ['BLOOD','STONE','SKY','MOLD','SKIN FLAKES']

location = ['IN THE DEPTHS OF HADES','SURROUNDED BY ICE','IN THE HEART OF A STORM','OUTSIDE AN OASIS','BENEATH THE DIRT']
light_source = ['BLAZING FIRE', 'GODRAYS', 'ELECTRICITY', 'MOONLIGHT','SOLAR RADIATION']
inhabitants = ['ROCKS','CHILDREN','BIRDPERSONS','DRUG ADDLED HORSES','ORGANIC CRYSTALS','E-COLI']
ruination = ['FLOODING','EARTHQUAKES','VOLCANIC ERUPTION','PESTILENCE','FAMINE','PLAGUE','NECROSIS','ZOMBIFICATION']
scenario = ['ESCAPE FROM', 'RETURN TO', 'AVOID', 'VISIT']
objective = ['YOUR FAMILY','THE TREASURE','YOUR LOVE','KNOWLEDGE','HELP','HAPPINESS']
print('')
print('A CITY OF ' + choice(material))
print('      ' + choice(location))
print('            LIT BY ' + choice(light_source))
print('                 DESTROYED BY ' + choice(ruination))
print('                         INHABITED BY ' + choice(inhabitants))
print('                              ' + choice(scenario) + ' THIS PLACE')
print('                                  FIND ' + choice(objective))
