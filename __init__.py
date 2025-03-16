def start_timer():
    import time
    return time.time()

def stop_timer(start_time):
    import time
    return time.time() - start_time

def calculate_wpm(words, time_taken):
    if time_taken > 0:
        return (words / time_taken) * 60
    return 0

def evaluate_typing_speed(text, time_taken):
    words = len(text.split())
    wpm = calculate_wpm(words, time_taken)
    return wpm