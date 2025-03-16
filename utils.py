import time
import random

def start_timer():
    return time.time()

def stop_timer(start_time):
    return time.time() - start_time

def get_random_sentence():
    sentences = [
        "Ceci est un exemple de texte pour l'entraînement à l'écriture.",
        "La rapidité et la précision sont essentielles pour une bonne dactylographie.",
        "Essayez de taper cette phrase le plus rapidement possible.",
        "La pratique régulière améliore la vitesse de frappe.",
        "Continuez à vous entraîner pour devenir un expert en dactylographie."
    ]
    return random.choice(sentences)