-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 04, 2020 at 03:42 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.26

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
-- Table structure for table `aspirant_login`
--


--
-- Dumping data for table `aspirant_login`
--

INSERT INTO `aspirant_login` (`id`, `prn`, `password`, `university`, `clg`, `type`) VALUES
(1, '22212720171124210004', '22212720171124210004', '', 'Shri Guru Gobind Singji College of Engineering, Nanded', 'alumni'),
(2, '22212720171124210005', '22212720171124210005', 'SRTMUN', 'MGM\'s College of Engineering', 'pending'),
(3, '22212720171124210006', '22212720171124210006', 'SRTMUN', 'MGM\'s College of Engineering', 'alumni'),
(4, '22212720171124210007', '22212720171124210007', 'SRTMUN', 'MGM\'s College of Engineering', 'alumni');

-- --------------------------------------------------------

--
-- Table structure for table `authority_login`
--

--
-- Dumping data for table `authority_login`
--

INSERT INTO `authority_login` (`id`, `Email`, `Password`, `Type`, `University`, `College`) VALUES
(1, 'dhe@goa.ac.in', 'dhe@goa.ac.in', 'DHE', NULL, NULL),
(2, 'director@gramin.ac.in', 'director@gramin.ac.in', 'DIR', 'SRTMUN', 'Gramin College of Engineering, Nanded'),
(3, 'director@matoshri.ac.in', 'director@matoshri.ac.in', 'DIR', 'SRTMUN', 'Matoshri Prathishtan, Nanded'),
(4, 'director@mgmcen.ac.in', 'director@mgmcen.ac.in', 'DIR', 'SRTMUN', 'MGM\'s College of Engineering, Nanded'),
(5, 'director@sggs.ac.in', 'director@sggs.ac.in', 'DIR', NULL, 'Shri Guru Gobind Singji College of Engineering, Nanded');

-- --------------------------------------------------------

--
-- Table structure for table `colleges`
--

-- Dumping data for table `colleges`
--

INSERT INTO `colleges` (`College_ID`, `College_Name`, `University`, `Director_Name`) VALUES
(1001, 'Gramin College of Engineering, Nanded', 'SRTMUN', 'Dr. A. M. Yadav'),
(2020, 'Shri Guru Gobind Singhji, Nanded', 'Autonomous', 'Dr. Y.V. Joshi'),
(2117, 'Matoshri Pratishthan, Nanded', 'SRTMUN', 'Dr. V. B. Chari'),
(2127, 'MGM\'s College of Engineering, Nanded', 'SRTMUN', 'Dr. Mrs. Geeta Lathkar');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `aspirant_login`
--


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
