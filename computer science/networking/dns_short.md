# Introduction
Bonjour à tous. Dans cette vidéo, nous allons voir le fonctionnement du
protocole DNS (Domain Name System). Nous examinerons à quoi il sert et comment
il fonctionne. En français, DNS se traduit par « système de nom de domaine ».

Les ordinateurs communiquent via des adresses IP. Pour accéder par exemple à
www.cmaisonneuve.qc.ca, votre ordinateur doit connaître son adresse IP. Le DNS
permet précisément de trouver cette adresse à partir du nom de domaine. C'est en
quelque sorte un annuaire. 

# Serveur récursif
Ainsi, si votre ordinateur ne connaît pas l’adresse IP du Collège, il interroge
un serveur DNS appelé « serveur récursif ». Chaque ordinateur connaît l’adresse
IP d’un serveur récursif, souvent celui de son fournisseur d’accès Internet.

Pour déterminer l’adresse IP, le serveur récursif lit le nom de domaine de
droite à gauche. Chaque partie (.ca, .qc.ca, cmaisonneuve.qc.ca, etc.) est gérée
par un serveur DNS spécifique. Le serveur récursif doit donc commencer par
interroger le serveur DNS du domaine de premier niveau, soit .ca dans notre
exemple. Mais quelle est l’adresse de ce serveur DNS ? Pour le savoir, le
serveur récursif doit consulter un serveur racine. Il en existe treize
dans le monde, leur adresse IP est fixe et connue à l’avance.

Une fois qu'il en obtient l'adresse, le serveur récursif interroge le serveur
DNS du domaine .ca, qui lui fournit l’adresse du serveur DNS s’occupant de
cmaisonneuve.qc.ca. En effet, il est possible qu'un serveur DNS de premier
niveau gère également certains domaines de second niveau comme par exemple
.qc.ca. 

Maintenant que le serveur récursif connaît l’adresse du serveur DNS de
cmaisonneuve.qc.ca, ce dernier lui fournit l'adresse IP du sous-domaine
www.cmaisonneuve.qc.ca. Il est important de comprendre que chaque sous-domaine
peut avoir une adresse IP distincte, car il peut être hébergé sur un serveur
distinct. Au collège par exemple, omnivox.cmaisonneuve.qc.ca pourrait avoir une
adresse IP différente de celle du site web principal.

Enfin, lorsque le serveur récursif obtient l’adresse IP du site recherché il la
retransmet à votre ordinateur.

# Résumé
En résumé, l’organisation des DNS est pyramidale : au sommet, les serveurs
racines, puis ceux des domaines de premier niveau (.ca, .com, etc.), ensuite les
serveurs des domaines de second niveau, et ainsi de suite. Les serveurs
récursifs parcourent cette hiérarchie pour trouver l’adresse IP d’un nom de
domaine. Pour compléter le tout, chaque ordinateur possède l’adresse IP d’un
serveur récursif.

# Conclusion
Voilà, c’est tout pour cette vidéo.