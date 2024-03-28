# Student Grade Management System
This Python script manages student grades across multiple subjects. It generates random student names and grades, 
and then performs various operations on the data, such as calculating averages, finding the highest and lowest grades, and identifying students with above-average grades in a specific subject.

## Features
- Generates a specified number of students (default: 100) with random names (first and last) from a predefined list.
- Assigns random grades (between 1 and 100) to each student for a set of subjects (default: ქართული, მათემატიკა, ინგლისური, ფიზიკა, ქიმია).
- Prints a formatted table with student names and their grades for each subject.
- Calculates and displays the student with the highest average grade across all subjects.
- Identifies and displays the students with the highest and lowest grades in the mathematics subject.
- Identifies and displays the list of students with above-average grades in the English subject.
- Identifies and displays the list of students who failed in Chemistry.
- Identifies and displays the list of students who is named 'გვანცა', and their grades are maximum in all subjects.
- Identifies and displays the list of students who is named 'გვანცა' and whose points are above 20 in every subject.

# Dependencies
The script requires the following Python libraries:
- numpy
- random
- namesdb (a custom module containing lists of Georgian first and last names)
- Another dependencies are in requirements.txt file
# Usage
Make sure you have the required libraries installed. You can install them using pip:

> pip install numpy
 
Make sure you have the <namesdb.py> file in the same directory as the main script. You can download the file from the 
repository. Run the main script, and it will generate the student data, print the formatted table, and display the requested 
information.

# Customization
You can customize the script by modifying the following variables:
- num_students: Change the number of students to be generated.
- subjects: Modify the list of subjects by adding, removing, or renaming entries.
- first_names and last_names (in namesdb.py): Replace the provided lists with your own lists of names, if desired.

  - Note: The script assumes that the namesdb.py file is present in the same directory as the main script. If you want 
  to use a different module or location for the names, you'll need to update the import statement accordingly.


>>Gvantsa