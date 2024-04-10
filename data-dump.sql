-- MySQL dump 10.13  Distrib 5.7.24, for osx11.1 (x86_64)
--
-- Host: localhost    Database: RideShare
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `DRIVER`
--

DROP TABLE IF EXISTS `DRIVER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DRIVER` (
  `user_id` int NOT NULL,
  `rating` int NOT NULL DEFAULT '0',
  `driver_mode` tinyint(1) DEFAULT '0',
  KEY `user_id` (`user_id`),
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `USER` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DRIVER`
--

LOCK TABLES `DRIVER` WRITE;
/*!40000 ALTER TABLE `DRIVER` DISABLE KEYS */;
INSERT INTO `DRIVER` VALUES (1,5,1),(2,0,0),(3,0,0),(4,0,1),(5,0,1),(6,0,1);
/*!40000 ALTER TABLE `DRIVER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TRIPLOGS`
--

DROP TABLE IF EXISTS `TRIPLOGS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TRIPLOGS` (
  `trip_id` int NOT NULL,
  `driver_id` int NOT NULL,
  `rider_id` int NOT NULL,
  `pickup_address` varchar(255) NOT NULL,
  `dropoff_address` varchar(255) NOT NULL,
  KEY `driver_id` (`driver_id`),
  KEY `rider_id` (`rider_id`),
  CONSTRAINT `driver_id` FOREIGN KEY (`driver_id`) REFERENCES `USER` (`user_id`),
  CONSTRAINT `rider_id` FOREIGN KEY (`rider_id`) REFERENCES `USER` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TRIPLOGS`
--

LOCK TABLES `TRIPLOGS` WRITE;
/*!40000 ALTER TABLE `TRIPLOGS` DISABLE KEYS */;
INSERT INTO `TRIPLOGS` VALUES (1,1,1,'',''),(2,1,5,'chapman university','dominos pizza'),(3,1,5,'panther village','chapman grand'),(4,1,6,'jimmy johns','disneyland pickup dropoff');
/*!40000 ALTER TABLE `TRIPLOGS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `USER`
--

DROP TABLE IF EXISTS `USER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `USER` (
  `user_id` int NOT NULL,
  `email` varchar(100) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `is_driver` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `USER`
--

LOCK TABLES `USER` WRITE;
/*!40000 ALTER TABLE `USER` DISABLE KEYS */;
INSERT INTO `USER` VALUES (1,'matt@gmail.com','matt',NULL),(2,'chewy@gmail.com','Chewy',NULL),(3,'yodie@gmail.yeet','Damien',NULL),(4,'macaroni@noodles.com','Macky',NULL),(5,'john@pork.gmail','John Pork',NULL),(6,'yeet@yodie.com','jumbo jimmy',NULL);
/*!40000 ALTER TABLE `USER` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-09 23:52:39
