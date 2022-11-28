-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: bd_practica
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `peliculas`
--

DROP TABLE IF EXISTS `peliculas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `peliculas` (
  `idpeliculas` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) COLLATE utf8mb3_bin DEFAULT NULL,
  `clasificacion` varchar(45) COLLATE utf8mb3_bin DEFAULT NULL,
  `duracion` varchar(10) COLLATE utf8mb3_bin DEFAULT NULL,
  `imagen` mediumtext COLLATE utf8mb3_bin,
  `sinopsis` longtext COLLATE utf8mb3_bin,
  PRIMARY KEY (`idpeliculas`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `peliculas`
--

LOCK TABLES `peliculas` WRITE;
/*!40000 ALTER TABLE `peliculas` DISABLE KEYS */;
INSERT INTO `peliculas` VALUES (1,'Pantera Negra: Wakanda Por Siempre','B','161','https://static.cinepolis.com/img/peliculas/40552/1/1/40552.jpg','En PANTERA NEGRA: WAKANDA POR SIEMPRE de Marvel Studios, la reina Ramonda (Angela Bassett), Shuri (Letitia Wright), M\'Baku (Winston Duke), Okoye (Danai Gurira) y las Dora Milaje (incluida Florence Kasumba) luchan por proteger a su nación de las potencias mundiales que intervienen tras la muerte del Rey T\'Challa. Mientras los habitantes de Wakanda se esfuerzan embarcarse en un nuevo capítulo, los héroes deben unirse con la ayuda de War Dog Nakia (Lupita Nyong\'o) y Everett Ross (Martin Freeman) y forjar un nuevo camino para el reino de Wakanda. El film que cuenta con Tenoch Huerta como Namor, rey de una nación submarina oculta, también está protagonizada por Dominique Thorne, Michaela Coel, Mabel Cadena y Alex Livanalli.'),(2,'Fuerza Bruta','S/C','106','https://static.cinepolis.com/img/peliculas/40293/1/1/40293.jpg','Ma Seok-do (Don Lee de Eternals) se dirige a un país extranjero para extraditar a un sospechoso. Sin embargo, en su viaje descubre casos de asesinato adicionales y sospecha de un asesino que ha cometido crímenes contra turistas desde hace años.'),(3,'Black Adam','B','126','https://static.cinepolis.com/img/peliculas/39642/1/1/39642.jpg','Casi 5,000 años después de obtener los poderes supremos de los antiguos dioses –y de ser encarcelado igual de rápido–, Black Adam (Dwayne Johnson) se libera de su tumba terrenal, listo para desatar su peculiar forma de justicia en el mundo moderno.');
/*!40000 ALTER TABLE `peliculas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post` (
  `idpost` int NOT NULL AUTO_INCREMENT,
  `usuario` varchar(45) COLLATE utf8mb3_bin DEFAULT NULL,
  `titulo` varchar(45) COLLATE utf8mb3_bin DEFAULT NULL,
  `comentario` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  PRIMARY KEY (`idpost`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
INSERT INTO `post` VALUES (1,'invitado','Prueba','Comentario de prueba'),(2,'invitado','Prueba','Comentario de prueba'),(3,'invitado','Prueba','Comentario de prueba'),(4,'invitado','Prueba','Comentario de prueba');
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quejas`
--

DROP TABLE IF EXISTS `quejas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quejas` (
  `idquejas` int NOT NULL AUTO_INCREMENT,
  `usuario` varchar(45) COLLATE utf8mb3_bin DEFAULT NULL,
  `queja` varchar(45) COLLATE utf8mb3_bin DEFAULT NULL,
  PRIMARY KEY (`idquejas`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quejas`
--

LOCK TABLES `quejas` WRITE;
/*!40000 ALTER TABLE `quejas` DISABLE KEYS */;
INSERT INTO `quejas` VALUES (1,'Prueba','Esto es una queja de prueba');
/*!40000 ALTER TABLE `quejas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `idusuarios` int NOT NULL AUTO_INCREMENT,
  `primerNombre` varchar(45) COLLATE utf8mb3_bin DEFAULT NULL,
  `segundoNombre` varchar(45) COLLATE utf8mb3_bin DEFAULT NULL,
  `apellidoPaterno` varchar(45) COLLATE utf8mb3_bin DEFAULT NULL,
  `apellidoMaterno` varchar(45) COLLATE utf8mb3_bin DEFAULT NULL,
  `correo` varchar(45) COLLATE utf8mb3_bin DEFAULT NULL,
  `usuario` varchar(45) COLLATE utf8mb3_bin DEFAULT NULL,
  `contraseña` longtext COLLATE utf8mb3_bin,
  PRIMARY KEY (`idusuarios`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Preuaba','PPrueba','pPrueba','ppPrueba','prueba@hotmail.com','Prueba','$5$rounds=535000$FrSILsega3it76mr$akPvDT9u1t.mD.AkToYgXZa1.Pyg13HLEIUyQVXOcr7');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-27 17:48:24
