-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Фев 23 2023 г., 17:11
-- Версия сервера: 8.0.31
-- Версия PHP: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `bos`
--

-- --------------------------------------------------------

--
-- Структура таблицы `account`
--

DROP TABLE IF EXISTS `account`;
CREATE TABLE IF NOT EXISTS `account` (
  `Id` int NOT NULL,
  `UserName` varchar(20) NOT NULL,
  `Hash` varchar(256) NOT NULL,
  `Salt` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`UserName`),
  KEY `Id` (`Id`),
  KEY `Hash` (`Hash`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `account`
--

INSERT INTO `account` (`Id`, `UserName`, `Hash`, `Salt`) VALUES
(0, 'admin', 'admin', 'admin'),
(1, 'katana', '311c814c874421272b7435e7199fae5c055245bb81632d9b33975b24dc2d6ec3', '1111101101000100011001000101001100100111100011010100110110011011001011111110000001000100011100001011000001010101110011011000010100011011011010111100110100101010110101001100001000101100011010100110110110111000110101100011011111001101101101001110100000100100');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;