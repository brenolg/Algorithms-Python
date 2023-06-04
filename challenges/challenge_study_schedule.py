def study_schedule(permanence_period, target_time):
    people_counter = 0

    try:
        for student in permanence_period:
            if student[0] <= target_time <= student[1]:
                people_counter += 1
    except (ValueError, TypeError):
        return None
    return people_counter
