#!/bin/env python
# -*- coding: utf-8 -*-

# evolution-python
# ================
# Home : http://live.gnome.org/Conduit/evolution-python
# Doc  : pydoc evolution.ebook
# Examples : http://talk.maemo.org/showthread.php?t=47840

import evolution
from ctypes import *

_properties = {
    # Property_name: ('object_type', 'description')
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

    # Property_name-sub_property: ('object_type', 'description', sub_property_index)
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
        
# Contact address description (not documented found at [forgotten])
class _ContactAddress(Structure):
    pass
_ContactAddress._fields_ = [("name", c_char_p), 
                  ("next", POINTER(_ContactAddress)), 
                  ("prev", POINTER(_ContactAddress))]

class EDS(object):
    
    """Access Evolution-Data-Server"""
    
    _contacts = None
    _books = None
        
    def _print_all_properties(self):
        """Printing of all properties.
            Useful to creates the table _properties"""
        import gobject
        print "Properties ===================================="
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
        print "Object types =================================="
        print obs
        print
            
    def _load(self):
        
        """Loads the list of all contacts from all address books.
             _contact[] is a list of type ebook.EContact
             with added property:
             'book' which contains the name of the book address"""
        
        if self._contacts == None:
            
            self._contacts = []
        
            # Retrieve all address books
            self.get_books()
            
            # Processing these books
            for book in self._books:
                ob = evolution.ebook.open_addressbook(book[1])
                cts = ob.get_all_contacts()
                for ct in cts:
                    ct.book = book[0]
                    self._contacts.append(ct)
    
    def _get_field(self, ct, prop):
        
        """Returns the value of the property prop <type 'str'> from the 
            contact ct <type 'ebook.EContact'>.
             If a problem occurs or if the property is undefined, this method
             return None or an empty string."""
        
        # Only if the property exists
        if prop not in _properties.keys():
            print "*** Error: property '{0}' unknown".format(prop)
            return None
        
        # Read the property type
        ptyp = _properties[prop][0]
        
        # Processing different types ------------------------------------------
        
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

        """Extract all categories from the contact ct <type 'ebook.EContact'>.
            Return a list of the categories which could be empty."""
        
        cat = ct.get_property('categories')
        if cat == None:
            return []
        return cat.split(',')

    def get_books(self):
        
        """Returns a list of all address books"""
        
        if self._books == None:
        
            # Retrieve all address books
            self._books = evolution.ebook.list_addressbooks()
            
        liste = []
        for book in self._books:
            liste.append(book[0])
        liste.sort()
        return liste

    def get_properties(self):
        
        """Returns a list of tuples.
            Each tuple contains : ('property_name', 'description')"""
        
        liste =[]
        
        for prop in sorted(_properties.iterkeys()):
            liste.append( (prop, _properties[prop][1]) )
            #if ct.get_property(prop.name) != None:
                #print '  ',  prop.name, ':', ct.get_property(prop.name)
        return liste
                
    def get_contact_list(self, cfg={}):
        
        """Returns a list of dictionary containing the selected contacts.
            Each key contains the field name and the value contains the data.
            
            The cfg parameter is a dictionary containing what is wanted in 
                the output. 
            If a key is omitted, a default value is taken (Between parentheses).
            Here are the possible values ​​for the Keys :

            - books = list of address books to include (all).
            - obooks = list of address books to omit (none).
            - cats = list of categories to include (all).
            - ocats = list of categories to be omitted (none).
            - fields = dictionary of fields to return (none).
                Each key is the field name as it will appear in the output list.
                The value is either a string or a list.
                - If it is a string, it represents the name of a property 
                    from the address book which value is used as output.
                - If it is a list it is a list of several properties.
                    In this case, the first property which value is non-empty 
                    is used as output.
        """
        
        self._load()
        liste = []
        
        # Porcessing of all contacts
        # (ct is of type ebook.EContact)
        for ct in self._contacts:
            
            # Only the selected address books
            if 'books' in cfg and ct.book not in cfg['books']:
                continue
        
            # Not the omitted address books
            if 'obooks' in cfg and ct.book in cfg['obooks']:
                continue
            
            # Only the selected categories
            if 'cats' in cfg and  \
                    set(cfg['cats']).isdisjoint(set(self._get_cats(ct))):
                continue
            
            # Not the omitted categories
            if 'ocats' in cfg and \
                    not set(cfg['ocats']).isdisjoint(set(self._get_cats(ct))):
                continue
            
            # Empty output
            cont = {}

            # Processing of the list of the fields to return
            for fld in cfg['fields'].iterkeys():
                
                props = cfg['fields'][fld]
                
                if type(props) == type(str()):
                    cont[fld] = self._get_field(ct, props)
                    
                elif type(props) in (type(tuple()),  type(list())):
                    for prop in props:
                        val = self._get_field(ct, prop)
                        if val != None and val != '':
                            break
                    cont[fld] =  val  # Even if nothing found
            
            liste.append(cont)
        
        return liste
