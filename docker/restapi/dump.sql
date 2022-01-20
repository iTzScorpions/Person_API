CREATE DATABASE IF NOT EXISTS `person`
USE `person`;

CREATE TABLE IF NOT EXISTS `person` (
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

