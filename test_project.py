import pytest
import sqlite3
import project  # Import your main application script

@pytest.fixture
def setup_db():
    # Set up a fresh test database
    conn = sqlite3.connect('flowers_test.db')  # Using a separate test database
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dahlias (
            dahlia_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            number INTEGER, 
            color TEXT NOT NULL,
            days INTEGER,
            image_url TEXT NOT NULL
        )
    ''')
    conn.commit()

    yield conn  # Yield the connection to be used in the tests

    # Clean up: Drop the table after tests
    cursor.execute('DROP TABLE IF EXISTS dahlias')
    conn.commit()
    conn.close()

def connect_db():
    conn = sqlite3.connect('flowers_test.db')
    return conn

def test_create_table(setup_db):
    project.drop_tables()  # Ensure table is dropped before creation
    project.create_table()
    conn = setup_db
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='dahlias'")
    table_exists = cursor.fetchone()
    assert table_exists is not None

def test_search_dahlias(setup_db):
    project.drop_tables()  # Ensure table is dropped before creation
    project.create_table()
    sample_data = [('Test Dahlia', 123, 'red', 10, 'test_image.png')]
    project.populate_table(sample_data)
    results = project.search_dahlias('red', 'color')
    assert len(results) == 1
    assert results[0][1] == 'Test Dahlia'

def test_populate_table(setup_db):
    project.drop_tables()  # Ensure table is dropped before creation
    project.create_table()
    sample_data = [('Test Dahlia', 123, 'red', 10, 'test_image.png')]
    project.populate_table(sample_data)
    results = project.search_dahlias('Test Dahlia', 'name')
    assert results is not None
    assert results[0][1] == 'Test Dahlia'

if __name__ == "__main__":
    pytest.main()
