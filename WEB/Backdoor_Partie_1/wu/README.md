# Solution
Il faut voir qu'il y a un port udp ouvert chelou
quand on envoie un paquet udp, on recoit une chaine en b64
Une fois décodé, on se rend compte qu'il faut se connecter
on se connecte en envoyant le mot de passe "hackday" encodé en base64
Une fois cela fait, on peut utiliser des commandes dans le docker, tout en mettant en base64 les commandes
sauf que au bout de 2 secs, on doit a nouveau s'authentifier
donc il faut scripter l'auth et les commandes pour comprendre ou aller
le flag est dans /root, et on est root

# Solution
You have to see that there is a strange open udp port
when we send an udp packet, we receive a b64 string
Once decoded, we realize that we have to connect
we connect by sending the password "hackday" encoded in base64
Once this is done, we can use commands in the docker, while putting the commands in base64
except that after 2 sec, we have to authenticate again
so you have to script the auth and the commands to understand where to go
the flag is in /root, and we are root

