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

# Table des carnets d'adresses concernés
addrs_books = [
    'Personnel', 
    'Professionnel', 
    'Emploi', 
    'Vériité', 
    'Informatique', 
    'Médical', 
    'Services', 
    'ETIC', 
    'Resto', 
    'Administratif', 
    'Shoping', 
    'Personnalitees', 
    'Educ', 
    'System-U', 
    'C470IP', 
]

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

eds=EDS()

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
for itm in eds.get_contact_list():
    pass
    if itm['book'] in addrs_books:
        print itm
print
