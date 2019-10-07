DROP USER IF EXISTS 'yaoandy107'@'%';

CREATE USER 'yaoandy107'@'%' IDENTIFIED BY '123qwe';

GRANT ALL ON narwhal.* TO 'yaoandy107'@'%' IDENTIFIED BY '123qwe';

FLUSH PRIVILEGES;


DROP DATABASE IF EXISTS
  narwhal;
CREATE DATABASE narwhal;


USE narwhal;

CREATE TABLE IF NOT EXISTS user(
  id        INT UNSIGNED  NOT NULL AUTO_INCREMENT,
  email     VARCHAR(191)  NOT NULL,
  password  VARCHAR(191)  NOT NULL,
  username  VARCHAR(191)  NOT NULL,
  level     TINYINT       NOT NULL,
  PRIMARY KEY (id),
  UNIQUE (email, username)
);

CREATE TABLE IF NOT EXISTS machine(
  id      INT       UNSIGNED  NOT NULL,
  user_id INT       UNSIGNED  NOT NULL,
  port    SMALLINT  UNSIGNED  NOT NULL,
  cpu     FLOAT     UNSIGNED  NOT NULL,
  memory  MEDIUMINT UNSIGNED  NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES user(id),
  UNIQUE (port)
);

CREATE TABLE IF NOT EXISTS project(
  id      INT UNSIGNED  NOT NULL AUTO_INCREMENT,
  user_id INT UNSIGNED  NOT NULL,
  name    VARCHAR(191)  NOT NULL,
  port    TINYINT       NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES user(id),
  UNIQUE (name)
);

CREATE TABLE IF NOT EXISTS addon(
  id          INT UNSIGNED  NOT NULL AUTO_INCREMENT,
  name        VARCHAR(191)  NOT NULL,
  project_id  INT UNSIGNED  NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES project(id),
  UNIQUE (name)
);