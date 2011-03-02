#!/bin/env python
# -*- coding: utf-8 -*-

# Site : http://live.gnome.org/Conduit/evolution-python
# Doc : pydoc evolution.ebook
# Exemples : http://talk.maemo.org/showthread.php?t=47840

"""
Imprime le carnet d'adresse sous forme de liste téléphonique.
Colonnes imprimées :
    Nom [name, full-name, given-name, family-name, nickname]
    Domicile (téléphone) [home-phone, home-phone-2, other-phone, primary-phone]
    Portable [mobile-phone]
    Bureau (téléphone) [business-phone, business-phone-2, company-phone]
    Adresse complete [address-home, address-work, address-other][x]
        x=0: ??
        x=1: Boîte postale
        x=2: Adresse (reste)
        x=3: Adresse ligne 1
        x=4: Ville
        x=5: État/Province
        x=6: Code postal
        x=7: Pays
    Adresse []
    Code postal []
    Ville []
Tri par nom
Exclusion des entrées ayant la catégorie [categories, category-list] 'no_print'
Exclusion des entrées sans téléphone (Domicile, Portable ou bureau)
"""

import evolution, sys
from ctypes import *

# Propriétés pour le nom par ordre de priorité
props_nom = [
    'file-as', 
    'name-or-org', 
    'full-name', 
    'family-name', 
    'given-name', 
    'nickname', 
]

# Propriétés pour le téléphone du domicile par ordre de priorité
props_dom = [
    'primary-phone', 
    'home-phone', 
    'home-phone-2', 
    'other-phone', 
]

# Propriétés pour le téléphone portable par ordre de priorité
props_port = [
    'mobile-phone', 
]

# Propriétés pour le téléphone du bureau par ordre de priorité
props_bur = [
    'business-phone', 
    'business-phone-2', 
    'company-phone', 
]

# Propriétés pour l'adresse par ordre de priorité
props_adr = [
    'address-home', 
    'address-work', 
    'address-other', 
    #'address-label-home', 
    #'address-label-work', 
    #'address-label-other', 
]

# Propriétés pour les catégories par ordre de priorité
props_cat = [
    'categories', 
    'category-list', 
]

def print_properties(contact, prop_list):
    s = ''
    beg = ''
    for prop in prop_list:
        val = contact.get_property(prop)
        if val == None:
            val = ''
        s += beg +"'" + prop + "' = '" + str(val) + "'"
        beg = ', '
    print s
        
# Decsciption d'une adresse
class ContactAddress(Structure):
    pass
ContactAddress._fields_ = [("name", c_char_p), 
                  ("next", POINTER(ContactAddress))]

class Evo(object):
    
    def __init__(self):
        
        self._contacts = []
        
        # Extraction de tous les carnets d'adresses
        self._books = evolution.ebook.list_addressbooks()
        
        # Traitement de ceux-ci
        for book in self._books:
            ob = evolution.ebook.open_addressbook(book[1])
            self._contacts += ob.get_all_contacts()
    
    def get_contact_list(self):
            
        liste = []
    
        # Traitement de tous les contacts 
        # (un contact ,ct est de type ebook.EContact)
        for ct in self._contacts:
        
            #print_properties(ct, props_nom)
            
            cont = {}
            #cont['vcard'] = ct.get_vcard_string()
            cont['nom'] = ct.get_property('file-as')
            cont['dom'] = ct.get_property('home-phone')
            
            adr = ct.get_property('address-home')
            cont['adr'] = adr
            if adr != None:
                pos = str(adr).find('at 0x')
                if pos > 0:
                    cl = ContactAddress.from_address(int(str(adr)[pos + 3:-1],  16))
                    cont['adr'] = []
                    while cl.name != None:
                        cont['adr'].append(str(cl.name))
                        cl = ContactAddress.from_address(addressof(cl.next))
                    #print cont['adr']
            
            cat = ct.get_property('categories')
            cont['cat'] = cat
            if cat != None:
                cont['cat'] = cat.split(',')
            
            liste.append(cont)
        
        return liste
    
    def get_property_names(self):
        names =[]
        for prop in self._contacts[0].props:
            names.append(prop.name)
            #if self._contacts[0].get_property(prop.name) != None:
                #print '  ',  prop.name, ':', self._contacts[0].get_property(prop.name)
        return names
                
ev=Evo()

for p in ev.get_property_names():
    pass
    #print p

for itm in ev.get_contact_list():
    pass
    print itm

sys.exit()
    

name_attributes = [
	"full-name",
	"given-name",
	"family-name",
	"nickname"
]

phone_attributes = [
	"assistant-phone",
	"business-phone",
	"business-phone-2",
	"business-fax",
	"callback-phone",
	"car-phone",
	"company-phone",
	"home-phone",
	"home-phone-2",
	"home-fax",
	"isdn-phone",
	"mobile-phone",
	"other-phone",
	"other-fax",
	"pager",
	"primary-phone",
	"radio",
	"telex",
	"tty",
]

def on_Contact_clicked():
	single_contact = []
	single_contact_numbers = []
	contact_list = []
	phone_list = []
	
	abook = evolution.ebook.open_addressbook("default")
	contacts = abook.get_all_contacts()
	contacts.sort(key=lambda obj: obj.get_name())

	for econtact in contacts:
		#help(econtact)
		single_contact = [econtact.get_property(name_attributes[2]), econtact.get_property(name_attributes[1])]
		for phone_attribute in phone_attributes:
			single_contact_numbers.append(econtact.get_property(phone_attribute))
		contact_list.append(single_contact)
		phone_list.append(single_contact_numbers)
		single_contact = []
		single_contact_numbers = []

	ID = 0
	for contact in contact_list:
		print ID
		print "--> %s, %s" %(contact[0], contact[1])
		print "~~~> %s" %(phone_list[ID][11])
		ID += 1

def on_Contact_clicked2():
    abook = evolution.ebook.open_addressbook("default")
    contacts = abook.get_all_contacts()
    #contacts.sort(key=lambda obj: obj.get_name())
    for econtact in contacts:
        numbers = econtact.get_property('phone')
        print numbers
	#--> <gpointer at 0x1bf4b0>



