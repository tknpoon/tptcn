
--
-- Table structure for table `tDailyPrice`
--

DROP TABLE IF EXISTS `tDailyPrice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tDailyPrice` (
  `vendorName` varchar(10) NOT NULL,
  `symbol` varchar(10) NOT NULL,
  `priceDate` datetime NOT NULL,
  `openPrice` decimal(10,3) DEFAULT NULL,
  `highPrice` decimal(10,3) DEFAULT NULL,
  `lowPrice` decimal(10,3) DEFAULT NULL,
  `closePrice` decimal(10,3) DEFAULT NULL,
  `volume` bigint(20) DEFAULT NULL,
  `adjClosePrice` decimal(10,3) DEFAULT NULL,
  PRIMARY KEY (`symbol`,`priceDate`,`vendorName`),
  KEY `index_vendor` (`vendorName`),
  KEY `index_symbol` (`symbol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tDailyPrice_yahoo`
--

DROP TABLE IF EXISTS `tDailyPrice_yahoo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tDailyPrice_yahoo` (
  `symbol` varchar(10) NOT NULL,
  `Date` datetime NOT NULL,
  `Open` decimal(10,3) DEFAULT NULL,
  `High` decimal(10,3) DEFAULT NULL,
  `Low` decimal(10,3) DEFAULT NULL,
  `Close` decimal(10,3) DEFAULT NULL,
  `Adj Close` decimal(10,3) DEFAULT NULL,
  `Volume` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`symbol`,`Date`),
  KEY `index_symbol` (`symbol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tHKEX_Quotation`
--

DROP TABLE IF EXISTS `tHKEX_Quotation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tHKEX_Quotation` (
  `symbol` varchar(10) NOT NULL,
  `Date` datetime NOT NULL,
  `Name` varchar(25) DEFAULT NULL,
  `Currency` varchar(3) DEFAULT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tHKEX_Sales`
--

DROP TABLE IF EXISTS `tHKEX_Sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tHKEX_Sales` (
  `symbol` varchar(10) NOT NULL,
  `Date` datetime NOT NULL,
  `Serial` varchar(7) NOT NULL,
  `Flag` varchar(1) DEFAULT NULL,
  `Price` decimal(10,3) DEFAULT NULL,
  `Volume` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`symbol`,`Date`,`Serial`),
  KEY `index_symbol_date` (`symbol`,`Date`),
  KEY `index_symbol` (`symbol`),
  KEY `index_date` (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tSymbol`
--

DROP TABLE IF EXISTS `tSymbol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tSymbol` (
  `symbol` varchar(10) NOT NULL,
  `preferredVendor` varchar(10) DEFAULT NULL,
  `availVendors` varchar(30) DEFAULT NULL,
  `currency` varchar(3) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`symbol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tVendor`
--

DROP TABLE IF EXISTS `tVendor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tVendor` (
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary table structure for view `vDaily`
--

DROP TABLE IF EXISTS `vDaily`;
/*!50001 DROP VIEW IF EXISTS `vDaily`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `vDaily` AS SELECT 
 1 AS `symbol`,
 1 AS `date`,
 1 AS `open`,
 1 AS `high`,
 1 AS `low`,
 1 AS `close`,
 1 AS `volume`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `vDaily`
--

-- Dump completed on 2018-01-25 22:23:12
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
-- Table structure for table `tDailyPrice`
--

DROP TABLE IF EXISTS `tDailyPrice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tDailyPrice` (
  `vendorName` varchar(10) NOT NULL,
  `symbol` varchar(10) NOT NULL,
  `priceDate` datetime NOT NULL,
  `openPrice` decimal(10,3) DEFAULT NULL,
  `highPrice` decimal(10,3) DEFAULT NULL,
  `lowPrice` decimal(10,3) DEFAULT NULL,
  `closePrice` decimal(10,3) DEFAULT NULL,
  `volume` bigint(20) DEFAULT NULL,
  `adjClosePrice` decimal(10,3) DEFAULT NULL,
  PRIMARY KEY (`symbol`,`priceDate`,`vendorName`),
  KEY `index_vendor` (`vendorName`),
  KEY `index_symbol` (`symbol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tDailyPrice_yahoo`
--

DROP TABLE IF EXISTS `tDailyPrice_yahoo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tDailyPrice_yahoo` (
  `symbol` varchar(10) NOT NULL,
  `Date` datetime NOT NULL,
  `Open` decimal(10,3) DEFAULT NULL,
  `High` decimal(10,3) DEFAULT NULL,
  `Low` decimal(10,3) DEFAULT NULL,
  `Close` decimal(10,3) DEFAULT NULL,
  `Adj Close` decimal(10,3) DEFAULT NULL,
  `Volume` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`symbol`,`Date`),
  KEY `index_symbol` (`symbol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tHKEX_Quotation`
--

DROP TABLE IF EXISTS `tHKEX_Quotation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tHKEX_Quotation` (
  `symbol` varchar(10) NOT NULL,
  `Date` datetime NOT NULL,
  `Name` varchar(25) DEFAULT NULL,
  `Currency` varchar(3) DEFAULT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tHKEX_Sales`
--

DROP TABLE IF EXISTS `tHKEX_Sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tHKEX_Sales` (
  `symbol` varchar(10) NOT NULL,
  `Date` datetime NOT NULL,
  `Serial` varchar(7) NOT NULL,
  `Flag` varchar(1) DEFAULT NULL,
  `Price` decimal(10,3) DEFAULT NULL,
  `Volume` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`symbol`,`Date`,`Serial`),
  KEY `index_symbol_date` (`symbol`,`Date`),
  KEY `index_symbol` (`symbol`),
  KEY `index_date` (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tSymbol`
--

DROP TABLE IF EXISTS `tSymbol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tSymbol` (
  `symbol` varchar(10) NOT NULL,
  `preferredVendor` varchar(10) DEFAULT NULL,
  `availVendors` varchar(30) DEFAULT NULL,
  `currency` varchar(3) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`symbol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tVendor`
--

DROP TABLE IF EXISTS `tVendor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tVendor` (
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary table structure for view `vDaily`
--

DROP TABLE IF EXISTS `vDaily`;
/*!50001 DROP VIEW IF EXISTS `vDaily`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `vDaily` AS SELECT 
 1 AS `symbol`,
 1 AS `date`,
 1 AS `open`,
 1 AS `high`,
 1 AS `low`,
 1 AS `close`,
 1 AS `volume`*/;
SET character_set_client = @saved_cs_client;

--
-- Dumping routines for database 'secmaster'
--

DELIMITER ;;
CREATE DEFINER=`tpuser`@`%` PROCEDURE `pDaily`(IN `symbol` VARCHAR(15))
SELECT * FROM vDaily
  WHERE vDaily.symbol = symbol ;;
DELIMITER ;
