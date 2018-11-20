SET time_zone = "America/Toronto";

CREATE DATABASE texada;
use texada;

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int(11) PRIMARY KEY NOT NULL,
  `name` varchar(255) NOT NULL
);

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `name`) VALUES
(1, 'Cesna 120'),
(2, 'DC-6 Twin Otter'),
(3, 'Piper M600'),
(4, 'Art Boom 6500');

--
-- Table structure for table `locations`
--

CREATE TABLE `locations` (
  `record_id` int(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
  `product_id` int(11) NOT NULL,
  `datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `longitude` decimal(10,7) NOT NULL,
  `latitude` decimal(10,7) NOT NULL,
  `elevation` int(5) NOT NULL
);

--
-- Indexes for table `locations`
--
ALTER TABLE `locations`
  ADD KEY `product_id` (`product_id`);


--
-- Constraints for table `locations`
--
ALTER TABLE `locations` ADD CONSTRAINT `fk_prod_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;



--
-- Dumping data for table `locations`
--

INSERT INTO locations
  (product_id, datetime, longitude, latitude, elevation)
VALUES
  (1, '2016-10-12 12:00:00', 43.2583264, -81.8149807, 500),
  (1, '2016-10-13 12:00:00', 42.559112, -79.286693, 550),
  (1, '2016-10-14 12:00:00', 43.559112, -85.286693, 600),
  (1, '2016-10-15 12:00:00', 42.3119735, -83.0941179, 650),
  (2, '2016-10-12 12:00:00', 43.459112, -80.386693, 500),
  (2, '2016-10-13 12:00:00', 42.459112, -79.386693, 450),
  (2, '2016-10-15 12:00:00', 44.459112, -81.386693, 400),
  (2, '2016-10-12 12:00:00', 43.2583264, -81.8149807, 500),
  (3, '2016-10-15 12:00:00', 44.459112, -81.386693, 500),
  (3, '2016-10-15 12:00:00', 45.459112, -82.386693, 600),
  (3, '2016-10-15 12:00:00', 46.459112, -83.386693, 700),
  (3, '2016-10-15 12:00:00', 47.459112, -84.386693, 800),
  (3, '2016-10-15 12:00:00', 48.459112, -85.386693, 900),
  (4, '2017-08-04 14:20:38', 43.7634618, -79.3688191, 800),
  (4, '2017-08-04 16:20:38', 43.8001468, -79.2342365, 400),
  (4, '2017-08-04 14:20:38', 44.51165, -80.1239422, 550),
  (4, '2017-08-04 14:20:38', 43.1501439, -79.0504945, 300);

-- --------------------------------------------------------