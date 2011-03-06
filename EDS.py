#!/bin/env python
# -*- coding: utf-8 -*-

# Site : http://live.gnome.org/Conduit/evolution-python
# Doc : pydoc evolution.ebook
# Exemples : http://talk.maemo.org/showthread.php?t=47840

import evolution
from ctypes import *

_properties = {
    'file-as': ('gchararray', 'File Under'),
    'book-uri': ('gchararray', 'Book URI'),
    'full-name': ('gchararray', 'Full Name'),
    'given-name': ('gchararray', 'Given Name'),
    'family-name': ('gchararray', 'Family Name'),
    'nickname': ('gchararray', 'Nickname'),
    'email-1': ('gchararray', 'Email 1'),
    'email-2': ('gchararray', 'Email 2'),
    'email-3': ('gchararray', 'Email 3'),
    'email-4': ('gchararray', 'Email 4'),
    'mailer': ('gchararray', 'Mailer'),
    'address-label-home': ('gchararray', 'Home Address Label'),
    'address-label-work': ('gchararray', 'Work Address Label'),
    'address-label-other': ('gchararray', 'Other Address Label'),
    'assistant-phone': ('gchararray', 'Assistant Phone'),
    'business-phone': ('gchararray', 'Business Phone'),
    'business-phone-2': ('gchararray', 'Business Phone 2'),
    'business-fax': ('gchararray', 'Business Fax'),
    'callback-phone': ('gchararray', 'Callback Phone'),
    'car-phone': ('gchararray', 'Car Phone'),
    'company-phone': ('gchararray', 'Company Phone'),
    'home-phone': ('gchararray', 'Home Phone'),
    'home-phone-2': ('gchararray', 'Home Phone 2'),
    'home-fax': ('gchararray', 'Home Fax'),
    'isdn-phone': ('gchararray', 'ISDN'),
    'mobile-phone': ('gchararray', 'Mobile Phone'),
    'other-phone': ('gchararray', 'Other Phone'),
    'other-fax': ('gchararray', 'Other Fax'),
    'pager': ('gchararray', 'Pager'),
    'primary-phone': ('gchararray', 'Primary Phone'),
    'radio': ('gchararray', 'Radio'),
    'telex': ('gchararray', 'Telex'),
    'tty': ('gchararray', 'TTY'),
    'org': ('gchararray', 'Organization'),
    'org-unit': ('gchararray', 'Organizational Unit'),
    'office': ('gchararray', 'Office'),
    'title': ('gchararray', 'Title'),
    'role': ('gchararray', 'Role'),
    'manager': ('gchararray', 'Manager'),
    'assistant': ('gchararray', 'Assistant'),
    'homepage-url': ('gchararray', 'Homepage URL'),
    'blog-url': ('gchararray', 'Blog URL'),
    'categories': ('gchararray', 'Categories'),
    'caluri': ('gchararray', 'Calendar URI'),
    'fburl': ('gchararray', 'Free/Busy URL'),
    'icscalendar': ('gchararray', 'ICS Calendar'),
    'video-url': ('gchararray', 'Video Conferencing URL'),
    'spouse': ('gchararray', "Spouse's Name"),
    'note': ('gchararray', 'Note'),
    'Rev': ('gchararray', 'Last Revision'),
    'name-or-org': ('gchararray', 'Name Or Org'),

    'address-home-pobox': ('EContactAddress', 'Address Home (PO Box)', 1),
    'address-home-line1': ('EContactAddress', 'Address Home (Line 1)', 3),
    'address-home-line2': ('EContactAddress', 'Address Home (Other Lines)', 2),
    'address-home-city': ('EContactAddress', 'Address Home (City)', 4),
    'address-home-state': ('EContactAddress', 'Address Home (State/Province)', 5),
    'address-home-post': ('EContactAddress', 'Address Home (Postcode)', 6),
    'address-home-country': ('EContactAddress', 'Address Home (Country)', 7),
    
    'address_work-pobox': ('EContactAddress', 'Address Work (PO Box)', 1),
    'address_work-line1': ('EContactAddress', 'Address Work (Line 1)', 3),
    'address_work-line2': ('EContactAddress', 'Address Work (Other Lines)', 2),
    'address_work-city': ('EContactAddress', 'Address Work (City)', 4),
    'address_work-state': ('EContactAddress', 'Address Work (State/Province)', 5),
    'address_work-post': ('EContactAddress', 'Address Work (Postcode)', 6),
    'address_work-country': ('EContactAddress', 'Address Work (Country)', 7),
    
    'address_other-pobox': ('EContactAddress', 'Address Other (PO Box)', 1),
    'address_other-line1': ('EContactAddress', 'Address Other (Line 1)', 3),
    'address_other-line2': ('EContactAddress', 'Address Other (Other Lines)', 2),
    'address_other-city': ('EContactAddress', 'Address Other (City)', 4),
    'address_other-state': ('EContactAddress', 'Address Other (State/Province)', 5),
    'address_other-post': ('EContactAddress', 'Address Other (Postcode)', 6),
    'address_other-country': ('EContactAddress', 'Address Other (Country)', 7),
    
    #'category-list': ('gpointer', 'Category List'),
    #'photo': ('EContactPhoto', 'Photo'),
    #'logo': ('EContactPhoto', 'Logo'),
    #'name': ('EContactName', 'Name'),
    #'email': ('gpointer', 'Email List'),
    'wants-html': ('gboolean', 'Wants HTML Mail'),
    'list': ('gboolean', 'List'),
    'list-show-addresses': ('gboolean', 'List Show Addresses'),
    #'birth-date': ('EContactDate', 'Birth Date'),
    #'anniversary': ('EContactDate', 'Anniversary'),
    #'x509Cert': ('EContactCert', 'X.509 Certificate'),
    #'geo': ('EContactGeo', 'Geographic Information'),
    #'phone': ('gpointer', 'Telephone'),
    #'sip': ('gpointer', 'SIP address'),
}

