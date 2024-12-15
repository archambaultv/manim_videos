# Introduction

Bonjour à tous. Nous allons voir dans cette vidéo le fonctionnement du protocole
DNS. Nous allons voir à quoi il sert et comment il fonctionne. 

D'abord je vous rappelle que les ordinateurs communiquent entre eux en utilisant
des adresses IP. Ces adresses sont des suites de chiffres qui permettent
d'identifier un ordinateur sur un réseau. La question est donc de savoir comment
fait-on pour connaître l'adresse IP d'un ordinateur ? Par exemple, quelle est
l'adresse IP du Collège de Maissoneuve ?

# Résolution de noms
Il faut donc une manière de traduire un nom de domaine comme cmaisonneuve.qc.ca
en une adresse IP. C'est là que le protocole DNS entre en jeu. DNS signifie
Domain Name System, soit système de noms de domaine en français. Son
fonctionnement va comme suit. Chaque ordinateur connecté à un réseau possède
l'addresse IP d'un serveur DNS. Ce serveur, appelé serveur récursif, joue un
rôle de détective. Lorsqu'on lui demande l'adresse IP d'un nom de domaine, il va
chercher l'information pour nous. Si ce serveur connaît l'adresse IP
correspondante, il la retourne. C'est souvent le cas pour les sites web
populaires, comme YouTube par exemple. Sinon, il va lire le nom de domaine à
l'envers, de la droite vers la gauche. Pour chaque partie du nom de domaine, le
serveur récursif va consulté un autre serveur DNS, spécialisé dans cette partie
du nom de domaine.

Par exemple, pour trouver l'adresse IP cmaisonneuve.qc.ca, le serveur récursif
va d'abord consulter un des treize serveurs racines. Ces serveurs racines
contiennent les adresses des serveurs DNS pour les domaines de premier niveau, soit .ca dans
notre cas. Le serveur racine va donc indiquer au serveur récursif l'adresse du
serveur DNS pour le domaine .ca. 

Ensuite, le serveur récursif va ensuite consulter ce serveur DNS, appelé serveur
de domaine de premier niveau. En théorie, ce serveur va indiquer au serveur
récursif l'adresse du serveur DNS pour le domaine qc.ca. En pratique, il se trouve
que le serveur DNS pour le domaine qc.ca est souvent même que pour le domaine .ca et il 
va donc indiquer l'adresse du serveur DNS pour le domaine cmaisonneuve.qc.ca.

Enfin, le serveur récursif va consulter ce dernier serveur DNS pour obtenir
l'adresse IP de cmaisonneuve.qc.ca.

# Conclusion
