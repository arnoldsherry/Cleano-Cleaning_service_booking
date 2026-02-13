-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Feb 09, 2026 at 04:19 AM
-- Server version: 9.1.0
-- PHP Version: 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_clean`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_category`
--

DROP TABLE IF EXISTS `adminapp_tbl_category`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_category` (
  `categoryid` int NOT NULL AUTO_INCREMENT,
  `categoryname` varchar(50) NOT NULL,
  PRIMARY KEY (`categoryid`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `adminapp_tbl_category`
--

INSERT INTO `adminapp_tbl_category` (`categoryid`, `categoryname`) VALUES
(1, 'Domestic');

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_district`
--

DROP TABLE IF EXISTS `adminapp_tbl_district`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_district` (
  `districtid` int NOT NULL AUTO_INCREMENT,
  `districtname` varchar(50) NOT NULL,
  PRIMARY KEY (`districtid`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `adminapp_tbl_district`
--

INSERT INTO `adminapp_tbl_district` (`districtid`, `districtname`) VALUES
(5, 'EKM'),
(10, 'Pathanamthitta'),
(7, 'Kollam'),
(9, 'Kasargod'),
(11, 'Kannur'),
(12, 'wayanad');

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_location`
--

DROP TABLE IF EXISTS `adminapp_tbl_location`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_location` (
  `locationid` int NOT NULL AUTO_INCREMENT,
  `locationname` varchar(50) NOT NULL,
  `districtid_id` int NOT NULL,
  PRIMARY KEY (`locationid`),
  KEY `adminapp_tbl_location_districtid_id_582f66a5` (`districtid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `adminapp_tbl_location`
--

INSERT INTO `adminapp_tbl_location` (`locationid`, `locationname`, `districtid_id`) VALUES
(4, 'karappuzha', 12),
(2, 'konnakad', 9),
(3, 'km', 9),
(5, 'edappally', 5),
(6, 'Kalamassery', 5),
(7, 'Piravom', 5),
(8, 'Alapuram', 5),
(9, 'Karimattom', 10),
(10, 'Kollasery', 7),
(11, 'Kannuketty', 11),
(12, 'Thamaressery', 12);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add tbl_district', 7, 'add_tbl_district'),
(26, 'Can change tbl_district', 7, 'change_tbl_district'),
(27, 'Can delete tbl_district', 7, 'delete_tbl_district'),
(28, 'Can view tbl_district', 7, 'view_tbl_district'),
(29, 'Can add tbl_login', 8, 'add_tbl_login'),
(30, 'Can change tbl_login', 8, 'change_tbl_login'),
(31, 'Can delete tbl_login', 8, 'delete_tbl_login'),
(32, 'Can view tbl_login', 8, 'view_tbl_login'),
(33, 'Can add tbl_location', 9, 'add_tbl_location'),
(34, 'Can change tbl_location', 9, 'change_tbl_location'),
(35, 'Can delete tbl_location', 9, 'delete_tbl_location'),
(36, 'Can view tbl_location', 9, 'view_tbl_location'),
(37, 'Can add tbl_category', 10, 'add_tbl_category'),
(38, 'Can change tbl_category', 10, 'change_tbl_category'),
(39, 'Can delete tbl_category', 10, 'delete_tbl_category'),
(40, 'Can view tbl_category', 10, 'view_tbl_category'),
(41, 'Can add user', 11, 'add_user'),
(42, 'Can change user', 11, 'change_user'),
(43, 'Can delete user', 11, 'delete_user'),
(44, 'Can view user', 11, 'view_user'),
(45, 'Can add tbl_login', 12, 'add_tbl_login'),
(46, 'Can change tbl_login', 12, 'change_tbl_login'),
(47, 'Can delete tbl_login', 12, 'delete_tbl_login'),
(48, 'Can view tbl_login', 12, 'view_tbl_login'),
(49, 'Can add tbl_company', 13, 'add_tbl_company'),
(50, 'Can change tbl_company', 13, 'change_tbl_company'),
(51, 'Can delete tbl_company', 13, 'delete_tbl_company'),
(52, 'Can view tbl_company', 13, 'view_tbl_company'),
(53, 'Can add tbl_service', 14, 'add_tbl_service'),
(54, 'Can change tbl_service', 14, 'change_tbl_service'),
(55, 'Can delete tbl_service', 14, 'delete_tbl_service'),
(56, 'Can view tbl_service', 14, 'view_tbl_service'),
(57, 'Can add tbl_booking', 15, 'add_tbl_booking'),
(58, 'Can change tbl_booking', 15, 'change_tbl_booking'),
(59, 'Can delete tbl_booking', 15, 'delete_tbl_booking'),
(60, 'Can view tbl_booking', 15, 'view_tbl_booking'),
(61, 'Can add tbl_payment', 16, 'add_tbl_payment'),
(62, 'Can change tbl_payment', 16, 'change_tbl_payment'),
(63, 'Can delete tbl_payment', 16, 'delete_tbl_payment'),
(64, 'Can view tbl_payment', 16, 'view_tbl_payment');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `companyapp_tbl_service`
--

