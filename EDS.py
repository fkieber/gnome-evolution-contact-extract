#!/bin/env python
# -*- coding: utf-8 -*-

# Site : http://live.gnome.org/Conduit/evolution-python
# Doc : pydoc evolution.ebook
# Exemples : http://talk.maemo.org/showthread.php?t=47840

import evolution
from ctypes import *

def _print_properties(contact, prop_list):
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
class _ContactAddress(Structure):
    pass
_ContactAddress._fields_ = [("name", c_char_p), 
                  ("next", POINTER(_ContactAddress)), 
                  ("prev", POINTER(_ContactAddress))]
                  #voir s'il n'y a pas un prev ???

class EDS(object):
    
    """Accès à Evolution-Data-Server"""
    
    _contacts = None
    _books = None
        
    def _load(self):
        
        """Charge la liste de tous les contact 
            de tous les carnets d'adresses.
            _contact[] sera une liste du type ebook.EContact
            avec une propritété suplémentaire :
            'book' qui contient le nom du carnet du contact"""
        
        if self._contacts == None:
            
            self._contacts = []
        
            # Extraction de tous les carnets d'adresses
            self.get_books()
            
            # Traitement de ceux-ci
            for book in self._books:
                ob = evolution.ebook.open_addressbook(book[1])
                cts = ob.get_all_contacts()
                for ct in cts:
                    ct.book = book[0]
                    self._contacts.append(ct)
    
    def get_books(self):
        
        """Renvoie la liste de tous les carnets d'adresses"""
        
        if self._books == None:
        
            # Extraction de tous les carnets d'adresses
            self._books = evolution.ebook.list_addressbooks()
            
        liste = []
        for book in self._books:
            liste.append(book[0])
        
        return liste

    def get_properties(self):
        
        """Renvoie une liste avec toutes propriétés possibles"""
        
        names =[]
        
        # Attention ceci peut créer dans le carnet par défaut, un contacte vide
        # avec juste le surnom rempli avec le nom du profil en cours !!!
        ct = evolution.ebook.get_self_contact()
        
        for prop in ct.props:
            names.append(prop.name)
            #if ct.get_property(prop.name) != None:
                #print '  ',  prop.name, ':', ct.get_property(prop.name)
        return names
                
    def get_contact_list(self):
        
        self._load()
        liste = []
    
        # Traitement de tous les contacts 
        # (un contact ,ct est de type ebook.EContact)
        for ct in self._contacts:
        
            #_print_properties(ct, props_nom)
            
            cont = {}
            #cont['vcard'] = ct.get_vcard_string()
            cont['book'] = ct.book
            cont['id'] = ct.get_property('id')
            cont['nom'] = ct.get_property('file-as')
            cont['dom'] = ct.get_property('home-phone')
            
            adr = ct.get_property('address-home')
            cont['adr'] = adr
            if adr != None:
                pos = str(adr).find('at 0x')
                if pos > 0:
                    cl = _ContactAddress.from_address(int(str(adr)[pos + 3:-1],  16))
                    cont['adr'] = []
                    while cl.name != None:
                        cont['adr'].append(str(cl.name))
                        cl = _ContactAddress.from_address(addressof(cl.next))
                    #print cont['adr']
            
            #cat = ct.get_property('category-list')
            cat = ct.get_property('categories')
            cont['cat'] = cat
            if cat != None:
                cont['cat'] = cat.split(',')
                #pos = str(cat).find('at 0x')
                #if pos > 0:
                    #cl = _ContactAddress.from_address(int(str(cat)[pos + 3:-1],  16))
                    #cont['cat'] = []
                    #while cl.name != None:
                        #cont['cat'].append(str(cl.name))
                        #cl = _ContactAddress.from_address(addressof(cl.next))
            
            liste.append(cont)
        
        return liste
