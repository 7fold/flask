CREATE DATABASE texada;
use texada;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "-05:00";

--
-- Table structure for table `locations`
--

CREATE TABLE `locations` (
  `record_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `longitude` decimal(10,7) NOT NULL,
  `latitude` decimal(10,7) NOT NULL,
  `elevation` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `locations`
--

INSERT INTO `locations` (`record_id`, `product_id`, `datetime`, `longitude`, `latitude`, `elevation`) VALUES
(18, 1, '2016-10-12 16:00:00', '43.2583264', '-81.8149807', 500),
(19, 1, '2016-10-13 16:00:00', '42.5591120', '-79.2866930', 550),
(20, 1, '2016-10-14 16:00:00', '43.5591120', '-85.2866930', 600),
(21, 1, '2016-10-15 16:00:00', '42.3119735', '-83.0941179', 650),
(22, 2, '2016-10-12 16:00:00', '43.4591120', '-80.3866930', 500),
(23, 2, '2016-10-13 16:00:00', '42.4591120', '-79.3866930', 450),
(24, 2, '2016-10-15 16:00:00', '44.4591120', '-81.3866930', 400),
(25, 2, '2016-10-12 16:00:00', '43.2583264', '-81.8149807', 500),
(26, 3, '2016-10-15 16:00:00', '44.4591120', '-81.3866930', 500),
(27, 3, '2016-10-15 16:00:00', '45.4591120', '-82.3866930', 600),
(28, 3, '2016-10-15 16:00:00', '46.4591120', '-83.3866930', 700),
(29, 3, '2016-10-15 16:00:00', '47.4591120', '-84.3866930', 800),
(30, 3, '2016-10-15 16:00:00', '48.4591120', '-85.3866930', 900),
(31, 4, '2017-08-04 18:20:38', '43.7634618', '-79.3688191', 800),
(32, 4, '2017-08-04 20:20:38', '43.8001468', '-79.2342365', 400),
(33, 4, '2017-08-04 18:20:38', '44.5116500', '-80.1239422', 550),
(34, 4, '2017-08-04 18:20:38', '43.1501439', '-79.0504945', 300);

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `name`) VALUES
(1, 'Cesna 120'),
(2, 'DC-6 Twin Otter'),
(3, 'Piper M600'),
(4, 'Art Boom 6500');

--
-- Indexes for table `locations`
--
ALTER TABLE `locations`
  ADD PRIMARY KEY (`record_id`),
  ADD KEY `product_id` (`product_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for table `locations`
--
ALTER TABLE `locations`
  MODIFY `record_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `locations`
--
ALTER TABLE `locations`
  ADD CONSTRAINT `fk_prod_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;




-- CREATE TABLE products (
--   id INT(11) PRIMARY KEY,
--   name VARCHAR(65) NOT NULL
-- );

-- INSERT INTO products
--   (id, name)
-- VALUES
--   (1, 'Cesna 120'),
--   (2, 'DC-6 Twin Otter'),
--   (3, 'Piper M600'),
--   (4, 'Art Boom 6500');

-- INSERT INTO locations
--   (product_id, datetime, longitude, latitude, elevation)
-- VALUES
--   (1, '2016-10-12 12:00:00', 43.2583264, -81.8149807, 500),
--   (1, '2016-10-13 12:00:00', 42.559112, -79.286693, 550),
--   (1, '2016-10-14 12:00:00', 43.559112, -85.286693, 600),
--   (1, '2016-10-15 12:00:00', 42.3119735, -83.0941179, 650),
--   (2, '2016-10-12 12:00:00', 43.459112, -80.386693, 500),
--   (2, '2016-10-13 12:00:00', 42.459112, -79.386693, 450),
--   (2, '2016-10-15 12:00:00', 44.459112, -81.386693, 400),
--   (2, '2016-10-12 12:00:00', 43.2583264, -81.8149807, 500),
--   (3, '2016-10-15 12:00:00', 44.459112, -81.386693, 500),
--   (3, '2016-10-15 12:00:00', 45.459112, -82.386693, 600),
--   (3, '2016-10-15 12:00:00', 46.459112, -83.386693, 700),
--   (3, '2016-10-15 12:00:00', 47.459112, -84.386693, 800),
--   (3, '2016-10-15 12:00:00', 48.459112, -85.386693, 900),
--   (4, '2017-08-04 14:20:38', 43.7634618, -79.3688191, 800),
--   (4, '2017-08-04 16:20:38', 43.8001468, -79.2342365, 400),
--   (4, '2017-08-04 14:20:38', 44.51165, -80.1239422, 550),
--   (4, '2017-08-04 14:20:38', 43.1501439, -79.0504945, 300);


  -- SELECT t1.id, t1.name as description, t2.datetime, t2.longitude, t2.latitude, t2.elevation from products t1 INNER JOIN locations t2 ON t1.id = t2.product_id
