SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Ayoub`
--
CREATE DATABASE IF NOT EXISTS `Ayoub` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `Ayoub`;

-- --------------------------------------------------------

--
-- Table structure for table `Absence`
--

CREATE TABLE `Absence` (
  `Id` int NOT NULL,
  `mat_emp` int NOT NULL,
  `mois` int NOT NULL,
  `Annee` int NOT NULL,
  `Total` decimal(5,2) NOT NULL DEFAULT '0.00'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Absence`
--

INSERT INTO `Absence` (`Id`, `mat_emp`, `mois`, `Annee`, `Total`) VALUES
(48, 4, 6, 2021, '0.00'),
(50, 1, 6, 2021, '0.00'),
(51, 2, 6, 2021, '0.00'),
(52, 3, 6, 2021, '8.00'),
(55, 5, 6, 2021, '0.00'),
(56, 6, 6, 2021, '0.00'),
(57, 7, 6, 2021, '8.00'),
(58, 8, 6, 2021, '0.00'),
(59, 9, 6, 2021, '0.00'),
(60, 10, 6, 2021, '0.00'),
(63, 1, 7, 2021, '0.00'),
(64, 2, 7, 2021, '0.00'),
(65, 3, 7, 2021, '0.00'),
(66, 4, 7, 2021, '0.00'),
(67, 5, 7, 2021, '0.00'),
(68, 6, 7, 2021, '9.00'),
(69, 7, 7, 2021, '0.00'),
(70, 8, 7, 2021, '0.00'),
(71, 9, 7, 2021, '0.00'),
(72, 10, 7, 2021, '0.00'),
(73, 1, 6, 2021, '0.00'),
(74, 1, 6, 2021, '0.00'),
(75, 11, 6, 2021, '0.00'),
(76, 1, 7, 2021, '0.00'),
(77, 1, 7, 2021, '0.00'),
(78, 1, 7, 2021, '0.00'),
(79, 1, 6, 2021, '0.00'),
(80, 1, 7, 2021, '0.00');

-- --------------------------------------------------------

--
-- Table structure for table `Administrateur`
--

