-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 17, 2023 at 09:29 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blog_flask`
--

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `author` varchar(30) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `content` text NOT NULL,
  `img_file` varchar(12) NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `author`, `slug`, `content`, `img_file`, `date`) VALUES
(1, 'This is the First Post', 'Aryan', 'first-post', 'In finance, stock (also capital stock) consists of all the shares by which ownership of a corporation or company is divided.[1] (Especially in American English, the word \"stocks\" is also used to refer to shares.)[1][2] A single share of the stock means fractional ownership of the corporation in proportion to the total number of shares. This typically entitles the shareholder (stockholder) to that fraction of the company\'s earnings, proceeds from liquidation of assets (after discharge of all senior claims such as secured and unsecured debt),[3] or voting power, often dividing these up in proportion to the amount of money each stockholder has invested. Not all stock is necessarily equal, as certain classes of stock may be issued for example without voting rights, with enhanced voting rights, or with a certain priority to receive profits or liquidation proceeds before or after other classes of shareholders.', 'post-bg.jpg', '2023-01-17 22:38:28'),
(2, 'This is the Second Post', 'Rahul', 'second-post', 'The content for the second post.', 'about-bg.jpg', '2023-01-17 12:44:15'),
(3, 'The Third Post', 'Raj', 'third-post', 'Content for the third post', 'post-bg.jpg', '2023-01-17 23:24:01'),
(4, 'The Fourth Post', 'Aryan', 'fourth-post', 'Content for the fourth post', 'post-bg.jpg', '2023-01-17 23:25:08'),
(5, 'The Fifth Post', 'Aryan', 'fifth-post', 'Content for the fifth post', 'post-bg.jpg', '2023-01-17 23:25:42'),
(6, 'The Sixth Post', 'Aryan', 'sixth-post', 'Content for the sixth post', 'post-bg.jpg', '2023-01-17 23:26:12'),
(7, 'The Seventh Post', 'Aryan', 'seventh-post', 'Content for the seventh post', 'post-bg.jpg', '2023-01-17 23:26:46'),
(8, 'The Eighth Post', 'Aryan', 'eighth-post', 'Content for the eighth post', 'post-bg.jpg', '2023-01-17 23:28:12'),
(9, 'The Ninth Post', 'Aryan', 'ninth-post', 'Content for the ninth post', 'post-bg.jpg', '2023-01-17 23:28:47'),
(10, 'The Tenth Post', 'Raj', 'tenth-post', 'Content for the tenth post', 'post-bg.jpg', '2023-01-18 01:59:02');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
