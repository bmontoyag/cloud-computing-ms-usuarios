
-- Esquema y tabla para usuarios
CREATE SCHEMA IF NOT EXISTS usuarios;
CREATE TABLE IF NOT EXISTS usuarios.usuarios (
  id SERIAL PRIMARY KEY,
  email VARCHAR(120) UNIQUE NOT NULL,
  nombre VARCHAR(120) NOT NULL,
  rol VARCHAR(50) DEFAULT 'empleado'
);

INSERT INTO usuarios.usuarios (email, nombre, rol) VALUES
  ('demo1@empresa.com','Demo Uno','admin')
ON CONFLICT (email) DO NOTHING;
