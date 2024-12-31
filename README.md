#### Video Demo:  [https://youtube.com/shorts/A5fPfT_6vmM]
#### Description:
## Dahlia Search Application

This desktop application that is designed to help my husband and me search and explore our extensive database of dahlia flowers. The key features is that you can easily find dahlias by entering their name, color, or unique identification number and you will get information about each dahlia, including its name, color, height, size, and an image.

The application is built using Python, Tkinter for the graphical user interface, and Pillow for image processing. It utilizes a SQLite database to store and retrieve detailed information about dahlias. The database is populated with our collection of dahlia varieties and our identification number.


## Features

- Search for dahlias by name, color, or number
- Display search results in a user-friendly interface
- Show images of the dahlias alongside their details

## Requirements ( see also the file requirements.txt)
    # sqlite3
        The sqlite3 module in Python provides an easy-to-use interface for interacting with SQLite databases.
    # Pillow
        Python Imaging Library used for image processing.
    # Tkinter
        Standard Python interface to the Tk GUI toolkit.


## libraries
    sqlite3
    tkinter
    pillow
    pytest


## Usage
    tart the application by running the command python3 project.py from the terminal. The main window will appear, displaying the search interface.

    >python3 project.py

## Limitations and future improvements
There are a few limitations that we plan to address in future updates:
    1. Color Limitations: The application can only display up to 5 dahlias per color correctly. While this isn’t an issue for our current collection, it limits scalability.
    2. Standalone Operation: We aim to make the application a standalone program. Currently, it must be run within the terminal, as I haven’t yet succeeded in packaging the images with PyInstaller.

## test
    Test_project.py can be used with pytest to test some of the functions

## sample
    Pictures of Dahlia flowers can be find in the folder dahlias

## files
    project.py
        The python script
    test_project.py
        the python scritp to test with Pytest
    requirements.txt
        all necessary Python libaries listed
    README.md
        this file
    create_Flower.py
        file the creates the datebase and fill it with sample data. Also included in project.py
    check_libraries_installed.py
        script to check all necessary Python libaries are installed.
    Dahlias
        folder with images of dahlias












Search for dahlias:

Enter a search query in the search bar.

Select the search criteria (name, color, or number).

Click the "Search" button to view the results.

Project Structure
    project.py: The main script that contains the application logic.

    flowers.db: The SQLite database containing information about dahlias.

    dahlias/: Directory containing images of the dahlias.

    README.md: This file.

    requirements.txt Requires Python libraries



project’s title: Our Dahlias
name: Carolina Nilsson
GitHub username:emilidasv
edX usernames:emilida
your city and country: Lafayette, CO, USA
date 12/31/2024
