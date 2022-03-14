# Gra survival

Jest to projekt zrobiony na programowanie obiektowe

## Przed Instalacja
By ten projekt działał potrzebny jest [Python](https://www.python.org/)<br>

## Instalacja
Po instalacji Python'a wystarczy zklonować projekt
`git clone https://github.com/patrykzp/gra-prog-obiektowe/ lokalizacja`

Po instalacji pików trzeba wykonać komendę `python -m pip install -r requirements.txt` lub `pip install -r requirements.txt` w folderze gry,
po czym wykonaj komendę `python main.py` lub `./main.py` by włączyć grę, jeżeli gra sie nie odpali na linuxie, trzeba wykonać komende `chmod +x main.py` 

## Cel gry

Przetrwaj

# Struktura gry

## Klasy

- klasa Game, odpowiedzialna za wyświetlanie wszystkich obiektów, przechowywanie globalnych obiektów, generowanie terenu oraz rozpoczęcie gry
 
- klasa Input, odpowiedzialna za pobieranie wartości od gracza

- klasa Menu, podstawa dla reszty innych scen. Jej obiekt w metodzie start() tworzy wszystkie elementy UI danej sceny 

- klasa Renderable, podstawowa klasa która powoduje. że dany obiekt MOŻE być renderowany, nadaje podstawowe atrybuty i metody:
  1. `update()` odpowiedzialną za ustawianie pozycji i rotacji, jest ona aktywowana co klatke
  2. `setImage(obrazek pygame)` ustawia sprite obiektu

- klasa Object, podstawowa klasa dziedzicząca od Renderable której instacją jest obiekt w grze który ma byc wyświetlany przez kamerę
posiada pozycje, rozmiar, rotacje, obrazek, referencje do obiektu Gry oraz metody
  1. `getLookAngle(pos_x,pos_y)` zwraca rotacje potrzebna dla obiektu żeby był zwrócony w strone danej pozycji
  2. `getFacingToVector(pos_x,pos_y)` zwraca kierunek w postaci pozycji x i pozycji y w strone danej pozycji
  3. `checkCollide(collider)` zwraca True/False w zależności czy dany obiekt koliduje z colliderem

- klasa Character, klasa dziedzicząca od Object, której zadaniem jest bycie podstawą dla każdego obiektu który posiada życie

- klasa Player, klasa dziedzicząca od Character, obiektem tej klasy steruje gracz, obsluguje ona poruszanie się oraz zwracanie się w strone myszki

- klasa NPC, klasa dziedzicząca od Character, obiekty tej klasy to przyjazne NPC które chodzą po mapce

- klasa Obstacle, klasa dziedzicząca od Object, której zadaniem jest bycie podstawą dla każdej przeszkody

- klasa UIObject, podstawowa klasa dziedzicząca od Renderable, której zadaniem jest bycie podstawą dla każdego elementu UI

- klasy IronOre, Tree, MineableRock oraz AppleTree dziedziczą od klasy Obstacle, każda z nich posiada inną metode `takeDamage(damage)` która odpowiedzialna jest za interakcje z obiektem 

- klasa Text, klasa dziedzicząca od UIObject, której obiekt wyświetla tekst, posiada metode `changeText(tekst)` która pozwala zmienić tekst tego obiektu.

- klasa Bar, klasa dziedzicząca od UIObject, której obiekt jest paskiem progressu, w zależności od atrybutu `progress` pasek wypełnia się (od 0 do 1)

- klasa Button, klasa dziedzicząca od UIObject, której obiekt jest przyciskiem, metodę onClick() można nadpisać na inną funkcje która bedzię się aktywować po kliknięciu w przycisk
