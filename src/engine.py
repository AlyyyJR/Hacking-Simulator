import json

class GameEngine:
    def __init__(self, puzzle_file):
        try:
            with open(puzzle_file, "r") as f:
                self.puzzles = json.load(f)
            if not isinstance(self.puzzles, list):
                raise ValueError(f"Le fichier {puzzle_file} ne contient pas une liste valide de puzzles.")
        except json.JSONDecodeError as e:
            raise ValueError(f"Erreur de lecture du fichier JSON {puzzle_file}: {e}")
        except FileNotFoundError:
            raise ValueError(f"Le fichier {puzzle_file} est introuvable.")
        except Exception as e:
            raise ValueError(f"Une erreur inattendue est survenue: {e}")

    def load_puzzle(self, puzzle_id):
        return next((p for p in self.puzzles if p["id"] == puzzle_id), None)

    def check_solution(self, puzzle, user_input):
        return user_input == puzzle["solution"]