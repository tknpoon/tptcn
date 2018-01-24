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
-- Dumping data for table `tSymbol`
--

LOCK TABLES `tSymbol` WRITE;
/*!40000 ALTER TABLE `tSymbol` DISABLE KEYS */;
INSERT INTO `tSymbol` VALUES ('000001.SS','yahoo','yahoo','CNY','SSE Composite Index'),('0001.HK','yahoo','yahoo;hkex;test','HKD','CKH Holdings'),('0002.HK','yahoo','yahoo;hkex','HKD','CLP Holdings'),('0003.HK','yahoo','yahoo;hkex','HKD','HK & China Gas'),('0004.HK','yahoo','yahoo;hkex','HKD','Wharf Holdings'),('0005.HK','yahoo','yahoo;hkex','HKD','HSBC Holdings'),('0006.HK','yahoo','yahoo;hkex','HKD','Power Assets'),('0011.HK','yahoo','yahoo;hkex','HKD','Hang Seng Bank'),('0012.HK','yahoo','yahoo;hkex','HKD','Henderson Land'),('0016.HK','yahoo','yahoo;hkex','HKD','SHK Ppt'),('0017.HK','yahoo','yahoo;hkex','HKD','New World Dev'),('0019.HK','yahoo','yahoo;hkex','HKD','Swire Pacific A'),('0023.HK','yahoo','yahoo;hkex','HKD','Bank of E Asia'),('0027.HK','yahoo','yahoo;hkex','HKD','Galaxy Ent'),('0052.HK','yahoo','yahoo;hkex','HKD','Fairwood'),('0066.HK','yahoo','yahoo;hkex','HKD','MTR Corporation'),('0083.HK','yahoo','yahoo;hkex','HKD','Sino Land'),('0087.HK','yahoo','yahoo;hkex','HKD','Swire Pacific B'),('0101.HK','yahoo','yahoo;hkex','HKD','Hang Lung Ppt'),('0144.HK','yahoo','yahoo;hkex','HKD','China Mer Port'),('0151.HK','yahoo','yahoo;hkex','HKD','Want Want China'),('0175.HK','yahoo','yahoo;hkex','HKD','Geely Auto'),('0267.HK','yahoo','yahoo;hkex','HKD','CITIC'),('0288.HK','yahoo','yahoo;hkex','HKD','WH Group'),('0386.HK','yahoo','yahoo;hkex','HKD','Sinopec Corp'),('0388.HK','yahoo','yahoo;hkex;test','HKD','HKEx'),('0390.HK','yahoo','yahoo;hkex','HKD','China Railway'),('0489.HK','yahoo','yahoo;hkex','HKD','Dongfeng Group'),('0688.HK','yahoo','yahoo;hkex','HKD','China Overseas'),('0700.HK','yahoo','yahoo;hkex','HKD','Tencent'),('0728.HK','yahoo','yahoo;hkex','HKD','China Telecom'),('0753.HK','yahoo','yahoo;hkex','HKD','Air China'),('0762.HK','yahoo','yahoo;hkex','HKD','China Unicom'),('0823.HK','yahoo','yahoo;hkex','HKD','Link REIT'),('0836.HK','yahoo','yahoo;hkex','HKD','China Res Power'),('0857.HK','yahoo','yahoo;hkex','HKD','PetroChina'),('0883.HK','yahoo','yahoo;hkex','HKD','CNOOC'),('0902.HK','yahoo','yahoo;hkex','HKD','Huaneng Power'),('0914.HK','yahoo','yahoo;hkex','HKD','Conch Cement'),('0939.HK','yahoo','yahoo;hkex','HKD','CCB'),('0941.HK','yahoo','yahoo;hkex','HKD','China Mobile'),('0992.HK','yahoo','yahoo;hkex','HKD','Lenovo Group'),('0998.HK','yahoo','yahoo;hkex','HKD','CITIC Bank'),('1038.HK','yahoo','yahoo;hkex','HKD','CKI Holdings'),('1044.HK','yahoo','yahoo;hkex','HKD','Hengan Int\'l'),('1083.HK','yahoo','yahoo;hkex','HKD','Towngas China'),('1088.HK','yahoo','yahoo;hkex','HKD','China Shenhua'),('1099.HK','yahoo','yahoo;hkex','HKD','Sinopharm'),('1109.HK','yahoo','yahoo;hkex','HKD','China Res Land'),('1113.HK','yahoo','yahoo;hkex','HKD','CK Asset'),('1186.HK','yahoo','yahoo;hkex','HKD','China Rail Cons'),('1211.HK','yahoo','yahoo;hkex','HKD','BYD Company'),('1288.HK','yahoo','yahoo;hkex','HKD','ABC'),('1299.HK','yahoo','yahoo;hkex','HKD','AIA'),('1336.HK','yahoo','yahoo;hkex','HKD','NCI'),('1339.HK','yahoo','yahoo;hkex','HKD','PICC Group'),('1359.HK','yahoo','yahoo;hkex','HKD','China Cinda'),('1398.HK','yahoo','yahoo;hkex','HKD','ICBC'),('1658.HK','yahoo','yahoo;hkex','HKD','PSBC'),('1686.HK','yahoo','yahoo;hkex','HKD','SunEVision'),('1928.HK','yahoo','yahoo;hkex','HKD','Sands China Ltd'),('1997.HK','yahoo','yahoo;hkex','HKD','Wharf REIC'),('2007.HK','yahoo','yahoo;hkex','HKD','Country Garden'),('2018.HK','yahoo','yahoo;hkex','HKD','AAC Tech'),('2318.HK','yahoo','yahoo;hkex','HKD','Ping An'),('2319.HK','yahoo','yahoo;hkex','HKD','Mengniu Dairy'),('2382.HK','yahoo','yahoo;hkex','HKD','Sunny Optical'),('2388.HK','yahoo','yahoo;hkex','HKD','BOC Hong Kong'),('2628.HK','yahoo','yahoo;hkex','HKD','China Life'),('2800.HK','yahoo','yahoo;hkex','HKD','Tracker Fund'),('2822.HK','hkex','yahoo;hkex','HKD','CSOP A50 ETF'),('2823.HK','hkex','yahoo;hkex','HKD','ISHARES A50 ETF'),('2828.HK','yahoo','yahoo;hkex','HKD','HS H ETF'),('2833.HK','hkex','yahoo;hkex','HKD','HS HSI ETF'),('3328.HK','yahoo','yahoo;hkex','HKD','Bankcomm'),('3988.HK','yahoo','yahoo;hkex','HKD','Bank of China'),('8008.HK','yahoo','yahoo;hkex','HKD','Sun eVision'),('DX-Y.NYB','yahoo','yahoo','USD','US Dollar Index Futures Cash'),('USDCNY=X','yahoo','yahoo','CNY','USDCNY=X'),('^HSI','yahoo','yahoo','HKD','Hang Seng Index ');
/*!40000 ALTER TABLE `tSymbol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `tVendor`
--

LOCK TABLES `tVendor` WRITE;
/*!40000 ALTER TABLE `tVendor` DISABLE KEYS */;
INSERT INTO `tVendor` VALUES ('hkex'),('hkma'),('yahoo');
/*!40000 ALTER TABLE `tVendor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-01-24 13:32:12
