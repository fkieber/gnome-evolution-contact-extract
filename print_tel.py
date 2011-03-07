#!/bin/env python
# -*- coding: utf-8 -*-

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

import sys
from EDS import EDS

# Table des carnets d'adresses exclus
excl_addrs_books = [
    'Envoyés', 
    'temp', 
]

# Liste des catégories à exclure
excl_cats = [
    'no_print', 
]

# Propriétés pour le nom par ordre de priorité
props_nom = [
    'file-as', 
    'name-or-orgs', 
    'full-name', 
    'family-name', 
    'given-name', 
    'nickname', 
]

# Propriétés pour le téléphone du domicile par ordre de priorité
props_dom = [
    'home-phone', 
    'home-phone-2', 
    'primary-phone', 
    'other-phone', 
]

# Propriétés pour le téléphone portable par ordre de priorité
props_port = 'mobile-phone'

# Propriétés pour le téléphone du bureau par ordre de priorité
props_bur = [
    'business-phone', 
    'business-phone-2', 
    'company-phone', 
]

# Propriétés pour l'adresse par ordre de priorité
props_adr_rue = (
    'address-home-line1', 
    'address_work-line1', 
    'address_other-line1', 
)
props_adr_cp = (
    'address-home-post', 
    'address_work-post', 
    'address_other-post', 
)
props_adr_ville = (
    'address-home-city', 
    'address_work-city', 
    'address_other-city', 
)

cfg = {
    'obooks': excl_addrs_books, 
    'ocats': excl_cats, 
    'fields': {
        'nom': props_nom,       # Nom
        'dom': props_dom,       # N° Tél. Domicile
        'port': props_port,     # N° Tél. portable
        'bur': props_bur,       # N° Tél. bureau
        'adr': props_adr_rue,   # Rue de l'adresse
        'cp': props_adr_cp,     # Code postal
        'ville': props_adr_ville, 
        #'test': 'list-show-addresses', 
    }
}

eds=EDS()

#eds._print_all_properties()

print "Liste des carnets d'adresses =================="
for itm in eds.get_books():
    pass
    #print itm
print

print "Liste des propriétés =========================="
for itm in eds.get_properties():
    pass
    #print itm
print

print "Liste des contacts ============================"
liste = eds.get_contact_list(cfg)
liste.sort(key=lambda e: e['nom'].lower())
for itm in liste:
    if itm['dom'] != None or itm['port'] != None or itm['bur'] != None:
        virg = ''
        s = ''
        for col in ('nom', 'dom', 'port', 'bur', 'adr', 'cp', 'ville'):
            if itm[col] == None:
                itm[col] = ''
	    if col == 'ville':
	    	itm[col] = itm[col].upper()
            s += virg + '"' +itm[col] + '"'
            virg = ' '
        print s
