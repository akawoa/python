-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dojos_and_ninjas
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `dojos_and_ninjas` ;

-- -----------------------------------------------------
-- Schema dojos_and_ninjas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dojos_and_ninjas` DEFAULT CHARACTER SET utf8 ;
USE `dojos_and_ninjas` ;

-- -----------------------------------------------------
-- Table `dojos_and_ninjas`.`dojos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dojos_and_ninjas`.`dojos` ;

CREATE TABLE IF NOT EXISTS `dojos_and_ninjas`.`dojos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dojos_and_ninjas`.`ninjas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dojos_and_ninjas`.`ninjas` ;

CREATE TABLE IF NOT EXISTS `dojos_and_ninjas`.`ninjas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `age` INT NULL,
  `image` VARCHAR(255) NULL,
  `dojo_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_ninjas_dojos_idx` (`dojo_id` ASC) VISIBLE,
  CONSTRAINT `fk_ninjas_dojos`
    FOREIGN KEY (`dojo_id`)
    REFERENCES `dojos_and_ninjas`.`dojos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
