CREATE TABLE IF NOT EXISTS bugs (
  id SERIAL PRIMARY KEY,
  source TEXT,
  source_id TEXT,
  title TEXT,
  description TEXT,
  stack_trace TEXT,
  environment JSONB,
  module_guess TEXT,
  priority TEXT,
  severity TEXT,
  assigned_to TEXT,
  repro_steps TEXT,
  repro_script TEXT,
  dockerfile TEXT,
  status TEXT DEFAULT 'OPEN',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS module_owners (
  id SERIAL PRIMARY KEY,
  module TEXT UNIQUE,
  owner TEXT
);

CREATE TABLE IF NOT EXISTS rules (
  id SERIAL PRIMARY KEY,
  name TEXT,
  match_pattern TEXT,
  priority TEXT
);