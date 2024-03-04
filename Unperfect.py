def gale_shapley(students, hospitals):
    # Initialize a list of free students
    free_students = list(students.keys())
    # Initialize a dictionary to store the current matches
    matches = {h: None for h in hospitals.keys()}
    # While there are free students who still have hospitals to propose to
    while free_students:
        for s in free_students:
            # Get the list of hospitals that this student prefers
            preferred_hospitals = students[s]
            # Check if the student has any hospitals left to propose to
            if preferred_hospitals:
                # Propose to the first hospital on the list
                h = preferred_hospitals.pop(0)
                # Check the current student that the hospital is matched with
                matched_student = matches[h]
                if not matched_student:
                    # If the hospital is free, match it with the student
                    matches[h] = s
                    free_students.remove(s)
                else:
                    # If the hospital is not free, check if it prefers the new student
                    if hospitals[h].index(s) < hospitals[h].index(matched_student):
                        # If the hospital prefers the new student, unmatch the current student
                        free_students.append(matched_student)
                        # And match the hospital with the new student
                        matches[h] = s
                        free_students.remove(s)
            else:
                # If the student has no hospitals left to propose to, remove them from the list of free students
                free_students.remove(s)
    return matches

students = {
    'Assal': ['Emam_Reza', 'Sina', 'Madani'],
    'Mahya': ['Sina', 'Emam_Reza', 'Madani'],
    'Maryam': ['Madani', 'Sina', 'Emam_Reza'],
    'Ali': ['Emam_Reza', 'Sina', 'Madani']
}

hospitals = {
    'Emam_Reza': ['Assal', 'Mahya', 'Maryam', 'Ali'],
    'Sina': ['Mahya', 'Assal', 'Maryam', 'Ali'],
    'Madani': ['Maryam', 'Mahya', 'Assal', 'Ali']
}

print(gale_shapley(students, hospitals))
