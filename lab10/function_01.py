def racer_disqualified(times, winner_times, n_penalties, penalties):
    """
    Determines if a racer is disqualified based on their times, penalties, and winner times.

    Parameters:
        times (list of int): List of the racer's times for three events.
        winner_times (list of int): List of winner times for the same three events.
        n_penalties (int): Number of penalties the racer incurred.
        penalties (list of int): List of penalty values.

    Returns:
        bool: True if the racer is disqualified, False otherwise.

    Raises:
        ValueError: If inputs do not meet the required types or constraints.
    """
    # Input validation
    if not (isinstance(times, list) and len(times) == 3 and all(isinstance(t, int) for t in times)):
        raise ValueError("times must be a list of three integers.")

    if not (isinstance(winner_times, list) and len(winner_times) == 3 and all(isinstance(wt, int) for wt in winner_times)):
        raise ValueError("winner_times must be a list of three integers.")

    if not isinstance(n_penalties, int):
        raise ValueError("n_penalties must be an integer.")

    if not (isinstance(penalties, list) and all(isinstance(p, int) for p in penalties)):
        raise ValueError("penalties must be a list of integers.")

    if n_penalties != len(penalties):
        raise ValueError("n_penalties must match the length of the penalties list.")

    disqualified = False
    tot_penalties = 0

    # Calculate total penalties and check for any excessive penalty
    for penalty in penalties:
        tot_penalties += penalty
        if penalty > 100:
            disqualified = True

    # Check for disqualification based on total penalties or number of penalties
    if tot_penalties > 100 or n_penalties > 5:
        disqualified = True

    # Check if any time exceeds 1.5 times the corresponding winner time
    for i in range(3):
        max_time = winner_times[i] * 1.5
        if times[i] > max_time:
            disqualified = True

    return True