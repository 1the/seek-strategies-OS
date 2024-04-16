# shortest seek time first

def sstf_algorithm(head_position, requests):
    sequence = []
    total_tracks = 0
    average_tracks = 0
    sorted_requests=[]
    # Reorder requests based on their distance from the current head position (Shortest Seek Time First algorithm)
    current_position = head_position
    sorted_requests.append(current_position)
    while requests:
        nearest = min(requests, key=lambda x: abs(x - current_position))
        sorted_requests.append(nearest)
        requests.remove(nearest)
        current_position = nearest

    # to insure correct calculation for total seek time
    current_position = head_position
    for request in sorted_requests:
        difference = abs(request - current_position)
        total_tracks += difference
        sequence.append(request)
        current_position = request
    average_tracks = total_tracks / (len(sorted_requests)-1)     # not to count the head with them

    return sequence, total_tracks, average_tracks