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

cd ~
mkdir Dev
cd Dev
mkdir max
cd max 
virtualenv -p python3 .
source bin/activate 
pip install Django==2.0.7
mkdir src
cd src
Django-admin createproject max  
