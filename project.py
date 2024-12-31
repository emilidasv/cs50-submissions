import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

def connect_db():
    conn = sqlite3.connect('flowers.db')
    return conn

def drop_tables(): 
        conn = sqlite3.connect('flowers.db')
        cursor = conn.cursor() 
        cursor.execute('DROP TABLE IF EXISTS dahlias') 
        conn.commit() 
        conn.close()

def create_table():
    conn = connect_db()
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
    conn.close()

def populate_table(data):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO dahlias (name, number, color, days, image_url) VALUES (?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    conn.close()

# Sample data to be inserted into the dahlias table
sample_data = [
('A-peeling',17,'yellow',150,'A-peeling.png'),
('Beep Beep',19,'puye',150,'Beep Beep.png'),
('Bodacious',12,'reye',150,'Bodacious.png'),
('Brandon Michael',8,'whpu',150,'Brandon Michael.png'),
('Bridezilla',38,'white',150,'Bridezilla.png'),
('Cabana Banana',4,'yellow',150,'Cabana Banana.png'),
('Cheyenne',40,'reye',150,'Cheyenne.png'),
('Citron du Cap',13,'yellow',150,'Citron du Cap.png'),
('Clearview Daniel',3,'yellow',150,'Clearview Daniel.png'),
('Clearview Jonas',36,'piye',150,'Clearview Jonas.png'),
('Crazy leg',41,'yere',150,'Crazy leg.png'),
('Crossfield Ebony',10,'red',150,'Crossfield Ebony.png'),
('Dancin Queen',37,'pink',150,'Dancin Queen.png'),
('Diva',35,'purple',150,'Diva.png'),
('Dream Catcher',20,'piye',150,'Dream Catcher.png'),
('Duet',44,'rewh',150,'Duet.png'),
('Einstein',15,'purple',150,'Einstein.png'),
('Enchantress',2,'puwh',150,'Enchantress.png'),
('Encore',42,'yellow',150,'Encore.png'),
('Fluffles',34,'piwh',150,'Fluffles.png'),
('Half Pint',22,'reye',150,'Half Pint.png'),
('Hulins Carneval',18,'whpu',150,'Hulins Carneval.png'),
('Innocence',26,'piye',150,'Innocence.png'),
('Jennifers Wedding',28,'purple',150,'Jennifers Wedding.png'),
('Juanita',23,'red',150,'Juanita.png'),
('Kasasagi',14,'reye',150,'Kasasagi.png'),
('Katie',31,'reye',150,'Katie.png'),
('Lady Liberty',21,'white',150,'Lady Liberty.png'),
('Mary Munns',9,'purple',150,'Mary Munns.png'),
('Matilda Houston',27,'red',150,'Matilda Houston.png'),
('Mikayla Miranda',7,'purple',150,'Mikayla Miranda.png'),
('Pinelands Pam',30,'yere',150,'Pinelands Pam.png'),
('Poppers',29,'yere',150,'Poppers.png'),
('Ryan C',43,'rewh',150,'Ryan C.png'),
('Santa Claus',11,'rewh',150,'Santa Claus.png'),
('Spartacus',1,'red',150,'Spartacus.png'),
('Spider Women',6,'puwh',150,'Spider Women.png'),
('Spoiled Rotten',39,'piye',150,'Spoiled Rotten.png'),
('Steven David',24,'orange',150,'Steven David.png'),
('Teddy',25,'orange',150,'Teddy.png'),
('Verones Obsedian',33,'black',150,'Verones Obsedian.png'),
('Voodoo',5,'red',150,'Voodoo.png'),
('Wheels',32,'yere',150,'Wheels.png'),
('Wildcat',16,'yere',150,'Wildcat.png')
]

def search_dahlias(query, search_by):
    conn = connect_db()
    cursor = conn.cursor()
    #print(f"Searching for {query} by {search_by}")
    if search_by == 'name':
        cursor.execute("SELECT * FROM dahlias WHERE name LIKE ?", ('%' + query + '%',))
    elif search_by == 'color':
        cursor.execute("SELECT * FROM dahlias WHERE color LIKE ?", ('%' + query + '%',))
    elif search_by == 'number':
        cursor.execute("SELECT * FROM dahlias WHERE number LIKE ?", ('%' + query + '%',))
    results = cursor.fetchall()
    #print(f"Results: {results}")
    conn.close()
    return results

def display_results(results, search_by):
    for widget in results_frame.winfo_children():
        widget.destroy()
    
    if not results:
        messagebox.showinfo("No Results", "No dahlias found.")
        return

    for i, row in enumerate(results):
        dahlia_id, name, number, color, days, image_url = row
        #print(dahlia_id)
        #print(i)
        ttk.Label(results_frame, text=f"Name: {name}").grid(row=i, column=0, padx=10, pady=5)
        ttk.Label(results_frame, text=f"Number: {number}").grid(row=i, column=1, padx=10, pady=5)
        #ttk.Label(results_frame, text=f"Color: {color}").grid(row=i, column=2, padx=10, pady=5)
        #ttk.Label(results_frame, text=f"Days: {days}").grid(row=i, column=3, padx=10, pady=5)
        
        try:
            image = Image.open(f"dahlias/{image_url}")
            #print(image_url)
            #image = image.resize((319, 458))
            if ((search_by == 'name') or (search_by == 'number')):
                image = image.resize((319, 458))
            elif search_by == 'color':
                image = image.resize((100, 150))

            photo = ImageTk.PhotoImage(image)
            image_label = ttk.Label(results_frame, image=photo)
            image_label.image = photo
            image_label.grid(row=i, column=3, padx=10, pady=5)
        except Exception as e:
            print(f"Error loading image: {e}")

def search():
    query = search_entry.get()
    search_by = search_option.get()
    results = search_dahlias(query, search_by)
    display_results(results, search_by)
    

def main():
    global root, search_entry, search_option, results_frame

    drop_tables()
    create_table()
    populate_table(sample_data)
    
    # Create the main Tkinter window
    root = tk.Tk()
    root.title("Dahlia Search  (if two colors:red-white->rewh , pink-yellow piye etc)")

    # Create and place the search widgets
    search_frame = ttk.Frame(root, padding="10")
    search_frame.grid(row=0, column=0, sticky="ew")

    search_label = ttk.Label(search_frame, text="Search Dahlias by:")
    search_label.grid(row=0, column=0, padx=5, pady=5)

    search_option = ttk.Combobox(search_frame, values=["name", "color", "number"], state="readonly")
    search_option.grid(row=0, column=1, padx=5, pady=5)
    search_option.current(0)

    search_entry = ttk.Entry(search_frame, width=30)
    search_entry.grid(row=0, column=2, padx=5, pady=5)

    search_button = ttk.Button(search_frame, text="Search", command=search)
    search_button.grid(row=0, column=3, padx=5, pady=5)

    # Create a frame to display results
    results_frame = ttk.Frame(root, padding="10")
    results_frame.grid(row=1, column=0, sticky="ew")

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()

