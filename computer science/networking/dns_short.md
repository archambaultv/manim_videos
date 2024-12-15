# Introduction

Bonjour à tous. Nous allons voir dans cette vidéo le fonctionnement du protocole
DNS. DNS signifie Domain Name System, soit système de nom de domaine en
français. Nous allons voir à quoi il sert et comment il fonctionne.

D'abord je vous rappelle que les ordinateurs communiquent entre eux en utilisant
des adresses IP. Si vous désirez, par exemple, vous connecter au site web du
Collège www.cmaisonneuve.qc.ca votre ordinateur doit connaître l'adresse IP de
ce site.

# Serveur récursif
C'est le protocole DNS qui permet justement de trouver l'adresse IP liée à un
nom de domaine. C'est en quelque sorte un annuaire téléphonique pour les
adresses IP. Ainsi, si votre ordinateur ne connaît pas l'adresse IP de
www.cmaisonneuve.qc.ca, il va demander à un serveur DNS appelé serveur récursif.
Tous les ordinateurs connectés à un réseau ont l'adresse IP d'un serveur
récursif, le plus souvent celui de leur fournisseur d'accès à Internet.

Le serveur récursif, pour trouver l'adresse IP du Collège, va lire le
nom de domaine à l'envers, de la droite vers la gauche. Dans notre exemple, la
dernière partie du nom de domaine est .ca. L'idée maîtresse du protocole DNS est
que chaque partie du nom de domaine est gérée par un serveur DNS spécifique.

Ainsi, le serveur récursif va devoir consulter le serveur DNS pour le domaine de
premier niveau .ca. Mais pour savoir l'adresse IP de ce dernier, le serveur
récursif doit d'abord consulter un serveur racine. Il existe treize serveurs
racines dans le monde et leur adresse IP est fixe et connue d'avance. Le serveur
racine indique donc l'adresse IP du serveur DNS pour le domaine .ca.

Ensuite, le serveur récursif va consulter ce serveur DNS spécifique pour les
domaines se terminant en .ca. Ce dernier pourrait indiquer l'adresse IP d'un
serveur DNS spécifique pour les domaines se terminant en .qc.ca. En réalité, il
arrive que le serveur DNS pour le domaine de premier niveau contienne les
informations de certains domaines de deuxième niveau particuliers. C'est le cas
pour le domaine .qc.ca. Donc le serveur récursif reçoit de la part du serveur
DNS pour le domaine .ca l'adresse IP du serveur DNS pour le domaine
cmaisonneuve.qc.ca. 

On pourrait penser ici que c'est l'adresse IP de cmaisonneuve.qc.ca qui devrait
être retournée. Mais en réalité, le nom de domaine du Collège possède plusieurs
sous-domaines. Par exemple, www.cmaisonneuve.qc.ca, omnivox.cmaisonneuve.qc.ca
et bottin.cmaisonneuve.qc.ca. Chacun de ces sous-domaines peut posséder une
adresse IP différente, c'est-à-dire être hébergé sur un serveur différent. C'est
pourquoi le serveur DNS pour le domaine .ca retourne l'adresse IP d'un serveur
DNS pour cmaisonneuve.qc.ca.

Enfin, le serveur récursif va consulter ce dernier serveur DNS spécifique et
obtenir l'adresse IP de www.cmaisonneuve.qc.ca.

# Résumé
En résumé, les serveurs DNS sont une organisation pyramidale. Les serveurs
racines sont au sommet de la pyramide. Ils indiquent l'adresse IP des serveurs
DNS pour les domaines de premier niveau. Ces derniers indiquent l'adresse IP des
serveurs DNS pour les domaines de deuxième niveau, et ainsi de suite. Les
serveurs récursifs ont pour rôle de parcourir cette pyramide pour trouver
l'adresse IP d'un nom de domaine. Pour que le tout soit complet, tel que
mentionné précédemment, chaque ordinateur connecté à un réseau possède l'adresse
IP d'un serveur récursif.

# Conclusion
Voilà, c'est tout pour cette vidéo.
