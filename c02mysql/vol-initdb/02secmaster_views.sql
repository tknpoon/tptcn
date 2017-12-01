INSERT INTO `exchange`(`abbrev`) VALUES ("HKG");

INSERT INTO `data_vendor`(`name`) VALUES ("yahoo");

CREATE VIEW `vSymbol` AS
 SELECT  e.abbrev exch, s.ticker ticker, s.name name, s.currency currency
 FROM    exchange e
 INNER JOIN symbol s ON (s.exchange_id = e.id);  

INSERT INTO `vSymbol`(`exch`, `ticker`, `name`,`currency`) VALUES ("HKG","0001.HK","CKJH","HKD");
