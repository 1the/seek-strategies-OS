# shortest seek time first

def sstf_algorithm(head_position, requests):
    sequence = []
    total_tracks = 0
    average_tracks = 0
    # Reorder requests based on their distance from the current head position (Shortest Seek Time First algorithm)
    requests.sort(key=lambda x: abs(x - head_position))
    current_position = head_position
    sequence.append(current_position)

    for request in requests:
        difference = abs(request - current_position)
        total_tracks += difference
        sequence.append(request)
        current_position = request
    average_tracks = total_tracks / len(requests)

    return sequence, total_tracks, average_tracks