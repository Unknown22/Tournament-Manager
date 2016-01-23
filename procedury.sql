#
CREATE DEFINER=`tournament`@`%` PROCEDURE `update_player_statistics` (`id_zaw` INT(10), `zdob_gole` INT(10), `str_gole` INT(10))  begin
	set @zaw=(select id_zawodnika from statystyki_zawodnika where id_zawodnika=id_zaw);
	if @zaw is not null then
		update statystyki_zawodnika set Rozegrane_mecze=Rozegrane_mecze+1 where id_zawodnika=@zaw;
		update statystyki_zawodnika set Zdobyte_gole_pkt_kille=Zdobyte_gole_pkt_kille+zdob_gole where id_zawodnika=@zaw;
		update statystyki_zawodnika set Stracone_gole_pkt_ilosc_zginiec=Stracone_gole_pkt_ilosc_zginiec+str_gole where id_zawodnika=@zaw;
	end if;
end;
#
CREATE DEFINER=`tournament`@`%` PROCEDURE `update_team_statistics` (`id_druz` INT(10), `czy_wygrana` INT(1), `zdob_gole` INT(10), `str_gole` INT(10))  begin
	set @druz=(select id_druzyny from statystyki_druzyny where id_druzyny=id_druz);
	if @druz is not null then
		if czy_wygrana=1 then
			update statystyki_druzyny set Ilosc_wygranych=Ilosc_wygranych+1 where Id_druzyny=@druz;
		else
			update statystyki_druzyny set Ilosc_przegranych=Ilosc_przegranych+1 where Id_druzyny=@druz;
		end if;
		update statystyki_druzyny set Zdobyte_gole_pkt_kille=Zdobyte_gole_pkt_kille+zdob_gole where Id_druzyny=@druz;
		update statystyki_druzyny set Stracone_gole_pkt_ilosc_zginiec=Stracone_gole_pkt_ilosc_zginiec+str_gole where Id_druzyny=@druz;
	end if;
end;
#