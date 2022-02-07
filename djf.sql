-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  lun. 07 fév. 2022 à 14:47
-- Version du serveur :  5.7.26
-- Version de PHP :  7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `djf`
--

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=57 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add c_emploi', 7, 'add_c_emploi'),
(26, 'Can change c_emploi', 7, 'change_c_emploi'),
(27, 'Can delete c_emploi', 7, 'delete_c_emploi'),
(28, 'Can view c_emploi', 7, 'view_c_emploi'),
(29, 'Can add entreprise', 8, 'add_entreprise'),
(30, 'Can change entreprise', 8, 'change_entreprise'),
(31, 'Can delete entreprise', 8, 'delete_entreprise'),
(32, 'Can view entreprise', 8, 'view_entreprise'),
(33, 'Can add travail', 9, 'add_travail'),
(34, 'Can change travail', 9, 'change_travail'),
(35, 'Can delete travail', 9, 'delete_travail'),
(36, 'Can view travail', 9, 'view_travail'),
(37, 'Can add deposer', 10, 'add_deposer'),
(38, 'Can change deposer', 10, 'change_deposer'),
(39, 'Can delete deposer', 10, 'delete_deposer'),
(40, 'Can view deposer', 10, 'view_deposer'),
(41, 'Can add visiteur', 11, 'add_visiteur'),
(42, 'Can change visiteur', 11, 'change_visiteur'),
(43, 'Can delete visiteur', 11, 'delete_visiteur'),
(44, 'Can view visiteur', 11, 'view_visiteur'),
(45, 'Can add notes', 12, 'add_notes'),
(46, 'Can change notes', 12, 'change_notes'),
(47, 'Can delete notes', 12, 'delete_notes'),
(48, 'Can view notes', 12, 'view_notes'),
(49, 'Can add langue maitrise', 13, 'add_languemaitrise'),
(50, 'Can change langue maitrise', 13, 'change_languemaitrise'),
(51, 'Can delete langue maitrise', 13, 'delete_languemaitrise'),
(52, 'Can view langue maitrise', 13, 'view_languemaitrise'),
(53, 'Can add langue', 14, 'add_langue'),
(54, 'Can change langue', 14, 'change_langue'),
(55, 'Can delete langue', 14, 'delete_langue'),
(56, 'Can view langue', 14, 'view_langue');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$9QiQW6tY1fxwV279U26SJm$wqP1iAMUVaq63HRDeTWSUXNYVPdSwQ6ypO2RaFRoomc=', '2022-02-06 14:18:36.764781', 1, 'beirouk', '', '', 'brk@gmail.com', 1, 1, '2022-01-31 16:42:48.316323'),
(2, 'pbkdf2_sha256$260000$YE4bvXwi6ixLjkA2o8MJbR$1u2Ktl7akVfjwIubq9cMZSm4Qf73RxxH0BKNaQoZ8zM=', '2022-02-07 02:39:18.017262', 0, 'chercheur', 'Mohamed', 'Beirouk', 'chercheur@gmail.com', 0, 1, '2022-01-31 20:27:49.465886'),
(3, 'pbkdf2_sha256$260000$LcP6d1bX08zKb0iGyQ18Pd$j6EnMRc5IqYsdPzUSa35+W4u+M4hHIHBuQsftVYjQug=', NULL, 0, 'medos', 'medos', 'ahmedou', 'medos@gmail.com', 0, 1, '2022-01-31 20:32:09.620560'),
(4, 'pbkdf2_sha256$260000$TVUtTgSIbsICnHUzZBMybg$q77Y3P+lGjOwxCvHaMFxMJyd0Q7DelGslWMi2XTTzdA=', NULL, 0, 'ahmed-mzn', 'ahmed', 'mly zeyn', 'ahmed-mzn@gmail.com', 0, 1, '2022-01-31 21:13:11.235519'),
(5, 'pbkdf2_sha256$260000$El3OTptJgCbH8gLzGTipat$wT5uiXDiWpNn+sTUBbWFZmxGEK1O4u+m2Yo7Umd/3SA=', '2022-02-06 14:19:37.673500', 0, 'Maurimatique', 'Med', 'ali', 'Maurimatique@gmail.com', 0, 1, '2022-01-31 21:53:39.194666');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'myappdjf', 'c_emploi'),
(8, 'myappdjf', 'entreprise'),
(9, 'myappdjf', 'travail'),
(10, 'myappdjf', 'deposer'),
(11, 'myappdjf', 'visiteur'),
(12, 'myappdjf', 'notes'),
(13, 'myappdjf', 'languemaitrise'),
(14, 'myappdjf', 'langue');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-01-31 16:37:22.647739'),
(2, 'auth', '0001_initial', '2022-01-31 16:37:23.078209'),
(3, 'admin', '0001_initial', '2022-01-31 16:37:23.194625'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-01-31 16:37:23.197393'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-01-31 16:37:23.215511'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-01-31 16:37:23.290748'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-01-31 16:37:23.329981'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-01-31 16:37:23.365944'),
(9, 'auth', '0004_alter_user_username_opts', '2022-01-31 16:37:23.372451'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-01-31 16:37:23.416089'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-01-31 16:37:23.419697'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-01-31 16:37:23.436192'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-01-31 16:37:23.477081'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-01-31 16:37:23.511839'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-01-31 16:37:23.552038'),
(16, 'auth', '0011_update_proxy_permissions', '2022-01-31 16:37:23.568937'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-01-31 16:37:23.610080'),
(18, 'myappdjf', '0001_initial', '2022-01-31 16:37:23.923513'),
(19, 'myappdjf', '0002_annoncesepingles_languemaitrise_notes_visiteur', '2022-01-31 16:37:24.234506'),
(20, 'myappdjf', '0003_alter_languemaitrise_niveau', '2022-01-31 16:37:24.273885'),
(21, 'myappdjf', '0004_auto_20220112_1741', '2022-01-31 16:37:24.443090'),
(22, 'myappdjf', '0005_auto_20220123_1923', '2022-01-31 16:37:24.467217'),
(23, 'myappdjf', '0006_languemaitrise_langue', '2022-01-31 16:37:24.539331'),
(24, 'sessions', '0001_initial', '2022-01-31 16:37:24.598899'),
(25, 'myappdjf', '0007_remove_langue_utilite', '2022-01-31 20:39:25.850513'),
(26, 'myappdjf', '0008_auto_20220131_2201', '2022-01-31 22:01:54.398030');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `myappdjf_c_emploi`
--

DROP TABLE IF EXISTS `myappdjf_c_emploi`;
CREATE TABLE IF NOT EXISTS `myappdjf_c_emploi` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `telephone` varchar(10) NOT NULL,
  `image` varchar(100) NOT NULL,
  `sexe` varchar(10) NOT NULL,
  `type` varchar(15) NOT NULL,
  `user_id` int(11) NOT NULL,
  `adresse` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `experience` varchar(100) NOT NULL,
  `skills` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myappdjf_c_emploi_user_id_d6f0a82d` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `myappdjf_c_emploi`
--

INSERT INTO `myappdjf_c_emploi` (`id`, `telephone`, `image`, `sexe`, `type`, `user_id`, `adresse`, `description`, `experience`, `skills`) VALUES
(1, '22222222', 'IMG_06341.JPG', 'Male', 'c_emploi', 2, 'Nouakchott Mauritania', 'j\'aime le devellopement', '5', 'travail en grp'),
(2, '33333333', 'IMG_10801.JPG', 'Male', 'c_emploi', 3, 'newyork usa', 'not a man', '5', 'man3rav 5'),
(3, '34343434', 'IMG-20210806-WA0484.jpg', 'Male', 'c_emploi', 4, 'here Canada', 'bla bla bla bla', '4', 'cool');

-- --------------------------------------------------------

--
-- Structure de la table `myappdjf_deposer`
--

DROP TABLE IF EXISTS `myappdjf_deposer`;
CREATE TABLE IF NOT EXISTS `myappdjf_deposer` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `entreprise` varchar(200) NOT NULL,
  `cv` varchar(100) NOT NULL,
  `date_depot` date NOT NULL,
  `c_emploi_id` bigint(20) NOT NULL,
  `travail_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myappdjf_deposer_c_emploi_id_91cee587` (`c_emploi_id`),
  KEY `myappdjf_deposer_travail_id_e437ae57` (`travail_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `myappdjf_entreprise`
--

DROP TABLE IF EXISTS `myappdjf_entreprise`;
CREATE TABLE IF NOT EXISTS `myappdjf_entreprise` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `telephone` varchar(10) NOT NULL,
  `image` varchar(100) NOT NULL,
  `sexe` varchar(10) NOT NULL,
  `type` varchar(15) NOT NULL,
  `status` varchar(20) NOT NULL,
  `nom_entreprise` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myappdjf_entreprise_user_id_f46b4b1d` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `myappdjf_entreprise`
--

INSERT INTO `myappdjf_entreprise` (`id`, `telephone`, `image`, `sexe`, `type`, `status`, `nom_entreprise`, `user_id`) VALUES
(1, '37419845', 'IMG-20210824-WA0042.jpg', 'Male', 'entreprise', 'Accepted', 'Maurimatique', 5);

-- --------------------------------------------------------

--
-- Structure de la table `myappdjf_langue`
--

DROP TABLE IF EXISTS `myappdjf_langue`;
CREATE TABLE IF NOT EXISTS `myappdjf_langue` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `myappdjf_langue`
--

INSERT INTO `myappdjf_langue` (`id`, `nom`, `description`) VALUES
(1, 'python', 'language de programmation mobile, desktop et web'),
(2, 'java', 'language de programmation mobile, desktop et web'),
(3, 'jee', 'language de programmation web'),
(4, 'php', 'language de programmation web'),
(5, 'sql', 'language de programmation bd'),
(6, 'flutter', 'framework devellopement mobile'),
(7, 'ionic', 'framework devellopement mobile'),
(8, 'dot net', 'framework devellopement mobile, desktop et web'),
(9, 'Langage C', 'langage de devellopement desktop'),
(10, 'Langage C++', 'langage de devellopement desktop');

-- --------------------------------------------------------

--
-- Structure de la table `myappdjf_languemaitrise`
--

DROP TABLE IF EXISTS `myappdjf_languemaitrise`;
CREATE TABLE IF NOT EXISTS `myappdjf_languemaitrise` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `c_emploi_id` bigint(20) NOT NULL,
  `langue_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myappdjf_languemaitrise_c_emploi_id_db1b39e4` (`c_emploi_id`),
  KEY `myappdjf_languemaitrise_langue_id_db0f7cf0` (`langue_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `myappdjf_languemaitrise`
--

INSERT INTO `myappdjf_languemaitrise` (`id`, `c_emploi_id`, `langue_id`) VALUES
(1, 2, 1),
(2, 2, 2),
(3, 2, 7),
(4, 2, 5);

-- --------------------------------------------------------

--
-- Structure de la table `myappdjf_notes`
--

DROP TABLE IF EXISTS `myappdjf_notes`;
CREATE TABLE IF NOT EXISTS `myappdjf_notes` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `note` int(11) NOT NULL,
  `c_emploi_id` bigint(20) NOT NULL,
  `visiteur_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myappdjf_notes_c_emploi_id_32cb2d30` (`c_emploi_id`),
  KEY `myappdjf_notes_visiteur_id_3822552d` (`visiteur_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `myappdjf_travail`
--

DROP TABLE IF EXISTS `myappdjf_travail`;
CREATE TABLE IF NOT EXISTS `myappdjf_travail` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date_debut` date NOT NULL,
  `date_fin` date NOT NULL,
  `titre` varchar(200) NOT NULL,
  `salaire` double NOT NULL,
  `image` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `experience` varchar(100) NOT NULL,
  `adresse` varchar(100) NOT NULL,
  `skills` varchar(200) NOT NULL,
  `date_creation` date NOT NULL,
  `entreprise_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myappdjf_travail_entreprise_id_c4b18941` (`entreprise_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `myappdjf_visiteur`
--

DROP TABLE IF EXISTS `myappdjf_visiteur`;
CREATE TABLE IF NOT EXISTS `myappdjf_visiteur` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myappdjf_visiteur_user_id_6d5aff77` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
