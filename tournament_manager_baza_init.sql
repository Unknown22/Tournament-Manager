-- phpMyAdmin SQL Dump
-- version 4.5.3.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1:3306
-- Czas generowania: 23 Sty 2016, 16:38
-- Wersja serwera: 5.7.10
-- Wersja PHP: 5.5.9-1ubuntu4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Baza danych: `tournamentmanage`
--


-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `druzyna`
--

CREATE TABLE `druzyna` (
  `Id_druzyny` int(10) NOT NULL,
  `Nazwa` varchar(100) NOT NULL,
  `Ilosc_zawodnikow` int(10) NOT NULL,
  `Id_turnieju` int(10) NOT NULL,
  `Logo` mediumblob
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Wyzwalacze `druzyna`
--

CREATE TRIGGER `add_team_statistics` AFTER INSERT ON `druzyna` FOR EACH ROW insert into statystyki_druzyny values(new.Id_druzyny, 0, 0, 0, 0);

CREATE TRIGGER `delete_team_statistics` BEFORE DELETE ON `druzyna` FOR EACH ROW delete from statystyki_druzyny where Id_druzyny=old.Id_druzyny;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `konto`
--

CREATE TABLE `konto` (
  `Rodzaj_konta` varchar(60) NOT NULL,
  `Uprawnienia_organizatora` bit(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `mecz`
--

CREATE TABLE `mecz` (
  `Id_meczu` int(10) NOT NULL,
  `Wynik` varchar(50) DEFAULT NULL,
  `Data_rozegrania` date DEFAULT NULL,
  `Id_turnieju` int(10) NOT NULL,
  `Id_druzynyI` int(10) NOT NULL,
  `Id_druzynyII` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `statystyki_druzyny`
--

CREATE TABLE `statystyki_druzyny` (
  `Id_druzyny` int(10) NOT NULL,
  `Ilosc_wygranych` int(20) DEFAULT NULL,
  `Ilosc_przegranych` int(20) DEFAULT NULL,
  `Zdobyte_gole_pkt_kille` int(20) DEFAULT NULL,
  `Stracone_gole_pkt_ilosc_zginiec` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `statystyki_zawodnika`
--

CREATE TABLE `statystyki_zawodnika` (
  `Id_zawodnika` int(10) NOT NULL,
  `Zdobyte_gole_pkt_kille` int(20) DEFAULT NULL,
  `Stracone_gole_pkt_ilosc_zginiec` int(20) DEFAULT NULL,
  `Rozegrane_mecze` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `turniej`
--

CREATE TABLE `turniej` (
  `Id_turnieju` int(10) NOT NULL,
  `Ilosc_druzyn` int(10) NOT NULL,
  `Czy_posiada_faze_grupowa` bit(1) NOT NULL,
  `Data_rozpoczecia` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `uzytkownik`
--

CREATE TABLE `uzytkownik` (
  `Id_uzytkownika` int(10) NOT NULL,
  `Nick` varchar(50) NOT NULL,
  `Haslo` varchar(60) NOT NULL,
  `Rodzaj_konta` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `uzytkownik-turniej`
--

CREATE TABLE `uzytkownik-turniej` (
  `Id_turnieju` int(10) NOT NULL,
  `Id_uzytkownika` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `zawodnik`
--

CREATE TABLE `zawodnik` (
  `Id_zawodnika` int(10) NOT NULL,
  `Imie` varchar(60) NOT NULL,
  `Nazwisko` varchar(60) NOT NULL,
  `Pozycja` varchar(70) NOT NULL,
  `Id_druzyny` int(10) DEFAULT NULL,
  `Zdjecie` mediumblob
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Wyzwalacze `zawodnik`
--

CREATE TRIGGER `add_player_statistics` AFTER INSERT ON `zawodnik` FOR EACH ROW insert into statystyki_zawodnika values(new.Id_zawodnika, 0, 0, 0);

CREATE TRIGGER `delete_player_statistics` BEFORE DELETE ON `zawodnik` FOR EACH ROW delete from statystyki_zawodnika where Id_zawodnika=old.Id_zawodnika;

--
-- Indeksy dla zrzutów tabel
--

--
-- Indexes for table `druzyna`
--
ALTER TABLE `druzyna`
  ADD PRIMARY KEY (`Id_druzyny`),
  ADD KEY `Id_turnieju` (`Id_turnieju`);

--
-- Indexes for table `konto`
--
ALTER TABLE `konto`
  ADD PRIMARY KEY (`Rodzaj_konta`);

--
-- Indexes for table `mecz`
--
ALTER TABLE `mecz`
  ADD PRIMARY KEY (`Id_meczu`),
  ADD KEY `Id_turnieju` (`Id_turnieju`),
  ADD KEY `Id_druzynyI` (`Id_druzynyI`) USING BTREE,
  ADD KEY `Id_druzynyII` (`Id_druzynyII`) USING BTREE;

--
-- Indexes for table `statystyki_druzyny`
--
ALTER TABLE `statystyki_druzyny`
  ADD PRIMARY KEY (`Id_druzyny`);

--
-- Indexes for table `statystyki_zawodnika`
--
ALTER TABLE `statystyki_zawodnika`
  ADD PRIMARY KEY (`Id_zawodnika`);

--
-- Indexes for table `turniej`
--
ALTER TABLE `turniej`
  ADD PRIMARY KEY (`Id_turnieju`);

--
-- Indexes for table `uzytkownik`
--
ALTER TABLE `uzytkownik`
  ADD PRIMARY KEY (`Id_uzytkownika`),
  ADD KEY `uzytkownik_ibfk_1` (`Rodzaj_konta`);

--
-- Indexes for table `uzytkownik-turniej`
--
ALTER TABLE `uzytkownik-turniej`
  ADD KEY `FK_ID_TURNIEJU` (`Id_turnieju`),
  ADD KEY `FK_ID_UZYTKOWNIKA` (`Id_uzytkownika`) USING BTREE;

--
-- Indexes for table `zawodnik`
--
ALTER TABLE `zawodnik`
  ADD PRIMARY KEY (`Id_zawodnika`),
  ADD KEY `Id_druzyny` (`Id_druzyny`) USING BTREE;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `druzyna`
--
ALTER TABLE `druzyna`
  ADD CONSTRAINT `druzyna_ibfk_1` FOREIGN KEY (`Id_turnieju`) REFERENCES `turniej` (`Id_turnieju`);

--
-- Ograniczenia dla tabeli `mecz`
--
ALTER TABLE `mecz`
  ADD CONSTRAINT `mecz_ibfk_1` FOREIGN KEY (`Id_turnieju`) REFERENCES `turniej` (`Id_turnieju`),
  ADD CONSTRAINT `mecz_ibfk_2` FOREIGN KEY (`Id_druzynyI`) REFERENCES `druzyna` (`Id_druzyny`),
  ADD CONSTRAINT `mecz_ibfk_3` FOREIGN KEY (`Id_druzynyII`) REFERENCES `druzyna` (`Id_druzyny`);

--
-- Ograniczenia dla tabeli `statystyki_druzyny`
--
ALTER TABLE `statystyki_druzyny`
  ADD CONSTRAINT `statystyki_druzyny_ibfk_1` FOREIGN KEY (`Id_druzyny`) REFERENCES `druzyna` (`Id_druzyny`);

--
-- Ograniczenia dla tabeli `statystyki_zawodnika`
--
ALTER TABLE `statystyki_zawodnika`
  ADD CONSTRAINT `statystyki_zawodnika_ibfk_1` FOREIGN KEY (`Id_zawodnika`) REFERENCES `zawodnik` (`Id_zawodnika`);

--
-- Ograniczenia dla tabeli `uzytkownik`
--
ALTER TABLE `uzytkownik`
  ADD CONSTRAINT `uzytkownik_ibfk_1` FOREIGN KEY (`Rodzaj_konta`) REFERENCES `konto` (`Rodzaj_konta`);

--
-- Ograniczenia dla tabeli `uzytkownik-turniej`
--
ALTER TABLE `uzytkownik-turniej`
  ADD CONSTRAINT `FK_ID_TURNIEJU` FOREIGN KEY (`Id_turnieju`) REFERENCES `turniej` (`Id_turnieju`),
  ADD CONSTRAINT `FK_ID_UZYTKOWNIKA` FOREIGN KEY (`Id_uzytkownika`) REFERENCES `uzytkownik` (`Id_uzytkownika`);

--
-- Ograniczenia dla tabeli `zawodnik`
--
ALTER TABLE `zawodnik`
  ADD CONSTRAINT `zawodnik_ibfk_2` FOREIGN KEY (`Id_druzyny`) REFERENCES `druzyna` (`Id_druzyny`);
