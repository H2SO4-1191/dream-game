import pygame

class AudioManager:
    def __init__(self):
        pygame.mixer.init()

        self.sfx = {
            1: "assets/sounds/roll.mp3",
            2: "assets/sounds/move.mp3",
            3: "assets/sounds/punish.mp3",
            4: "assets/sounds/game_over.mp3",
            5: "assets/sounds/choice.mp3"
        }

        self.music_path = "assets/music/dice_poker_music.mp3"

    def play_music(self, loop=True):
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.play(-1 if loop else 0)

    def stop_music(self):
        pygame.mixer.music.stop()

    def play(self, track_id):
        sound_path = self.sfx.get(track_id)
        if not sound_path:
            return

        sound = pygame.mixer.Sound(sound_path)
        sound.play()