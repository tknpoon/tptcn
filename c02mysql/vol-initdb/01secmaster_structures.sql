CREATE TABLE `tVendor` (
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`name`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `tSymbol` (
  `symbol` varchar(15) NOT NULL,
  `preferredVendor` varchar(10) NULL,
  `availVendors` varchar(30) NULL,
  `currency` varchar(10) NULL,
  `name` varchar(255) NULL, 
  PRIMARY KEY (`symbol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `tDailyPrice` (
  `vendorName` varchar(10) NOT NULL,
  `symbol` varchar(15) NOT NULL,
  `priceDate` datetime NOT NULL,
  `openPrice` decimal(19,4) NULL,
  `highPrice` decimal(19,4) NULL,
  `lowPrice` decimal(19,4) NULL,
  `closePrice` decimal(19,4) NULL,
  `volume` bigint NULL,
  `adjClosePrice` decimal(19,4) NULL,
  PRIMARY KEY (`symbol`,`priceDate`,`vendorName`),
  KEY `index_vendor` (`vendorName`),
  KEY `index_symbol` (`symbol`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `tDailyPrice_yahoo` (
  `symbol` varchar(15) NOT NULL,
  `Date` datetime NOT NULL,
  `Open` decimal(19,4) NULL,
  `High` decimal(19,4) NULL,
  `Low` decimal(19,4) NULL,
  `Close` decimal(19,4) NULL,
  `Adj Close` decimal(19,4) NULL,
  `Volume` bigint NULL,
  PRIMARY KEY (`symbol`,`Date`),
  KEY `index_symbol` (`symbol`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE VIEW `vDaily` AS
  SELECT d.`symbol` AS `symbol`,
    d.`priceDate` AS `date`,
    d.`openPrice` AS `open`,
    d.`highPrice` AS `high`,
    d.`lowPrice` AS `low`,
    d.`closePrice` AS `close`,
    d.`volume` AS `volume` 
  FROM  `tDailyPrice` d 
  INNER JOIN `tSymbol` s ON (s.preferredVendor = d.vendorName AND s.symbol = d.symbol);

CREATE PROCEDURE `pDaily`(IN `symbol` VARCHAR(15))
 SELECT * FROM vDaily
  WHERE vDaily.symbol = symbol
