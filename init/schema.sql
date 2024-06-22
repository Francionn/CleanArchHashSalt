CREATE DATABASE if not exists db_hash_salt;

use db_hash_salt;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE userpasswords (
    userpassword_id INT AUTO_INCREMENT PRIMARY KEY,
    
    passwordhash VARCHAR(255) NOT NULL,
    user_id INT NOT NULL,
    
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX idx_user_email ON users (email);