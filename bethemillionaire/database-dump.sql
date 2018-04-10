-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: localhost    Database: databasbethemillionaire
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.17.10.1

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
-- Table structure for table `account_automated_webinar_funnel_version_1`
--

DROP TABLE IF EXISTS `account_automated_webinar_funnel_version_1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_automated_webinar_funnel_version_1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `campaign_name` varchar(100) DEFAULT NULL,
  `visitors` int(11) DEFAULT NULL,
  `leads` int(11) DEFAULT NULL,
  `conversion_rate` int(11) DEFAULT NULL,
  `campaign_link` varchar(200) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_automated_we_user_id_790cab8a_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_automated_webinar_funnel_version_1`
--

LOCK TABLES `account_automated_webinar_funnel_version_1` WRITE;
/*!40000 ALTER TABLE `account_automated_webinar_funnel_version_1` DISABLE KEYS */;
INSERT INTO `account_automated_webinar_funnel_version_1` VALUES (4,'Automated Webinar Funnel Version 1',0,0,0,'',11),(5,'Automated Webinar Funnel Version 1',6,1,0,'',12),(6,'Automated Webinar Funnel Version 1',1,0,0,'',13),(7,'Automated Webinar Funnel Version 1',0,0,0,'',14),(8,'Automated Webinar Funnel Version 1',0,0,0,'',15),(9,'Automated Webinar Funnel Version 1',0,0,0,'',16),(10,'Automated Webinar Funnel Version 1',0,0,0,'',17),(11,'Automated Webinar Funnel Version 1',0,0,0,'',18),(12,'Automated Webinar Funnel Version 1',0,0,0,'',19),(13,'Automated Webinar Funnel Version 1',0,0,0,'',20),(14,'Automated Webinar Funnel Version 1',0,0,0,'',21),(15,'Automated Webinar Funnel Version 1',0,0,0,'',22),(16,'Automated Webinar Funnel Version 1',0,0,0,'',23),(17,'Automated Webinar Funnel Version 1',0,0,0,'',24);
/*!40000 ALTER TABLE `account_automated_webinar_funnel_version_1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_automated_webinar_funnel_version_2`
--

DROP TABLE IF EXISTS `account_automated_webinar_funnel_version_2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_automated_webinar_funnel_version_2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `campaign_name` varchar(100) DEFAULT NULL,
  `visitors` int(11) DEFAULT NULL,
  `leads` int(11) DEFAULT NULL,
  `conversion_rate` int(11) DEFAULT NULL,
  `campaign_link` varchar(200) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_automated_we_user_id_dbcc0b0a_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_automated_webinar_funnel_version_2`
--

LOCK TABLES `account_automated_webinar_funnel_version_2` WRITE;
/*!40000 ALTER TABLE `account_automated_webinar_funnel_version_2` DISABLE KEYS */;
INSERT INTO `account_automated_webinar_funnel_version_2` VALUES (4,'Automated Webinar Funnel Version 2',0,0,0,'',11),(5,'Automated Webinar Funnel Version 2',3,1,0,'',12),(6,'Automated Webinar Funnel Version 2',0,0,0,'',13),(7,'Automated Webinar Funnel Version 2',0,0,0,'',14),(8,'Automated Webinar Funnel Version 2',0,0,0,'',15),(9,'Automated Webinar Funnel Version 2',0,0,0,'',16),(10,'Automated Webinar Funnel Version 2',0,0,0,'',17),(11,'Automated Webinar Funnel Version 2',0,0,0,'',18),(12,'Automated Webinar Funnel Version 2',0,0,0,'',19),(13,'Automated Webinar Funnel Version 2',0,0,0,'',20),(14,'Automated Webinar Funnel Version 2',0,0,0,'',21),(15,'Automated Webinar Funnel Version 2',0,0,0,'',22),(16,'Automated Webinar Funnel Version 2',0,0,0,'',23),(17,'Automated Webinar Funnel Version 2',0,0,0,'',24);
/*!40000 ALTER TABLE `account_automated_webinar_funnel_version_2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_aweberaccount`
--

DROP TABLE IF EXISTS `account_aweberaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_aweberaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `aweber_username` varchar(100) DEFAULT NULL,
  `create_on` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_aweberaccount_user_id_a4f87321_fk_account_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_aweberaccount`
--

LOCK TABLES `account_aweberaccount` WRITE;
/*!40000 ALTER TABLE `account_aweberaccount` DISABLE KEYS */;
INSERT INTO `account_aweberaccount` VALUES (4,NULL,'2018-03-31 21:19:34.670259',11),(5,NULL,'2018-03-31 21:27:49.155717',12),(6,NULL,'2018-03-31 21:28:35.128844',13),(7,NULL,'2018-03-31 21:30:10.615578',14),(8,NULL,'2018-03-31 21:32:07.901076',15),(9,NULL,'2018-03-31 21:32:58.391859',16),(10,NULL,'2018-04-01 20:00:05.337283',17),(11,NULL,'2018-04-01 20:19:50.481421',18),(12,NULL,'2018-04-01 20:28:52.532647',19),(13,NULL,'2018-04-01 20:53:22.322565',20),(14,NULL,'2018-04-01 21:01:51.779344',21),(15,NULL,'2018-04-01 21:10:52.353752',22),(16,NULL,'2018-04-01 21:14:08.277446',23),(17,NULL,'2018-04-01 22:20:45.081565',24);
/*!40000 ALTER TABLE `account_aweberaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_bethemillionaire_3_step_registration_funnel`
--

DROP TABLE IF EXISTS `account_bethemillionaire_3_step_registration_funnel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_bethemillionaire_3_step_registration_funnel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `campaign_name` varchar(100) DEFAULT NULL,
  `visitors` int(11) DEFAULT NULL,
  `leads` int(11) DEFAULT NULL,
  `conversion_rate` int(11) DEFAULT NULL,
  `campaign_link` varchar(200) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_bethemillion_user_id_b330eed1_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_bethemillionaire_3_step_registration_funnel`
--

LOCK TABLES `account_bethemillionaire_3_step_registration_funnel` WRITE;
/*!40000 ALTER TABLE `account_bethemillionaire_3_step_registration_funnel` DISABLE KEYS */;
INSERT INTO `account_bethemillionaire_3_step_registration_funnel` VALUES (5,'BeTheMillionaire 3-Step Registration Funnel',0,0,0,'',11),(6,'BeTheMillionaire 3-Step Registration Funnel',10,1,0,'',12),(7,'BeTheMillionaire 3-Step Registration Funnel',0,0,0,'',13),(8,'BeTheMillionaire 3-Step Registration Funnel',0,0,0,'',14),(9,'BeTheMillionaire 3-Step Registration Funnel',0,0,0,'',15),(10,'BeTheMillionaire 3-Step Registration Funnel',0,0,0,'',16),(11,'BeTheMillionaire 3-Step Registration Funnel',0,0,0,'',17),(12,'BeTheMillionaire 3-Step Registration Funnel',0,0,0,'',18),(13,'BeTheMillionaire 3-Step Registration Funnel',0,0,0,'',19),(14,'BeTheMillionaire 3-Step Registration Funnel',0,0,0,'',20),(15,'BeTheMillionaire 3-Step Registration Funnel',0,0,0,'',21),(16,'BeTheMillionaire 3-Step Registration Funnel',0,0,0,'',22),(17,'BeTheMillionaire 3-Step Registration Funnel',0,0,0,'',23),(18,'BeTheMillionaire 3-Step Registration Funnel',0,0,0,'',24);
/*!40000 ALTER TABLE `account_bethemillionaire_3_step_registration_funnel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_bitconnect_direct_funnel`
--

DROP TABLE IF EXISTS `account_bitconnect_direct_funnel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_bitconnect_direct_funnel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `campaign_name` varchar(100) DEFAULT NULL,
  `visitors` int(11) DEFAULT NULL,
  `leads` int(11) DEFAULT NULL,
  `conversion_rate` int(11) DEFAULT NULL,
  `campaign_link` varchar(200) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_bitconnect_d_user_id_b6079407_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_bitconnect_direct_funnel`
--

LOCK TABLES `account_bitconnect_direct_funnel` WRITE;
/*!40000 ALTER TABLE `account_bitconnect_direct_funnel` DISABLE KEYS */;
INSERT INTO `account_bitconnect_direct_funnel` VALUES (4,'Bitconnect Direct Funnel',0,0,0,'',11),(5,'Bitconnect Direct Funnel',2,0,0,'',12),(6,'Bitconnect Direct Funnel',0,0,0,'',13),(7,'Bitconnect Direct Funnel',0,0,0,'',14),(8,'Bitconnect Direct Funnel',0,0,0,'',15),(9,'Bitconnect Direct Funnel',0,0,0,'',16),(10,'Bitconnect Direct Funnel',0,0,0,'',17),(11,'Bitconnect Direct Funnel',0,0,0,'',18),(12,'Bitconnect Direct Funnel',0,0,0,'',19),(13,'Bitconnect Direct Funnel',0,0,0,'',20),(14,'Bitconnect Direct Funnel',0,0,0,'',21),(15,'Bitconnect Direct Funnel',0,0,0,'',22),(16,'Bitconnect Direct Funnel',0,0,0,'',23),(17,'Bitconnect Direct Funnel',0,0,0,'',24);
/*!40000 ALTER TABLE `account_bitconnect_direct_funnel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_bitconnectaccount`
--

DROP TABLE IF EXISTS `account_bitconnectaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_bitconnectaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bitconnect_username` varchar(100) DEFAULT NULL,
  `create_on` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_bitconnectac_user_id_16bca533_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_bitconnectaccount`
--

LOCK TABLES `account_bitconnectaccount` WRITE;
/*!40000 ALTER TABLE `account_bitconnectaccount` DISABLE KEYS */;
INSERT INTO `account_bitconnectaccount` VALUES (4,NULL,'2018-03-31 21:19:34.644816',11),(5,'mmmm','2018-03-31 21:27:49.141772',12),(6,NULL,'2018-03-31 21:28:35.107914',13),(7,NULL,'2018-03-31 21:30:10.597643',14),(8,NULL,'2018-03-31 21:32:07.877530',15),(9,NULL,'2018-03-31 21:32:58.375136',16),(10,NULL,'2018-04-01 20:00:05.301512',17),(11,NULL,'2018-04-01 20:19:50.457586',18),(12,NULL,'2018-04-01 20:28:52.513845',19),(13,NULL,'2018-04-01 20:53:22.293402',20),(14,NULL,'2018-04-01 21:01:51.748490',21),(15,NULL,'2018-04-01 21:10:52.329603',22),(16,NULL,'2018-04-01 21:14:08.254020',23),(17,NULL,'2018-04-01 22:20:45.044135',24);
/*!40000 ALTER TABLE `account_bitconnectaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_bitpandaaccount`
--

DROP TABLE IF EXISTS `account_bitpandaaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_bitpandaaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bitpanda_username` varchar(100) DEFAULT NULL,
  `create_on` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_bitpandaacco_user_id_41fef8a5_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_bitpandaaccount`
--

LOCK TABLES `account_bitpandaaccount` WRITE;
/*!40000 ALTER TABLE `account_bitpandaaccount` DISABLE KEYS */;
INSERT INTO `account_bitpandaaccount` VALUES (4,NULL,'2018-03-31 21:19:34.714184',11),(5,NULL,'2018-03-31 21:27:49.201454',12),(6,NULL,'2018-03-31 21:28:35.166012',13),(7,NULL,'2018-03-31 21:30:10.641622',14),(8,NULL,'2018-03-31 21:32:07.938812',15),(9,NULL,'2018-03-31 21:32:58.421117',16),(10,NULL,'2018-04-01 20:00:05.403713',17),(11,NULL,'2018-04-01 20:19:50.525738',18),(12,NULL,'2018-04-01 20:28:52.569766',19),(13,NULL,'2018-04-01 20:53:22.365905',20),(14,NULL,'2018-04-01 21:01:51.827420',21),(15,NULL,'2018-04-01 21:10:52.390891',22),(16,NULL,'2018-04-01 21:14:08.309996',23),(17,NULL,'2018-04-01 22:20:45.136818',24);
/*!40000 ALTER TABLE `account_bitpandaaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_cexioaccount`
--

DROP TABLE IF EXISTS `account_cexioaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_cexioaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cexio_username` varchar(100) DEFAULT NULL,
  `create_on` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_cexioaccount_user_id_b5a082b3_fk_account_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_cexioaccount`
--

LOCK TABLES `account_cexioaccount` WRITE;
/*!40000 ALTER TABLE `account_cexioaccount` DISABLE KEYS */;
INSERT INTO `account_cexioaccount` VALUES (4,NULL,'2018-03-31 21:19:34.708499',11),(5,NULL,'2018-03-31 21:27:49.197679',12),(6,NULL,'2018-03-31 21:28:35.161273',13),(7,NULL,'2018-03-31 21:30:10.636673',14),(8,NULL,'2018-03-31 21:32:07.933371',15),(9,NULL,'2018-03-31 21:32:58.416826',16),(10,NULL,'2018-04-01 20:00:05.394566',17),(11,NULL,'2018-04-01 20:19:50.518645',18),(12,NULL,'2018-04-01 20:28:52.565733',19),(13,NULL,'2018-04-01 20:53:22.359921',20),(14,NULL,'2018-04-01 21:01:51.823071',21),(15,NULL,'2018-04-01 21:10:52.386371',22),(16,NULL,'2018-04-01 21:14:08.304405',23),(17,NULL,'2018-04-01 22:20:45.131875',24);
/*!40000 ALTER TABLE `account_cexioaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_clickfunnelsaccount`
--

DROP TABLE IF EXISTS `account_clickfunnelsaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_clickfunnelsaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clickfunnels_username` varchar(100) DEFAULT NULL,
  `create_on` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_clickfunnels_user_id_c71aab8a_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_clickfunnelsaccount`
--

LOCK TABLES `account_clickfunnelsaccount` WRITE;
/*!40000 ALTER TABLE `account_clickfunnelsaccount` DISABLE KEYS */;
INSERT INTO `account_clickfunnelsaccount` VALUES (4,NULL,'2018-03-31 21:19:34.658541',11),(5,NULL,'2018-03-31 21:27:49.147871',12),(6,NULL,'2018-03-31 21:28:35.117456',13),(7,NULL,'2018-03-31 21:30:10.605392',14),(8,NULL,'2018-03-31 21:32:07.889609',15),(9,NULL,'2018-03-31 21:32:58.382512',16),(10,NULL,'2018-04-01 20:00:05.318449',17),(11,NULL,'2018-04-01 20:19:50.469499',18),(12,NULL,'2018-04-01 20:28:52.523442',19),(13,NULL,'2018-04-01 20:53:22.309513',20),(14,NULL,'2018-04-01 21:01:51.760334',21),(15,NULL,'2018-04-01 21:10:52.343665',22),(16,NULL,'2018-04-01 21:14:08.266228',23),(17,NULL,'2018-04-01 22:20:45.061682',24);
/*!40000 ALTER TABLE `account_clickfunnelsaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_clickmagicaccount`
--

DROP TABLE IF EXISTS `account_clickmagicaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_clickmagicaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clickmagic_username` varchar(100) DEFAULT NULL,
  `create_on` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_clickmagicac_user_id_ddf9bb0e_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_clickmagicaccount`
--

LOCK TABLES `account_clickmagicaccount` WRITE;
/*!40000 ALTER TABLE `account_clickmagicaccount` DISABLE KEYS */;
INSERT INTO `account_clickmagicaccount` VALUES (4,NULL,'2018-03-31 21:19:34.651857',11),(5,'nnnn','2018-03-31 21:27:49.144767',12),(6,NULL,'2018-03-31 21:28:35.112806',13),(7,NULL,'2018-03-31 21:30:10.601316',14),(8,NULL,'2018-03-31 21:32:07.885472',15),(9,NULL,'2018-03-31 21:32:58.378616',16),(10,NULL,'2018-04-01 20:00:05.311149',17),(11,NULL,'2018-04-01 20:19:50.465772',18),(12,NULL,'2018-04-01 20:28:52.518254',19),(13,NULL,'2018-04-01 20:53:22.302177',20),(14,NULL,'2018-04-01 21:01:51.755627',21),(15,NULL,'2018-04-01 21:10:52.337481',22),(16,NULL,'2018-04-01 21:14:08.261195',23),(17,NULL,'2018-04-01 22:20:45.051744',24);
/*!40000 ALTER TABLE `account_clickmagicaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_coinbaseaccount`
--

DROP TABLE IF EXISTS `account_coinbaseaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_coinbaseaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `coinbase_username` varchar(100) DEFAULT NULL,
  `create_on` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_coinbaseacco_user_id_d1f419ce_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_coinbaseaccount`
--

LOCK TABLES `account_coinbaseaccount` WRITE;
/*!40000 ALTER TABLE `account_coinbaseaccount` DISABLE KEYS */;
INSERT INTO `account_coinbaseaccount` VALUES (4,NULL,'2018-03-31 21:19:34.689285',11),(5,NULL,'2018-03-31 21:27:49.185004',12),(6,NULL,'2018-03-31 21:28:35.147306',13),(7,NULL,'2018-03-31 21:30:10.626442',14),(8,NULL,'2018-03-31 21:32:07.918078',15),(9,NULL,'2018-03-31 21:32:58.402957',16),(10,NULL,'2018-04-01 20:00:05.363565',17),(11,NULL,'2018-04-01 20:19:50.501514',18),(12,NULL,'2018-04-01 20:28:52.550761',19),(13,NULL,'2018-04-01 20:53:22.342610',20),(14,NULL,'2018-04-01 21:01:51.801532',21),(15,NULL,'2018-04-01 21:10:52.372202',22),(16,NULL,'2018-04-01 21:14:08.291154',23),(17,NULL,'2018-04-01 22:20:45.105702',24);
/*!40000 ALTER TABLE `account_coinbaseaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_coinmamaaccount`
--

DROP TABLE IF EXISTS `account_coinmamaaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_coinmamaaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `coin_mama_username` varchar(100) DEFAULT NULL,
  `create_on` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_coinmamaacco_user_id_4ed30ae1_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_coinmamaaccount`
--

LOCK TABLES `account_coinmamaaccount` WRITE;
/*!40000 ALTER TABLE `account_coinmamaaccount` DISABLE KEYS */;
INSERT INTO `account_coinmamaaccount` VALUES (4,NULL,'2018-03-31 21:19:34.732770',11),(5,'ppp','2018-03-31 21:27:49.212399',12),(6,NULL,'2018-03-31 21:28:35.181624',13),(7,NULL,'2018-03-31 21:30:10.654012',14),(8,NULL,'2018-03-31 21:32:07.952777',15),(9,NULL,'2018-03-31 21:32:58.433264',16),(10,NULL,'2018-04-01 20:00:05.437286',17),(11,NULL,'2018-04-01 20:19:50.540218',18),(12,NULL,'2018-04-01 20:28:52.583765',19),(13,NULL,'2018-04-01 20:53:22.384172',20),(14,NULL,'2018-04-01 21:01:51.850943',21),(15,NULL,'2018-04-01 21:10:52.406857',22),(16,NULL,'2018-04-01 21:14:08.321082',23),(17,NULL,'2018-04-01 22:20:45.159126',24);
/*!40000 ALTER TABLE `account_coinmamaaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_course_giveaway_3_steps_funnel`
--

DROP TABLE IF EXISTS `account_course_giveaway_3_steps_funnel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_course_giveaway_3_steps_funnel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `campaign_name` varchar(100) DEFAULT NULL,
  `visitors` int(11) DEFAULT NULL,
  `leads` int(11) DEFAULT NULL,
  `conversion_rate` int(11) DEFAULT NULL,
  `campaign_link` varchar(200) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_course_givea_user_id_d6820304_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_course_giveaway_3_steps_funnel`
--

LOCK TABLES `account_course_giveaway_3_steps_funnel` WRITE;
/*!40000 ALTER TABLE `account_course_giveaway_3_steps_funnel` DISABLE KEYS */;
INSERT INTO `account_course_giveaway_3_steps_funnel` VALUES (4,'Course Giveaway 3 Steps Funnel',0,0,0,'',11),(5,'Course Giveaway 3 Steps Funnel',3,1,0,'',12),(6,'Course Giveaway 3 Steps Funnel',0,0,0,'',13),(7,'Course Giveaway 3 Steps Funnel',0,0,0,'',14),(8,'Course Giveaway 3 Steps Funnel',0,0,0,'',15),(9,'Course Giveaway 3 Steps Funnel',0,0,0,'',16),(10,'Course Giveaway 3 Steps Funnel',0,0,0,'',17),(11,'Course Giveaway 3 Steps Funnel',0,0,0,'',18),(12,'Course Giveaway 3 Steps Funnel',0,0,0,'',19),(13,'Course Giveaway 3 Steps Funnel',0,0,0,'',20),(14,'Course Giveaway 3 Steps Funnel',0,0,0,'',21),(15,'Course Giveaway 3 Steps Funnel',0,0,0,'',22),(16,'Course Giveaway 3 Steps Funnel',0,0,0,'',23),(17,'Course Giveaway 3 Steps Funnel',0,0,0,'',24);
/*!40000 ALTER TABLE `account_course_giveaway_3_steps_funnel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_course_giveaway_direct_registration`
--

DROP TABLE IF EXISTS `account_course_giveaway_direct_registration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_course_giveaway_direct_registration` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `campaign_name` varchar(100) DEFAULT NULL,
  `visitors` int(11) DEFAULT NULL,
  `leads` int(11) DEFAULT NULL,
  `conversion_rate` int(11) DEFAULT NULL,
  `campaign_link` varchar(200) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_course_givea_user_id_75a85568_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_course_giveaway_direct_registration`
--

LOCK TABLES `account_course_giveaway_direct_registration` WRITE;
/*!40000 ALTER TABLE `account_course_giveaway_direct_registration` DISABLE KEYS */;
INSERT INTO `account_course_giveaway_direct_registration` VALUES (4,'Course Giveaway Direct Registration',0,0,0,'',11),(5,'Course Giveaway Direct Registration',2,1,0,'',12),(6,'Course Giveaway Direct Registration',0,0,0,'',13),(7,'Course Giveaway Direct Registration',0,0,0,'',14),(8,'Course Giveaway Direct Registration',0,0,0,'',15),(9,'Course Giveaway Direct Registration',0,0,0,'',16),(10,'Course Giveaway Direct Registration',0,0,0,'',17),(11,'Course Giveaway Direct Registration',0,0,0,'',18),(12,'Course Giveaway Direct Registration',0,0,0,'',19),(13,'Course Giveaway Direct Registration',0,0,0,'',20),(14,'Course Giveaway Direct Registration',0,0,0,'',21),(15,'Course Giveaway Direct Registration',0,0,0,'',22),(16,'Course Giveaway Direct Registration',0,0,0,'',23),(17,'Course Giveaway Direct Registration',0,0,0,'',24);
/*!40000 ALTER TABLE `account_course_giveaway_direct_registration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_cryptopaycardaccount`
--

DROP TABLE IF EXISTS `account_cryptopaycardaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_cryptopaycardaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cryptopay_card_username` varchar(100) DEFAULT NULL,
  `create_on` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_cryptopaycar_user_id_bb4cdf52_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_cryptopaycardaccount`
--

LOCK TABLES `account_cryptopaycardaccount` WRITE;
/*!40000 ALTER TABLE `account_cryptopaycardaccount` DISABLE KEYS */;
INSERT INTO `account_cryptopaycardaccount` VALUES (4,NULL,'2018-03-31 21:19:34.702072',11),(5,NULL,'2018-03-31 21:27:49.193386',12),(6,NULL,'2018-03-31 21:28:35.157375',13),(7,NULL,'2018-03-31 21:30:10.632836',14),(8,NULL,'2018-03-31 21:32:07.927607',15),(9,NULL,'2018-03-31 21:32:58.413231',16),(10,NULL,'2018-04-01 20:00:05.382396',17),(11,NULL,'2018-04-01 20:19:50.513443',18),(12,NULL,'2018-04-01 20:28:52.560765',19),(13,NULL,'2018-04-01 20:53:22.353326',20),(14,NULL,'2018-04-01 21:01:51.815711',21),(15,NULL,'2018-04-01 21:10:52.381551',22),(16,NULL,'2018-04-01 21:14:08.298817',23),(17,NULL,'2018-04-01 22:20:45.122516',24);
/*!40000 ALTER TABLE `account_cryptopaycardaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_direct_registration`
--

DROP TABLE IF EXISTS `account_direct_registration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_direct_registration` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `campaign_name` varchar(100) DEFAULT NULL,
  `visitors` int(11) DEFAULT NULL,
  `leads` int(11) DEFAULT NULL,
  `conversion_rate` int(11) DEFAULT NULL,
  `campaign_link` varchar(200) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_direct_regis_user_id_00c422ed_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_direct_registration`
--

LOCK TABLES `account_direct_registration` WRITE;
/*!40000 ALTER TABLE `account_direct_registration` DISABLE KEYS */;
INSERT INTO `account_direct_registration` VALUES (6,'Direct Registration',0,0,0,'',11),(7,'Direct Registration',37,4,0,'',12),(8,'Direct Registration',1,0,0,'',13),(9,'Direct Registration',0,0,0,'',14),(10,'Direct Registration',0,0,0,'',15),(11,'Direct Registration',1,1,0,'',16),(12,'Direct Registration',0,0,0,'',17),(13,'Direct Registration',0,0,0,'',18),(14,'Direct Registration',0,0,0,'',19),(15,'Direct Registration',0,0,0,'',20),(16,'Direct Registration',0,0,0,'',21),(17,'Direct Registration',0,0,0,'',22),(18,'Direct Registration',0,0,0,'',23),(19,'Direct Registration',0,0,0,'',24);
/*!40000 ALTER TABLE `account_direct_registration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_getresponseaccount`
--

DROP TABLE IF EXISTS `account_getresponseaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_getresponseaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `getresponse_username` varchar(100) DEFAULT NULL,
  `create_on` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_getresponsea_user_id_eed99f81_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_getresponseaccount`
--

LOCK TABLES `account_getresponseaccount` WRITE;
/*!40000 ALTER TABLE `account_getresponseaccount` DISABLE KEYS */;
INSERT INTO `account_getresponseaccount` VALUES (4,NULL,'2018-03-31 21:19:34.664428',11),(5,NULL,'2018-03-31 21:27:49.152142',12),(6,NULL,'2018-03-31 21:28:35.124100',13),(7,NULL,'2018-03-31 21:30:10.611090',14),(8,NULL,'2018-03-31 21:32:07.896826',15),(9,NULL,'2018-03-31 21:32:58.386846',16),(10,NULL,'2018-04-01 20:00:05.328210',17),(11,NULL,'2018-04-01 20:19:50.478601',18),(12,NULL,'2018-04-01 20:28:52.528373',19),(13,NULL,'2018-04-01 20:53:22.315035',20),(14,NULL,'2018-04-01 21:01:51.772496',21),(15,NULL,'2018-04-01 21:10:52.348077',22),(16,NULL,'2018-04-01 21:14:08.271242',23),(17,NULL,'2018-04-01 22:20:45.071563',24);
/*!40000 ALTER TABLE `account_getresponseaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_getresponseautoresponderaddcontact`
--

DROP TABLE IF EXISTS `account_getresponseautoresponderaddcontact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_getresponseautoresponderaddcontact` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `campaignId` varchar(30) DEFAULT NULL,
  `api_key` varchar(50) DEFAULT NULL,
  `isEnable` varchar(10) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_getresponsea_user_id_2e469703_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_getresponseautoresponderaddcontact`
--

LOCK TABLES `account_getresponseautoresponderaddcontact` WRITE;
/*!40000 ALTER TABLE `account_getresponseautoresponderaddcontact` DISABLE KEYS */;
INSERT INTO `account_getresponseautoresponderaddcontact` VALUES (4,'','','enable',11),(5,'','','enable',12),(6,'','','enable',13),(7,'','','enable',14),(8,'','','enable',15),(9,'','','enable',16),(10,'','','enable',17),(11,'','','enable',18),(12,'','','enable',19),(13,'','','enable',20),(14,'','','enable',21),(15,'','','enable',22),(16,'','','enable',23),(17,'','','enable',24);
/*!40000 ALTER TABLE `account_getresponseautoresponderaddcontact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_how_to_set_up_your_bethemillionaire_system`
--

DROP TABLE IF EXISTS `account_how_to_set_up_your_bethemillionaire_system`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_how_to_set_up_your_bethemillionaire_system` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `campaign_name` varchar(100) DEFAULT NULL,
  `visitors` int(11) DEFAULT NULL,
  `leads` int(11) DEFAULT NULL,
  `conversion_rate` int(11) DEFAULT NULL,
  `campaign_link` varchar(200) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_how_to_set_u_user_id_e67b9cc7_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_how_to_set_up_your_bethemillionaire_system`
--

LOCK TABLES `account_how_to_set_up_your_bethemillionaire_system` WRITE;
/*!40000 ALTER TABLE `account_how_to_set_up_your_bethemillionaire_system` DISABLE KEYS */;
INSERT INTO `account_how_to_set_up_your_bethemillionaire_system` VALUES (4,'How To Set Up Your BeTheMillionaire System',0,0,0,'',11),(5,'How To Set Up Your BeTheMillionaire System',3,0,0,'',12),(6,'How To Set Up Your BeTheMillionaire System',1,0,0,'',13),(7,'How To Set Up Your BeTheMillionaire System',0,0,0,'',14),(8,'How To Set Up Your BeTheMillionaire System',0,0,0,'',15),(9,'How To Set Up Your BeTheMillionaire System',0,0,0,'',16),(10,'How To Set Up Your BeTheMillionaire System',0,0,0,'',17),(11,'How To Set Up Your BeTheMillionaire System',0,0,0,'',18),(12,'How To Set Up Your BeTheMillionaire System',0,0,0,'',19),(13,'How To Set Up Your BeTheMillionaire System',0,0,0,'',20),(14,'How To Set Up Your BeTheMillionaire System',0,0,0,'',21),(15,'How To Set Up Your BeTheMillionaire System',0,0,0,'',22),(16,'How To Set Up Your BeTheMillionaire System',0,0,0,'',23),(17,'How To Set Up Your BeTheMillionaire System',0,0,0,'',24);
/*!40000 ALTER TABLE `account_how_to_set_up_your_bethemillionaire_system` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_indacoinaccount`
--

DROP TABLE IF EXISTS `account_indacoinaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_indacoinaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `indacoin_username` varchar(100) DEFAULT NULL,
  `create_on` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_indacoinacco_user_id_26271e88_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_indacoinaccount`
--

LOCK TABLES `account_indacoinaccount` WRITE;
/*!40000 ALTER TABLE `account_indacoinaccount` DISABLE KEYS */;
INSERT INTO `account_indacoinaccount` VALUES (4,NULL,'2018-03-31 21:19:34.726380',11),(5,NULL,'2018-03-31 21:27:49.208694',12),(6,NULL,'2018-03-31 21:28:35.177533',13),(7,NULL,'2018-03-31 21:30:10.650734',14),(8,NULL,'2018-03-31 21:32:07.947224',15),(9,NULL,'2018-03-31 21:32:58.429722',16),(10,NULL,'2018-04-01 20:00:05.428844',17),(11,NULL,'2018-04-01 20:19:50.536075',18),(12,NULL,'2018-04-01 20:28:52.579469',19),(13,NULL,'2018-04-01 20:53:22.377503',20),(14,NULL,'2018-04-01 21:01:51.843260',21),(15,NULL,'2018-04-01 21:10:52.400924',22),(16,NULL,'2018-04-01 21:14:08.317303',23),(17,NULL,'2018-04-01 22:20:45.151685',24);
/*!40000 ALTER TABLE `account_indacoinaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_latest_webinar_replay_btm`
--

DROP TABLE IF EXISTS `account_latest_webinar_replay_btm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_latest_webinar_replay_btm` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `campaign_name` varchar(100) DEFAULT NULL,
  `visitors` int(11) DEFAULT NULL,
  `leads` int(11) DEFAULT NULL,
  `conversion_rate` int(11) DEFAULT NULL,
  `campaign_link` varchar(200) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_latest_webin_user_id_62440029_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_latest_webinar_replay_btm`
--

LOCK TABLES `account_latest_webinar_replay_btm` WRITE;
/*!40000 ALTER TABLE `account_latest_webinar_replay_btm` DISABLE KEYS */;
INSERT INTO `account_latest_webinar_replay_btm` VALUES (4,'Latest Webinar Replay BTM',0,0,0,'',11),(5,'Latest Webinar Replay BTM',4,0,0,'',12),(6,'Latest Webinar Replay BTM',0,0,0,'',13),(7,'Latest Webinar Replay BTM',0,0,0,'',14),(8,'Latest Webinar Replay BTM',0,0,0,'',15),(9,'Latest Webinar Replay BTM',0,0,0,'',16),(10,'Latest Webinar Replay BTM',0,0,0,'',17),(11,'Latest Webinar Replay BTM',0,0,0,'',18),(12,'Latest Webinar Replay BTM',0,0,0,'',19),(13,'Latest Webinar Replay BTM',0,0,0,'',20),(14,'Latest Webinar Replay BTM',0,0,0,'',21),(15,'Latest Webinar Replay BTM',0,0,0,'',22),(16,'Latest Webinar Replay BTM',0,0,0,'',23),(17,'Latest Webinar Replay BTM',0,0,0,'',24);
/*!40000 ALTER TABLE `account_latest_webinar_replay_btm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_ledgernanosaccount`
--

DROP TABLE IF EXISTS `account_ledgernanosaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_ledgernanosaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ledger_nano_s_username` varchar(100) DEFAULT NULL,
  `create_on` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_ledgernanosa_user_id_8bbf822c_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_ledgernanosaccount`
--

LOCK TABLES `account_ledgernanosaccount` WRITE;
/*!40000 ALTER TABLE `account_ledgernanosaccount` DISABLE KEYS */;
INSERT INTO `account_ledgernanosaccount` VALUES (4,NULL,'2018-03-31 21:19:34.676633',11),(5,NULL,'2018-03-31 21:27:49.176056',12),(6,NULL,'2018-03-31 21:28:35.133466',13),(7,NULL,'2018-03-31 21:30:10.619189',14),(8,NULL,'2018-03-31 21:32:07.904975',15),(9,NULL,'2018-03-31 21:32:58.396039',16),(10,NULL,'2018-04-01 20:00:05.346973',17),(11,NULL,'2018-04-01 20:19:50.486415',18),(12,NULL,'2018-04-01 20:28:52.537459',19),(13,NULL,'2018-04-01 20:53:22.328836',20),(14,NULL,'2018-04-01 21:01:51.785037',21),(15,NULL,'2018-04-01 21:10:52.360506',22),(16,NULL,'2018-04-01 21:14:08.281727',23),(17,NULL,'2018-04-01 22:20:45.087908',24);
/*!40000 ALTER TABLE `account_ledgernanosaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_localbitcoinsaccount`
--

DROP TABLE IF EXISTS `account_localbitcoinsaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_localbitcoinsaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `local_bitcoins_username` varchar(100) DEFAULT NULL,
  `create_on` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_localbitcoin_user_id_35636f53_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_localbitcoinsaccount`
--

LOCK TABLES `account_localbitcoinsaccount` WRITE;
/*!40000 ALTER TABLE `account_localbitcoinsaccount` DISABLE KEYS */;
INSERT INTO `account_localbitcoinsaccount` VALUES (4,NULL,'2018-03-31 21:19:34.720468',11),(5,NULL,'2018-03-31 21:27:49.205256',12),(6,NULL,'2018-03-31 21:28:35.172552',13),(7,NULL,'2018-03-31 21:30:10.646608',14),(8,NULL,'2018-03-31 21:32:07.942583',15),(9,NULL,'2018-03-31 21:32:58.425372',16),(10,NULL,'2018-04-01 20:00:05.412978',17),(11,NULL,'2018-04-01 20:19:50.531459',18),(12,NULL,'2018-04-01 20:28:52.574119',19),(13,NULL,'2018-04-01 20:53:22.372875',20),(14,NULL,'2018-04-01 21:01:51.835471',21),(15,NULL,'2018-04-01 21:10:52.395459',22),(16,NULL,'2018-04-01 21:14:08.313583',23),(17,NULL,'2018-04-01 22:20:45.144364',24);
/*!40000 ALTER TABLE `account_localbitcoinsaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_membershiplevel`
--

DROP TABLE IF EXISTS `account_membershiplevel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_membershiplevel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `level` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `package` varchar(20) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_membershiplevel`
--

LOCK TABLES `account_membershiplevel` WRITE;
/*!40000 ALTER TABLE `account_membershiplevel` DISABLE KEYS */;
INSERT INTO `account_membershiplevel` VALUES (1,1,'free','free',0),(2,2,'premium','monthly',97),(3,3,'vip','monthly',297),(4,4,'premium','bi_annually',450),(5,5,'vip','bi_annually',1497),(6,6,'premium','yearly',850),(7,7,'vip','yearly',2497);
/*!40000 ALTER TABLE `account_membershiplevel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_mike_hobbs_usi_tech_team_webinar_90_bitcoins_in_6_months`
--

DROP TABLE IF EXISTS `account_mike_hobbs_usi_tech_team_webinar_90_bitcoins_in_6_months`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_mike_hobbs_usi_tech_team_webinar_90_bitcoins_in_6_months` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `campaign_name` varchar(100) DEFAULT NULL,
  `visitors` int(11) DEFAULT NULL,
  `leads` int(11) DEFAULT NULL,
  `conversion_rate` int(11) DEFAULT NULL,
  `campaign_link` varchar(200) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_mike_hobbs_u_user_id_a285cef4_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_mike_hobbs_usi_tech_team_webinar_90_bitcoins_in_6_months`
--

LOCK TABLES `account_mike_hobbs_usi_tech_team_webinar_90_bitcoins_in_6_months` WRITE;
/*!40000 ALTER TABLE `account_mike_hobbs_usi_tech_team_webinar_90_bitcoins_in_6_months` DISABLE KEYS */;
INSERT INTO `account_mike_hobbs_usi_tech_team_webinar_90_bitcoins_in_6_months` VALUES (4,'Mike Hobbs Usi-Tech Team Webinar (90 bitcoins in 6 months)',0,0,0,'',11),(5,'Mike Hobbs Usi-Tech Team Webinar (90 bitcoins in 6 months)',2,0,0,'',12),(6,'Mike Hobbs Usi-Tech Team Webinar (90 bitcoins in 6 months)',0,0,0,'',13),(7,'Mike Hobbs Usi-Tech Team Webinar (90 bitcoins in 6 months)',0,0,0,'',14),(8,'Mike Hobbs Usi-Tech Team Webinar (90 bitcoins in 6 months)',0,0,0,'',15),(9,'Mike Hobbs Usi-Tech Team Webinar (90 bitcoins in 6 months)',0,0,0,'',16),(10,'Mike Hobbs Usi-Tech Team Webinar (90 bitcoins in 6 months)',0,0,0,'',17),(11,'Mike Hobbs Usi-Tech Team Webinar (90 bitcoins in 6 months)',0,0,0,'',18),(12,'Mike Hobbs Usi-Tech Team Webinar (90 bitcoins in 6 months)',0,0,0,'',19),(13,'Mike Hobbs Usi-Tech Team Webinar (90 bitcoins in 6 months)',0,0,0,'',20),(14,'Mike Hobbs Usi-Tech Team Webinar (90 bitcoins in 6 months)',0,0,0,'',21),(15,'Mike Hobbs Usi-Tech Team Webinar (90 bitcoins in 6 months)',0,0,0,'',22),(16,'Mike Hobbs Usi-Tech Team Webinar (90 bitcoins in 6 months)',0,0,0,'',23),(17,'Mike Hobbs Usi-Tech Team Webinar (90 bitcoins in 6 months)',0,0,0,'',24);
/*!40000 ALTER TABLE `account_mike_hobbs_usi_tech_team_webinar_90_bitcoins_in_6_months` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_payment`
--

DROP TABLE IF EXISTS `account_payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_payment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `intent` varchar(50) DEFAULT NULL,
  `payer_ID` varchar(100) DEFAULT NULL,
  `payment_ID` varchar(100) DEFAULT NULL,
  `payment_Token` varchar(100) DEFAULT NULL,
  `is_verify` varchar(10) NOT NULL,
  `creation_time` datetime(6) NOT NULL,
  `membership_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `account_payment_membership_id_463338d5_fk_account_m` (`membership_id`),
  KEY `account_payment_user_id_af05f0c2_fk_account_userprofile_id` (`user_id`),
  CONSTRAINT `account_payment_membership_id_463338d5_fk_account_m` FOREIGN KEY (`membership_id`) REFERENCES `account_membershiplevel` (`id`),
  CONSTRAINT `account_payment_user_id_af05f0c2_fk_account_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_payment`
--

LOCK TABLES `account_payment` WRITE;
/*!40000 ALTER TABLE `account_payment` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_preregistration`
--

DROP TABLE IF EXISTS `account_preregistration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_preregistration` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_preregistration`
--

LOCK TABLES `account_preregistration` WRITE;
/*!40000 ALTER TABLE `account_preregistration` DISABLE KEYS */;
INSERT INTO `account_preregistration` VALUES (1,'nnnn@gmail.com'),(2,'zzz@gmail.com'),(3,'sjdf@gmail.com'),(4,'sjkdbk@gmail.com'),(5,'sdlkmskl@jh.com'),(6,'lsdnskjldnslknd@hmail.com');
/*!40000 ALTER TABLE `account_preregistration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_spectrocoincardaccount`
--

DROP TABLE IF EXISTS `account_spectrocoincardaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_spectrocoincardaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `spectrocoin_card_username` varchar(100) DEFAULT NULL,
  `create_on` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_spectrocoinc_user_id_f895b764_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_spectrocoincardaccount`
--

LOCK TABLES `account_spectrocoincardaccount` WRITE;
/*!40000 ALTER TABLE `account_spectrocoincardaccount` DISABLE KEYS */;
INSERT INTO `account_spectrocoincardaccount` VALUES (4,NULL,'2018-03-31 21:19:34.696245',11),(5,NULL,'2018-03-31 21:27:49.189036',12),(6,NULL,'2018-03-31 21:28:35.152607',13),(7,NULL,'2018-03-31 21:30:10.629846',14),(8,NULL,'2018-03-31 21:32:07.923539',15),(9,NULL,'2018-03-31 21:32:58.408369',16),(10,NULL,'2018-04-01 20:00:05.372670',17),(11,NULL,'2018-04-01 20:19:50.505818',18),(12,NULL,'2018-04-01 20:28:52.554982',19),(13,NULL,'2018-04-01 20:53:22.347818',20),(14,NULL,'2018-04-01 21:01:51.809867',21),(15,NULL,'2018-04-01 21:10:52.377275',22),(16,NULL,'2018-04-01 21:14:08.295211',23),(17,NULL,'2018-04-01 22:20:45.115522',24);
/*!40000 ALTER TABLE `account_spectrocoincardaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_trezorsaccount`
--

DROP TABLE IF EXISTS `account_trezorsaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_trezorsaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `trezor_username` varchar(100) DEFAULT NULL,
  `create_on` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_trezorsaccou_user_id_25247dfd_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_trezorsaccount`
--

LOCK TABLES `account_trezorsaccount` WRITE;
/*!40000 ALTER TABLE `account_trezorsaccount` DISABLE KEYS */;
INSERT INTO `account_trezorsaccount` VALUES (4,NULL,'2018-03-31 21:19:34.682622',11),(5,NULL,'2018-03-31 21:27:49.180251',12),(6,NULL,'2018-03-31 21:28:35.141338',13),(7,NULL,'2018-03-31 21:30:10.621908',14),(8,NULL,'2018-03-31 21:32:07.909609',15),(9,NULL,'2018-03-31 21:32:58.399554',16),(10,NULL,'2018-04-01 20:00:05.354871',17),(11,NULL,'2018-04-01 20:19:50.494843',18),(12,NULL,'2018-04-01 20:28:52.546119',19),(13,NULL,'2018-04-01 20:53:22.336134',20),(14,NULL,'2018-04-01 21:01:51.794213',21),(15,NULL,'2018-04-01 21:10:52.365530',22),(16,NULL,'2018-04-01 21:14:08.285979',23),(17,NULL,'2018-04-01 22:20:45.096110',24);
/*!40000 ALTER TABLE `account_trezorsaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_userprofile`
--

DROP TABLE IF EXISTS `account_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone_number` varchar(18) DEFAULT NULL,
  `website` varchar(400) DEFAULT NULL,
  `facebook` varchar(100) DEFAULT NULL,
  `skype` varchar(100) DEFAULT NULL,
  `profile_picture` varchar(100) DEFAULT NULL,
  `join_date` datetime(6) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `membership_id` int(11),
  `sponsor_id` int(11),
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  KEY `account_userprofile_sponsor_id_6a9d63dd_fk_account_u` (`sponsor_id`),
  KEY `account_userprofile_membership_id_35066d79_fk_account_m` (`membership_id`),
  CONSTRAINT `account_userprofile_membership_id_35066d79_fk_account_m` FOREIGN KEY (`membership_id`) REFERENCES `account_membershiplevel` (`id`),
  CONSTRAINT `account_userprofile_sponsor_id_6a9d63dd_fk_account_u` FOREIGN KEY (`sponsor_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_userprofile`
--

LOCK TABLES `account_userprofile` WRITE;
/*!40000 ALTER TABLE `account_userprofile` DISABLE KEYS */;
INSERT INTO `account_userprofile` VALUES (11,'pbkdf2_sha256$36000$8PC7zSbacM0p$zrvM4uQbOj0oXGPbA9T7GeNELZ1CSy2WViamicX1bSg=','2018-03-31 21:21:04.807572',1,'ddd','ddd@gmail.com',NULL,NULL,NULL,NULL,'','2018-03-31 21:19:34.525391',1,1,NULL,NULL),(12,'pbkdf2_sha256$36000$bjK2v6ZNqUIe$YQyAOg3/KkaTfLUiJAjJusHPQT/8bH6ZqfmRyNCeA7w=','2018-04-03 14:22:42.030848',1,'admin','admin@gmail.com','019742658881','www.asokti1.com','mubarak','mubarak','images/user/2018-02-06-19-13-34-557_KcD9SRa.jpg','2018-03-31 21:27:49.074366',1,1,1,12),(13,'pbkdf2_sha256$36000$0XUVaqJxcgQw$yfVs49bM4QlUJl3YpnruwL5/7nIKDXZTHGMebUvKBrw=',NULL,0,'nnn','nnnn@gmail.com',NULL,NULL,NULL,NULL,'','2018-03-31 21:28:35.004692',1,0,NULL,12),(14,'pbkdf2_sha256$36000$2x68aPr8ZPJ8$8P9ADmO8gjed5cCdObUVGDbu71qoewvve9ni3Eqye1I=',NULL,0,'mmm','mmmm@gmail.com',NULL,NULL,NULL,NULL,'','2018-03-31 21:30:10.517107',1,0,NULL,12),(15,'pbkdf2_sha256$36000$DU9szErPCzFv$lqZAGOvhUpQ9AsMORZQ4rrPCBqbU64joRIdDuEXR9jM=',NULL,0,'ppp','ppp@gmail.com',NULL,NULL,NULL,NULL,'','2018-03-31 21:32:07.793201',1,0,NULL,12),(16,'pbkdf2_sha256$36000$GveMb6kTmb7y$qvetxXxdzmXNDOe6GQqS3q/dk53cLwmOlkOCz3496+M=',NULL,0,'qqq','qqqq@gmail.com',NULL,NULL,NULL,NULL,'','2018-03-31 21:32:58.299795',1,0,1,12),(17,'pbkdf2_sha256$36000$jWTCe5eNsE94$UZCcXoHwuSn9z7enAitN0WPF8QBBCpBadwPZEg0ugH4=',NULL,0,'aaa','aaa@gmail.com',NULL,NULL,NULL,NULL,'','2018-04-01 20:00:05.148603',1,0,1,12),(18,'pbkdf2_sha256$36000$dvirI5mbErQQ$SbH6AHU2Ys4vtrT0llO430MuMPy/XbqrvsW7AbEPvg4=',NULL,0,'jsdhnfk','kjsbdf@gmail.com',NULL,NULL,NULL,NULL,'','2018-04-01 20:19:50.363909',1,0,1,12),(19,'pbkdf2_sha256$36000$eavuX39eDBYb$Qh10dlCnpYWTwDKVPxyaGe6xmk0RUH1ABYEnsEgDAUQ=',NULL,0,'ujsdhfik','snfs@gmail.com',NULL,NULL,NULL,NULL,'','2018-04-01 20:28:52.421754',1,0,1,12),(20,'pbkdf2_sha256$36000$0tnwlAAcN2rV$Wy1iYpWrKA6xhAkL7AN84INUiNXHN8USNXz7B3ue8e8=',NULL,0,'sajkfsjdk','skdbj@gmail.com',NULL,NULL,NULL,NULL,'','2018-04-01 20:53:22.148666',1,0,1,12),(21,'pbkdf2_sha256$36000$DbSxcBNlscBx$4504PYS8M5LBzvkOomh6v6HKxnoNrQoO8SxEz5FbV/8=',NULL,0,'sldn','kjsdfb@gmail.com',NULL,NULL,NULL,NULL,'','2018-04-01 21:01:51.652478',1,0,1,12),(22,'pbkdf2_sha256$36000$zXqrtNIZSfgC$s/HNShQODMhFhoTbAVkIYj+5Bmcer2rgKwf/OKNeiqU=',NULL,0,'kjasbshab','sjdfnksdj@gmail.com',NULL,NULL,NULL,NULL,'','2018-04-01 21:10:52.225912',1,0,1,12),(23,'pbkdf2_sha256$36000$IXAYz3Z15J3N$u2/flP/jaLFkjRPVI3gSWFruMnA+jq6UAO8TFv9d13g=',NULL,0,'kjasbshab1','sjdfnksdj1@gmail.com',NULL,NULL,NULL,NULL,'','2018-04-01 21:14:08.128191',1,0,1,12),(24,'pbkdf2_sha256$36000$6LF2bymRJ1PT$IAB4udTwV/x8VBdH7nKr3TNoDW73ym68jxFlK97CzKU=',NULL,0,'kldnskj','ksdjfkj@gmail.com',NULL,NULL,NULL,NULL,'','2018-04-01 22:20:44.917503',1,0,1,16);
/*!40000 ALTER TABLE `account_userprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_userprofile_groups`
--

DROP TABLE IF EXISTS `account_userprofile_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_userprofile_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_userprofile_groups_userprofile_id_group_id_4df7adaa_uniq` (`userprofile_id`,`group_id`),
  KEY `account_userprofile_groups_group_id_211ffaa0_fk_auth_group_id` (`group_id`),
  CONSTRAINT `account_userprofile__userprofile_id_7ead1ac5_fk_account_u` FOREIGN KEY (`userprofile_id`) REFERENCES `account_userprofile` (`id`),
  CONSTRAINT `account_userprofile_groups_group_id_211ffaa0_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_userprofile_groups`
--

LOCK TABLES `account_userprofile_groups` WRITE;
/*!40000 ALTER TABLE `account_userprofile_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_userprofile_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_userprofile_referrals`
--

DROP TABLE IF EXISTS `account_userprofile_referrals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_userprofile_referrals` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_userprofile_id` int(11) NOT NULL,
  `to_userprofile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_userprofile_refe_from_userprofile_id_to_u_66a0dacf_uniq` (`from_userprofile_id`,`to_userprofile_id`),
  KEY `account_userprofile__to_userprofile_id_6486cc32_fk_account_u` (`to_userprofile_id`),
  CONSTRAINT `account_userprofile__from_userprofile_id_f94807e3_fk_account_u` FOREIGN KEY (`from_userprofile_id`) REFERENCES `account_userprofile` (`id`),
  CONSTRAINT `account_userprofile__to_userprofile_id_6486cc32_fk_account_u` FOREIGN KEY (`to_userprofile_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_userprofile_referrals`
--

LOCK TABLES `account_userprofile_referrals` WRITE;
/*!40000 ALTER TABLE `account_userprofile_referrals` DISABLE KEYS */;
INSERT INTO `account_userprofile_referrals` VALUES (7,12,13),(8,12,14),(9,12,15),(10,12,16),(11,12,17),(12,12,18),(13,12,19),(14,12,20),(15,12,21),(16,12,22),(17,12,23),(18,16,15),(19,16,24);
/*!40000 ALTER TABLE `account_userprofile_referrals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_userprofile_user_permissions`
--

DROP TABLE IF EXISTS `account_userprofile_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_userprofile_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_userprofile_user_userprofile_id_permissio_856edf21_uniq` (`userprofile_id`,`permission_id`),
  KEY `account_userprofile__permission_id_0ca2725a_fk_auth_perm` (`permission_id`),
  CONSTRAINT `account_userprofile__permission_id_0ca2725a_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `account_userprofile__userprofile_id_d6f0e4ab_fk_account_u` FOREIGN KEY (`userprofile_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_userprofile_user_permissions`
--

LOCK TABLES `account_userprofile_user_permissions` WRITE;
/*!40000 ALTER TABLE `account_userprofile_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_userprofile_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_usi_tech_7_figure_plan_in_2018`
--

DROP TABLE IF EXISTS `account_usi_tech_7_figure_plan_in_2018`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_usi_tech_7_figure_plan_in_2018` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `campaign_name` varchar(100) DEFAULT NULL,
  `visitors` int(11) DEFAULT NULL,
  `leads` int(11) DEFAULT NULL,
  `conversion_rate` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_usi_tech_7_f_user_id_8d52d354_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_usi_tech_7_figure_plan_in_2018`
--

LOCK TABLES `account_usi_tech_7_figure_plan_in_2018` WRITE;
/*!40000 ALTER TABLE `account_usi_tech_7_figure_plan_in_2018` DISABLE KEYS */;
INSERT INTO `account_usi_tech_7_figure_plan_in_2018` VALUES (4,'Usi Tech 7 Figure Plan In 2018!',0,0,0,11),(5,'Usi Tech 7 Figure Plan In 2018!',2,0,0,12),(6,'Usi Tech 7 Figure Plan In 2018!',0,0,0,13),(7,'Usi Tech 7 Figure Plan In 2018!',0,0,0,14),(8,'Usi Tech 7 Figure Plan In 2018!',0,0,0,15),(9,'Usi Tech 7 Figure Plan In 2018!',0,0,0,16),(10,'Usi Tech 7 Figure Plan In 2018!',0,0,0,17),(11,'Usi Tech 7 Figure Plan In 2018!',0,0,0,18),(12,'Usi Tech 7 Figure Plan In 2018!',0,0,0,19),(13,'Usi Tech 7 Figure Plan In 2018!',0,0,0,20),(14,'Usi Tech 7 Figure Plan In 2018!',0,0,0,21),(15,'Usi Tech 7 Figure Plan In 2018!',0,0,0,22),(16,'Usi Tech 7 Figure Plan In 2018!',0,0,0,23),(17,'Usi Tech 7 Figure Plan In 2018!',0,0,0,24);
/*!40000 ALTER TABLE `account_usi_tech_7_figure_plan_in_2018` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_usi_tech_btc_packages_calculator`
--

DROP TABLE IF EXISTS `account_usi_tech_btc_packages_calculator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_usi_tech_btc_packages_calculator` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `campaign_name` varchar(100) DEFAULT NULL,
  `visitors` int(11) DEFAULT NULL,
  `leads` int(11) DEFAULT NULL,
  `conversion_rate` int(11) DEFAULT NULL,
  `campaign_link` varchar(200) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_usi_tech_btc_user_id_2f9a83e6_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_usi_tech_btc_packages_calculator`
--

LOCK TABLES `account_usi_tech_btc_packages_calculator` WRITE;
/*!40000 ALTER TABLE `account_usi_tech_btc_packages_calculator` DISABLE KEYS */;
INSERT INTO `account_usi_tech_btc_packages_calculator` VALUES (4,'USI-TECH BTC-Packages Calculator',0,0,0,'',11),(5,'USI-TECH BTC-Packages Calculator',0,0,0,'',12),(6,'USI-TECH BTC-Packages Calculator',0,0,0,'',13),(7,'USI-TECH BTC-Packages Calculator',0,0,0,'',14),(8,'USI-TECH BTC-Packages Calculator',0,0,0,'',15),(9,'USI-TECH BTC-Packages Calculator',0,0,0,'',16),(10,'USI-TECH BTC-Packages Calculator',0,0,0,'',17),(11,'USI-TECH BTC-Packages Calculator',0,0,0,'',18),(12,'USI-TECH BTC-Packages Calculator',0,0,0,'',19),(13,'USI-TECH BTC-Packages Calculator',0,0,0,'',20),(14,'USI-TECH BTC-Packages Calculator',0,0,0,'',21),(15,'USI-TECH BTC-Packages Calculator',0,0,0,'',22),(16,'USI-TECH BTC-Packages Calculator',0,0,0,'',23),(17,'USI-TECH BTC-Packages Calculator',0,0,0,'',24);
/*!40000 ALTER TABLE `account_usi_tech_btc_packages_calculator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_usi_tech_direct_funnel`
--

DROP TABLE IF EXISTS `account_usi_tech_direct_funnel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_usi_tech_direct_funnel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `campaign_name` varchar(100) DEFAULT NULL,
  `visitors` int(11) DEFAULT NULL,
  `leads` int(11) DEFAULT NULL,
  `conversion_rate` int(11) DEFAULT NULL,
  `campaign_link` varchar(200) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_usi_tech_dir_user_id_0a0d86c0_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_usi_tech_direct_funnel`
--

LOCK TABLES `account_usi_tech_direct_funnel` WRITE;
/*!40000 ALTER TABLE `account_usi_tech_direct_funnel` DISABLE KEYS */;
INSERT INTO `account_usi_tech_direct_funnel` VALUES (4,'Usi-Tech Direct Funnel',0,0,0,'',11),(5,'Usi-Tech Direct Funnel',2,0,0,'',12),(6,'Usi-Tech Direct Funnel',0,0,0,'',13),(7,'Usi-Tech Direct Funnel',0,0,0,'',14),(8,'Usi-Tech Direct Funnel',0,0,0,'',15),(9,'Usi-Tech Direct Funnel',0,0,0,'',16),(10,'Usi-Tech Direct Funnel',0,0,0,'',17),(11,'Usi-Tech Direct Funnel',0,0,0,'',18),(12,'Usi-Tech Direct Funnel',0,0,0,'',19),(13,'Usi-Tech Direct Funnel',0,0,0,'',20),(14,'Usi-Tech Direct Funnel',0,0,0,'',21),(15,'Usi-Tech Direct Funnel',0,0,0,'',22),(16,'Usi-Tech Direct Funnel',0,0,0,'',23),(17,'Usi-Tech Direct Funnel',0,0,0,'',24);
/*!40000 ALTER TABLE `account_usi_tech_direct_funnel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_usi_tech_funnel`
--

DROP TABLE IF EXISTS `account_usi_tech_funnel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_usi_tech_funnel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `campaign_name` varchar(100) DEFAULT NULL,
  `visitors` int(11) DEFAULT NULL,
  `leads` int(11) DEFAULT NULL,
  `conversion_rate` int(11) DEFAULT NULL,
  `campaign_link` varchar(200) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_usi_tech_fun_user_id_ffa9288d_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_usi_tech_funnel`
--

LOCK TABLES `account_usi_tech_funnel` WRITE;
/*!40000 ALTER TABLE `account_usi_tech_funnel` DISABLE KEYS */;
INSERT INTO `account_usi_tech_funnel` VALUES (4,'Usi-Tech Funnel',0,0,0,'',11),(5,'Usi-Tech Funnel',3,2,0,'',12),(6,'Usi-Tech Funnel',0,0,0,'',13),(7,'Usi-Tech Funnel',0,0,0,'',14),(8,'Usi-Tech Funnel',0,0,0,'',15),(9,'Usi-Tech Funnel',0,0,0,'',16),(10,'Usi-Tech Funnel',0,0,0,'',17),(11,'Usi-Tech Funnel',0,0,0,'',18),(12,'Usi-Tech Funnel',0,0,0,'',19),(13,'Usi-Tech Funnel',0,0,0,'',20),(14,'Usi-Tech Funnel',0,0,0,'',21),(15,'Usi-Tech Funnel',0,0,0,'',22),(16,'Usi-Tech Funnel',0,0,0,'',23),(17,'Usi-Tech Funnel',0,0,0,'',24);
/*!40000 ALTER TABLE `account_usi_tech_funnel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_usitechaccount`
--

DROP TABLE IF EXISTS `account_usitechaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_usitechaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usi_username` varchar(100) DEFAULT NULL,
  `create_on` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_usitechaccou_user_id_c166210e_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_usitechaccount`
--

LOCK TABLES `account_usitechaccount` WRITE;
/*!40000 ALTER TABLE `account_usitechaccount` DISABLE KEYS */;
INSERT INTO `account_usitechaccount` VALUES (4,NULL,'2018-03-31 21:19:34.638460',11),(5,'nnnn','2018-03-31 21:27:49.139596',12),(6,NULL,'2018-03-31 21:28:35.100627',13),(7,NULL,'2018-03-31 21:30:10.592283',14),(8,NULL,'2018-03-31 21:32:07.873639',15),(9,NULL,'2018-03-31 21:32:58.369871',16),(10,NULL,'2018-04-01 20:00:05.288905',17),(11,NULL,'2018-04-01 20:19:50.452354',18),(12,NULL,'2018-04-01 20:28:52.508082',19),(13,NULL,'2018-04-01 20:53:22.286787',20),(14,NULL,'2018-04-01 21:01:51.742952',21),(15,NULL,'2018-04-01 21:10:52.320002',22),(16,NULL,'2018-04-01 21:14:08.246962',23),(17,NULL,'2018-04-01 22:20:45.034707',24);
/*!40000 ALTER TABLE `account_usitechaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `administration_videolink`
--

DROP TABLE IF EXISTS `administration_videolink`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `administration_videolink` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lesson_name` varchar(255) DEFAULT NULL,
  `video_link` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administration_videolink`
--

LOCK TABLES `administration_videolink` WRITE;
/*!40000 ALTER TABLE `administration_videolink` DISABLE KEYS */;
INSERT INTO `administration_videolink` VALUES (1,'m_1_l_1','<iframe width=\"100%\" height=\"100%\" src=\"https://www.youtube.com/embed/SULM_ZuVs2s\" frameborder=\"0\" allow=\"autoplay; encrypted-media\" allowfullscreen></iframe>'),(2,'m_1_l_2','<iframe width=\"100%\" height=\"100%\" src=\"https://www.youtube.com/embed/oO1x6iwyomI\" frameborder=\"0\" allow=\"autoplay; encrypted-media\" allowfullscreen></iframe>'),(3,'m_2_l_1','<iframe width=\"100%\" height=\"100%\" src=\"https://www.youtube.com/embed/XDUwNE01Dhc\" frameborder=\"0\" gesture=\"media\" allow=\"encrypted-media\" autoplay=\"true\" allowfullscreen></iframe>'),(4,'m_2_l_2','<iframe width=\"100%\" height=\"100%\" src=\"https://www.youtube.com/embed/w8ezovecv_k\" frameborder=\"0\" gesture=\"media\" allow=\"encrypted-media\" autoplay=\"true\" allowfullscreen></iframe>'),(5,'m_2_l_3','<iframe width=\"100%\" height=\"100%\" src=\"https://www.youtube.com/embed/tUKOf_Otsx8\" frameborder=\"0\" gesture=\"media\" allow=\"encrypted-media\" autoplay=\"true\" allowfullscreen></iframe>'),(6,'m_2_l_4','<iframe width=\"100%\" height=\"100%\" src=\"https://www.youtube.com/embed/FGFk44Dxdpw\" frameborder=\"0\" gesture=\"media\" allow=\"encrypted-media\" autoplay=\"true\" allowfullscreen></iframe>'),(7,'m_3_l_1','<iframe width=\"100%\" height=\"100%\" src=\"https://www.youtube.com/embed/PBKCiuTNSsI\" frameborder=\"0\" allow=\"autoplay; encrypted-media\" allowfullscreen></iframe>'),(8,'m_3_l_2','<iframe width=\"100%\" height=\"100%\" src=\"https://www.youtube.com/embed/i8RvRUH81uQ\" frameborder=\"0\" allow=\"autoplay; encrypted-media\" allowfullscreen></iframe>'),(9,'m_3_l_3','<iframe width=\"100%\" height=\"100%\" src=\"https://www.youtube.com/embed/LZQD6ubnsBk\" frameborder=\"0\" allow=\"autoplay; encrypted-media\" allowfullscreen></iframe>');
/*!40000 ALTER TABLE `administration_videolink` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=151 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add PayPal IPN',6,'add_paypalipn'),(17,'Can change PayPal IPN',6,'change_paypalipn'),(18,'Can delete PayPal IPN',6,'delete_paypalipn'),(19,'Can add affiliate link control',7,'add_affiliatelinkcontrol'),(20,'Can change affiliate link control',7,'change_affiliatelinkcontrol'),(21,'Can delete affiliate link control',7,'delete_affiliatelinkcontrol'),(22,'Can add user profile',8,'add_userprofile'),(23,'Can change user profile',8,'change_userprofile'),(24,'Can delete user profile',8,'delete_userprofile'),(25,'Can add automated_ webinar_ funnel_ version_1',9,'add_automated_webinar_funnel_version_1'),(26,'Can change automated_ webinar_ funnel_ version_1',9,'change_automated_webinar_funnel_version_1'),(27,'Can delete automated_ webinar_ funnel_ version_1',9,'delete_automated_webinar_funnel_version_1'),(28,'Can add automated_ webinar_ funnel_ version_2',10,'add_automated_webinar_funnel_version_2'),(29,'Can change automated_ webinar_ funnel_ version_2',10,'change_automated_webinar_funnel_version_2'),(30,'Can delete automated_ webinar_ funnel_ version_2',10,'delete_automated_webinar_funnel_version_2'),(31,'Can add aweber account',11,'add_aweberaccount'),(32,'Can change aweber account',11,'change_aweberaccount'),(33,'Can delete aweber account',11,'delete_aweberaccount'),(34,'Can add be the millionaire_3_ step_ registration_ funnel',12,'add_bethemillionaire_3_step_registration_funnel'),(35,'Can change be the millionaire_3_ step_ registration_ funnel',12,'change_bethemillionaire_3_step_registration_funnel'),(36,'Can delete be the millionaire_3_ step_ registration_ funnel',12,'delete_bethemillionaire_3_step_registration_funnel'),(37,'Can add bitconnect_ direct_ funnel',13,'add_bitconnect_direct_funnel'),(38,'Can change bitconnect_ direct_ funnel',13,'change_bitconnect_direct_funnel'),(39,'Can delete bitconnect_ direct_ funnel',13,'delete_bitconnect_direct_funnel'),(40,'Can add bitconnect account',14,'add_bitconnectaccount'),(41,'Can change bitconnect account',14,'change_bitconnectaccount'),(42,'Can delete bitconnect account',14,'delete_bitconnectaccount'),(43,'Can add bit panda account',15,'add_bitpandaaccount'),(44,'Can change bit panda account',15,'change_bitpandaaccount'),(45,'Can delete bit panda account',15,'delete_bitpandaaccount'),(46,'Can add cex io account',16,'add_cexioaccount'),(47,'Can change cex io account',16,'change_cexioaccount'),(48,'Can delete cex io account',16,'delete_cexioaccount'),(49,'Can add click funnels account',17,'add_clickfunnelsaccount'),(50,'Can change click funnels account',17,'change_clickfunnelsaccount'),(51,'Can delete click funnels account',17,'delete_clickfunnelsaccount'),(52,'Can add click magic account',18,'add_clickmagicaccount'),(53,'Can change click magic account',18,'change_clickmagicaccount'),(54,'Can delete click magic account',18,'delete_clickmagicaccount'),(55,'Can add coin base account',19,'add_coinbaseaccount'),(56,'Can change coin base account',19,'change_coinbaseaccount'),(57,'Can delete coin base account',19,'delete_coinbaseaccount'),(58,'Can add coin mama account',20,'add_coinmamaaccount'),(59,'Can change coin mama account',20,'change_coinmamaaccount'),(60,'Can delete coin mama account',20,'delete_coinmamaaccount'),(61,'Can add course_ giveaway_3_ steps_ funnel',21,'add_course_giveaway_3_steps_funnel'),(62,'Can change course_ giveaway_3_ steps_ funnel',21,'change_course_giveaway_3_steps_funnel'),(63,'Can delete course_ giveaway_3_ steps_ funnel',21,'delete_course_giveaway_3_steps_funnel'),(64,'Can add course_ giveaway_ direct_ registration',22,'add_course_giveaway_direct_registration'),(65,'Can change course_ giveaway_ direct_ registration',22,'change_course_giveaway_direct_registration'),(66,'Can delete course_ giveaway_ direct_ registration',22,'delete_course_giveaway_direct_registration'),(67,'Can add crypto pay card account',23,'add_cryptopaycardaccount'),(68,'Can change crypto pay card account',23,'change_cryptopaycardaccount'),(69,'Can delete crypto pay card account',23,'delete_cryptopaycardaccount'),(70,'Can add direct_ registration',24,'add_direct_registration'),(71,'Can change direct_ registration',24,'change_direct_registration'),(72,'Can delete direct_ registration',24,'delete_direct_registration'),(73,'Can add get response account',25,'add_getresponseaccount'),(74,'Can change get response account',25,'change_getresponseaccount'),(75,'Can delete get response account',25,'delete_getresponseaccount'),(76,'Can add get response autoresponder add contact',26,'add_getresponseautoresponderaddcontact'),(77,'Can change get response autoresponder add contact',26,'change_getresponseautoresponderaddcontact'),(78,'Can delete get response autoresponder add contact',26,'delete_getresponseautoresponderaddcontact'),(79,'Can add how_ to_ set_ up_ your_ be the millionaire_ system',27,'add_how_to_set_up_your_bethemillionaire_system'),(80,'Can change how_ to_ set_ up_ your_ be the millionaire_ system',27,'change_how_to_set_up_your_bethemillionaire_system'),(81,'Can delete how_ to_ set_ up_ your_ be the millionaire_ system',27,'delete_how_to_set_up_your_bethemillionaire_system'),(82,'Can add inda coin account',28,'add_indacoinaccount'),(83,'Can change inda coin account',28,'change_indacoinaccount'),(84,'Can delete inda coin account',28,'delete_indacoinaccount'),(85,'Can add latest_ webinar_ replay_btm',29,'add_latest_webinar_replay_btm'),(86,'Can change latest_ webinar_ replay_btm',29,'change_latest_webinar_replay_btm'),(87,'Can delete latest_ webinar_ replay_btm',29,'delete_latest_webinar_replay_btm'),(88,'Can add ledger nano s account',30,'add_ledgernanosaccount'),(89,'Can change ledger nano s account',30,'change_ledgernanosaccount'),(90,'Can delete ledger nano s account',30,'delete_ledgernanosaccount'),(91,'Can add local bitcoins account',31,'add_localbitcoinsaccount'),(92,'Can change local bitcoins account',31,'change_localbitcoinsaccount'),(93,'Can delete local bitcoins account',31,'delete_localbitcoinsaccount'),(94,'Can add membershiplevel',32,'add_membershiplevel'),(95,'Can change membershiplevel',32,'change_membershiplevel'),(96,'Can delete membershiplevel',32,'delete_membershiplevel'),(97,'Can add mike_ hobbs_ usi_ tech_ team_ webinar_90_bitcoins_in_6_months',33,'add_mike_hobbs_usi_tech_team_webinar_90_bitcoins_in_6_months'),(98,'Can change mike_ hobbs_ usi_ tech_ team_ webinar_90_bitcoins_in_6_months',33,'change_mike_hobbs_usi_tech_team_webinar_90_bitcoins_in_6_months'),(99,'Can delete mike_ hobbs_ usi_ tech_ team_ webinar_90_bitcoins_in_6_months',33,'delete_mike_hobbs_usi_tech_team_webinar_90_bitcoins_in_6_months'),(100,'Can add payment',34,'add_payment'),(101,'Can change payment',34,'change_payment'),(102,'Can delete payment',34,'delete_payment'),(103,'Can add preregistration',35,'add_preregistration'),(104,'Can change preregistration',35,'change_preregistration'),(105,'Can delete preregistration',35,'delete_preregistration'),(106,'Can add spectro coin card account',36,'add_spectrocoincardaccount'),(107,'Can change spectro coin card account',36,'change_spectrocoincardaccount'),(108,'Can delete spectro coin card account',36,'delete_spectrocoincardaccount'),(109,'Can add trezor s account',37,'add_trezorsaccount'),(110,'Can change trezor s account',37,'change_trezorsaccount'),(111,'Can delete trezor s account',37,'delete_trezorsaccount'),(112,'Can add usi_ tech_7_ figure_ plan_ in_2018',38,'add_usi_tech_7_figure_plan_in_2018'),(113,'Can change usi_ tech_7_ figure_ plan_ in_2018',38,'change_usi_tech_7_figure_plan_in_2018'),(114,'Can delete usi_ tech_7_ figure_ plan_ in_2018',38,'delete_usi_tech_7_figure_plan_in_2018'),(115,'Can add usi_ tech_ btc_ packages_ calculator',39,'add_usi_tech_btc_packages_calculator'),(116,'Can change usi_ tech_ btc_ packages_ calculator',39,'change_usi_tech_btc_packages_calculator'),(117,'Can delete usi_ tech_ btc_ packages_ calculator',39,'delete_usi_tech_btc_packages_calculator'),(118,'Can add usi_ tech_ direct_ funnel',40,'add_usi_tech_direct_funnel'),(119,'Can change usi_ tech_ direct_ funnel',40,'change_usi_tech_direct_funnel'),(120,'Can delete usi_ tech_ direct_ funnel',40,'delete_usi_tech_direct_funnel'),(121,'Can add usi_ tech_ funnel',41,'add_usi_tech_funnel'),(122,'Can change usi_ tech_ funnel',41,'change_usi_tech_funnel'),(123,'Can delete usi_ tech_ funnel',41,'delete_usi_tech_funnel'),(124,'Can add usi tech account',42,'add_usitechaccount'),(125,'Can change usi tech account',42,'change_usitechaccount'),(126,'Can delete usi tech account',42,'delete_usitechaccount'),(127,'Can add comment',43,'add_comment'),(128,'Can change comment',43,'change_comment'),(129,'Can delete comment',43,'delete_comment'),(130,'Can add note',44,'add_note'),(131,'Can change note',44,'change_note'),(132,'Can delete note',44,'delete_note'),(133,'Can add step control',45,'add_stepcontrol'),(134,'Can change step control',45,'change_stepcontrol'),(135,'Can delete step control',45,'delete_stepcontrol'),(136,'Can add sub comment',46,'add_subcomment'),(137,'Can change sub comment',46,'change_subcomment'),(138,'Can delete sub comment',46,'delete_subcomment'),(139,'Can add lesson',47,'add_lesson'),(140,'Can change lesson',47,'change_lesson'),(141,'Can delete lesson',47,'delete_lesson'),(142,'Can add module',48,'add_module'),(143,'Can change module',48,'change_module'),(144,'Can delete module',48,'delete_module'),(145,'Can add step',49,'add_step'),(146,'Can change step',49,'change_step'),(147,'Can delete step',49,'delete_step'),(148,'Can add video link',50,'add_videolink'),(149,'Can change video link',50,'change_videolink'),(150,'Can delete video link',50,'delete_videolink');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_account_userprofile_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_account_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=86 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (25,'2018-03-31 21:24:30.485020','1','admin',3,'',8,11),(26,'2018-03-31 21:34:52.281189','12','admin',2,'[{\"changed\": {\"fields\": [\"membership\", \"sponsor\", \"phone_number\", \"website\", \"facebook\", \"skype\", \"profile_picture\"]}}]',8,12),(27,'2018-04-01 22:20:10.881123','16','qqq',2,'[{\"changed\": {\"fields\": [\"referrals\"]}}]',8,12),(28,'2018-04-02 19:57:26.655053','1','affiliate-link-1',1,'[{\"added\": {}}]',7,12),(29,'2018-04-02 19:57:44.934057','2','affiliate-link-2',1,'[{\"added\": {}}]',7,12),(30,'2018-04-02 19:58:01.334322','3','affiliate-link-3',1,'[{\"added\": {}}]',7,12),(31,'2018-04-02 19:59:02.485349','4','affiliate-link-4',1,'[{\"added\": {}}]',7,12),(32,'2018-04-02 19:59:17.195741','5','affiliate-link-5',1,'[{\"added\": {}}]',7,12),(33,'2018-04-02 19:59:30.684185','6','affiliate-link-6',1,'[{\"added\": {}}]',7,12),(34,'2018-04-02 20:01:43.221941','7','affiliate-link-7',1,'[{\"added\": {}}]',7,12),(35,'2018-04-02 20:01:55.184748','8','affiliate-link-8',1,'[{\"added\": {}}]',7,12),(36,'2018-04-02 20:02:07.871472','9','affiliate-link-9',1,'[{\"added\": {}}]',7,12),(37,'2018-04-02 20:02:24.209724','10','affiliate-link-10',1,'[{\"added\": {}}]',7,12),(38,'2018-04-02 20:02:41.811794','11','affiliate-link-11',1,'[{\"added\": {}}]',7,12),(39,'2018-04-02 20:02:57.256556','12','affiliate-link-12',1,'[{\"added\": {}}]',7,12),(40,'2018-04-02 20:04:52.947190','13','affiliate-link-13',1,'[{\"added\": {}}]',7,12),(41,'2018-04-02 20:05:05.215377','14','affiliate-link-14',1,'[{\"added\": {}}]',7,12),(42,'2018-04-02 21:01:38.947952','1','module-1',1,'[{\"added\": {}}]',48,12),(43,'2018-04-02 21:01:51.461110','2','module-2',1,'[{\"added\": {}}]',48,12),(44,'2018-04-02 21:02:02.605942','3','module-3',1,'[{\"added\": {}}]',48,12),(45,'2018-04-02 21:02:14.208218','4','module-4',1,'[{\"added\": {}}]',48,12),(46,'2018-04-02 21:02:26.629337','5','module-5',1,'[{\"added\": {}}]',48,12),(47,'2018-04-02 21:02:39.796277','6','module-6',1,'[{\"added\": {}}]',48,12),(48,'2018-04-02 21:03:12.013788','8','module-7',1,'[{\"added\": {}}]',48,12),(49,'2018-04-02 21:04:02.045163','1','module-1-lesson-1',1,'[{\"added\": {}}]',47,12),(50,'2018-04-02 21:04:16.499693','2','module-1-lesson-2',1,'[{\"added\": {}}]',47,12),(51,'2018-04-02 21:04:33.601245','3','module-2-lesson-1',1,'[{\"added\": {}}]',47,12),(52,'2018-04-02 21:04:48.615704','4','module-2-lesson-2',1,'[{\"added\": {}}]',47,12),(53,'2018-04-02 21:05:10.035719','5','module-2-lesson-3',1,'[{\"added\": {}}]',47,12),(54,'2018-04-02 21:05:26.098745','6','module-2-lesson-4',1,'[{\"added\": {}}]',47,12),(55,'2018-04-02 21:05:40.668699','7','module-3-lesson-1',1,'[{\"added\": {}}]',47,12),(56,'2018-04-02 21:05:55.513717','8','module-3-lesson-2',1,'[{\"added\": {}}]',47,12),(57,'2018-04-02 21:06:18.666779','9','module-3-lesson-3',1,'[{\"added\": {}}]',47,12),(58,'2018-04-02 21:06:39.219703','10','module-4-lesson-1',1,'[{\"added\": {}}]',47,12),(59,'2018-04-02 21:06:55.527752','11','module-4-lesson-2',1,'[{\"added\": {}}]',47,12),(60,'2018-04-02 21:07:15.542640','12','module-4-lesson-3',1,'[{\"added\": {}}]',47,12),(61,'2018-04-02 21:07:39.857651','13','module-5-lesson-1',1,'[{\"added\": {}}]',47,12),(62,'2018-04-02 21:07:54.199658','14','module-5-lesson-2',1,'[{\"added\": {}}]',47,12),(63,'2018-04-02 21:08:09.749172','15','module-5-lesson-3',1,'[{\"added\": {}}]',47,12),(64,'2018-04-02 21:08:24.298138','16','module-5-lesson-4',1,'[{\"added\": {}}]',47,12),(65,'2018-04-02 21:08:42.439187','17','module-5-lesson-5',1,'[{\"added\": {}}]',47,12),(66,'2018-04-02 21:08:57.760066','18','module-5-lesson-6',1,'[{\"added\": {}}]',47,12),(67,'2018-04-02 21:09:15.529563','19','module-6-lesson-1',1,'[{\"added\": {}}]',47,12),(68,'2018-04-02 21:09:36.768773','20','module-6-lesson-2',1,'[{\"added\": {}}]',47,12),(69,'2018-04-02 21:09:51.037506','21','module-7-lesson-1',1,'[{\"added\": {}}]',47,12),(70,'2018-04-02 21:10:04.587646','22','module-7-lesson-2',1,'[{\"added\": {}}]',47,12),(71,'2018-04-02 21:10:18.437607','23','module-7-lesson-3',1,'[{\"added\": {}}]',47,12),(72,'2018-04-02 21:34:38.119103','1','step-1',1,'[{\"added\": {}}]',45,12),(73,'2018-04-02 21:34:50.161402','2','step-2',1,'[{\"added\": {}}]',45,12),(74,'2018-04-02 21:35:01.702055','3','step-3',1,'[{\"added\": {}}]',45,12),(75,'2018-04-02 21:35:12.828084','4','step-4',1,'[{\"added\": {}}]',45,12),(76,'2018-04-02 21:35:24.446593','5','step-5',1,'[{\"added\": {}}]',45,12),(77,'2018-04-03 14:30:01.468369','1','m_1_l_1',1,'[{\"added\": {}}]',50,12),(78,'2018-04-03 14:30:22.108341','2','m_1_l_2',1,'[{\"added\": {}}]',50,12),(79,'2018-04-03 14:30:33.359612','3','m_2_l_1',1,'[{\"added\": {}}]',50,12),(80,'2018-04-03 14:30:45.328487','4','m_2_l_2',1,'[{\"added\": {}}]',50,12),(81,'2018-04-03 14:31:01.609128','5','m_2_l_3',1,'[{\"added\": {}}]',50,12),(82,'2018-04-03 14:31:11.370270','6','m_2_l_4',1,'[{\"added\": {}}]',50,12),(83,'2018-04-03 14:31:23.272072','7','m_3_l_1',1,'[{\"added\": {}}]',50,12),(84,'2018-04-03 14:31:33.299479','8','m_3_l_2',1,'[{\"added\": {}}]',50,12),(85,'2018-04-03 14:31:46.094529','9','m_3_l_3',1,'[{\"added\": {}}]',50,12);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (9,'account','automated_webinar_funnel_version_1'),(10,'account','automated_webinar_funnel_version_2'),(11,'account','aweberaccount'),(12,'account','bethemillionaire_3_step_registration_funnel'),(14,'account','bitconnectaccount'),(13,'account','bitconnect_direct_funnel'),(15,'account','bitpandaaccount'),(16,'account','cexioaccount'),(17,'account','clickfunnelsaccount'),(18,'account','clickmagicaccount'),(19,'account','coinbaseaccount'),(20,'account','coinmamaaccount'),(21,'account','course_giveaway_3_steps_funnel'),(22,'account','course_giveaway_direct_registration'),(23,'account','cryptopaycardaccount'),(24,'account','direct_registration'),(25,'account','getresponseaccount'),(26,'account','getresponseautoresponderaddcontact'),(27,'account','how_to_set_up_your_bethemillionaire_system'),(28,'account','indacoinaccount'),(29,'account','latest_webinar_replay_btm'),(30,'account','ledgernanosaccount'),(31,'account','localbitcoinsaccount'),(32,'account','membershiplevel'),(33,'account','mike_hobbs_usi_tech_team_webinar_90_bitcoins_in_6_months'),(34,'account','payment'),(35,'account','preregistration'),(36,'account','spectrocoincardaccount'),(37,'account','trezorsaccount'),(8,'account','userprofile'),(42,'account','usitechaccount'),(38,'account','usi_tech_7_figure_plan_in_2018'),(39,'account','usi_tech_btc_packages_calculator'),(40,'account','usi_tech_direct_funnel'),(41,'account','usi_tech_funnel'),(1,'admin','logentry'),(50,'administration','videolink'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(7,'home','affiliatelinkcontrol'),(6,'ipn','paypalipn'),(47,'lessons','lesson'),(48,'lessons','module'),(49,'lessons','step'),(5,'sessions','session'),(43,'topic','comment'),(44,'topic','note'),(45,'topic','stepcontrol'),(46,'topic','subcomment');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-03-31 19:53:51.276164'),(2,'contenttypes','0002_remove_content_type_name','2018-03-31 19:53:51.351473'),(3,'auth','0001_initial','2018-03-31 19:53:51.612265'),(4,'auth','0002_alter_permission_name_max_length','2018-03-31 19:53:51.629745'),(5,'auth','0003_alter_user_email_max_length','2018-03-31 19:53:51.643796'),(6,'auth','0004_alter_user_username_opts','2018-03-31 19:53:51.658814'),(7,'auth','0005_alter_user_last_login_null','2018-03-31 19:53:51.668231'),(8,'auth','0006_require_contenttypes_0002','2018-03-31 19:53:51.672277'),(9,'auth','0007_alter_validators_add_error_messages','2018-03-31 19:53:51.683752'),(10,'auth','0008_alter_user_username_max_length','2018-03-31 19:53:51.693581'),(11,'account','0001_initial','2018-03-31 19:53:55.500516'),(12,'admin','0001_initial','2018-03-31 19:53:55.705768'),(13,'admin','0002_logentry_remove_auto_add','2018-03-31 19:53:55.760963'),(14,'administration','0001_initial','2018-03-31 19:53:55.790614'),(15,'home','0001_initial','2018-03-31 19:53:55.820049'),(16,'ipn','0001_initial','2018-03-31 19:53:55.925192'),(17,'ipn','0002_paypalipn_mp_id','2018-03-31 19:53:55.979871'),(18,'ipn','0003_auto_20141117_1647','2018-03-31 19:53:56.070728'),(19,'ipn','0004_auto_20150612_1826','2018-03-31 19:53:56.613625'),(20,'ipn','0005_auto_20151217_0948','2018-03-31 19:53:56.717537'),(21,'ipn','0006_auto_20160108_1112','2018-03-31 19:53:56.823373'),(22,'ipn','0007_auto_20160219_1135','2018-03-31 19:53:56.857305'),(23,'lessons','0001_initial','2018-03-31 19:53:57.005848'),(24,'sessions','0001_initial','2018-03-31 19:53:57.049011'),(25,'topic','0001_initial','2018-03-31 19:53:57.417241'),(26,'account','0002_auto_20180401_0205','2018-03-31 20:05:25.882371'),(27,'account','0003_auto_20180401_0329','2018-03-31 21:29:51.865997');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4cjwxpv3wls9qftanbdtwr8beluhwg9f','OGExMWZhNzJhZTU3NzRmMzBkMTFlN2EwZjk0ZDUwMDg1OThiNGQ5ODp7Il9hdXRoX3VzZXJfaWQiOiIxMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMGZlYWJjOTgyYTJiMWVkMmY3NWFiMTBmYjI3OGZiMWY2M2I4YjlhOCJ9','2018-04-17 14:22:42.037479'),('7jxqac9etqh8nqqxh6vxne5cq35q7yzi','OGExMWZhNzJhZTU3NzRmMzBkMTFlN2EwZjk0ZDUwMDg1OThiNGQ5ODp7Il9hdXRoX3VzZXJfaWQiOiIxMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMGZlYWJjOTgyYTJiMWVkMmY3NWFiMTBmYjI3OGZiMWY2M2I4YjlhOCJ9','2018-04-16 19:37:38.217258'),('bxv1b20dn5scxcznwcjmc1l205mf4r5b','OGExMWZhNzJhZTU3NzRmMzBkMTFlN2EwZjk0ZDUwMDg1OThiNGQ5ODp7Il9hdXRoX3VzZXJfaWQiOiIxMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMGZlYWJjOTgyYTJiMWVkMmY3NWFiMTBmYjI3OGZiMWY2M2I4YjlhOCJ9','2018-04-15 19:59:11.653145'),('j71b9mm46sgme1nb1uy52vlnwyqclcs0','OGExMWZhNzJhZTU3NzRmMzBkMTFlN2EwZjk0ZDUwMDg1OThiNGQ5ODp7Il9hdXRoX3VzZXJfaWQiOiIxMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMGZlYWJjOTgyYTJiMWVkMmY3NWFiMTBmYjI3OGZiMWY2M2I4YjlhOCJ9','2018-04-14 21:28:49.936914'),('tv2rzp23qoch2q6femgkdpdmwm6opmtd','MmRmOGE0M2UwZTJiMmIyMjJjODExZDI2Y2RhNDYxYzEzNzNhYThmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjOWUwYTEyYTQ4YWI1YjBlZjIzYjI5MjI0NzcxNDNkM2YxY2E4YWZiIn0=','2018-04-14 20:51:40.008004'),('vjieael98djgg2h9f0xgy8pnm8jsq6eh','OGExMWZhNzJhZTU3NzRmMzBkMTFlN2EwZjk0ZDUwMDg1OThiNGQ5ODp7Il9hdXRoX3VzZXJfaWQiOiIxMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMGZlYWJjOTgyYTJiMWVkMmY3NWFiMTBmYjI3OGZiMWY2M2I4YjlhOCJ9','2018-04-15 21:39:33.527938'),('xgwfjil4nee48t68a3f43ppoiglh4fci','MmRmOGE0M2UwZTJiMmIyMjJjODExZDI2Y2RhNDYxYzEzNzNhYThmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjOWUwYTEyYTQ4YWI1YjBlZjIzYjI5MjI0NzcxNDNkM2YxY2E4YWZiIn0=','2018-04-14 20:07:13.844136');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_affiliatelinkcontrol`
--

DROP TABLE IF EXISTS `home_affiliatelinkcontrol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_affiliatelinkcontrol` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `short_name` varchar(100) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_on` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_affiliatelinkcontrol`
--

LOCK TABLES `home_affiliatelinkcontrol` WRITE;
/*!40000 ALTER TABLE `home_affiliatelinkcontrol` DISABLE KEYS */;
INSERT INTO `home_affiliatelinkcontrol` VALUES (1,'BeTheMillionaire 3-Step Registration Funnel','affiliate-link-1',1,'2018-04-02 19:57:26.633156'),(2,'Direct Registration','affiliate-link-2',1,'2018-04-02 19:57:44.932283'),(3,'Automated Webinar Funnel Version 1','affiliate-link-3',1,'2018-04-02 19:58:01.332468'),(4,'Automated Webinar Funnel Version 2','affiliate-link-4',1,'2018-04-02 19:59:02.484233'),(5,'Course Giveaway Direct Registration','affiliate-link-5',1,'2018-04-02 19:59:17.193235'),(6,'Course Giveaway 3 Steps Funnel','affiliate-link-6',1,'2018-04-02 19:59:30.682619'),(7,'Latest Webinar Replay BTM','affiliate-link-7',1,'2018-04-02 20:01:43.219755'),(8,'Usi-Tech Funnel','affiliate-link-8',1,'2018-04-02 20:01:55.182279'),(9,'Usi-Tech Direct Funnel','affiliate-link-9',1,'2018-04-02 20:02:07.870380'),(10,'Usi-Tech BTC-Packages Calculator','affiliate-link-10',1,'2018-04-02 20:02:24.208367'),(11,'Bitconnect Direct Funnel','affiliate-link-11',1,'2018-04-02 20:02:41.809890'),(12,'Mike Hobbs Usi-Tech Team Webinar (90 bitcoins in 6 months)','affiliate-link-12',1,'2018-04-02 20:02:57.255417'),(13,'How To Set Up Your BeTheMillionaire System','affiliate-link-13',1,'2018-04-02 20:04:52.946264'),(14,'Usi Tech 7 Figure Plan In 2018!','affiliate-link-14',1,'2018-04-02 20:05:05.213704');
/*!40000 ALTER TABLE `home_affiliatelinkcontrol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lessons_lesson`
--

DROP TABLE IF EXISTS `lessons_lesson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lessons_lesson` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `short_name` varchar(50) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_on` datetime(6) NOT NULL,
  `module_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lessons_lesson_module_id_43312367_fk_lessons_module_id` (`module_id`),
  CONSTRAINT `lessons_lesson_module_id_43312367_fk_lessons_module_id` FOREIGN KEY (`module_id`) REFERENCES `lessons_module` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lessons_lesson`
--

LOCK TABLES `lessons_lesson` WRITE;
/*!40000 ALTER TABLE `lessons_lesson` DISABLE KEYS */;
INSERT INTO `lessons_lesson` VALUES (1,'Lesson 1 – Welcome To BeTheMillionaire System','module-1-lesson-1',1,'2018-04-02 21:04:02.043071',1),(2,'Lesson 2 – Foundation & Overview Of Bitcoins Wealth Club System','module-1-lesson-2',1,'2018-04-02 21:04:16.498972',1),(3,'Lesson 1 – Why Bitcoins & Cryptocurrencies Are The Most Exciting Investment Vehicles To Grow Your Wealth On Earth Today','module-2-lesson-1',1,'2018-04-02 21:04:33.600200',2),(4,'Lesson 2 – What Are The Best Bitcoin Wallets To Use To Store Your Bitcoins Safely?','module-2-lesson-2',1,'2018-04-02 21:04:48.614600',2),(5,'Lesson 3 – The Complete Guide To Easily Buying Bitcoins Online & Offline','module-2-lesson-3',1,'2018-04-02 21:05:10.034420',2),(6,'Lesson 4 – How To Turn Bitcoins Into Cash & Buy Anything You Want With VISA Debit Cards','module-2-lesson-4',1,'2018-04-02 21:05:26.097225',2),(7,'Lesson 1 – 4 Ways To Produce Income & How To Become Financially Free','module-3-lesson-1',1,'2018-04-02 21:05:40.665353',3),(8,'Lesson 2 – Why Banks Are Biggest Scammers & Why Typical Investment Vehicles SUCK','module-3-lesson-2',1,'2018-04-02 21:05:55.511731',3),(9,'Lesson 3 – 5 Primary Ways To Grow Your Wealth In Bitcoins','module-3-lesson-3',1,'2018-04-02 21:06:18.665562',3),(10,'Lesson 1 – 3 Strategies To Hit $30K+ A Month In Bitcoins & How To Make Minimum 472% ROI A Year Totally Passively','module-4-lesson-1',1,'2018-04-02 21:06:39.218769',4),(11,'Lesson 2 – How To Leverage Billion Dollar Cryptocurrency To Passively Earn Up To 40% Monthly Returns On Autopilot','module-4-lesson-2',1,'2018-04-02 21:06:55.526387',4),(12,'Lesson 3 – How To Learn From Multi-Millionaires Like Kevin Harrington From Shark Tank & Earn Bitcoins Instantly!','module-4-lesson-3',1,'2018-04-02 21:07:15.541322',4),(13,'Lesson 1 – Set Up Bitcoins Wealth Club System Correctly','module-5-lesson-1',1,'2018-04-02 21:07:39.855350',5),(14,'Lesson 2 – Connect Your Autoresponder To Bitcoins Wealth Club To Build Your List (Optional)','module-5-lesson-2',1,'2018-04-02 21:07:54.197976',5),(15,'Lesson 3 – How To Promote Your Affiliate Links & FunnelsLesson 3 – How To Promote Your Affiliate Links & Funnels','module-5-lesson-3',1,'2018-04-02 21:08:09.747715',5),(16,'Lesson 4 – How To Promote Bitcoins Wealth Club On Facebook Groups','module-5-lesson-4',1,'2018-04-02 21:08:24.297014',5),(17,'Lesson 5 – How To Learn Advanced Marketing Strategies & Become Online Recruiting Master','module-5-lesson-5',1,'2018-04-02 21:08:42.437920',5),(18,'Lesson 6 How To Get Premium & VIP Level Coaching & Own 20% Of Profits Of BeTheMillionaire','module-5-lesson-6',1,'2018-04-02 21:08:57.758969',5),(19,'Lesson 1 – How To Leverage Micro-Profit System To Trade At Minimum 1% A Day','module-6-lesson-1',1,'2018-04-02 21:09:15.528945',6),(20,'How My Friend Caleb Earns Over $1,000,000 A Year Trading Cryptocurrencies','module-6-lesson-2',1,'2018-04-02 21:09:36.768271',6),(21,'How To Achieve Your Goals & Dreams','module-7-lesson-1',1,'2018-04-02 21:09:51.036413',8),(22,'Lesson - 2 – Your Daily Method Of Operation','module-7-lesson-2',1,'2018-04-02 21:10:04.586582',8),(23,'Top Bitcoin Resources','module-7-lesson-3',1,'2018-04-02 21:10:18.436687',8);
/*!40000 ALTER TABLE `lessons_lesson` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lessons_module`
--

DROP TABLE IF EXISTS `lessons_module`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lessons_module` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `short_name` varchar(50) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_on` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lessons_module`
--

LOCK TABLES `lessons_module` WRITE;
/*!40000 ALTER TABLE `lessons_module` DISABLE KEYS */;
INSERT INTO `lessons_module` VALUES (1,'Module 1 – How Bitcoins Wealth Club Can Help You Massively Grow Your Wealth','module-1',1,'2018-04-02 21:01:38.940824'),(2,'Module 2 – What Is Bitcoin & Why It’s Completely Revolutionizing Money','module-2',1,'2018-04-02 21:01:51.459627'),(3,'Module 3 – The Secret To Wealth Acceleration','module-3',1,'2018-04-02 21:02:02.604307'),(4,'Module 4 – How To Passively Multiply Your Money By 5X Over & Over Again & Earn Multiple Streams Of R','module-4',1,'2018-04-02 21:02:14.206832'),(5,'Module 5 – How Bitcoins Wealth Club System Works & How To Promote It To Accelerate Your Wealth','module-5',1,'2018-04-02 21:02:26.570070'),(6,'Module 6 – How To Trade Cryptocurrencies Yourself & Invest Into Altcoins','module-6',1,'2018-04-02 21:02:39.795658'),(8,'Module 7 – How To Achieve Your Dreams With Bitcoins Wealth Club System','module-7',1,'2018-04-02 21:03:12.013050');
/*!40000 ALTER TABLE `lessons_module` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lessons_step`
--

DROP TABLE IF EXISTS `lessons_step`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lessons_step` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `short_name` varchar(50) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_on` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lessons_step`
--

LOCK TABLES `lessons_step` WRITE;
/*!40000 ALTER TABLE `lessons_step` DISABLE KEYS */;
/*!40000 ALTER TABLE `lessons_step` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paypal_ipn`
--

DROP TABLE IF EXISTS `paypal_ipn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `paypal_ipn` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `business` varchar(127) NOT NULL,
  `charset` varchar(255) NOT NULL,
  `custom` varchar(256) NOT NULL,
  `notify_version` decimal(64,2) DEFAULT NULL,
  `parent_txn_id` varchar(19) NOT NULL,
  `receiver_email` varchar(254) NOT NULL,
  `receiver_id` varchar(255) NOT NULL,
  `residence_country` varchar(2) NOT NULL,
  `test_ipn` tinyint(1) NOT NULL,
  `txn_id` varchar(255) NOT NULL,
  `txn_type` varchar(255) NOT NULL,
  `verify_sign` varchar(255) NOT NULL,
  `address_country` varchar(64) NOT NULL,
  `address_city` varchar(40) NOT NULL,
  `address_country_code` varchar(64) NOT NULL,
  `address_name` varchar(128) NOT NULL,
  `address_state` varchar(40) NOT NULL,
  `address_status` varchar(255) NOT NULL,
  `address_street` varchar(200) NOT NULL,
  `address_zip` varchar(20) NOT NULL,
  `contact_phone` varchar(20) NOT NULL,
  `first_name` varchar(64) NOT NULL,
  `last_name` varchar(64) NOT NULL,
  `payer_business_name` varchar(127) NOT NULL,
  `payer_email` varchar(127) NOT NULL,
  `payer_id` varchar(13) NOT NULL,
  `auth_amount` decimal(64,2) DEFAULT NULL,
  `auth_exp` varchar(28) NOT NULL,
  `auth_id` varchar(19) NOT NULL,
  `auth_status` varchar(255) NOT NULL,
  `exchange_rate` decimal(64,16) DEFAULT NULL,
  `invoice` varchar(127) NOT NULL,
  `item_name` varchar(127) NOT NULL,
  `item_number` varchar(127) NOT NULL,
  `mc_currency` varchar(32) NOT NULL,
  `mc_fee` decimal(64,2) DEFAULT NULL,
  `mc_gross` decimal(64,2) DEFAULT NULL,
  `mc_handling` decimal(64,2) DEFAULT NULL,
  `mc_shipping` decimal(64,2) DEFAULT NULL,
  `memo` varchar(255) NOT NULL,
  `num_cart_items` int(11) DEFAULT NULL,
  `option_name1` varchar(64) NOT NULL,
  `option_name2` varchar(64) NOT NULL,
  `payer_status` varchar(255) NOT NULL,
  `payment_date` datetime(6) DEFAULT NULL,
  `payment_gross` decimal(64,2) DEFAULT NULL,
  `payment_status` varchar(255) NOT NULL,
  `payment_type` varchar(255) NOT NULL,
  `pending_reason` varchar(255) NOT NULL,
  `protection_eligibility` varchar(255) NOT NULL,
  `quantity` int(11) DEFAULT NULL,
  `reason_code` varchar(255) NOT NULL,
  `remaining_settle` decimal(64,2) DEFAULT NULL,
  `settle_amount` decimal(64,2) DEFAULT NULL,
  `settle_currency` varchar(32) NOT NULL,
  `shipping` decimal(64,2) DEFAULT NULL,
  `shipping_method` varchar(255) NOT NULL,
  `tax` decimal(64,2) DEFAULT NULL,
  `transaction_entity` varchar(255) NOT NULL,
  `auction_buyer_id` varchar(64) NOT NULL,
  `auction_closing_date` datetime(6) DEFAULT NULL,
  `auction_multi_item` int(11) DEFAULT NULL,
  `for_auction` decimal(64,2) DEFAULT NULL,
  `amount` decimal(64,2) DEFAULT NULL,
  `amount_per_cycle` decimal(64,2) DEFAULT NULL,
  `initial_payment_amount` decimal(64,2) DEFAULT NULL,
  `next_payment_date` datetime(6) DEFAULT NULL,
  `outstanding_balance` decimal(64,2) DEFAULT NULL,
  `payment_cycle` varchar(255) NOT NULL,
  `period_type` varchar(255) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `product_type` varchar(255) NOT NULL,
  `profile_status` varchar(255) NOT NULL,
  `recurring_payment_id` varchar(255) NOT NULL,
  `rp_invoice_id` varchar(127) NOT NULL,
  `time_created` datetime(6) DEFAULT NULL,
  `amount1` decimal(64,2) DEFAULT NULL,
  `amount2` decimal(64,2) DEFAULT NULL,
  `amount3` decimal(64,2) DEFAULT NULL,
  `mc_amount1` decimal(64,2) DEFAULT NULL,
  `mc_amount2` decimal(64,2) DEFAULT NULL,
  `mc_amount3` decimal(64,2) DEFAULT NULL,
  `password` varchar(24) NOT NULL,
  `period1` varchar(255) NOT NULL,
  `period2` varchar(255) NOT NULL,
  `period3` varchar(255) NOT NULL,
  `reattempt` varchar(1) NOT NULL,
  `recur_times` int(11) DEFAULT NULL,
  `recurring` varchar(1) NOT NULL,
  `retry_at` datetime(6) DEFAULT NULL,
  `subscr_date` datetime(6) DEFAULT NULL,
  `subscr_effective` datetime(6) DEFAULT NULL,
  `subscr_id` varchar(19) NOT NULL,
  `username` varchar(64) NOT NULL,
  `case_creation_date` datetime(6) DEFAULT NULL,
  `case_id` varchar(255) NOT NULL,
  `case_type` varchar(255) NOT NULL,
  `receipt_id` varchar(255) NOT NULL,
  `currency_code` varchar(32) NOT NULL,
  `handling_amount` decimal(64,2) DEFAULT NULL,
  `transaction_subject` varchar(256) NOT NULL,
  `ipaddress` char(39) DEFAULT NULL,
  `flag` tinyint(1) NOT NULL,
  `flag_code` varchar(16) NOT NULL,
  `flag_info` longtext NOT NULL,
  `query` longtext NOT NULL,
  `response` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `from_view` varchar(6) DEFAULT NULL,
  `mp_id` varchar(128) DEFAULT NULL,
  `option_selection1` varchar(200) NOT NULL,
  `option_selection2` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `paypal_ipn_txn_id_8fa22c44` (`txn_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paypal_ipn`
--

LOCK TABLES `paypal_ipn` WRITE;
/*!40000 ALTER TABLE `paypal_ipn` DISABLE KEYS */;
/*!40000 ALTER TABLE `paypal_ipn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `topic_comment`
--

DROP TABLE IF EXISTS `topic_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `topic_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic` varchar(255) DEFAULT NULL,
  `comment` longtext,
  `create_on` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `topic_comment_user_id_87de75ef_fk_account_userprofile_id` (`user_id`),
  CONSTRAINT `topic_comment_user_id_87de75ef_fk_account_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `topic_comment`
--

LOCK TABLES `topic_comment` WRITE;
/*!40000 ALTER TABLE `topic_comment` DISABLE KEYS */;
INSERT INTO `topic_comment` VALUES (1,'module-1','new','2018-04-02 20:49:05.662048',12),(2,'module-1','hi','2018-04-02 20:49:22.599529',12),(3,'module-2','hhhh','2018-04-02 20:52:03.216213',12),(4,'module-2','khvhgc','2018-04-02 20:52:15.589684',12),(5,'module-3','jkbjhm','2018-04-02 20:54:17.810906',12),(6,'module-4','nskdn','2018-04-02 20:55:34.003162',12),(7,'module-4','zk','2018-04-02 20:55:48.286229',12),(8,'module-5','sldnskjnd','2018-04-02 20:56:58.214940',12),(9,'module-5','sldnskjndxmlsdm','2018-04-02 20:57:02.126248',12),(10,'module-6','sldknskldn','2018-04-02 20:58:09.225659',12),(11,'module-7','lskdnksnd','2018-04-02 20:59:31.434349',12),(12,'step-1-overview','ldsnskjln','2018-04-02 21:36:06.272302',12),(13,'step-2-setup-bitcoinwallet','sdnkjsndkjs','2018-04-02 21:42:15.106344',12),(14,'step-3-wealth-vehicles','slkndskln','2018-04-02 21:50:10.751445',12),(15,'step-3-setup-multiple-passive-profile','jldsnjksd','2018-04-02 21:57:02.800199',12),(16,'step-5-start-promoting-btm','lfnldsknf','2018-04-02 22:04:58.754002',12),(17,'module-1-lesson-1','sl;dmslmd','2018-04-03 14:32:58.948042',12),(18,'module-1-lesson-2','sdlnskjdn','2018-04-03 14:34:50.180779',12),(19,'module-2-lesson-1','slkdmslkdmn','2018-04-03 14:36:55.748321',12),(20,'module-2-lesson-2','sldnsknd','2018-04-03 14:38:27.095214',12),(21,'module-2-lesson-3','lsdlskdlks','2018-04-03 14:40:51.787554',12),(22,'module-2-lesson-4','skdmslkd','2018-04-03 14:43:20.295440',12),(23,'module-3-lesson-1','osdnfjsdn','2018-04-03 14:45:54.011658',12),(24,'module-3-lesson-2','sdnskjnd','2018-04-03 14:52:05.222375',12),(25,'module-3-lesson-3','slkdslnd','2018-04-03 14:57:52.935389',12),(26,'module-4-lesson-1','skdklsd sd','2018-04-03 15:04:17.824174',12),(27,'module-4-lesson-2','lskdslkmd','2018-04-03 15:05:48.040328',12),(28,'module-4-lesson-3','sdkskl','2018-04-03 15:07:27.212733',12);
/*!40000 ALTER TABLE `topic_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `topic_note`
--

DROP TABLE IF EXISTS `topic_note`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `topic_note` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic` varchar(200) DEFAULT NULL,
  `note` longtext,
  `created_on` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `topic_note_user_id_c9aabfd3_fk_account_userprofile_id` (`user_id`),
  CONSTRAINT `topic_note_user_id_c9aabfd3_fk_account_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `topic_note`
--

LOCK TABLES `topic_note` WRITE;
/*!40000 ALTER TABLE `topic_note` DISABLE KEYS */;
INSERT INTO `topic_note` VALUES (1,'module-1-lesson-1','lskdnksnd','2018-04-03 14:32:45.769646',12),(2,'module-1-lesson-2','yyy','2018-04-03 14:34:42.675136',12),(3,'module-2-lesson-1','ldjknksjdfnkjsd sdknsd','2018-04-03 14:36:48.263805',12),(4,'module-2-lesson-2','lkmnlskds dks','2018-04-03 14:38:17.575314',12),(5,'module-2-lesson-3','sdnsjdn','2018-04-03 14:40:44.055821',12),(6,'module-2-lesson-4','skdmslkm','2018-04-03 14:42:31.624241',12),(7,'module-3-lesson-1','lsslkmd','2018-04-03 14:45:45.327770',12),(8,'module-3-lesson-2','slkdskldn','2018-04-03 14:51:57.767560',12),(9,'module-3-lesson-3','sldnsdn','2018-04-03 14:57:47.080169',12),(10,'module-4-lesson-1','lksdmlskm','2018-04-03 15:04:10.097840',12),(11,'module-4-lesson-2','slkdslk','2018-04-03 15:05:57.432849',12),(12,'module-4-lesson-3','sdmslkdm','2018-04-03 15:07:18.041346',12);
/*!40000 ALTER TABLE `topic_note` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `topic_stepcontrol`
--

DROP TABLE IF EXISTS `topic_stepcontrol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `topic_stepcontrol` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `short_name` varchar(100) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_on` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `topic_stepcontrol`
--

LOCK TABLES `topic_stepcontrol` WRITE;
/*!40000 ALTER TABLE `topic_stepcontrol` DISABLE KEYS */;
INSERT INTO `topic_stepcontrol` VALUES (1,'Step 1 – The Foundation & Overview','step-1',1,'2018-04-02 21:34:38.080443'),(2,'Step 2 – Set Up Your Bitcoin Wallet Load It With Bitcoins','step-2',1,'2018-04-02 21:34:50.155520'),(3,'Step 3 – Set Up Your Multiple Passive Profits Wealth Building Vehicles Inside The System','step-3',1,'2018-04-02 21:35:01.700813'),(4,'Step 4 - How To Earn Extra $20K A Month, Get Access To 7 Figures Live Mentoring, And Earn BONUS FREE Bitcoins','step-4',1,'2018-04-02 21:35:12.826966'),(5,'Step 5 – Start Promoting Bitcoins Wealth Club System & Earn Bitcoins In Multiple Ways!','step-5',1,'2018-04-02 21:35:24.445268');
/*!40000 ALTER TABLE `topic_stepcontrol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `topic_subcomment`
--

DROP TABLE IF EXISTS `topic_subcomment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `topic_subcomment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic` varchar(255) DEFAULT NULL,
  `subcomment` longtext,
  `create_on` datetime(6) NOT NULL,
  `comment_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `topic_subcomment_comment_id_49b84646_fk_topic_comment_id` (`comment_id`),
  KEY `topic_subcomment_user_id_b7a439ae_fk_account_userprofile_id` (`user_id`),
  CONSTRAINT `topic_subcomment_comment_id_49b84646_fk_topic_comment_id` FOREIGN KEY (`comment_id`) REFERENCES `topic_comment` (`id`),
  CONSTRAINT `topic_subcomment_user_id_b7a439ae_fk_account_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `topic_subcomment`
--

LOCK TABLES `topic_subcomment` WRITE;
/*!40000 ALTER TABLE `topic_subcomment` DISABLE KEYS */;
INSERT INTO `topic_subcomment` VALUES (1,'module-1','yes','2018-04-02 20:49:14.847544',1,12),(2,'module-2','jkj','2018-04-02 20:52:09.269572',3,12),(3,'module-3','kjbjk','2018-04-02 20:54:23.557510',5,12),(4,'module-4','dnskl','2018-04-02 20:55:40.320364',6,12),(5,'module-6','nskjdn','2018-04-02 20:58:14.464271',10,12),(6,'module-7','sd.slkd','2018-04-02 20:59:36.019195',11,12),(7,'step-1-overview','ldknskjln','2018-04-02 21:36:12.903985',12,12),(8,'step-2-setup-bitcoinwallet','asnn','2018-04-02 21:42:21.421553',13,12),(9,'step-3-wealth-vehicles','lkdnklnd','2018-04-02 21:50:16.514058',14,12),(10,'step-3-setup-multiple-passive-profile','s;dmslkmd','2018-04-02 21:57:09.929125',15,12),(11,'step-5-start-promoting-btm','s;mlksmd','2018-04-02 22:05:05.836565',16,12),(12,'module-1-lesson-2','lskdmnskl','2018-04-03 14:34:54.666661',18,12),(13,'module-2-lesson-1','lkdnlksa','2018-04-03 14:37:00.541784',19,12),(14,'module-2-lesson-2','lsdnsklnd','2018-04-03 14:38:33.371713',20,12),(15,'module-2-lesson-3','aldlskmnd','2018-04-03 14:40:59.510888',21,12),(16,'module-2-lesson-4','sdnsklnd','2018-04-03 14:43:27.328550',22,12),(17,'module-3-lesson-1','skdmlkdfm','2018-04-03 14:46:00.540861',23,12),(18,'module-3-lesson-3','xcndn','2018-04-03 14:57:58.134810',25,12),(19,'module-4-lesson-1','skdmlks','2018-04-03 15:04:25.414608',26,12);
/*!40000 ALTER TABLE `topic_subcomment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-03 21:27:31
