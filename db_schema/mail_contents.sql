-- phpMyAdmin SQL Dump
-- version 4.8.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 04, 2018 at 05:53 PM
-- Server version: 10.1.33-MariaDB
-- PHP Version: 7.2.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `popo`
--

-- --------------------------------------------------------

--
-- Table structure for table `mail_contents`
--

CREATE TABLE `mail_contents` (
  `mail_id` varchar(128) NOT NULL,
  `from` text,
  `to` text,
  `subject` text,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mail_contents`
--

INSERT INTO `mail_contents` (`mail_id`, `from`, `to`, `subject`, `date`) VALUES
('16441e7797bd3d3e', 'YouTube <noreply@youtube.com>', 'rnknanthakumar@gmail.com', 'Action Mania V2 just uploaded a video', '2018-06-27'),
('164453af0811a69b', 'YouTube <noreply@youtube.com>', 'rnknanthakumar@gmail.com', 'Action Mania V2 just uploaded a video', '2018-06-28'),
('1644a12079f7ba96', 'YouTube <noreply@youtube.com>', 'rnknanthakumar@gmail.com', 'Action Mania V2 just uploaded a video', '2018-06-28'),
('16454d51b32748dd', 'YouTube <noreply@youtube.com>', 'rnknanthakumar@gmail.com', 'Action Mania V2 just uploaded a video', '2018-07-01'),
('16459d1c7398ad48', 'Amazon Web Services <aws-apac-marketing@amazon.com>', 'rnknanthakumar@gmail.com', 'Don\'t Miss the Opportunity to Hear from Experts | AWS Innovate Online Conference 2018', '2018-07-02'),
('16465a748d9a3afb', 'YouTube <noreply@youtube.com>', 'rnknanthakumar@gmail.com', 'Action Mania V2 just uploaded a video', '2018-07-04'),
('16469e6f5e42f179', 'YouTube <noreply@youtube.com>', 'rnknanthakumar@gmail.com', 'Action Mania V2 just uploaded a video', '2018-07-05'),
('1646a15a76f06cc4', 'YouTube <noreply@youtube.com>', 'rnknanthakumar@gmail.com', '1 Kg Biriyani just uploaded a video', '2018-07-05'),
('1646b82c232f8cd9', 'YouTube <noreply@youtube.com>', 'rnknanthakumar@gmail.com', 'Action Mania V2 just uploaded a video', '2018-07-05'),
('164984a294f93e45', 'YouTube <noreply@youtube.com>', 'rnknanthakumar@gmail.com', 'Action Mania V2 just uploaded a video', '2018-07-14');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mail_contents`
--
ALTER TABLE `mail_contents`
  ADD PRIMARY KEY (`mail_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
