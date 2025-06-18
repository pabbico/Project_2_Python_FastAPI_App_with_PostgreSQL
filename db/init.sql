-- Create tables
CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

-- Insert sample data
INSERT INTO items (name, description)
VALUES 
    ('Item 1', 'First sample item'),
    ('Item 2', 'Second sample item'),
    ('Item 3', 'Three sample item'),
    ('Item 4', 'Four sample item'),
    ('Item 5', 'Five sample item'),
    ('Item 6', 'Six sample item')
ON CONFLICT (id) DO NOTHING;