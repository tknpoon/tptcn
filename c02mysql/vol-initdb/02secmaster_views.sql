INSERT INTO `tVendor`(`name`) VALUES ("yahoo");
INSERT INTO `tVendor`(`name`) VALUES ("hkex");
INSERT INTO `tVendor`(`name`) VALUES ("hkma");

INSERT INTO `tSymbol`(`symbol`, `preferredVendor`) VALUES ("0001.HK", "yahoo");
INSERT INTO `tSymbol`(`symbol`, `preferredVendor`) VALUES ("0002.HK", "yahoo");

INSERT INTO `tDailyPrice` (`vendorName`, `symbol`, `priceDate`, `openPrice`, `highPrice`, `lowPrice`, `closePrice`, `volume`)
  VALUES ("yahoo", "0002.HK", "2017-12-01", 1,2,0,2,20);

CREATE VIEW `vDaily` AS
  SELECT d.`symbol` AS `symbol`,
    d.`priceDate` AS `date`,
    d.`openPrice` AS `open`,
    d.`highPrice` AS `high`,
    d.`lowPrice` AS `low`,
    d.`closePrice` AS `close`,
    d.`volume` AS `volume` 
  FROM  `tDailyPrice` d 
  JOIN `tSymbol` s ON (s.preferredVendor = d.vendorName);
