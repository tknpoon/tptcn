-- MySQL dump 10.13  Distrib 5.7.20, for Linux (x86_64)
--
-- Host: localhost    Database: secmaster
-- ------------------------------------------------------
-- Server version	5.7.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `secmaster`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `secmaster` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;

USE `secmaster`;

--
-- Table structure for table `tDailyPrice`
--

DROP TABLE IF EXISTS `tDailyPrice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tDailyPrice` (
  `symbol` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `date` datetime NOT NULL,
  `open` decimal(10,3) DEFAULT NULL,
  `high` decimal(10,3) DEFAULT NULL,
  `low` decimal(10,3) DEFAULT NULL,
  `close` decimal(10,3) DEFAULT NULL,
  `volume` bigint(20) DEFAULT NULL,
  `adjClose` decimal(10,3) DEFAULT NULL,
  PRIMARY KEY (`symbol`,`date`),
  KEY `index_symbol` (`symbol`) USING BTREE,
  KEY `index_Date` (`date`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tHKEX_Quotation`
--

DROP TABLE IF EXISTS `tHKEX_Quotation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tHKEX_Quotation` (
  `symbol` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `Date` datetime NOT NULL,
  `Name` varchar(25) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Currency` varchar(3) COLLATE utf8_unicode_ci DEFAULT NULL,
  `PrevClose` decimal(10,3) DEFAULT NULL,
  `High` decimal(10,3) DEFAULT NULL,
  `Low` decimal(10,3) DEFAULT NULL,
  `Close` decimal(10,3) DEFAULT NULL,
  `Bid` decimal(10,3) DEFAULT NULL,
  `Ask` decimal(10,3) DEFAULT NULL,
  `Volume` bigint(20) DEFAULT NULL,
  `Turnover` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`symbol`,`Date`),
  KEY `index_symbol` (`symbol`),
  KEY `index_date` (`Date`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tHKEX_Sales`
--

DROP TABLE IF EXISTS `tHKEX_Sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tHKEX_Sales` (
  `symbol` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `Date` datetime NOT NULL,
  `Serial` varchar(7) COLLATE utf8_unicode_ci NOT NULL,
  `Flag` varchar(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Price` decimal(10,3) DEFAULT NULL,
  `Volume` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`symbol`,`Date`,`Serial`),
  KEY `index_symbol_date` (`symbol`,`Date`),
  KEY `index_symbol` (`symbol`),
  KEY `index_date` (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tHKMA`
--

DROP TABLE IF EXISTS `tHKMA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tHKMA` (
  `Date` datetime NOT NULL,
  `CertIndebtAfterDisc` int(11) DEFAULT NULL,
  `CertIndebtBeforeDisc` int(11) DEFAULT NULL,
  `GovtCirAfterDisc` int(11) DEFAULT NULL,
  `GovtCirBeforeDisc` int(11) DEFAULT NULL,
  `CloseAggBalAfterDisc` int(11) DEFAULT NULL,
  `CloseAggBalBeforeDisc` int(11) DEFAULT NULL,
  `OutstandEFNAfterDisc` int(11) DEFAULT NULL,
  `OutstandEFNBeforeDisc` int(11) DEFAULT NULL,
  `OutstandEFNBankAfterDisc` int(11) DEFAULT NULL,
  `OutstandEFNBankBeforeDisc` int(11) DEFAULT NULL,
  `Total` int(11) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tSymbol`
--

DROP TABLE IF EXISTS `tSymbol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tSymbol` (
  `symbol` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `preferredVendor` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `availVendors` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `currency` varchar(3) COLLATE utf8_unicode_ci DEFAULT NULL,
  `name` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`symbol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tSymbolMeta`
--

DROP TABLE IF EXISTS `tSymbolMeta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tSymbolMeta` (
  `symbol` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `type` varchar(10) COLLATE utf8_unicode_ci NOT NULL COMMENT 'source / split / dividend / rename',
  `date` datetime NOT NULL COMMENT 'startDate for source / exDate for dividend / eventDate for others',
  `vendor` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'for source',
  `code` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'for source',
  `endDate` datetime DEFAULT NULL COMMENT 'source',
  `value` decimal(10,3) DEFAULT NULL COMMENT 'split ratio / dividend',
  PRIMARY KEY (`symbol`,`type`,`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tTR_Daily`
--

DROP TABLE IF EXISTS `tTR_Daily`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tTR_Daily` (
  `symbol` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `Date` datetime NOT NULL,
  `Open` decimal(10,3) DEFAULT NULL,
  `High` decimal(10,3) DEFAULT NULL,
  `Low` decimal(10,3) DEFAULT NULL,
  `Close` decimal(10,3) DEFAULT NULL,
  `Volume` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`symbol`,`Date`),
  KEY `index_symbol` (`symbol`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tVendor`
--

DROP TABLE IF EXISTS `tVendor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tVendor` (
  `name` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tYAHOO_Daily`
--

DROP TABLE IF EXISTS `tYAHOO_Daily`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tYAHOO_Daily` (
  `symbol` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `Date` datetime NOT NULL,
  `Open` decimal(10,3) DEFAULT NULL,
  `High` decimal(10,3) DEFAULT NULL,
  `Low` decimal(10,3) DEFAULT NULL,
  `Close` decimal(10,3) DEFAULT NULL,
  `Adj Close` decimal(10,3) DEFAULT NULL,
  `Volume` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`symbol`,`Date`),
  KEY `index_symbol` (`symbol`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping routines for database 'secmaster'
--
/*!50003 DROP PROCEDURE IF EXISTS `pDaily` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`tpuser`@`%` PROCEDURE `pDaily`(IN `symbol` VARCHAR(15))
SELECT * FROM tDailyPrice
  WHERE tDailyPrice.symbol = symbol ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `pHKEXquote` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8_unicode_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`tpuser`@`%` PROCEDURE `pHKEXquote`(IN `fromdate` DATETIME, IN `todate` DATETIME)
    NO SQL
    COMMENT 'Replace HKEX Quotes H,L,C to tDailyPrice based on tSymbolMeta'
REPLACE INTO tDailyPrice (symbol,date,open,high,low,close,volume)
    SELECT
        t2.symbol,
        q.Date as date,
        IF(q.PrevClose > q.High, q.High, IF(q.PrevClose < q.Low, q.Low, q.PrevClose)) as open,
        q.High as high,
        q.Low as low,
        q.Close as close,
        q.Volume as volume
    FROM
      tHKEX_Quotation q,
      (
        SELECT
          symbol,
          code,
          IFNULL(Date,DATE(NOW())) AS startDate,
          IFNULL(endDate,DATE(NOW())) AS endDate
        FROM tSymbolMeta
        WHERE type='source'
          AND vendor='hkex'
      ) t2
    WHERE q.Date >= `fromdate` AND q.Date <= `todate`
      AND q.symbol = t2.code
      AND q.Date >= t2.startDate
      AND q.Date <= t2.endDate ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `pHKEXupdateOpen` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8_unicode_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`tpuser`@`%` PROCEDURE `pHKEXupdateOpen`(IN `fromdate` DATETIME, IN `todate` DATETIME)
    NO SQL
    COMMENT 'Replace HKEX first Trade as Open to tDailyPrice'
UPDATE
  tDailyPrice dest,
  (
    SELECT
      tmeta.symbol,
      topen.Date as date,
      topen.Price as open
    FROM
      (
        SELECT s1.symbol, s1.date, s1.Price
        FROM
          tHKEX_Sales s1
          JOIN (SELECT symbol, Date, MIN(Serial) as Serial
                  FROM tHKEX_Sales
                  WHERE 1
                    AND tHKEX_Sales.Date >= `fromdate` AND tHKEX_Sales.Date <= `todate`
                    AND tHKEX_Sales.Flag NOT IN ('P','M','D','C')
                  GROUP BY symbol, Date
          ) s2
          ON s1.symbol = s2.symbol
          AND s1.Date = s2.Date
          AND s1.Serial = s2.Serial
      ) topen,
      (
        SELECT
          symbol,
          code,
          IFNULL(Date,DATE(NOW())) AS startDate,
          IFNULL(endDate,DATE(NOW())) AS endDate
        FROM tSymbolMeta
        WHERE 1
          AND type='source'
          AND vendor='hkex'
      ) tmeta
    WHERE 1
      AND topen.symbol = tmeta.code
      AND topen.date >= tmeta.startDate
      AND topen.date <= tmeta.endDate
  ) src
SET dest.open = src.open
WHERE dest.symbol = src.symbol
  AND dest.date = src.date ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-21 21:22:09
