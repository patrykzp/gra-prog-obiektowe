# Gra survival

Jest to projekt zrobiony na programowanie obiektowe

## Przed Instalacja
By ten projekt działał potrzebny jest [python](https://www.python.org/)<br>
Dla pewności wymagana jest wersja pythona 3.8

## Instalacja
Po instalacji pygame wystarczy zklonować projekt
`git clone https://github.com/patrykzp/gra-prog-obiektowe/ (lokalizacja)`

## Cel gry

Przetrwaj

# Struktura gry

## Klasy

- klasa Game, odpowiedzialna za wyświetlanie wszystkich obiektów i przechowywanie globalnych obiektów

- klasa Input, odpowiedzialna za pobieranie wartości od gracza

- klasa Object, podstawowa klasa dla każdego obiektu w grze który ma byc wyświetlany
posiada pozycje, rozmiar, rotacje, obrazek, referencje do obiektu Gry oraz metody
1. `update()` odpowiedzialną za ustawianie pozycji i rotacji, jest ona aktywowana co klatke
2. `setImage(obrazek pygame)` ustawia sprite obiektu
3. `getLookAngle(pos_x,pos_y)` zwraca rotacje potrzebna dla obiektu żeby był zwrócony w strone danej pozycji

- klasa Character, klasa dziedzicząca od Obiektu której zadaniem jest bycie podstawą dla każdego obiektu który posiada życie

- klasa Player, klasa dziedzicząca od Character, obiektem tej klasy steruje gracz, obsluguje ona poruszanie się oraz zwracanie się w strone myszki

- klasa NPC, klasa dziedzicząca od Character, obiekty tej klasy to przyjazne NPC które chodzą po mapce

- klasa Obstacle, klasa dziedzicząca od Obiektu której zadaniem jest bycie podstawą dla każdej przeszkody
