--
-- Wyzwalacze `druzyna`
--

CREATE TRIGGER add_team_statistics AFTER INSERT
ON druzyna
BEGIN
	FOR EACH ROW insert into statystyki_druzyny values(new.Id_druzyny, 0, 0, 0, 0)
END;

CREATE TRIGGER `delete_team_statistics` BEFORE DELETE ON `druzyna` BEGIN FOR EACH ROW delete from statystyki_druzyny where Id_druzyny=old.Id_druzyny END;

--
-- Wyzwalacze `zawodnik`
--

CREATE TRIGGER `add_player_statistics` AFTER INSERT ON `zawodnik` FOR EACH ROW insert into statystyki_zawodnika values(new.Id_zawodnika, 0, 0, 0);

CREATE TRIGGER `delete_player_statistics` BEFORE DELETE ON `zawodnik` FOR EACH ROW delete from statystyki_zawodnika where Id_zawodnika=old.Id_zawodnika;

