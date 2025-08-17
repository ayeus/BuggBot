
-- MySQL schema for BuggBit
CREATE TABLE IF NOT EXISTS bugs (
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  source VARCHAR(32) DEFAULT 'manual',
  source_id VARCHAR(128),
  title VARCHAR(512) NOT NULL,
  description TEXT,
  stack_trace MEDIUMTEXT,
  environment JSON,
  module_guess VARCHAR(255),
  priority ENUM('P0','P1','P2') DEFAULT 'P2',
  severity ENUM('Critical','High','Medium','Low') DEFAULT 'Low',
  assigned_to VARCHAR(128),
  repro_steps MEDIUMTEXT,
  repro_script MEDIUMTEXT,
  dockerfile MEDIUMTEXT,
  status ENUM('OPEN','IN_PROGRESS','RESOLVED','CLOSED') DEFAULT 'OPEN',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX idx_source_id (source_id),
  INDEX idx_priority (priority),
  INDEX idx_status (status)
);

CREATE TABLE IF NOT EXISTS module_owners (
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  module VARCHAR(255) UNIQUE,
  owner VARCHAR(128) NOT NULL
);

CREATE TABLE IF NOT EXISTS rules (
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  match_pattern VARCHAR(512),
  priority ENUM('P0','P1','P2') NOT NULL
);
