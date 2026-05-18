# **Search Engine Helper 🔍**

A simple and lightweight Python script for searching and matching names from a predefined list. This program uses a custom "fuzzy search" algorithm that allows it to find relevant results even if the user's input has partial matches or minor typos.

## **📌 Description**

The script contains a basic dataset (a list of strings, currently popular titles like *Jujutsu Kaisen, Mo Dao Zu Shi, One Piece, Apothecary Diaries*). When a user enters a search query, the program:

1. Removes all spaces and converts letters to lowercase for an objective comparison.  
2. Splits both the search query and the database names into individual letters.  
3. Counts the number of shared letters between the input and the target names.  
4. Returns the result if the match ratio is **65% or higher**, and the number of correct letters exceeds the number of wrong ones.

## **🚀 Features**

* **Case-Insensitive:** ONE PIECE and one piece are treated exactly the same.  
* **Ignores Spaces:** A query like mo daozu shi will still successfully find the correct match.  
* **Fault Tolerant:** The algorithm relies on the presence of correct characters, so it can forgive minor typos or incomplete inputs.

## **🛠️ How to Use**

1. Make sure you have [Python 3.x](https://www.python.org/) installed on your machine.  
2. Clone this repository or download the Search engine helper.py file.  
3. Run the script in your terminal or command prompt:  
   python "Search engine helper.py"

4. Enter the name you want to search for when the Enter name: prompt appears.

## **💡 Example**

Enter name: jujutsu  

Searching for: jujutsu

Results: \['Jujutsu Kaisen'\]

## **📝 Developer Notes**

This project was created for educational purposes to demonstrate how to work with loops, lists, and custom string-filtering logic in Python. You can easily expand the names\_list with your own data or integrate this search function into a larger project.
