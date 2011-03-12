#Extraction/Affichage/Impression des contacts gnome/evolution.

###Dépendances
[dev-python/evolution-python](http://live.gnome.org/Conduit/evolution-python)

###Description
Extraction/Affichage/Impression des contacts de gnome/evolution.

Pour l’instant, seul la génération d’une liste de contacts au
format "CSV" est supportée.

- La configuration se fait dans le source "print_tel.py".
- On peut choisir plusieurs carnets d’adresses à traiter ou à omettre.
- On peut choisir plusieurs catégories pour inclure ou exclure des contacts.
- On peut choisir les champs à extraire.
- Chaque champ peut provenir de plusieurs propriétés du contact.
  Dans ce cas, c’est la première propriété renseignée qui est prise.

###A Faire :

- Une interface graphique permettant de configurer une extraction.
- Sauvegarde d’une extraction.
- Affichage des données extraites.
- Impression des données extraites.

###Licence
Voir le fichier LICENCE