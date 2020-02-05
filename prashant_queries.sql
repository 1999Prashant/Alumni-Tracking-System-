-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 04, 2020 at 03:46 AM
-- Server version: 10.1.25-MariaDB
-- PHP Version: 7.1.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `alumni_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `alumni_details`
--

CREATE TABLE `alumni_details` (
  `PRN` int(11) NOT NULL,
  `Name` varchar(30) DEFAULT NULL,
  `Year` int(11) NOT NULL,
  `Branch` varchar(40) DEFAULT NULL,
  `Specialization` varchar(40) DEFAULT NULL,
  `Work_Ex` varchar(20) DEFAULT NULL,
  `College` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `alumni_details`
--

INSERT INTO `alumni_details` (`PRN`, `Name`, `Year`, `Branch`, `Specialization`, `Work_Ex`, `College`) VALUES
(123456, 'SANGMESH SOMAWAR', 2013, 'Computer Science and Engineering ', 'IOT', '4 Years', 'MGM\'S COLLEGE OF ENGINEERING NANDED'),
(145236, 'JUNED KHAN', 2008, 'Computer Science and Engineering ', 'Machine Learning', '10 Years', 'MGM\'S COLLEGE OF ENGINEERING NANDED'),
(158799, 'RAHUL BISEN', 2006, 'Information Technology ', 'Artificial intelligence ', '3 Years', 'SGGS COLLEGE OF ENGINEERING NANDED'),
(653214, 'Rupali Bhange', 2005, 'Computer Science and Engineering ', 'Front-End Developer ', '2 Years', 'SGGS COLLEGE OF ENGINEERING NANDED');

-- --------------------------------------------------------

--
-- Table structure for table `authority_login`
--

CREATE TABLE `authority_login` (
  `Email` int(11) NOT NULL,
  `Password` varchar(60) DEFAULT NULL,
  `Type` varchar(60) NOT NULL,
  `University` varchar(60) DEFAULT NULL,
  `College` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `colleges`
--

CREATE TABLE `colleges` (
  `College_ID` int(11) NOT NULL,
  `College_Name` varchar(60) DEFAULT NULL,
  `University` varchar(60) NOT NULL,
  `Director_Name` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `student_details`
--

CREATE TABLE `student_details` (
  `PRN` int(11) NOT NULL,
  `Name` varchar(30) DEFAULT NULL,
  `Year` int(11) NOT NULL,
  `Alumni` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_details`
--

INSERT INTO `student_details` (`PRN`, `Name`, `Year`, `Alumni`) VALUES
(457822, 'PRASAD NAGTHANE', 2018, 'MINAL KAMINWAR'),
(568462, 'BHAKTI PATIL', 2019, 'JUNED KHAN'),
(659752, 'PRASHANT PHULARI', 2020, 'SANGAMESH SOMAWAR'),
(784512, 'SHWETA DINKALE', 2017, 'RUPALI BHANGE'),
(879451, 'FURKHAN SHAIKH', 2020, 'SANGAMESH SOMAWAR');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alumni_details`
--
ALTER TABLE `alumni_details`
  ADD PRIMARY KEY (`PRN`);

--
-- Indexes for table `authority_login`
--
ALTER TABLE `authority_login`
  ADD PRIMARY KEY (`Email`);

--
-- Indexes for table `colleges`
--
ALTER TABLE `colleges`
  ADD PRIMARY KEY (`College_ID`);

--
-- Indexes for table `student_details`
--
ALTER TABLE `student_details`
  ADD PRIMARY KEY (`PRN`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `alumni_details`
--
ALTER TABLE `alumni_details`
  MODIFY `PRN` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=653215;
--
-- AUTO_INCREMENT for table `authority_login`
--
ALTER TABLE `authority_login`
  MODIFY `Email` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `colleges`
--
ALTER TABLE `colleges`
  MODIFY `College_ID` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `student_details`
--
ALTER TABLE `student_details`
  MODIFY `PRN` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=879452;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
