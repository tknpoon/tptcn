CREATE TABLE `tVendor` (
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`name`) 
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE `tSymbol` (
  `symbol` varchar(15) NOT NULL,
  `name` varchar(255) NULL, 
  `currency` varchar(32) NULL,
  PRIMARY KEY (`symbol`),
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE `tDailyPrice` (
  `vendor_name` varchar(10) NOT NULL,
  `symbol` varchar(15) NOT NULL,
  `price_date` datetime NOT NULL,
  `open_price` decimal(19,4) NULL,
  `high_price` decimal(19,4) NULL,
  `low_price` decimal(19,4) NULL,
  `close_price` decimal(19,4) NULL,
  `volume` bigint NULL,
  PRIMARY KEY (`symbol`,`price_date`,`vendor_name`),
  KEY `index_vendor` (`vendor_name`),
  KEY `index_symbol` (`symbol`) 
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

