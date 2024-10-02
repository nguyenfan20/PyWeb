-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tmdt
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `price` float NOT NULL,
  `brand_id` int NOT NULL,
  `image` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `screen` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `chip` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `ram` int NOT NULL,
  `rom` int NOT NULL,
  `weight` float NOT NULL,
  `description` varchar(500) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `brand_id` (`brand_id`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`brand_id`) REFERENCES `brand` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Dell Gaming G3 3500',100,1,'static/images/product/Dell/dell07.jpg',48,'OLED 24inch','Core i5 8thGen',8,512,2.2,'THIS IS DESCRIPTION'),(2,'Dell XPS 8570',100,1,'static/images/product/Dell/dell05.jpg',42,'OLED 24inch','Core i5 8thGen',8,512,2.2,'THIS IS DESCRIPTION'),(3,'Dell Latitude E7410',100,1,'static/images/product/Dell/dell04.jpg',44,'OLED 24inch','Core i5 8thGen',8,512,2.2,'THIS IS DESCRIPTION'),(4,'Dell Latitude 7420',200,1,'static/images/product/Dell/dell01.jpg',49,'OLED 24inch','Core i5 8thGen',8,512,2.2,'THIS IS DESCRIPTION'),(5,'Dell Precision 3541',150,1,'static/images/product/Dell/dell02.jpg',45,'OLED 24inch','Core i5 8thGen',8,512,2.2,'THIS IS DESCRIPTION'),(6,'Dell XPS 9710',160,1,'static/images/product/Dell/dell01.jpg',49,'OLED 24inch','Core i5 8thGen',8,512,2.2,'THIS IS DESCRIPTION'),(7,'Lenovo ThinkPad',100,2,'static/images/product/Mac/mac01.jpg',36,'OLED 24inch','Core i5 8thGen',8,512,2.2,'THIS IS DESCRIPTION'),(8,'Macbook',500,6,'static/images/product/Mac/mac02.jpg',44,'OLED 24inch','Core i5 8thGen',8,512,2.2,'THIS IS DESCRIPTION'),(9,'Macbook Pro 16 inch',100,6,'static/images/product/Mac/mac01.jpg',85,'OLED 24inch','Core i5 8thGen',8,512,2.2,'THIS IS DESCRIPTION'),(10,'Dell Inspiration 3501',159,1,'static/images/product/Dell/dell08.png',50,'OLED 24inch','Core i5 8thGen',8,512,2.2,'THIS IS DESCRIPTION'),(11,'Laptop Inspiration 5821',100,1,'static/images/product/Dell/dell06.jpg',47,'OLED 24inch','Core i5 8thGen',8,512,2.2,'THIS IS DESCRIPTION'),(12,'Dell XPS 15 9570',100,1,'static/images/product/Dell/dell09.jpg',50,'OLED 24inch','Core i5 8thGen',8,512,2.2,'THIS IS DESCRIPTION'),(13,'Macbook Pro M1',100,6,'static/images/product/Mac/mac03.jpg',50,'OLED 24inch','Core i5 8thGen',8,512,2.2,'THIS IS DESCRIPTION'),(14,'Macbook Pro Gen2',100,6,'static/images/product/Mac/mac04.jpeg',43,'OLED 24inch','Core i5 8thGen',8,512,2.2,'THIS IS DESCRIPTION'),(15,'Macbook Gen1',100,6,'static/images/product/Mac/mac02.jpg',50,'OLED 24inch','Core i5 8thGen',8,512,2.2,'THIS IS DESCRIPTION'),(16,'Macbook Pro MAX',100,6,'static/images/product/Mac/mac03.jpg',50,'OLED 24inch','Core i5 8thGen',8,512,2.2,'THIS IS DESCRIPTION'),(17,'Macbook Air 2017',160,6,'static/images/product/Mac/mac01.jpg',50,'OLED 24inch','Core i5 8thGen',8,512,2.2,'THIS IS DESCRIPTION'),(18,'Macbook Air Pro 2018',100,6,'static/images/product/Mac/mac02.jpg',50,'OLED 24inch','Core i5 8thGen',8,512,2.2,'THIS IS DESCRIPTION'),(19,'Macbook Air Pro 2019',100,6,'static/images/product/Mac/mac02.jpg',46,'OLED 24inch','Core i5 8thGen',8,512,2.2,'THIS IS DESCRIPTION'),(20,'Macbook Air 2016',100,6,'static/images/product/Mac/mac04.jpeg',44,'OLED 24inch','Core i5 8thGen',8,512,2.2,'THIS IS DESCRIPTION'),(21,'Macbook Pro MAX Gen1',100,6,'static/images/product/Mac/mac03.jpg',40,'OLED 24inch','Core i5 8thGen',8,512,2.2,'THIS IS DESCRIPTION'),(22,'Dell Inpriration 10',100,1,'static/images/product/Dell/dell01.jpg',46,'OLED 24inch','Core i5 8thGen',8,512,2.2,'THIS IS DESCRIPTION');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-21 12:43:11
