CREATE TABLE `users` (
    `id` INT AUTO_INCREMENT,
    `first_name` VARCHAR(32),
    `last_name` VARCHAR(32),
    `username` VARCHAR(32) NOT NULL,
    `password` VARCHAR(32) NOT NULL,
    PRIMARY KEY(`id`)
);


CREATE TABLE `schools` (
    `school_id` AUTO_INCREMENT,
    `school_name` VARCHAR(32) NOT NULL,
    `school_location` VARCHAR(32),
    `founded` DATE,
    `type` ENUM ('Elementary School','Middle School','High School','College','University','Community College','Other')) NOT NULL,
    PRIMARY KEY(`school_id`)
);

CREATE TABLE `companies` (
    `company_id` AUTO_INCREMENT,
    `company_name` VARCHAR(32) NOT NULL,
    `company_location` VARCHAR(32),
    `industry` VARCHAR(32) NOT NULL,
    PRIMARY KEY(`company_id`)
);

CREATE TABLE `user_connections` (
    `person1_id` INT NOT NULL,
    `person2_id` INT NOT NULL,
    PRIMARY KEY(`person1_id`, person2_id),
    FOREIGN KEY(`person1_id`) REFERENCES `users`(`id`),
    FOREIGN KEY(`person2_id`) REFERENCES `users`(`id`)
);

CREATE TABLE `school_connections` (
    `person_id` INT NOT NULL,
    `school_id` INT NOT NULL,
    `start_date` DATE,
    `end_date` DATE,
    `degree` VARCHAR(32),
    PRIMARY KEY(`person_id`, `school_id`),
    FOREIGN KEY(`person_id`) REFERENCES `users`(`id`),
    FOREIGN KEY(`school_id`) REFERENCES `users`(`id`)
);

CREATE TABLE `company_connections` (
    `person_id` INT,
    `company_id` INT,
    `start_date` DATE,
    `end_date` DATE,
    `title` VARCHAR(32),
    PRIMARY KEY(`person_id`, `company_id`),
    FOREIGN KEY(`person_id`) REFERENCES `users`(`id`),
    FOREIGN KEY(`company_id`) REFERENCES `companies`(`company_id`)
);

