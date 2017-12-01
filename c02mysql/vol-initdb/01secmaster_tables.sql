CREATE TABLE `tVendor` (
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`name`) 
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE `tSymbol` (
  `symbol` varchar(15) NOT NULL,
  `name` varchar(255) NULL, 
  `currency` varchar(32) NULL,
  `preferredVendor` varchar(10) NULL,
  PRIMARY KEY (`symbol`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE `tDailyPrice` (
  `vendorName` varchar(10) NOT NULL,
  `symbol` varchar(15) NOT NULL,
  `priceDate` datetime NOT NULL,
  `openPrice` decimal(19,4) NULL,
  `highPrice` decimal(19,4) NULL,
  `lowPrice` decimal(19,4) NULL,
  `closePrice` decimal(19,4) NULL,
  `volume` bigint NULL,
  PRIMARY KEY (`symbol`,`priceDate`,`vendorName`),
  KEY `index_vendor` (`vendorName`),
  KEY `index_symbol` (`symbol`) 
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