CREATE TABLE `Administrateur` (
  `Id` int NOT NULL,
  `Num_Mat` int DEFAULT NULL,
  `Username` varchar(25) DEFAULT NULL,
  `MotDePasse` varchar(25) DEFAULT NULL,
  `Email` varchar(50) NOT NULL,
  `Motdepasse_Email` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Administrateur`
--

INSERT INTO `Administrateur` (`Id`, `Num_Mat`, `Username`, `MotDePasse`, `Email`, `Motdepasse_Email`) VALUES
(1, 2, 'Directeur', '1234', 'ssaigayub@gmail.com', 'Ayoub2000'),
(2, 3, 'RH', '1234', 'ayoubelbahti6@gmail.com', 'Ayoub2000');

-- --------------------------------------------------------

--
-- Table structure for table `Conge`
--

CREATE TABLE `Conge` (
  `Id` int NOT NULL,
  `Mat_Emp` int DEFAULT NULL,
  `Type_de_Conge` varchar(25) DEFAULT NULL,
  `type_grp` int DEFAULT NULL,
  `DateDebut` date DEFAULT NULL,
  `DateFin` date DEFAULT NULL,
  `NbrJours` decimal(3,1) DEFAULT NULL,
  `Validation` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT 'C',
  `tempDeTravail` varchar(25) DEFAULT NULL,
  `secondTemp` varchar(25) NOT NULL,
  `nbr_Samedi` int NOT NULL DEFAULT '0',
  `nbr_Samedi_Consommer` int NOT NULL DEFAULT '0',
  `Messages` int DEFAULT '0'
) ;

--
-- Dumping data for table `Conge`
--

INSERT INTO `Conge` (`Id`, `Mat_Emp`, `Type_de_Conge`, `type_grp`, `DateDebut`, `DateFin`, `NbrJours`, `Validation`, `tempDeTravail`, `secondTemp`, `nbr_Samedi`, `nbr_Samedi_Consommer`, `Messages`) VALUES
(365, 5, 'CP', NULL, '2021-06-09', '2021-06-13', '3.0', 'C', '06h -> 14h', '06h -> 14h', 0, 1, 0),
(368, 7, 'CSS', NULL, '2021-07-02', '2021-07-05', '2.0', 'V', '06h -> 14h', 'Aucun', 0, 0, 0),
(372, 5, 'CP', NULL, '2021-06-30', '2021-07-05', '4.0', 'V', '06h -> 14h', 'Normal', 0, 1, 0),
(375, 5, 'CSS', NULL, '2021-07-08', '2021-07-12', '3.0', 'H', '06h -> 14h', '06h -> 14h', 0, 0, 0),
(376, 7, 'CE', NULL, '2021-07-08', '2021-07-12', '2.0', 'V', '06h -> 14h', '06h -> 14h', 0, 1, 1),
(377, 7, 'CE', NULL, '2021-07-08', '2021-07-12', '3.0', 'C', '06h -> 14h', 'Normal', 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `CongeCSS`
--

CREATE TABLE `CongeCSS` (
  `Id` int NOT NULL,
  `mat_emp` int DEFAULT NULL,
  `nbr_jours` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `CongeCSS`
--

INSERT INTO `CongeCSS` (`Id`, `mat_emp`, `nbr_jours`) VALUES
(1, 1, NULL),
(2, 2, NULL),
(3, 3, NULL),
(4, 4, '0.00'),
(5, 5, '0.00'),
(6, 6, '0.00'),
(7, 7, '2.00'),
(8, 8, '0.00'),
(9, 9, '0.00'),
(10, 10, '0.00'),
(11, 11, '0.00');

-- --------------------------------------------------------

--
-- Table structure for table `CongeEvenement`
--

CREATE TABLE `CongeEvenement` (
  `Id` int NOT NULL,
  `id_emp` int DEFAULT NULL,
  `NbrJours` decimal(5,2) DEFAULT '4.00'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `CongeEvenement`
--

INSERT INTO `CongeEvenement` (`Id`, `id_emp`, `NbrJours`) VALUES
(1, 1, '4.00'),
(2, 2, '4.00'),
(3, 3, '4.00'),
(10, 4, '4.00'),
(14, 5, '1.00'),
(15, 6, '4.00'),
(16, 7, '2.00'),
(17, 8, '4.00'),
(18, 9, '4.00'),
(19, 10, '4.00'),
(20, 11, '4.00');

-- --------------------------------------------------------

--
-- Table structure for table `CongePaye`
--

CREATE TABLE `CongePaye` (
  `Id` int NOT NULL,
  `id_emp` int DEFAULT NULL,
  `nbr_jours` decimal(5,2) DEFAULT '18.00'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `CongePaye`
--

INSERT INTO `CongePaye` (`Id`, `id_emp`, `nbr_jours`) VALUES
(1, 1, '18.00'),
(2, 2, '18.00'),
(3, 3, '18.00'),
(9, 4, '18.00'),
(13, 5, '14.00'),
(14, 6, '18.00'),
(15, 7, '18.00'),
(16, 8, '18.00'),
(17, 9, '18.00'),
(18, 10, '18.00'),
(19, 11, '18.00');

-- --------------------------------------------------------

--
-- Table structure for table `CongeRecupere`
--

CREATE TABLE `CongeRecupere` (
  `Id` int NOT NULL,
  `id_emp` int DEFAULT NULL,
  `heures_récupération` decimal(5,2) DEFAULT '0.00'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `CongeRecupere`
--

INSERT INTO `CongeRecupere` (`Id`, `id_emp`, `heures_récupération`) VALUES
(13, 4, '0.00'),
(15, 1, '5.00'),
(16, 2, '0.00'),
(17, 3, '5.00'),
(20, 5, '0.00'),
(21, 6, '0.00'),
(22, 7, '0.00'),
(23, 8, '0.00'),
(24, 9, '0.00'),
(25, 10, '0.00'),
(26, 11, '0.00');

-- --------------------------------------------------------

--
-- Table structure for table `Employees`
--

CREATE TABLE `Employees` (
  `Mat_Emp` int NOT NULL,
  `Cin` varchar(12) DEFAULT NULL,
  `Nom` varchar(25) DEFAULT NULL,
  `Prenom` varchar(25) DEFAULT NULL,
  `DateDeNaissance` date DEFAULT NULL,
  `Age` int DEFAULT NULL,
  `SituationFamiliale` varchar(12) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `NbrEnfants` int DEFAULT NULL,
  `NumTelephone` varchar(25) DEFAULT NULL,
  `Adresse` varchar(100) DEFAULT NULL,
  `LieuDeLicence` varchar(100) DEFAULT NULL,
  `NiveauEtude` varchar(10) DEFAULT NULL,
  `Diplome` varchar(25) DEFAULT NULL,
  `Formation` varchar(25) DEFAULT NULL,
  `Fonction` varchar(25) DEFAULT NULL,
  `Mat_Responsable` int DEFAULT NULL,
  `TypeContrat` varchar(25) DEFAULT NULL,
  `NumCnss` varchar(25) DEFAULT NULL,
  `Service` varchar(25) DEFAULT NULL,
  `SalaireNet` decimal(7,2) DEFAULT NULL,
  `Taux_Horaire` decimal(6,2) NOT NULL,
  `DateEntree` date DEFAULT NULL,
  `nbr_Samedi` int NOT NULL DEFAULT '3',
  `Anciennete` decimal(12,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Employees`
--

INSERT INTO `Employees` (`Mat_Emp`, `Cin`, `Nom`, `Prenom`, `DateDeNaissance`, `Age`, `SituationFamiliale`, `NbrEnfants`, `NumTelephone`, `Adresse`, `LieuDeLicence`, `NiveauEtude`, `Diplome`, `Formation`, `Fonction`, `Mat_Responsable`, `TypeContrat`, `NumCnss`, `Service`, `SalaireNet`, `Taux_Horaire`, `DateEntree`, `nbr_Samedi`, `Anciennete`) VALUES
(1, 'N443311', 'EL BAHTI', 'Ayoub', '2000-11-08', 20, 'Célibataire', 0, '+212617079641', 'Casablanca, Maroc', 'Essaouira', 'Bac+2', 'DUT', 'ESTC', '', 3, 'stagiaire', '1244564', 'Informatique', '5700.00', '0.00', '2021-05-03', 3, '1.00'),
(2, 'N4123', 'Bensam', 'jalal', '2000-12-23', 21, 'Célibataire', 0, '+21265974512', 'casablanca,neouaser', 'Casablanca', 'Bac+5', 'Ingénieure', 'ssss', 'Admin', NULL, 'XXX', 'XXXXXXXXXXXX', 'XXXXXXXXXXX', '17852.00', '0.00', '2010-11-03', 3, '11.00'),
(3, 'HB4521', 'BOUGASSA', 'Soukaina', '1999-09-09', 22, 'Marié', 0, '+212674669223', 'Casablanca', 'Casablanca', 'Bac+5', 'Diplome', 'Frmt', 'DH', 2, 'nnnn', '12546868', 'dh', '4000.00', '0.00', '2020-01-14', 3, '2.00'),
(4, 'Lm4589', 'EL AMRANI', 'Assia', '1998-07-11', 22, 'Célibataire', 0, '+212793939471', 'Casablanca, Maroc', 'LAARAICH', 'Bac+3', 'LPGLAASRI', 'ESTC', 'Responsable', 3, 'XXXX', '12345', 'Management', '5700.00', '15.12', '2021-05-03', 3, NULL),
(5, 'B4526', 'BASIR', 'Mihammed', '1999-11-08', 21, 'Célibataire', 0, '+2154545', 'Casablanca, Maroc', 'Casablanca', 'Bac+2', 'DUT', 'ESTC', '', 1, 'stagiaire', '52632', 'Informatique', '5700.00', '0.00', '2021-05-03', 3, NULL),
(6, 'V4526', 'SSADAN', 'toto', '2000-11-08', 20, 'Célibataire', 0, '', 'Casablanca, Maroc', 'Essaouira', 'Bac+2', 'DUT', 'ESTC', 'XXXXXXX', 3, 'stagiaire', 'c451256', 'Informatique', '5700.00', '0.00', '2021-05-03', 3, NULL),
(7, 'N4526655', 'saiid', 'FOFO', '2000-11-08', 20, 'Célibataire', 0, '5458', 'Casablanca, Maroc', 'Essaouira', 'Bac+2', 'DUT', 'ESTC', 'XXXXXXX', 4, 'stagiaire', '135689', 'Informatique', '5700.00', '0.00', '2021-05-03', 3, NULL),
(8, '4455', 'saadia', 'salaho', '2000-11-08', 20, 'Célibataire', 0, '+212617079641', 'Casablanca, Maroc', 'casabnava', 'Bac+2', 'DUT', 'ESTC', '', 3, 'stagiaire', '256', 'Informatique', '5700.00', '14.25', '2021-05-03', 3, NULL),
(9, 'SSSSS', 'SSSS', 'SSSS', '2000-11-08', 20, 'Célibataire', 0, '+212617079641', 'Casablanca, Maroc', 'Essaouira', 'Bac+2', 'DUT', 'ESTC', 'SSS', 3, 'stagiaire', '12S5', 'Informatique', '5700.00', '0.00', '2021-05-03', 3, '61.00'),
(10, '52211', 'DDD', 'toto', '2000-11-08', 20, 'Célibataire', 0, '+2126559641', 'Casablanca, Maroc', 'Essaouira', 'Bac+2', 'DUT', 'ESTC', 'XXXXXXX', 3, 'stagiaire', '45DD', 'Informatique', '5700.00', '0.00', '2021-07-02', 3, '1.00'),
(11, 'N4526', 'aayar', 'smail', '2000-11-08', 20, 'Marié', 1, '+212617079641', 'Casablanca, Maroc', 'Essaouira', 'Bac+2', 'DUT', 'ESTC', '', 3, 'stagiaire', '4578', 'Informatique', '4000.00', '15.00', '2021-05-03', 3, '65.00');

-- --------------------------------------------------------

--
-- Table structure for table `Groupe`
--

CREATE TABLE `Groupe` (
  `Code` int NOT NULL,
  `Nom` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `HeureNormales`
--

CREATE TABLE `HeureNormales` (
  `Id` int NOT NULL,
  `mat_emp` int DEFAULT NULL,
  `mois` int DEFAULT NULL,
  `Annee` int DEFAULT NULL,
  `Total` decimal(5,2) DEFAULT '0.00'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `HeureNormales`
--

INSERT INTO `HeureNormales` (`Id`, `mat_emp`, `mois`, `Annee`, `Total`) VALUES
(57, 4, 6, 2021, '25.10'),
(59, 1, 6, 2021, '76.90'),
(60, 2, 6, 2021, '0.00'),
(61, 3, 6, 2021, '8.30'),
(64, 5, 6, 2021, '26.00'),
(65, 6, 6, 2021, '0.00'),
(66, 7, 6, 2021, '0.00'),
(67, 8, 6, 2021, '0.00'),
(68, 9, 6, 2021, '0.00'),
(69, 10, 6, 2021, '0.00'),
(70, 1, 7, 2021, '40.60'),
(71, 2, 7, 2021, '0.00'),
(72, 3, 7, 2021, '15.60'),
(73, 4, 7, 2021, '0.00'),
(74, 5, 7, 2021, '0.00'),
(75, 6, 7, 2021, '0.00'),
(76, 7, 7, 2021, '0.00'),
(77, 8, 7, 2021, '0.00'),
(78, 9, 7, 2021, '0.00'),
(79, 10, 7, 2021, '0.00'),
(82, 11, 6, 2021, '0.00');

-- --------------------------------------------------------

--
-- Table structure for table `HeureSupplémentaires`
--

CREATE TABLE `HeureSupplémentaires` (
  `id` int NOT NULL,
  `mat_emp` int DEFAULT NULL,
  `mois` int NOT NULL,
  `Annee` int NOT NULL,
  `Total` decimal(4,2) NOT NULL DEFAULT '0.00',
  `Vingt_cinq` decimal(4,2) DEFAULT '0.00',
  `cinquante` decimal(4,2) DEFAULT '0.00',
  `cent` decimal(4,2) DEFAULT '0.00'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

--
-- Dumping data for table `HeureSupplémentaires`
--

INSERT INTO `HeureSupplémentaires` (`id`, `mat_emp`, `mois`, `Annee`, `Total`, `Vingt_cinq`, `cinquante`, `cent`) VALUES
(56, 4, 6, 2021, '4.00', '0.00', '1.00', '0.00'),
(58, 1, 6, 2021, '3.00', '1.00', '0.00', '0.00'),
(59, 2, 6, 2021, '0.00', '0.00', '0.00', '0.00'),
(62, 3, 6, 2021, '2.00', '2.00', '0.00', '0.00'),
(65, 5, 6, 2021, '0.00', '0.00', '0.00', '0.00'),
(66, 6, 6, 2021, '0.00', '0.00', '0.00', '0.00'),
(67, 7, 6, 2021, '0.00', '0.00', '0.00', '0.00'),
(68, 8, 6, 2021, '0.00', '0.00', '0.00', '0.00'),
(69, 9, 6, 2021, '0.00', '0.00', '0.00', '0.00'),
(70, 10, 6, 2021, '0.00', '0.00', '0.00', '0.00'),
(71, 1, 7, 2021, '6.00', '1.00', '0.00', '0.00'),
(72, 2, 7, 2021, '0.00', '0.00', '0.00', '0.00'),
(73, 3, 7, 2021, '3.00', '2.00', '1.00', '0.00'),
(74, 4, 7, 2021, '0.00', '0.00', '0.00', '0.00'),
(75, 5, 7, 2021, '0.00', '0.00', '0.00', '0.00'),
(76, 6, 7, 2021, '0.00', '0.00', '0.00', '0.00'),
(77, 7, 7, 2021, '0.00', '0.00', '0.00', '0.00'),
(78, 8, 7, 2021, '0.00', '0.00', '0.00', '0.00'),
(79, 9, 7, 2021, '0.00', '0.00', '0.00', '0.00'),
(80, 10, 7, 2021, '0.00', '0.00', '0.00', '0.00'),
(81, 11, 6, 2021, '0.00', '0.00', '0.00', '0.00');

-- --------------------------------------------------------

--
-- Table structure for table `Message`
--

CREATE TABLE `Message` (
  `Id` int NOT NULL,
  `Id_Conge` int DEFAULT NULL,
  `Contenu` varchar(1500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Message`
--

INSERT INTO `Message` (`Id`, `Id_Conge`, `Contenu`) VALUES
(35, 376, 'bonjour xxxxxxxx');

-- --------------------------------------------------------

--
-- Table structure for table `Mois`
--

CREATE TABLE `Mois` (
  `Code_Mois` int NOT NULL,
  `Nom` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Mois`
--

INSERT INTO `Mois` (`Code_Mois`, `Nom`) VALUES
(1, 'Janvier'),
(2, 'Février'),
(3, 'Mars'),
(4, 'Avril'),
(5, 'Mai'),
(6, 'Juin'),
(7, 'Juillet'),
(8, 'Août'),
(9, 'Septembre'),
(10, 'Octobre'),
(11, 'Novembre'),
(12, 'Décembre');

-- --------------------------------------------------------

--
-- Table structure for table `Pointage`
--

CREATE TABLE `Pointage` (
  `Id` int NOT NULL,
  `id_emp` int DEFAULT NULL,
  `Temps_de_travail` varchar(25) DEFAULT NULL,
  `Date_Jour` date NOT NULL,
  `Heure_Entrer` varchar(7) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `Heure_mise_en_consideration` decimal(5,2) NOT NULL DEFAULT '0.00',
  `Heure_Sortir` varchar(7) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `NbrHeures` decimal(4,2) NOT NULL DEFAULT '0.00',
  `HeuresSupp` decimal(3,2) NOT NULL DEFAULT '0.00',
  `vintCinq` decimal(3,2) NOT NULL DEFAULT '0.00',
  `cinquante` decimal(3,2) NOT NULL DEFAULT '0.00',
  `cent` decimal(3,2) NOT NULL DEFAULT '0.00',
  `Temps_considéré` decimal(5,2) NOT NULL DEFAULT '0.00',
  `Absence` int NOT NULL DEFAULT '0',
  `estCongé` int NOT NULL DEFAULT '0',
  `heures_récupération` decimal(5,2) NOT NULL DEFAULT '0.00',
  `Retard` decimal(5,2) NOT NULL DEFAULT '0.00'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Pointage`
--

INSERT INTO `Pointage` (`Id`, `id_emp`, `Temps_de_travail`, `Date_Jour`, `Heure_Entrer`, `Heure_mise_en_consideration`, `Heure_Sortir`, `NbrHeures`, `HeuresSupp`, `vintCinq`, `cinquante`, `cent`, `Temps_considéré`, `Absence`, `estCongé`, `heures_récupération`, `Retard`) VALUES
(94, 1, NULL, '2021-07-25', NULL, '0.00', NULL, '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', 0, 0, '0.00', '0.00'),
(95, 2, NULL, '2021-07-25', NULL, '0.00', NULL, '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', 0, 0, '0.00', '0.00'),
(96, 3, NULL, '2021-07-25', NULL, '0.00', NULL, '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', 0, 0, '0.00', '0.00'),
(97, 4, NULL, '2021-07-25', NULL, '0.00', NULL, '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', 0, 0, '0.00', '0.00'),
(98, 5, NULL, '2021-07-25', NULL, '0.00', NULL, '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', 0, 0, '0.00', '0.00'),
(99, 6, NULL, '2021-07-25', NULL, '0.00', NULL, '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', 0, 0, '0.00', '0.00'),
(100, 7, NULL, '2021-07-25', NULL, '0.00', NULL, '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', 0, 0, '0.00', '0.00'),
(101, 8, NULL, '2021-07-25', NULL, '0.00', NULL, '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', 0, 0, '0.00', '0.00'),
(102, 9, NULL, '2021-07-25', NULL, '0.00', NULL, '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', 0, 0, '0.00', '0.00'),
(103, 10, NULL, '2021-07-25', NULL, '0.00', NULL, '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', 0, 0, '0.00', '0.00'),
(104, 11, NULL, '2021-07-25', NULL, '0.00', NULL, '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', 0, 0, '0.00', '0.00'),
(105, 1, 'Normal', '2021-07-26', '08:30', '8.30', '18:00', '9.00', '1.00', '1.00', '0.00', '0.00', '0.00', 0, 0, '3.00', '0.30');

-- --------------------------------------------------------

--
-- Table structure for table `Responsable`
--

CREATE TABLE `Responsable` (
  `Id` int NOT NULL,
  `Num_Mat` int DEFAULT NULL,
  `Username` varchar(25) DEFAULT NULL,
  `MotDePasse` varchar(25) DEFAULT NULL,
  `Email` varchar(50) NOT NULL,
  `Motdepasse_Email` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Responsable`
--

INSERT INTO `Responsable` (`Id`, `Num_Mat`, `Username`, `MotDePasse`, `Email`, `Motdepasse_Email`) VALUES
(1, 1, 'responsable1', '1234', 'ssaigayub@gmail.com', 'Ayoub2000'),
(2, 4, 'responsable2', '1234', 'ssaigayub@gmail.com', 'Ayoub2000');

-- --------------------------------------------------------

--
-- Table structure for table `TypeConge`
--

CREATE TABLE `TypeConge` (
  `Code` varchar(25) NOT NULL,
  `Nom` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `TypeConge`
--

INSERT INTO `TypeConge` (`Code`, `Nom`) VALUES
('CE', 'Congé spécial'),
('CP', 'Congé payé'),
('CR', 'Congé de récupération'),
('CSS', 'Congé sans solde');

-- --------------------------------------------------------

--
-- Table structure for table `Validation`
--

CREATE TABLE `Validation` (
  `Code` char(1) NOT NULL,
  `Nom` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Validation`
--

INSERT INTO `Validation` (`Code`, `Nom`) VALUES
('C', 'En cours'),
('H', 'Accepter par RH'),
('M', 'réactifier'),
('R', 'Refusé'),
('S', 'Supprimer'),
('V', 'Validé');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Absence`
--
ALTER TABLE `Absence`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `fk_absence_employees` (`mat_emp`);

--
-- Indexes for table `Administrateur`
--
ALTER TABLE `Administrateur`
  ADD PRIMARY KEY (`Id`),
  ADD UNIQUE KEY `Username` (`Username`,`MotDePasse`),
  ADD KEY `Num_Mat` (`Num_Mat`);

--
-- Indexes for table `Conge`
--
ALTER TABLE `Conge`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Mat_Emp` (`Mat_Emp`),
  ADD KEY `Validation` (`Validation`),
  ADD KEY `Type_de_Conge` (`Type_de_Conge`),
  ADD KEY `type_grp` (`type_grp`),
  ADD KEY `Messages` (`Messages`);

--
-- Indexes for table `CongeCSS`
--
ALTER TABLE `CongeCSS`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `mat_emp` (`mat_emp`);

--
-- Indexes for table `CongeEvenement`
--
ALTER TABLE `CongeEvenement`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `id_emp` (`id_emp`);

--
-- Indexes for table `CongePaye`
--
ALTER TABLE `CongePaye`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `id_emp` (`id_emp`);

--
-- Indexes for table `CongeRecupere`
--
ALTER TABLE `CongeRecupere`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `num_emp` (`id_emp`);

--
-- Indexes for table `Employees`
--
ALTER TABLE `Employees`
  ADD PRIMARY KEY (`Mat_Emp`),
  ADD UNIQUE KEY `Cin` (`Cin`),
  ADD KEY `fK_Responsable` (`Mat_Responsable`);

--
-- Indexes for table `Groupe`
--
ALTER TABLE `Groupe`
  ADD PRIMARY KEY (`Code`);

--
-- Indexes for table `HeureNormales`
--
ALTER TABLE `HeureNormales`
  ADD PRIMARY KEY (`Id`),
  ADD UNIQUE KEY `check_heures` (`mat_emp`,`mois`,`Annee`),
  ADD KEY `mois` (`mois`);

--
-- Indexes for table `HeureSupplémentaires`
--
ALTER TABLE `HeureSupplémentaires`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `check_heures` (`mat_emp`,`mois`,`Annee`),
  ADD KEY `check_mois` (`mois`);

--
-- Indexes for table `Message`
--
ALTER TABLE `Message`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Id_Conge` (`Id_Conge`);

--
-- Indexes for table `Mois`
--
ALTER TABLE `Mois`
  ADD PRIMARY KEY (`Code_Mois`);

--
-- Indexes for table `Pointage`
--
ALTER TABLE `Pointage`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `id_emp` (`id_emp`);

--
-- Indexes for table `Responsable`
--
ALTER TABLE `Responsable`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Num_Mat` (`Num_Mat`);

--
-- Indexes for table `TypeConge`
--
ALTER TABLE `TypeConge`
  ADD PRIMARY KEY (`Code`);

--
-- Indexes for table `Validation`
--
ALTER TABLE `Validation`
  ADD PRIMARY KEY (`Code`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Absence`
--
ALTER TABLE `Absence`
  MODIFY `Id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;

--
-- AUTO_INCREMENT for table `Conge`
--
ALTER TABLE `Conge`
  MODIFY `Id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `CongeEvenement`
--
ALTER TABLE `CongeEvenement`
  MODIFY `Id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `CongePaye`
--
ALTER TABLE `CongePaye`
  MODIFY `Id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `CongeRecupere`
--
ALTER TABLE `CongeRecupere`
  MODIFY `Id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `HeureNormales`
--
ALTER TABLE `HeureNormales`
  MODIFY `Id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=88;

--
-- AUTO_INCREMENT for table `HeureSupplémentaires`
--
ALTER TABLE `HeureSupplémentaires`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=82;

--
-- AUTO_INCREMENT for table `Message`
--
ALTER TABLE `Message`
  MODIFY `Id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `Pointage`
--
ALTER TABLE `Pointage`
  MODIFY `Id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=106;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Absence`
--
ALTER TABLE `Absence`
  ADD CONSTRAINT `fk_absence_employees` FOREIGN KEY (`mat_emp`) REFERENCES `Employees` (`Mat_Emp`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Constraints for table `Administrateur`
--
ALTER TABLE `Administrateur`
  ADD CONSTRAINT `Administrateur_ibfk_1` FOREIGN KEY (`Num_Mat`) REFERENCES `Employees` (`Mat_Emp`);

--
-- Constraints for table `Conge`
--
ALTER TABLE `Conge`
  ADD CONSTRAINT `Conge_ibfk_1` FOREIGN KEY (`Mat_Emp`) REFERENCES `Employees` (`Mat_Emp`),
  ADD CONSTRAINT `Conge_ibfk_2` FOREIGN KEY (`Type_de_Conge`) REFERENCES `TypeConge` (`Code`),
  ADD CONSTRAINT `Conge_ibfk_3` FOREIGN KEY (`Validation`) REFERENCES `Validation` (`Code`),
  ADD CONSTRAINT `fk_Group` FOREIGN KEY (`type_grp`) REFERENCES `Groupe` (`Code`);

--
-- Constraints for table `CongeCSS`
--
ALTER TABLE `CongeCSS`
  ADD CONSTRAINT `CongeCSS_ibfk_1` FOREIGN KEY (`mat_emp`) REFERENCES `Employees` (`Mat_Emp`);

--
-- Constraints for table `CongeEvenement`
--
ALTER TABLE `CongeEvenement`
  ADD CONSTRAINT `CongeEvenement_ibfk_1` FOREIGN KEY (`id_emp`) REFERENCES `Employees` (`Mat_Emp`);

--
-- Constraints for table `CongePaye`
--
ALTER TABLE `CongePaye`
  ADD CONSTRAINT `CongePaye_ibfk_1` FOREIGN KEY (`id_emp`) REFERENCES `Employees` (`Mat_Emp`);

--
-- Constraints for table `CongeRecupere`
--
ALTER TABLE `CongeRecupere`
  ADD CONSTRAINT `CongeRecupere_ibfk_1` FOREIGN KEY (`id_emp`) REFERENCES `Employees` (`Mat_Emp`);

--
-- Constraints for table `Employees`
--
ALTER TABLE `Employees`
  ADD CONSTRAINT `fK_Responsable` FOREIGN KEY (`Mat_Responsable`) REFERENCES `Employees` (`Mat_Emp`);

--
-- Constraints for table `HeureNormales`
--
ALTER TABLE `HeureNormales`
  ADD CONSTRAINT `HeureNormales_ibfk_1` FOREIGN KEY (`mat_emp`) REFERENCES `Employees` (`Mat_Emp`),
  ADD CONSTRAINT `HeureNormales_ibfk_2` FOREIGN KEY (`mois`) REFERENCES `Mois` (`Code_Mois`);

--
-- Constraints for table `HeureSupplémentaires`
--
ALTER TABLE `HeureSupplémentaires`
  ADD CONSTRAINT `check_mois` FOREIGN KEY (`mois`) REFERENCES `Mois` (`Code_Mois`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `HeureSupplémentaires_ibfk_2` FOREIGN KEY (`mat_emp`) REFERENCES `Employees` (`Mat_Emp`);

--
-- Constraints for table `Message`
--
ALTER TABLE `Message`
  ADD CONSTRAINT `Message_ibfk_1` FOREIGN KEY (`Id_Conge`) REFERENCES `Conge` (`Id`);

--
-- Constraints for table `Pointage`
--
ALTER TABLE `Pointage`
  ADD CONSTRAINT `Pointage_ibfk_1` FOREIGN KEY (`id_emp`) REFERENCES `Employees` (`Mat_Emp`);

--
-- Constraints for table `Responsable`
--
ALTER TABLE `Responsable`
  ADD CONSTRAINT `Responsable_ibfk_1` FOREIGN KEY (`Num_Mat`) REFERENCES `Employees` (`Mat_Emp`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