_obj_types = [
    'EContactAddress', 
    'EContactCert', 
    'EContactDate', 
    'EContactGeo', 
    'EContactName', 
    'EContactPhoto', 
    'gboolean', 
    'gchararray', 
    'gpointer'
]


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
        
    def _print_all_properties(self):
        """Impression de toutes les propriétés.
            Permeet de créer le tableau _properties"""
        import gobject
        print "Liste des propriétés =========================="
        ct = evolution.ebook.EContact()
        obt = []
        for prop in gobject.list_properties(ct):
            obt.append(str(prop.value_type).split()[1])
            print "    '{0}': ('{1}', '{2}'),".format(prop.name, 
                      obt[-1], 
                      prop.name.title().replace('-', ' '))
        obs = list(set(obt))
        obs.sort()
        print
        print "Liste des types d'objet ======================="
        print obs
        print
            
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
    
    def _get_field(self, ct, prop):
        
        """Retourne la valeur de la propriété prop <type 'str'> de la fiche du 
            contacte ct <type 'ebook.EContact'>
            Si un problème ou si la propriété est non définie cette fonction
            retourne None ou une chaîne vide."""
        
        # Seulement si la propriété existe
        if prop not in _properties.keys():
            print "*** Erreur: propriété '{0}' inconnue".format(prop)
            return None
        
        # On récupère le type de la propriété
        ptyp = _properties[prop][0]
        
        # Traitement des différents type --------------------------------------
        
        if ptyp == 'gchararray':
            val = ct.get_property(prop)
            if val == None:
                return None
            return val.rstrip()
        
        if ptyp == 'gboolean':
            val = ct.get_property(prop)
            if val == None:
                return None
            return val
        
        if ptyp == 'EContactAddress':
            itm = ct.get_property(prop.rpartition('-')[0])
            if itm == None:
                return None
            pos = str(itm).find('at 0x')
            if pos == 0:
                return None
            cl = _ContactAddress.from_address(int(str(itm)[pos + 3:-1],  16))
            itms = []
            while cl.name != None:
                itms.append(str(cl.name).rstrip())
                cl = _ContactAddress.from_address(addressof(cl.next))
            try:
                return itms[_properties[prop][2]]
            except:
                return None
        
        return None
        
    def _get_cats(self, ct):

        """Extrait la liste des catégories de la fiche du 
            contacte ct <type 'ebook.EContact'>
            Au retour une liste contenant les catégories. 
            Celle-ci peut être vide."""
        
        cat = ct.get_property('categories')
        if cat == None:
            return []
        return cat.split(',')

    def get_books(self):
        
        """Renvoie la liste de tous les carnets d'adresses"""
        
        if self._books == None:
        
            # Extraction de tous les carnets d'adresses
            self._books = evolution.ebook.list_addressbooks()
            
        liste = []
        for book in self._books:
            liste.append(book[0])
        liste.sort()
        return liste

    def get_properties(self):
        
        """Renvoie une liste de tupples
            Chaque tupple contient: ('le nom', 'la description de la propriété')"""
        
        liste =[]
        
        for prop in sorted(_properties.iterkeys()):
            liste.append( (prop, _properties[prop][1]) )
            #if ct.get_property(prop.name) != None:
                #print '  ',  prop.name, ':', ct.get_property(prop.name)
        return liste
                
    def get_contact_list(self, cfg={}):
        
        """Renvoi une liste des contacts.
            La liste est une liste de dictionnaires dont les clés sont les 
            noms des champs et leur contenu la valeur du champ.
            
            le paramètre cfg est un dictionnaire. Si une clé n'est pas 
            présente, une valeur par défaut (entre parenthèse) est prise.
            Voici les clés possibles :
            - books = liste des carnets d'adresse à inclure (tous).
            - obooks = liste des carnets d'adresses à omettre (aucun).
            - cats = liste des catégories à inclure (toutes).
            - ocats = liste des catégories à omettre (aucune).
            - fields = dictionnaire des champs à sortir (aucun).
                Chaque clé est le nom du champ tel qu'il apparaîtra dans la 
                liste en sortie.
                La valeur de la clé est soit une chaîne ou une liste.
                - Si c'est une chaîne, elle représente le nom d'une propriété 
                    du carnet d'adresses.
                - Si c'est une liste, elle contient un ensemble de propriétés. 
                    Dans ce cas, la première propriété non vide est prise.
        """
        
        self._load()
        liste = []
        
        # Traitement de tous les contacts 
        # (un contact ,ct est de type ebook.EContact)
        for ct in self._contacts:
            
            # Que les carnets d'adresses choisis
            if 'books' in cfg and ct.book not in cfg['books']:
                continue
        
            # Pas les carnets d'adresses à omettre
            if 'obooks' in cfg and ct.book in cfg['obooks']:
                continue
            
            # Que les catégories choisies
            if 'cats' in cfg and  \
                    set(cfg['cats']).isdisjoint(set(self._get_cats(ct))):
                continue
            
            # Pas les catégories à omettre
            if 'ocats' in cfg and \
                    not set(cfg['ocats']).isdisjoint(set(self._get_cats(ct))):
                continue
            
            # Init de la sortie
            cont = {}

            # Parcours de la liste des champs à sortir
            for fld in cfg['fields'].iterkeys():
                
                props = cfg['fields'][fld]
                
                if type(props) == type(str()):
                    cont[fld] = self._get_field(ct, props)
                    
                elif type(props) in (type(tuple()),  type(list())):
                    for prop in props:
                        val = self._get_field(ct, prop)
                        if val != None and val != '':
                            break
                    cont[fld] =  val  # Même si rien trouvé
            
            liste.append(cont)
        
        return liste