DROP TABLE IF EXISTS `companyapp_tbl_service`;
CREATE TABLE IF NOT EXISTS `companyapp_tbl_service` (
  `serviceid` int NOT NULL AUTO_INCREMENT,
  `servicename` varchar(100) NOT NULL,
  `totalamount` bigint NOT NULL,
  `image` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `compid_id` int NOT NULL,
  `categoryid_id` int NOT NULL,
  PRIMARY KEY (`serviceid`),
  KEY `companyapp_tbl_service_compid_id_fa62de89` (`compid_id`),
  KEY `companyapp_tbl_service_categoryid_id_6ff42243` (`categoryid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `companyapp_tbl_service`
--

INSERT INTO `companyapp_tbl_service` (`serviceid`, `servicename`, `totalamount`, `image`, `description`, `compid_id`, `categoryid_id`) VALUES
(4, 'Window Cleaning', 2500, 'wind_cleninf_Oa8bjpe.jpg', 'Cleans window', 17, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'adminapp', 'tbl_district'),
(8, 'adminapp', 'tbl_login'),
(9, 'adminapp', 'tbl_location'),
(10, 'adminapp', 'tbl_category'),
(11, 'guestapp', 'user'),
(12, 'guestapp', 'tbl_login'),
(13, 'guestapp', 'tbl_company'),
(14, 'companyapp', 'tbl_service'),
(15, 'userapp', 'tbl_booking'),
(16, 'userapp', 'tbl_payment');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=60 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-11-27 05:57:48.964063'),
(2, 'auth', '0001_initial', '2025-11-27 05:57:49.377697'),
(3, 'admin', '0001_initial', '2025-11-27 05:57:49.505689'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-11-27 05:57:49.512634'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-11-27 05:57:49.522437'),
(6, 'adminapp', '0001_initial', '2025-11-27 05:57:49.533853'),
(7, 'contenttypes', '0002_remove_content_type_name', '2025-11-27 05:57:49.593389'),
(8, 'auth', '0002_alter_permission_name_max_length', '2025-11-27 05:57:49.622499'),
(9, 'auth', '0003_alter_user_email_max_length', '2025-11-27 05:57:49.676844'),
(10, 'auth', '0004_alter_user_username_opts', '2025-11-27 05:57:49.695687'),
(11, 'auth', '0005_alter_user_last_login_null', '2025-11-27 05:57:49.739434'),
(12, 'auth', '0006_require_contenttypes_0002', '2025-11-27 05:57:49.740917'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2025-11-27 05:57:49.748998'),
(14, 'auth', '0008_alter_user_username_max_length', '2025-11-27 05:57:49.782413'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2025-11-27 05:57:49.814143'),
(16, 'auth', '0010_alter_group_name_max_length', '2025-11-27 05:57:49.845867'),
(17, 'auth', '0011_update_proxy_permissions', '2025-11-27 05:57:49.855819'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2025-11-27 05:57:49.888403'),
(19, 'sessions', '0001_initial', '2025-11-27 05:57:49.920083'),
(20, 'adminapp', '0002_tbl_login', '2025-11-28 05:47:13.178566'),
(21, 'adminapp', '0003_tbl_location', '2025-12-04 10:07:21.167174'),
(22, 'adminapp', '0004_tbl_category', '2025-12-11 06:27:47.117994'),
(23, 'guestapp', '0001_initial', '2025-12-15 04:53:31.418935'),
(24, 'guestapp', '0002_tbl_login_rename_placeid_user_locationid_and_more', '2025-12-16 10:13:28.900030'),
(25, 'adminapp', '0005_delete_tbl_login', '2025-12-16 10:13:28.911315'),
(26, 'guestapp', '0003_tbl_company', '2026-01-06 09:53:56.670221'),
(27, 'guestapp', '0004_rename_phoneno_tbl_company_contact_tbl_company_city_and_more', '2026-01-08 08:39:53.739934'),
(28, 'guestapp', '0005_alter_tbl_company_city_alter_tbl_company_state_and_more', '2026-01-08 08:39:53.751057'),
(29, 'guestapp', '0006_tbl_company_username', '2026-01-08 09:43:18.264984'),
(30, 'guestapp', '0007_alter_tbl_company_username', '2026-01-08 09:43:18.269654'),
(31, 'guestapp', '0008_tbl_company_description_tbl_company_image', '2026-01-09 04:28:03.173206'),
(32, 'guestapp', '0009_alter_tbl_company_description_and_more', '2026-01-09 04:28:03.182186'),
(33, 'guestapp', '0010_tbl_company_status', '2026-01-09 04:57:02.443333'),
(34, 'guestapp', '0011_tbl_login_status', '2026-01-09 05:00:39.690464'),
(51, 'companyapp', '0004_alter_tbl_service_image', '2026-01-19 06:49:35.758919'),
(36, 'guestapp', '0012_remove_tbl_company_verificationstatus', '2026-01-14 06:13:55.113625'),
(37, 'guestapp', '0013_user_name', '2026-01-14 06:15:10.065419'),
(38, 'guestapp', '0014_alter_user_name', '2026-01-14 06:15:20.858595'),
(50, 'companyapp', '0003_alter_tbl_service_image', '2026-01-19 06:49:35.752967'),
(41, 'guestapp', '0015_alter_tbl_company_image', '2026-01-16 05:33:26.806372'),
(49, 'companyapp', '0002_alter_tbl_service_serviceid', '2026-01-19 06:49:35.717215'),
(43, 'guestapp', '0016_alter_tbl_company_image', '2026-01-16 05:54:14.178459'),
(48, 'companyapp', '0001_initial', '2026-01-19 06:49:35.680278'),
(45, 'guestapp', '0017_alter_tbl_company_image', '2026-01-16 06:02:12.071743'),
(47, 'guestapp', '0018_alter_tbl_company_image', '2026-01-16 07:13:44.951633'),
(52, 'companyapp', '0005_alter_tbl_service_image', '2026-01-19 06:49:35.792227'),
(53, 'companyapp', '0006_alter_tbl_service_image', '2026-01-19 06:49:35.798354'),
(54, 'companyapp', '0007_tbl_service_categoryid', '2026-01-19 06:49:35.884448'),
(55, 'userapp', '0001_initial', '2026-01-23 05:43:15.654796'),
(56, 'userapp', '0002_tbl_booking_loginid', '2026-01-23 10:09:26.093261'),
(57, 'userapp', '0003_alter_tbl_booking_loginid', '2026-01-23 10:09:26.119415'),
(58, 'userapp', '0004_remove_tbl_booking_loginid', '2026-01-23 10:12:57.343867'),
(59, 'userapp', '0005_tbl_payment', '2026-01-29 09:30:56.463548');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('gwbhmrfp1x0i82k73njwprng3v46wmfq', 'eyJsb2dpbmlkIjoxLCJ1c2VybmFtZSI6ImFkbWluIn0:1vnWc0:4k1q9rrrFJCgJBpttySseEJk-xV8hprTQYbe65pModQ', '2026-02-18 06:43:40.412865');

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_tbl_company`
--

DROP TABLE IF EXISTS `guestapp_tbl_company`;
CREATE TABLE IF NOT EXISTS `guestapp_tbl_company` (
  `compid` int NOT NULL AUTO_INCREMENT,
  `compname` varchar(50) NOT NULL,
  `contact` varchar(11) NOT NULL,
  `locationid_id` int NOT NULL,
  `loginid_id` int NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `street` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `description` varchar(200) NOT NULL,
  `image` varchar(100) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`compid`),
  KEY `guestapp_tbl_company_locationid_id_657881e8` (`locationid_id`),
  KEY `guestapp_tbl_company_loginid_id_d66faff3` (`loginid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `guestapp_tbl_company`
--

INSERT INTO `guestapp_tbl_company` (`compid`, `compname`, `contact`, `locationid_id`, `loginid_id`, `city`, `state`, `street`, `username`, `description`, `image`, `status`) VALUES
(17, 'KClean', '45677890', 5, 39, 'Kochi', 'Kerala', 'Nagr', 'kclean123', 'Good', '1000041020.jpg', 'Accepted'),
(16, 'ArnClean1', '8590058532', 6, 38, 'Kochi', 'Kerala', 'Alfiya nagar', 'arnclean1234', 'Good', 'ragraph_text.png', 'Accepted');

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_tbl_login`
--

DROP TABLE IF EXISTS `guestapp_tbl_login`;
CREATE TABLE IF NOT EXISTS `guestapp_tbl_login` (
  `loginid` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `role` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`loginid`)
) ENGINE=MyISAM AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `guestapp_tbl_login`
--

INSERT INTO `guestapp_tbl_login` (`loginid`, `username`, `password`, `role`, `status`) VALUES
(1, 'admin', 'admin', 'admin', 'Accepted'),
(39, 'kclean123', '123', 'company', 'Accepted'),
(21, 'Arnold', '123', 'user', 'Accepted'),
(24, 'Bilvert', '123', 'user', 'Accepted'),
(38, 'arnclean1234', '123', 'company', 'Accepted');

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_user`
--

DROP TABLE IF EXISTS `guestapp_user`;
CREATE TABLE IF NOT EXISTS `guestapp_user` (
  `userid` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `contact` varchar(15) NOT NULL,
  `email` varchar(50) NOT NULL,
  `loginid_id` int NOT NULL,
  `locationid_id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`userid`),
  KEY `guestapp_user_loginid_id_1c0e4c4e` (`loginid_id`),
  KEY `guestapp_user_placeid_id_2c0cf2e3` (`locationid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `guestapp_user`
--

INSERT INTO `guestapp_user` (`userid`, `username`, `password`, `contact`, `email`, `loginid_id`, `locationid_id`, `name`) VALUES
(3, 'Bilvert', '123', '45677890', 'arnoldsherry999@gmail.com', 24, 11, 'bilvert');

-- --------------------------------------------------------

--
-- Table structure for table `userapp_tbl_booking`
--

DROP TABLE IF EXISTS `userapp_tbl_booking`;
CREATE TABLE IF NOT EXISTS `userapp_tbl_booking` (
  `bookingid` int NOT NULL AUTO_INCREMENT,
  `bookingstatus` varchar(50) NOT NULL,
  `bookingdate` date NOT NULL,
  `serviceid_id` int NOT NULL,
  `userid_id` int NOT NULL,
  PRIMARY KEY (`bookingid`),
  KEY `userapp_tbl_booking_serviceid_id_4289bd0b` (`serviceid_id`),
  KEY `userapp_tbl_booking_userid_id_fde6a056` (`userid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `userapp_tbl_booking`
--

INSERT INTO `userapp_tbl_booking` (`bookingid`, `bookingstatus`, `bookingdate`, `serviceid_id`, `userid_id`) VALUES
(9, 'Requested', '2026-02-04', 4, 3),
(8, 'Requested', '2026-02-04', 4, 3),
(7, 'Paid', '2026-02-03', 4, 3);

-- --------------------------------------------------------

--
-- Table structure for table `userapp_tbl_payment`
--

DROP TABLE IF EXISTS `userapp_tbl_payment`;
CREATE TABLE IF NOT EXISTS `userapp_tbl_payment` (
  `paymentid` int NOT NULL AUTO_INCREMENT,
  `paymentdate` date NOT NULL,
  `totalamount` int NOT NULL,
  `paymentstatus` varchar(50) NOT NULL,
  `bookingid_id` int NOT NULL,
  PRIMARY KEY (`paymentid`),
  KEY `userapp_tbl_payment_bookingid_id_f9e4a766` (`bookingid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `userapp_tbl_payment`
--

INSERT INTO `userapp_tbl_payment` (`paymentid`, `paymentdate`, `totalamount`, `paymentstatus`, `bookingid_id`) VALUES
(2, '2026-02-02', 2500, 'Paid', 7);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
