#!/bin/env python
# -*- coding: utf-8 -*-

# Site : http://live.gnome.org/Conduit/evolution-python
# Doc : pydoc evolution.ebook
# Exemples : http://talk.maemo.org/showthread.php?t=47840

"""
Imprime le carnet d'adresse sous forme de liste téléphonique.
Colonnes imprimées :
    Nom
    Domicile (téléphone)
    Portable
    Bureau (téléphone)
    Adresse
    Code postal
    Ville
Tri par nom
Exclusion des entrées ayant la catégorie 'no_print'
Exclusion des entrées sans téléphone (Domicile, Portable ou bureau)
"""

import evolution, sys

class Evo(object):
    
    liste = []
    
    def __init__(self):
        
        # Extraction de tous les carnets d'adresses
        self._books = evolution.ebook.list_addressbooks()
        
        # Traitement de ceux-ci
        for book in self._books:
            print "Carnet d'adresse : {0}".format(book[0])
            ob = evolution.ebook.open_addressbook(book[1])
            cts = ob.get_all_contacts()
            
            # Traitement de tous les contacts
            for ct in cts:
                cont = {}
                cont['nom'] = ct.get_property('full-name')
                cont['dom'] = ct.get_property('home-phone')
                self.liste.append(cont)
                
        print self.liste
                
    
eee=Evo()
    
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



