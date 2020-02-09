# max1

Il software serve a gestire liste di ricette, ingredienti e utenti attraverso form da compilare on line, 
da cui si rilevano le seguenti informazioni:

Ricette:
1) nome 
2) tipo 
3) autore 
4) difficoltà 
5) descrizione 
6) immagine allegata
7) ingredienti 
8) nazionalità

Ingredienti:
1) nome
2) calorie 

Utenti:
1) nome 
2) cognome 
3) data di nascita
4) sesso 
5) email 

La procedura di installazione nel terminal e' la seguente:

1) cd ~
2) mkdir Dev
3) cd Dev
4) mkdir max
5) cd max 
6) virtualenv -p python3 .
7) source bin/activate 
8) pip install Django==2.0.7
9) mkdir src
10) cd src
11) Django-admin createproject max  
