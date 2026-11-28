def compute_average(grades: list[float]) -> float:
    if len(grades) < 2:
        return 0
    min_grade = min(grades)
    max_grade = max(grades)
    total = sum(grade for grade in grades if grade not in (min_grade, max_grade))
    return total / (len(grades) - 2)