import os
import shutil
import json
import requests
import subprocess
from pathlib import Path

# --- Configuration & Paths ---
BASE_DIR = Path(os.getenv('APPDATA')) / "DiscordQuestCompleter"
DATA_DIR = BASE_DIR / "Data"
INFO_JSON_URL = "https://raw.githubusercontent.com/TakiiiNotFound/DiscordQuestBypass/refs/heads/main/Data/Info.json"
DEFAULT_EXE_URL = "https://raw.githubusercontent.com/TakiiiNotFound/DiscordQuestBypass/refs/heads/main/Data/default.exe"

# Ensure the base directory exists
BASE_DIR.mkdir(parents=True, exist_ok=True)

def clear_screen():
    """Clears the terminal console based on the OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_cache():
    """Deletes everything inside %appdata%\\DiscordQuestCompleter\\Data"""
    print(f"\n[!] Clearing cache in {DATA_DIR}...")
    if DATA_DIR.exists():
        try:
            shutil.rmtree(DATA_DIR)
            DATA_DIR.mkdir(parents=True, exist_ok=True)
            print("[+] Cache cleared successfully.")
        except Exception as e:
            print(f"[-] Error clearing cache: {e}")
    else:
        print("[?] Cache folder is already empty.")
    input("\nPress Enter to return to menu...")

def update_library():
    """Downloads Info.json and default.exe to the base folder"""
    print("\n[*] Updating library resources from GitHub...")
    files = {
        "Info.json": INFO_JSON_URL,
        "default.exe": DEFAULT_EXE_URL
    }
    
    for filename, url in files.items():
        try:
            response = requests.get(url, timeout=15)
            response.raise_for_status()
            with open(BASE_DIR / filename, "wb") as f:
                f.write(response.content)
            print(f"[+] Successfully updated: {filename}")
        except Exception as e:
            print(f"[-] Failed to download {filename}: {e}")
    input("\nPress Enter to return to menu...")

def select_game():
    """Parses Info.json and manages game-specific folders/exes"""
    info_path = BASE_DIR / "Info.json"
    default_exe_source = BASE_DIR / "default.exe"

    if not info_path.exists():
        print("[-] Info.json missing. Please run 'Update library' first.")
        input("\nPress Enter to return to menu...")
        return

    try:
        with open(info_path, 'r') as f:
            data = json.load(f)
            game_list = data.get("games", [])
    except Exception as e:
        print(f"[-] Error reading Info.json: {e}")
        input("\nPress Enter to return to menu...")
        return

    print("\n--- Available Games ---")
    for i, game in enumerate(game_list):
        print(f"{i + 1}. {game['name']}")

    choice = input("\nSelect a game (number) or 'b' to go back: ")
    if choice.lower() == 'b':
        return
        
    if not choice.isdigit() or not (1 <= int(choice) <= len(game_list)):
        print("[-] Invalid selection.")
        input("\nPress Enter to return to menu...")
        return

    selected = game_list[int(choice) - 1]
    
    # Define the deep path for the game within the Data folder
    game_folder = DATA_DIR / selected['path']
    game_exe_path = game_folder / selected['executable']

    # 1. Create sub-folders[cite: 1]
    if not game_folder.exists():
        print(f"[*] Creating directory structure: {selected['path']}")
        game_folder.mkdir(parents=True, exist_ok=True)

    # 2. Deploy the executable if missing[cite: 1]
    if not game_exe_path.exists():
        if default_exe_source.exists():
            print(f"[*] Deploying {selected['executable']}...")
            shutil.copy(default_exe_source, game_exe_path)
        else:
            print("[-] Error: default.exe missing. Run 'Update library' first!")
            input("\nPress Enter to return to menu...")
            return

    # 3. Launch in a NEW window with local path context
    try:
        print(f"[+] Launching {selected['name']} in a new window...")
        
        # subprocess.CREATE_NEW_CONSOLE ensures it gets its own window on Windows
        # cwd ensures the target's relative path is its own folder
        subprocess.Popen(
            [str(game_exe_path)], 
            cwd=str(game_folder),
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        print("[!] Executable process started independently.")
    except Exception as e:
        print(f"[-] Failed to launch: {e}")
    
    input("\nPress Enter to return to menu...")

def main():
    while True:
        clear_screen()
        print("==============================")
        print("   Discord Quest Completer")
        print("==============================")
        print("1. Select Game")
        print("2. Update library")
        print("3. Clear Cache")
        print("4. Exit")
        
        user_input = input("\n> ")

        if user_input == '1':
            clear_screen()
            select_game()
        elif user_input == '2':
            clear_screen()
            update_library()
        elif user_input == '3':
            clear_screen()
            clear_cache()
        elif user_input == '4':
            print("Goodbye!")
            break
        else:
            print("[-] Unknown option.")
            input("Press Enter to try again...")

if __name__ == "__main__":
    main()
