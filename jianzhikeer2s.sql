/*
 Navicat Premium Data Transfer

 Source Server         : mysql80
 Source Server Type    : MySQL
 Source Server Version : 80014
 Source Host           : localhost:3306
 Source Schema         : jianzhikeer2

 Target Server Type    : MySQL
 Target Server Version : 80014
 File Encoding         : 65001

 Date: 31/03/2019 21:25:24
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for jzk_advertising
-- ----------------------------
DROP TABLE IF EXISTS `jzk_advertising`;
CREATE TABLE `jzk_advertising`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '广告标题',
  `content` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '广告内容',
  `link` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '广告链接',
  `time` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '发帖时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '兼职客儿的广告数据库' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of jzk_advertising
-- ----------------------------
INSERT INTO `jzk_advertising` VALUES (1, 'test', 'testtest', 'test', '2019-01-02 15:57:04');
INSERT INTO `jzk_advertising` VALUES (2, '测试广告', '展示在手机网页的广告', 'test', '2019-01-02 20:34:29');
INSERT INTO `jzk_advertising` VALUES (3, '测试转换', '测试转换测试转换', 'test', '2019-01-02 20:34:33');
INSERT INTO `jzk_advertising` VALUES (4, '反倒是', '反倒是', '反倒是', '2019-01-02 15:40:18');

-- ----------------------------
-- Table structure for jzk_collects
-- ----------------------------
DROP TABLE IF EXISTS `jzk_collects`;
CREATE TABLE `jzk_collects`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NULL DEFAULT NULL COMMENT '收藏用户id',
  `pid` int(11) NULL DEFAULT NULL COMMENT '帖子id',
  `time` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '收藏时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '收藏' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of jzk_collects
-- ----------------------------
INSERT INTO `jzk_collects` VALUES (1, 1, 15, '2019-01-02 19:44:20');
INSERT INTO `jzk_collects` VALUES (2, 1, 22, '2019-01-02 20:28:47');
INSERT INTO `jzk_collects` VALUES (3, 1, 16, '2019-01-06 14:31:14');
INSERT INTO `jzk_collects` VALUES (4, 1, 4, '2019-01-09 17:48:53');

-- ----------------------------
-- Table structure for jzk_feedback
-- ----------------------------
DROP TABLE IF EXISTS `jzk_feedback`;
CREATE TABLE `jzk_feedback`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NULL DEFAULT NULL COMMENT '反馈用户id',
  `content` varchar(800) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '反馈内容',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for jzk_inform
-- ----------------------------
DROP TABLE IF EXISTS `jzk_inform`;
CREATE TABLE `jzk_inform`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '内容',
  `time` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '发布时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '公告' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of jzk_inform
-- ----------------------------
INSERT INTO `jzk_inform` VALUES (1, '测试公告', '2019-01-02 15:18:20');
INSERT INTO `jzk_inform` VALUES (5, '又来一个测试', '2019-01-02 15:34:03');
INSERT INTO `jzk_inform` VALUES (6, '继续测试', '2019-01-02 15:35:08');
INSERT INTO `jzk_inform` VALUES (7, '鲁', '2019-01-02 15:35:25');
INSERT INTO `jzk_inform` VALUES (8, '来吧', '2019-01-02 15:35:47');
INSERT INTO `jzk_inform` VALUES (9, '测试5', '2019-01-02 15:37:18');
INSERT INTO `jzk_inform` VALUES (10, '再来一个', '2019-01-02 15:37:41');
INSERT INTO `jzk_inform` VALUES (11, '跳转', '2019-01-02 15:39:50');
INSERT INTO `jzk_inform` VALUES (12, '测试稍等', '2019-01-02 15:44:16');
INSERT INTO `jzk_inform` VALUES (13, '村上春树', '2019-01-02 15:44:21');
INSERT INTO `jzk_inform` VALUES (14, '发生', '2019-01-02 15:44:25');
INSERT INTO `jzk_inform` VALUES (15, '我就是一个测试的公告而已，没有其他什么了', '2019-01-02 15:55:12');
INSERT INTO `jzk_inform` VALUES (16, '就会根据规划', '2019-01-12 10:57:40');

-- ----------------------------
-- Table structure for jzk_is_merchant
-- ----------------------------
DROP TABLE IF EXISTS `jzk_is_merchant`;
CREATE TABLE `jzk_is_merchant`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NULL DEFAULT NULL COMMENT '商家id',
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '店铺名字',
  `address` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '地址',
  `detail` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '店铺详细介绍',
  `people_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '联系人姓名',
  `people_tel` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '联系人电话',
  `lincese` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '营业执照',
  `grade` int(3) NULL DEFAULT 1 COMMENT '商家等级',
  `is_vip` int(2) NULL DEFAULT 0 COMMENT '是否vip',
  `is_check` int(2) NULL DEFAULT 0 COMMENT '是否已审核',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '注册商家' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of jzk_is_merchant
-- ----------------------------
INSERT INTO `jzk_is_merchant` VALUES (4, 1, '个梵蒂冈', '个梵蒂冈', '个梵蒂冈', '改点', '18398663416', '', 1, 0, 1);
INSERT INTO `jzk_is_merchant` VALUES (5, 1, 'agam', '四川大学', '没有介绍', '电饭锅', '234234243', '', 1, 0, 1);
INSERT INTO `jzk_is_merchant` VALUES (6, 1, 'jhgjgh', 'hgf', '商店介绍', 'fgh', '4535', '', 1, 0, 1);
INSERT INTO `jzk_is_merchant` VALUES (7, 1, 'jkhkhj', 'hjkhjk', '商店介绍', '5464', '645646', '', 1, 0, 0);

-- ----------------------------
-- Table structure for jzk_jianzhi_type
-- ----------------------------
DROP TABLE IF EXISTS `jzk_jianzhi_type`;
CREATE TABLE `jzk_jianzhi_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '类型名字',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 19 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of jzk_jianzhi_type
-- ----------------------------
INSERT INTO `jzk_jianzhi_type` VALUES (4, '促销');
INSERT INTO `jzk_jianzhi_type` VALUES (2, '充场');
INSERT INTO `jzk_jianzhi_type` VALUES (18, '其他');
INSERT INTO `jzk_jianzhi_type` VALUES (8, '助教');
INSERT INTO `jzk_jianzhi_type` VALUES (15, '地摊拉访');
INSERT INTO `jzk_jianzhi_type` VALUES (3, '安保');
INSERT INTO `jzk_jianzhi_type` VALUES (11, '实习');
INSERT INTO `jzk_jianzhi_type` VALUES (17, '审核录入');
INSERT INTO `jzk_jianzhi_type` VALUES (13, '打包分拣');
INSERT INTO `jzk_jianzhi_type` VALUES (9, '文员');
INSERT INTO `jzk_jianzhi_type` VALUES (12, '服务员');
INSERT INTO `jzk_jianzhi_type` VALUES (6, '模特');
INSERT INTO `jzk_jianzhi_type` VALUES (1, '派单');
INSERT INTO `jzk_jianzhi_type` VALUES (5, '礼仪');
INSERT INTO `jzk_jianzhi_type` VALUES (10, '设计');
INSERT INTO `jzk_jianzhi_type` VALUES (16, '话务客服');
INSERT INTO `jzk_jianzhi_type` VALUES (7, '销售');
INSERT INTO `jzk_jianzhi_type` VALUES (14, '问卷调查');

-- ----------------------------
-- Table structure for jzk_posts
-- ----------------------------
DROP TABLE IF EXISTS `jzk_posts`;
CREATE TABLE `jzk_posts`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NULL DEFAULT NULL COMMENT '发帖用户id',
  `title` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '帖子标题',
  `people_tel` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '联系人电话',
  `people` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '联系人名',
  `content` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '帖子内容',
  `wages` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '工资',
  `benefits` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '效益',
  `need_num` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '所需人数',
  `start_time` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '开始时间',
  `end_time` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '结束时间',
  `addres` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '工作地点',
  `other` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '其他要求',
  `is_top` int(2) NULL DEFAULT 0 COMMENT '是否置顶',
  `is_check` int(2) NULL DEFAULT 0 COMMENT '是否已审核，倒计时',
  `is_completed` int(2) NULL DEFAULT 0 COMMENT '是否已完成',
  `jianzhi_type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '兼职类型，外建',
  `jianzhi_time_type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '兼职时间类型',
  `public_time` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '发布时间',
  `count_down_time` timestamp(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `jianzhi_type`(`jianzhi_type`) USING BTREE,
  CONSTRAINT `jianzhi_type` FOREIGN KEY (`jianzhi_type`) REFERENCES `jzk_jianzhi_type` (`name`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 28 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '帖子' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of jzk_posts
-- ----------------------------
INSERT INTO `jzk_posts` VALUES (1, 1, '测试添加兼职', '44', '测试添加兼职', '测试添加兼职', '3', '元/周', '2', '2019-01-02 19:22:54', '2019-01-02 19:22:54', '测试添加兼职', 'on', 0, 1, NULL, '派单', '0', '2019-01-02 19:22:54', NULL);
INSERT INTO `jzk_posts` VALUES (2, 1, '来吧', '45345', '来吧', '来吧来吧', '45', '0', '343', '2019-01-02 19:22:55', '2019-01-02 19:22:55', '来吧', 'on', 0, 1, NULL, '派单', '1', '2019-01-02 19:22:55', NULL);
INSERT INTO `jzk_posts` VALUES (3, 1, '测试哦', '35435', 'agam', '测试哦测试哦测试哦测试哦', '23', '3', '23', '2019-01-02 20:33:40', '2019-03-31 20:33:52', '测试哦', 'on', 0, 1, NULL, '派单', '3', '2019-03-31 20:33:52', '2019-03-31 20:33:52');
INSERT INTO `jzk_posts` VALUES (4, 1, '个人的非官方', '', '个人的非官方', '个人的非官方个人的非官方', '345', '2', '435', '2019-01-06 14:09:40', '2019-01-06 14:09:40', '个人的非官方', '个人的非官方个人的非官方个人的非官方', 0, 1, NULL, '派单', '3', '2019-01-06 14:09:40', '2019-01-06 14:09:40');
INSERT INTO `jzk_posts` VALUES (5, 1, '股份大股东', '434', '股份大股东', '股份大股东股份大股东', '个地方官', '元/周', '43', '2019-01-06 14:10:20', '2019-01-06 14:10:20', '股份大股东3', '股份大股东股份大股东股份大股东', 0, 1, NULL, '派单', '0', '2019-01-06 14:10:20', '2019-01-06 14:10:20');
INSERT INTO `jzk_posts` VALUES (6, 1, '这次是认真的兼职', '4353', '方法', '这次是认真的兼职', '4535', '元/小时', '43', '2019-01-06 14:09:19', '2019-01-06 14:09:19', '这次是认真的兼职', '这次是认真的兼职这次是认真的兼职这次是认真的兼职这次是认真的兼职', 1, 0, NULL, '派单', '0', '2019-01-06 14:09:19', '2019-01-06 14:09:19');
INSERT INTO `jzk_posts` VALUES (7, 1, '陈师傅', '', '陈师傅', '陈师傅陈师傅', '43', '元/月', '3', '2019-01-06 14:07:35', '2019-01-06 14:07:35', '陈师傅', '陈师傅陈师傅陈师傅', 1, 1, NULL, '派单', '1', '2019-01-06 14:07:35', '2019-01-06 14:07:35');
INSERT INTO `jzk_posts` VALUES (8, 1, '发的所发生的', '其他', '其他', '其他', '其他', '元/周', '其他', '2019-01-06 14:07:46', '2019-01-06 14:07:46', '其他', '其他', 1, 1, NULL, '安保', '长期兼职', '2019-01-06 14:07:46', '2019-01-06 14:07:46');
INSERT INTO `jzk_posts` VALUES (17, 1, '对方公司的', '543534', '对方公司的', '对方公司的', '543', '元/小时', '4', '2019-01-01 12:00:00', '2019-01-01 19:34:00', '北京市故宫博物馆', '对方公司的', 1, 0, NULL, '地摊拉访', '短期兼职', '2019-01-02 20:10:53', NULL);
INSERT INTO `jzk_posts` VALUES (18, 1, '方法都不', '18398663521', '方法都不', '方法都不', '56', '元/天', '343', '2019-01-02 20:19:47', '2019-01-02 20:19:50', '清华大学', '大锅饭', 0, 0, NULL, '充场', '周末兼职', '2019-01-02 20:21:18', NULL);
INSERT INTO `jzk_posts` VALUES (22, 1, '每个地方刚', '18954554154', '范德萨范德萨', '每个地方刚', '56456', '元/小时', '3', '2019-01-03 15:17:48', '2019-01-03 15:17:48', '青海省西宁市政府', '每个地方刚每个地方刚', 0, 0, NULL, '促销', '其他兼职', '2019-01-03 15:17:48', NULL);
INSERT INTO `jzk_posts` VALUES (27, 1, 'dsfds', '34534354', 'g', 'sdfsdfdsf', '45', '元/小时', '4', '2019-01-01 12:00:00', '2019-01-01 19:34:00', 'dfgdfgfd', 'dfgdfg', 0, 0, 0, '派单', '短期兼职', '2019-03-28 21:13:04', NULL);
INSERT INTO `jzk_posts` VALUES (28, 1, 'test', '11223343543', 'root', '发大概的风格地方', '324', '元/小时', '23', '2019-03-31 20:51:01', '2019-04-02 00:00:00', '四川大学', '十分的舒服的事', 1, 0, 0, '充场', '周末兼职', '2019-03-31 20:51:16', NULL);
INSERT INTO `jzk_posts` VALUES (29, 1, '人多', '123456655', '梵蒂冈', '24似懂非懂舒服的', '12', '元/小时', '2342', '2019-01-01 12:00:00', '2019-01-01 19:34:00', '从百分点', '古典风格', 0, 0, 0, '派单', '短期兼职', '2019-03-31 20:52:35', NULL);

-- ----------------------------
-- Table structure for jzk_sign_up
-- ----------------------------
DROP TABLE IF EXISTS `jzk_sign_up`;
CREATE TABLE `jzk_sign_up`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NULL DEFAULT NULL COMMENT '用户id',
  `pid` int(11) NULL DEFAULT NULL COMMENT '帖子id',
  `is_confirme` int(2) NULL DEFAULT 0 COMMENT '商家是否已审核',
  `is_sign_in` int(2) NULL DEFAULT 0 COMMENT '是否以签到',
  `is_complete` int(2) NULL DEFAULT 0 COMMENT '是否以完成s',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '相关报名信息表\r\n如果增加完成后的评价呢' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of jzk_sign_up
-- ----------------------------
INSERT INTO `jzk_sign_up` VALUES (1, 1, 15, 1, 0, 0);
INSERT INTO `jzk_sign_up` VALUES (2, 2, 22, 1, 1, 0);
INSERT INTO `jzk_sign_up` VALUES (3, 1, 16, 1, 0, 1);
INSERT INTO `jzk_sign_up` VALUES (4, 1, 4, 1, 0, 0);

-- ----------------------------
-- Table structure for jzk_user
-- ----------------------------
DROP TABLE IF EXISTS `jzk_user`;
CREATE TABLE `jzk_user`  (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `unionid` int(11) NULL DEFAULT NULL,
  `openid` int(11) NULL DEFAULT NULL,
  `nickname` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `sex` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `province` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `city` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `country` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `avator` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `account` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '登录账号',
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '密码',
  `birthday` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '生日',
  `address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '现居地址',
  `tel` varchar(12) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '联系电话',
  `mail` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '邮箱',
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '姓名',
  `experience` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '兼职经历',
  `freetime` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '空闲时间',
  `payzhifubao` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '支付宝账号',
  `education` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '教育经历',
  `qqnum` int(12) NULL DEFAULT NULL COMMENT 'qq号码',
  `credit` int(2) NULL DEFAULT 1 COMMENT '信誉',
  `group` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '权限外键',
  `is_merchant` int(2) NULL DEFAULT 0 COMMENT '是否为商家',
  PRIMARY KEY (`uid`) USING BTREE,
  INDEX `jzk_user_group`(`group`) USING BTREE,
  CONSTRAINT `jzk_user_group` FOREIGN KEY (`group`) REFERENCES `jzk_user_groups` (`name`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of jzk_user
-- ----------------------------
INSERT INTO `jzk_user` VALUES (1, NULL, NULL, '阿甘', '男', '四川省', '成都市', '中国', NULL, 'root', 'pbkdf2:sha256:50000$2EG327Ua$16ad5c9d20c026d956d06da6229433b60fc9fc6d1d5765b3fd479244d3360184', NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, 1);

-- ----------------------------
-- Table structure for jzk_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `jzk_user_groups`;
CREATE TABLE `jzk_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NULL DEFAULT NULL COMMENT '用户id',
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '用户组名',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '用户组权限相关' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of jzk_user_groups
-- ----------------------------
INSERT INTO `jzk_user_groups` VALUES (1, 1, 'root');

-- ----------------------------
-- Table structure for jzk_wx_user
-- ----------------------------
DROP TABLE IF EXISTS `jzk_wx_user`;
CREATE TABLE `jzk_wx_user`  (
  `uid` int(11) NOT NULL AUTO_INCREMENT COMMENT '用户id',
  `unionid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'unionid可以帮助识别不同公众账号下的用户是否是同一个人',
  `openid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'OpenID是此网站上或应用中唯一对应用户身份的标识',
  `nickname` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '昵称',
  `sex` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '性别',
  `province` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '省份',
  `city` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '城市',
  `country` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '国家',
  `avator` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '头像',
  PRIMARY KEY (`uid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '用户微信信息' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
