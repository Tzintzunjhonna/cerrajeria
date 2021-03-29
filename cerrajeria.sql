-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 02-08-2019 a las 20:09:01
-- Versión del servidor: 5.6.17
-- Versión de PHP: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `cerrajeria`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consultacarro`
--

CREATE TABLE IF NOT EXISTS `consultacarro` (
  `Id` int(255) NOT NULL AUTO_INCREMENT,
  `Marca` varchar(255) NOT NULL,
  `Modelo` varchar(255) NOT NULL,
  `Ubicacion` varchar(255) NOT NULL,
  `Correo` varchar(255) NOT NULL,
  `Tipo_trabajo` varchar(255) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Volcado de datos para la tabla `consultacarro`
--

INSERT INTO `consultacarro` (`Id`, `Marca`, `Modelo`, `Ubicacion`, `Correo`, `Tipo_trabajo`) VALUES
(2, 'ford', 'Campana', 'El molino #123', 'Jhonathan@gmail.com', 'abrir-car'),
(3, 'Ford', 'x', 'Xalpa', 'xalpa@gmail', 'abrir-car'),
(4, 'sad', 'asd', 'asd', 'asd@c', 'rep-chapa');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consultacasa`
--

CREATE TABLE IF NOT EXISTS `consultacasa` (
  `Id` int(255) NOT NULL AUTO_INCREMENT,
  `Domicilio` varchar(255) NOT NULL,
  `Numero` varchar(255) NOT NULL,
  `Correo` varchar(255) NOT NULL,
  `Referencias` varchar(255) NOT NULL,
  `Tipo_trabajo` varchar(255) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Volcado de datos para la tabla `consultacasa`
--

INSERT INTO `consultacasa` (`Id`, `Domicilio`, `Numero`, `Correo`, `Referencias`, `Tipo_trabajo`) VALUES
(2, 'sasx', '324234', 'asdas@asdsa', 'asdasdas', 'rep-switch'),
(3, 'xalpa', '24546', 'xalpahabk@sasa', 'por la utt', 'abrir-casa'),
(4, 'sdfds', '234432', 'd@dasa', 'asdsadas', 'abrir-casa'),
(5, 'sa', '3424', 'dsad@dcd', 'ddssd', 'abrir-casa');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservacarro`
--

CREATE TABLE IF NOT EXISTS `reservacarro` (
  `Id` int(10) NOT NULL AUTO_INCREMENT,
  `Marca` varchar(255) NOT NULL,
  `Modelo` varchar(255) NOT NULL,
  `Ubicacion` varchar(255) NOT NULL,
  `Correo` varchar(255) NOT NULL,
  `Tipo_trabajo` varchar(255) NOT NULL,
  `Fecha` text NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=15 ;

--
-- Volcado de datos para la tabla `reservacarro`
--

INSERT INTO `reservacarro` (`Id`, `Marca`, `Modelo`, `Ubicacion`, `Correo`, `Tipo_trabajo`, `Fecha`) VALUES
(11, 'Ford', 'Campana', 'El molino #123', 'Jhonathan@gmail.com', 'rep-chapa', '2552-05-25'),
(12, 'Ford', 'Campana', 'El molino #123', 'Jhonathan@gmail.com', 'rep-chapa', '2222-02-02'),
(13, 'Ford', 'Campana', 'El molino #123', 'Jhonathan@gmail.com', 'rep-chapa', '3232-02-03'),
(14, 'Ford', 'Campana', 'El molino #123', 'Jhonathan@gmail.com', 'rep-chapa', '3232-02-03');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservacasa`
--

CREATE TABLE IF NOT EXISTS `reservacasa` (
  `Id` int(255) NOT NULL AUTO_INCREMENT,
  `Domicilio` varchar(255) NOT NULL,
  `Numero` varchar(255) NOT NULL,
  `Correo` varchar(255) NOT NULL,
  `Referencias` varchar(300) NOT NULL,
  `Tipo_trabajo` varchar(255) NOT NULL,
  `Fecha` varchar(255) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=37 ;

--
-- Volcado de datos para la tabla `reservacasa`
--

INSERT INTO `reservacasa` (`Id`, `Domicilio`, `Numero`, `Correo`, `Referencias`, `Tipo_trabajo`, `Fecha`) VALUES
(4, 'weffsd', '24232312', 'csac@dwdq', 'wdqwdwqd', 'abrir-car', '4322-03-04'),
(5, 'dwqdqw', '32252', 'dscdaf@sdasd', 'sadasdasdd', 'abrir-casa', '4545-05-04'),
(6, 'axAXa', '651654', 'casc@sdasd', 'adsd', 'duplicado', '0004-04-04'),
(7, 'hfhfgh', '54245245', 'sdfs@asdasd', 'adsadsadsadsasa', 'abrir-casa', '5255-02-05'),
(8, 'sgfsg', '5245324', 'bfdbdfb@ffdgd', 'gdfgdfgdfg', 'rep-switch', '2563-02-04'),
(9, 'hfghj', '6838386', 'bfgbr@dffs', 'fddsfdsfsd', 'cam-chapa', '7577-05-07'),
(10, '59454', '5191', '269@dsd', 'sdfdsdcs', 'abrir-casa', '0277-04-04'),
(11, '6665656', '4654654', '45464@654', '6545646', 'abrir-casa', '5444-05-05'),
(12, 'erfe', '23424234', 'fds@efwef', 'wefwfw', 'duplicado', '4542-02-05'),
(13, 'ewfweff', 'we423424', 'sdvsd@sdasdas', 'dasdadsad', 'abrir-casa', '5225-02-25'),
(15, 'hjdsaghid', '456465', 'khbdkhasgd@sda', 'asdasdasd', 'abrir-car', '5455-05-04'),
(16, 'asdasd', '6541654', 'dfsd@asdad', 'asdasdasd', 'abrir-car', '5255-02-25'),
(17, 'dsfsdf', '52455', 'fdsvd@xsasx', 'asaxxa', 'abrir-car', '5255-02-25'),
(19, 'wdgwqdg|', '684464', 'jhcouwc@sjwsj', 'hdohowhd', 'duplicado', '5545-05-05'),
(20, 'dcsdcs', '324234234', 'ascasc@sasd', 'asdasda', 'abrir-car', '22525-02-25'),
(31, 'sxasx', '3424', 'dq@fysa', 'cdc', 'abrir-casa', '4424-02-12'),
(32, 'sad', '423423', 'sadd@sda', 'sadasdas', 'abrir-car', '4244-02-24'),
(33, 'sdfsdf', '324324', 'vdfv@ffwf', 'wefw', 'abrir-casa', '3333-03-23'),
(34, 'efew', '32434', 'fdsf@ffsd', 'dsfdf', 'abrir-casa', '0232-03-31'),
(35, 'privada', '246464', 'privada@gmail', 'cerca del panteon', 'abrir-car', '2019-02-01'),
(36, 'wqe', '32', 'f@ef', 'wqddq', 'abrir-casa', '2332-04-05');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE IF NOT EXISTS `usuario` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `apellido` varchar(255) NOT NULL,
  `correo` varchar(255) NOT NULL,
  `pass` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `nombre`, `apellido`, `correo`, `pass`) VALUES
(1, 'carlos', 'lopez', 'carlos@gmail', '123456789'),
(2, 'Jhonathan', 'Contreras', '123@123', '123'),
(3, 'Jhonathan', 'Contreras', '123@123', '123'),
(4, 'asdasdasd', 'dadasd', 'dsdas@ddf', 'sdfsdfdsfsd'),
(5, 'Jhonathan', 'Contreras', 'Contreras@gmail.com', '123456789'),
(6, 'hola', 'wey', 'hola@gmail', '123456789'),
(7, 'carlos', 'ayuda', 'my@haydxd', 'dxdx');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
