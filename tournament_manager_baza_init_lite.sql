
CREATE TABLE [druzyna] ('Id_druzyny' INTEGER NOT NULL PRIMARY KEY, 'Nazwa' TEXT NOT NULL, 'Ilosc_zawodnikow' INTEGER NOT NULL, 'Id_turnieju' INTEGER NOT NULL, 'Logo' BLOB);


CREATE TABLE [konto] ('Rodzaj_konta' TEXT NOT NULL PRIMARY KEY, 'Uprawnienia_organizatora' TEXT NOT NULL);


CREATE TABLE [mecz] ('Id_meczu' INTEGER NOT NULL PRIMARY KEY, 'Wynik' TEXT, 'Data_rozegrania' DATE, 'Id_turnieju' INTEGER NOT NULL, 'Id_druzynyI' INTEGER NOT NULL, 'Id_druzynyII' INTEGER NOT NULL);


CREATE TABLE [statystyki_druzyny] ('Id_druzyny' INTEGER NOT NULL PRIMARY KEY, 'Ilosc_wygranych' INTEGER, 'Ilosc_przegranych' INTEGER, 'Zdobyte_gole_pkt_kille' INTEGER, 'Stracone_gole_pkt_ilosc_zginiec' INTEGER);


CREATE TABLE [statystyki_zawodnika] ('Id_zawodnika' INTEGER NOT NULL PRIMARY KEY, 'Zdobyte_gole_pkt_kille' INTEGER, 'Stracone_gole_pkt_ilosc_zginiec' INTEGER, 'Rozegrane_mecze' INTEGER);


CREATE TABLE [turniej] ('Id_turnieju' INTEGER NOT NULL PRIMARY KEY, 'Ilosc_druzyn' INTEGER NOT NULL, 'Czy_posiada_faze_grupowa' TEXT NOT NULL, 'Data_rozpoczecia' DATE NOT NULL);


CREATE TABLE [uzytkownik] ('Id_uzytkownika' INTEGER NOT NULL PRIMARY KEY, 'Nick' TEXT NOT NULL, 'Haslo' TEXT NOT NULL, 'Rodzaj_konta' TEXT NOT NULL);


CREATE TABLE [uzytkownik-turniej] ('Id_turnieju' INTEGER NOT NULL, 'Id_uzytkownika' INTEGER NOT NULL);


CREATE TABLE [zawodnik] ('Id_zawodnika' INTEGER NOT NULL PRIMARY KEY, 'Imie' TEXT NOT NULL, 'Nazwisko' TEXT NOT NULL, 'Pozycja' TEXT NOT NULL, 'Id_druzyny' INTEGER, 'Zdjecie' BLOB);