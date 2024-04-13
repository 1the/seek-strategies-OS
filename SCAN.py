# scan

def scan_algorithm(head_position, direction, tracks, requests):
    sequence = []
    total_tracks = 0
    average_tracks = 0
    current_position = head_position
    # DO NOT use get() with string var: direction
    direction_factor = -1 if direction == "Inward" else 1  # -1 for inward, 1 for outward

    # Separate requests into two lists based on direction
    requests_greater = [req for req in requests if req >= head_position]    # inward
    requests_smaller = [req for req in requests if req < head_position]     # outward

    # Sort the requests in their respective directions
    requests_greater.sort()
    requests_smaller.sort(reverse=True)

    # Initialize the sequence of tracks visited
    sequence = [head_position]

    # Proceed in the chosen direction
    if direction_factor == -1:  # inward
        for req in requests_greater:
            sequence.append(req)
        if len(sequence) > 0:
            sequence.append(tracks - 1)  # Go to the edge track
            head_position = tracks - 1
            for req in requests_smaller:
                sequence.append(req)
    else:                              # outward
        for req in requests_smaller:
            sequence.append(req)
        if len(sequence) > 0:
            sequence.append(0)  # Go to track 0
            head_position = 0
            for req in requests_greater:
                sequence.append(req)

    # Calculate the total traveled tracks
    total_tracks = sum(abs(sequence[i] - sequence[i + 1]) for i in range(len(sequence) - 1))
    # Calculate the average traveled tracks
    average_tracks = total_tracks / len(requests)

    return sequence, total_tracks, average_tracks