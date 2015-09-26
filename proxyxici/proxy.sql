/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50617
Source Host           : localhost:3306
Source Database       : spider

Target Server Type    : MYSQL
Target Server Version : 50617
File Encoding         : 65001

Date: 2015-06-22 10:38:57
*/

SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for `proxy`
-- ----------------------------
DROP TABLE IF EXISTS `proxy`;
CREATE TABLE `proxy` (
  `id`                BIGINT(20) UNSIGNED     NOT NULL AUTO_INCREMENT,
  `proxy_ip`          VARCHAR(200)
                      COLLATE utf8_unicode_ci NOT NULL,
  `proxy_port`        VARCHAR(50)
                      COLLATE utf8_unicode_ci NOT NULL,
  `proxy_location`    VARCHAR(100)
                      COLLATE utf8_unicode_ci          DEFAULT NULL,
  `proxy_type`        VARCHAR(50)
                      COLLATE utf8_unicode_ci NOT NULL,
  `proxy_security`    VARCHAR(50)
                      COLLATE utf8_unicode_ci NOT NULL,
  `last_vertify_time` DATETIME                         DEFAULT NULL,
  `is_valid`          SMALLINT(6)                      DEFAULT '0',
  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  AUTO_INCREMENT = 1
  DEFAULT CHARSET = utf8
  COLLATE = utf8_unicode_ci;