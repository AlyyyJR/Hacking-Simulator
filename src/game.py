from engine import GameEngine
from interface import show_puzzle, show_result
from hacking_tools import crack_md5, find_hidden_file
import hashlib

class Game:
    def __init__(self):
        self.engine = GameEngine("puzzles/level1.json")

    def start(self):
        puzzle = self.engine.load_puzzle(1)
        show_puzzle(puzzle)

        if puzzle["type"] == "password_crack":
            user_input = input("Entrez un mot de passe à tester: ").strip()
            user_hashed = hashlib.md5(user_input.encode()).hexdigest()  # Convertir en hash
            
            # Debugging prints
            print(f"DEBUG: Hash de l'entrée utilisateur: {user_hashed}")
            if "hash" in puzzle:
                print(f"DEBUG: Hash attendu: {puzzle['hash']}")
                success = (user_hashed == puzzle["hash"])  # Comparer les hashes
            else:
                print("DEBUG: Aucune valeur de hash attendue dans le puzzle.")
                success = False
        
        elif puzzle["type"] == "file_manipulation":
            user_input = input("Tapez 'scan' pour trouver le fichier caché: ").strip()
            if user_input.lower() == "scan":
                solution = find_hidden_file()
                success = (solution == puzzle["solution"])
            else:
                success = False
        
        show_result(success)