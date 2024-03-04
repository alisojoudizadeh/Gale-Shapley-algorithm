# Gale-Shapley Algorithm

This Python script implements the Gale-Shapley algorithm, also known as the Stable Marriage Problem. The algorithm finds a stable match between two sets (students and hospitals in this case) given their preferences.

## How to Run

You can run this script using Python 3. Here's an example command:

bash
```
python3 gale_shapley.py
```
Input
```
The input to the algorithm is two dictionaries: students and hospitals. Each dictionary key represents a student or a hospital, and the value is a list that represents their preferences. The first element in the list is the most preferred choice.

Here’s an example input:
students = {
    'Assal': ['Emam_Reza', 'Sina', 'Madani'],
    'Mahya': ['Sina', 'Emam_Reza', 'Madani'],
    'Maryam': ['Madani', 'Sina', 'Emam_Reza']
}

hospitals = {
    'Emam_Reza': ['Assal', 'Mahya', 'Maryam'],
    'Sina': ['Mahya', 'Assal', 'Maryam'],
    'Madani': ['Maryam', 'Mahya', 'Assal']
}
```
```Output
The output of the script is a dictionary where each key is a hospital and the value is the student that the hospital is matched with. The algorithm guarantees that a stable match will be found if one exists.
```
Algorithm
```The Gale-Shapley algorithm works as follows:
Initialize a list of free students and a dictionary to store the current matches.
While there are free students who still have hospitals to propose to, each student proposes to the first hospital on their list.
If the hospital is free, it is matched with the student. If the hospital is not free, it checks if it prefers the new student over the current match. If it does, it unmatches the current student and matches with the new student.
The algorithm continues until a stable match is found where no student and hospital would both prefer each other over their current partners.
```
License
This project is licensed under the Sahand University of Technology License.
```
Please replace the filename (`gale_shapley.py`) in the "How to Run" section with the actual filename of your Python script. Also, you may want to add more sections to this README, such as "Installation", "Contributing", etc., depending on the needs of your project. I hope this helps! Let me know if you have any other questions.
```
