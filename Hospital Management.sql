-- MySQL dump 10.13  Distrib 5.7.9, for Win32 (AMD64)
--
-- Host: localhost    Database: hospital
-- ------------------------------------------------------
-- Server version	5.1.50-community

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
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bill` (
  `ID` int(2) NOT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Bed_Type` varchar(20) DEFAULT NULL,
  `Rent` int(10) DEFAULT NULL,
  `Duration` int(10) DEFAULT NULL,
  `Total_Bill` int(20) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
INSERT INTO `bill` VALUES (1,'Vimal','Single Room',865000,173,885000);
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor_info`
--

DROP TABLE IF EXISTS `doctor_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `doctor_info` (
  `ID` int(2) NOT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Department` varchar(20) DEFAULT NULL,
  `Type` varchar(20) DEFAULT NULL,
  `Salary` int(6) DEFAULT NULL,
  `Day` varchar(100) DEFAULT NULL,
  `FEES` int(5) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor_info`
--

LOCK TABLES `doctor_info` WRITE;
/*!40000 ALTER TABLE `doctor_info` DISABLE KEYS */;
INSERT INTO `doctor_info` VALUES (1,'Avinash','ENT','Consultant',170000,'Monday,Wednesday,Friday',700),(2,'Vikas','ENT','Surgeon',350000,'Tuesday,Thursday,Saturday',1000),(3,'Lodhi','ENT','Physician',150000,'Sunday',500),(4,'Ved','Cardiology','Consultant',200000,'Monday,Wednesday,Friday',700),(5,'Anand','Cardiology','Surgeon',500000,'Tuesday,Thursday,Saturday',1000),(6,'Bhav','Cardiology','Physician',150000,'Sunday',500),(7,'Shanaya','Urology','Consultant',300000,'Monday,Wednesday,Friday',700),(8,'Kriti','Urology','Surgeon',500000,'Tuesday,Thursday,Saturday',1000),(9,'Rohit','Urology','Physician',150000,'Every',500);
/*!40000 ALTER TABLE `doctor_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `opd`
--

DROP TABLE IF EXISTS `opd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `opd` (
  `PNO` int(5) NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  `Day` varchar(50) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `DocName` varchar(50) DEFAULT NULL,
  `Fees` int(5) DEFAULT NULL,
  PRIMARY KEY (`PNO`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opd`
--

LOCK TABLES `opd` WRITE;
/*!40000 ALTER TABLE `opd` DISABLE KEYS */;
INSERT INTO `opd` VALUES (1,'Rahul','Urology','Wednesday','2023-05-28','Shanaya',700);
/*!40000 ALTER TABLE `opd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient_info`
--

DROP TABLE IF EXISTS `patient_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `patient_info` (
  `ID` int(2) NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Dept` varchar(50) DEFAULT NULL,
  `Gender` varchar(5) DEFAULT NULL,
  `Age` int(5) DEFAULT NULL,
  `Date_adm` date DEFAULT NULL,
  `Date_dis` date DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_info`
--

LOCK TABLES `patient_info` WRITE;
/*!40000 ALTER TABLE `patient_info` DISABLE KEYS */;
INSERT INTO `patient_info` VALUES (1,'Nayak','ENT','M',36,'2023-03-28','2023-05-01'),(2,'Adil','ENT','M',47,'2023-03-13','2023-05-19');
/*!40000 ALTER TABLE `patient_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salary`
--

DROP TABLE IF EXISTS `salary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `salary` (
  `ID` int(2) NOT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `TA` int(10) DEFAULT NULL,
  `DA` int(10) DEFAULT NULL,
  `Tax` int(10) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salary`
--

LOCK TABLES `salary` WRITE;
/*!40000 ALTER TABLE `salary` DISABLE KEYS */;
INSERT INTO `salary` VALUES (1,'Avinash',51000,51000,312000),(2,'Vikas',51000,51000,960000),(3,'Lodhi',51000,51000,351000),(4,'Ved',51000,51000,405000),(5,'Anand',51000,51000,1325000),(6,'Bhav',51000,51000,351000),(7,'Shanaya',51000,51000,805000),(8,'Kriit',51000,51000,1325000),(9,'Rohit',51000,51000,351000);
/*!40000 ALTER TABLE `salary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tests`
--

DROP TABLE IF EXISTS `tests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tests` (
  `Pat_ID` varchar(50) DEFAULT NULL,
  `Test` varchar(255) DEFAULT NULL,
  `Test_id` int(2) DEFAULT NULL,
  `Date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tests`
--

LOCK TABLES `tests` WRITE;
/*!40000 ALTER TABLE `tests` DISABLE KEYS */;
INSERT INTO `tests` VALUES ('1','CT Scan',1,'2023-04-02 00:00:00'),('1','MRI',2,'2023-04-10 00:00:00'),('1','Ostoscopy',3,'2023-04-15 00:00:00');
/*!40000 ALTER TABLE `tests` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-01 20:10:57
