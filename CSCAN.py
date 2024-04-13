# circular-scan

def cscan_algorithm(head_position, direction, tracks, requests):
    sequence = []
    total_tracks = 0
    average_tracks = 0
    current_position = head_position
    direction_factor = -1 if direction == "Inward" else 1  # -1 for inward, 1 for outward

    # Separate requests into two lists based on direction
    requests_greater = [req for req in requests if req >= head_position]    # inward
    requests_smaller = [req for req in requests if req < head_position] # outward

    # Initialize the sequence of tracks visited
    sequence = [head_position]

    # Proceed in the chosen direction
    if direction_factor == -1:  # inward
        # Sort the requests in their respective directions
        requests_greater.sort()  # ascending
        requests_smaller.sort()  # ascending
        for req in requests_greater:
            sequence.append(req)
        if len(sequence) > 0:
            sequence.append(tracks - 1)  # Go to the innermost track
            head_position = tracks - 1
            sequence.append(0)  # Go to the outer track without proceeding requests
            head_position = 0
            for req in requests_smaller:    # handling the rest requests
                sequence.append(req)
    else:                              # outward
        requests_greater.sort(reverse=True)  # descending
        requests_smaller.sort(reverse=True)  # descending
        for req in requests_smaller:
            sequence.append(req)
        if len(sequence) > 0:
            sequence.append(0)  # Go to the outer track
            head_position = 0
            sequence.append(tracks - 1)  # Go to the innermost track without proceeding requests
            head_position = tracks - 1
            for req in requests_greater:
                sequence.append(req)

    # Calculate the total traveled tracks
    for i in range(len(sequence) - 1):
        total_tracks += abs(sequence[i] - sequence[i + 1])
    # Calculate the average traveled tracks
    average_tracks = total_tracks / len(requests)

    return sequence, total_tracks, average_tracks