DROP TABLE IF EXISTS `tCenta_CCL`;
CREATE TABLE `tCenta_CCL` (
    `ID` int(11) NOT NULL AUTO_INCREMENT,
    `FromDate` date NOT NULL,
    `ToDate` date NOT NULL,
    `CCL_HK` float DEFAULT NULL,
    `CCL_KLN` float DEFAULT NULL,
    `CCL_NTE` float DEFAULT NULL,
    `CCL_NTW` float DEFAULT NULL,
    `CCL_mass` float DEFAULT NULL,
    `CCL_L` float DEFAULT NULL,
    `CCL_SM` float DEFAULT NULL,
    `CCL` float DEFAULT NULL,
    PRIMARY KEY (`ID`),
    UNIQUE KEY `FromDate` (`FromDate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Centa net Data'
