-- Create database if not exists
CREATE DATABASE IF NOT EXISTS `record`;

-- Use the created database
USE `record`;

-- Create table to store customer details
CREATE TABLE IF NOT EXISTS `customer` (
    `CustomerID` INT AUTO_INCREMENT PRIMARY KEY,
    `CustomerName` VARCHAR(100) NOT NULL,
    `MothersName` VARCHAR(100),
    `FathersName` VARCHAR(100),
    `Gender` VARCHAR(10) NOT NULL,
    `City` VARCHAR(100),
    `MobileNumber` VARCHAR(15) NOT NULL,
    `State` VARCHAR(100),
    `EmailId` VARCHAR(100)
);
