DROP TABLE IF EXISTS `tTest`;
CREATE TABLE `tTest` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Date` date NOT NULL,
  `symbol` VARCHAR(10) NULL,
  `a` bigint(20) DEFAULT NULL,
  `b` bigint(20) DEFAULT NULL,
  `c` bigint(20) DEFAULT NULL,
  `d` bigint(20) DEFAULT NULL,
  PRIMARY KEY (ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
COMMIT;
