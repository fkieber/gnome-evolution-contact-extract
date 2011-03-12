#!/bin/env python
# -*- coding: utf-8 -*-

"""
Prints the address book as a telephone list.
Printed columns [followed by properties between brackets]:
    Name [name, full-name, given-name, family-name, nickname]
    Home (phone) [home-phone, home-phone-2, other-phone, primary-phone]
    Mobile [mobile-phone]
    Office (phone) [business-phone, business-phone-2, company-phone]
    Postal Address [address-home, address-work, address-other][x]
        x=0: ??
        x=1: PO Box
        x=2: Address (remains)
        x=3: Address line 1
        x=4: City
        x=5: State/Province
        x=6: Postcode
        x=7: Country
    Address []
    Postcode []
    City []
Sort by name
Omitting entries with the category [categories, category-list] 'no_print'
Omitting entries without a phone (home, mobile or desktop)
"""

import sys
from EDS import EDS

# Omottid address books
excl_addrs_books = [
    'Envoyés', 
    'temp', 
]

# Omitted categories
excl_cats = [
    'no_print', 
]

# Properties for name in order of priority
props_name = [
    'file-as', 
    'name-or-orgs', 
    'full-name', 
    'family-name', 
    'given-name', 
    'nickname', 
]

# Properties for home phone in order of priority
props_home = [
    'home-phone', 
    'home-phone-2', 
    'primary-phone', 
    'other-phone', 
]

# Properties for mobile phone in order of priority
props_mobile = 'mobile-phone'

# Properties for office phone in order of priority
props_office = [
    'business-phone', 
    'business-phone-2', 
    'company-phone', 
]

# Properties for address in order of priority
props_addr_street = (
    'address-home-line1', 
    'address_work-line1', 
    'address_other-line1', 
)
props_addr_post = (
    'address-home-post', 
    'address_work-post', 
    'address_other-post', 
)
props_addr_city = (
    'address-home-city', 
    'address_work-city', 
    'address_other-city', 
)

cfg = {
    'obooks': excl_addrs_books, 
    'ocats': excl_cats, 
    'fields': {
        'name': props_name,         # Name
        'home': props_home,         # Home phone nbr
        'mobile': props_mobile,     # Mobile phone nbr
        'office': props_office,     # Office phone nbr
        'addr': props_addr_street,  # Street name
        'post': props_addr_post,    # Postcode
        'city': props_addr_city,    # City
        #'test': 'list-show-addresses', 
    }
}

eds=EDS()

#eds._print_all_properties()

print "List of Address Books ======================="
for itm in eds.get_books():
    pass
    #print itm
print

print "List of Properties =========================="
for itm in eds.get_properties():
    pass
    #print itm
print

print "List of Contacts ============================"
liste = eds.get_contact_list(cfg)
liste.sort(key=lambda e: e['name'].lower())
for itm in liste:
    if itm['home'] != None or itm['mobile'] != None or itm['office'] != None:
        virg = ''
        s = ''
        for col in ('name', 'home', 'mobile', 'office', 'addr', 'post', 'city'):
            if itm[col] == None:
                itm[col] = ''
            if col == 'city':
                itm[col] = itm[col].upper()
            s += virg + '"' +itm[col] + '"'
            virg = ' '
        print s
