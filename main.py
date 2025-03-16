from utils.utils import get_random_sentence

def display_instructions():
    print("Bienvenue dans l'entraînement à l'écriture!")
    print("Vous allez avoir un texte à taper. Essayez de le faire le plus rapidement possible.")
    print("Lorsque vous êtes prêt, appuyez sur 'Entrée' pour commencer.")

def main():
    while True:
        display_instructions()
        input()  # Attendre que l'utilisateur appuie sur 'Entrée'
        
        text_to_type = get_random_sentence()
        print(f"\nTapez le texte suivant:\n{text_to_type}\n")
        
        user_input = input("Votre saisie: ")
        
        if user_input == text_to_type:
            print("Bravo! Vous avez tapé le texte correctement.")
        else:
            print("Il y a des erreurs dans votre saisie. Essayez encore!")
        
        play_again = input("Voulez-vous essayer une autre phrase? (o/n): ")
        if play_again.lower() != 'o':
            break

if __name__ == "__main__":
    main()