from game import Game

def main():
    g = Game()

    while g.running:
        g.current_menu.display_menu()
        g.game_loop()


if __name__ == "__main__":
    main()