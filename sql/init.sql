DROP USER IF EXISTS 'yaoandy107'@'%';

CREATE USER 'yaoandy107'@'%' IDENTIFIED BY 'ntuthacker';

GRANT ALL ON narwhal.* TO 'yaoandy107'@'%' IDENTIFIED BY 'ntuthacker';

FLUSH PRIVILEGES;


DROP DATABASE IF EXISTS
  narwhal;
CREATE DATABASE narwhal;


USE narwhal;

CREATE TABLE IF NOT EXISTS user(
  id        INT UNSIGNED  NOT NULL AUTO_INCREMENT,
  email     VARCHAR(255)  NOT NULL,
  password  VARCHAR(255)  NOT NULL,
  username  VARCHAR(255)  NOT NULL,
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
  name    VARCHAR(255)  NOT NULL,
  port    TINYINT       NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES user(id),
  UNIQUE (name)
);

CREATE TABLE IF NOT EXISTS addon(
  id          INT UNSIGNED  NOT NULL AUTO_INCREMENT,
  name        VARCHAR(255)  NOT NULL,
  project_id  INT UNSIGNED  NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES project(id),
  UNIQUE (name)
);