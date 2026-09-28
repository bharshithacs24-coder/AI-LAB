def vacuum_cleaner_agent(location, status_A, status_B):
    """
    Simple Reflex Agent for Vacuum Cleaner Problem[span_0](start_span)[span_0](end_span)
    Rules from image[span_1](start_span)[span_1](end_span):
    1. If status = 'Dirty' -> return 'Suck' (Pick the dust)[span_2](start_span)[span_2](end_span)
    2. Else if location = 'A' -> return 'Right[span_3](start_span)'[span_3](end_span)
    3. Else if location = 'B' -> return 'Left[span_4](start_span)'[span_4](end_span)
    """
    # Determine the status of the current room
    current_status = status_A if location == 'A' else status_B
    
    # Reflex rules[span_5](start_span)[span_5](end_span)
    if current_status == 'Dirty':
        return 'Suck' # Pick the dust[span_6](start_span)[span_6](end_span)
    elif location == 'A':
        return 'Right' # Move to room B[span_7](start_span)[span_7](end_span)
    elif location == 'B':
        return 'Left' # Move to room A[span_8](start_span)[span_8](end_span)


def run_environment(location='A', status_A='Dirty', status_B='Dirty'):
    # Convert status values to readable text
    rooms = {'A': status_A, 'B': status_B}
    
    print(f"Initial State: Location = {location}, Room A = {rooms['A']}, Room B = {rooms['B']}\n")
    
    step = 1
    # Run loop until both rooms A and B are clean[span_9](start_span)[span_9](end_span)
    while rooms['A'] == 'Dirty' or rooms['B'] == 'Dirty':
        action = vacuum_cleaner_agent(location, rooms['A'], rooms['B'])
        print(f"Step {step}: Agent at Room {location} (Status: {rooms[location]}) -> Action: {action}")
        
        # Perform action
        if action == 'Suck':
            rooms[location] = 'Clean'
        elif action == 'Right':
            location = 'B'
        elif action == 'Left':
            location = 'A'
            
        step += 1
        
    print(f"\nFinal State: Room A = {rooms['A']}, Room B = {rooms['B']}")
    print("Both A & B are clean. Stopping.") # Step 6 from image[span_10](start_span)[span_10](end_span)


# Test the environment with initial states from image[span_11](start_span)[span_11](end_span)
if __name__ == "__main__":
    # 1. Initialize two rooms A and B with clean or dirty[span_12](start_span)[span_12](end_span)
    # 2. Position vacuum cleaner at room A[span_13](start_span)[span_13](end_span)
    run_environment(location='A', status_A='Dirty', status_B='Dirty')

