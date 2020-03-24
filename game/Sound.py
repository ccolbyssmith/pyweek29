import pygame

import pygame_gui

class Sound:
    def __init__(self, manager, width, height):
        self.sounds = [pygame.mixer.Sound("data/ButtonSound.wav"), pygame.mixer.Sound("data/NewsPaperMusic.wav")]
        pygame.mixer.music.load("data/RepeatMusic.mp3")
        self.musicSlide = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(pygame.Rect(width - 150, height - 20, 140, 15),
                                                                                      .5, [0,.5], manager, None, None, None)
        self.masterSoundSlide = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(pygame.Rect(width - 150, height - 40, 140, 15),
                                                                                            1, [0,1], manager, None, None, None)

    def playMusic(self):
        self.updateVolume()
        pygame.mixer.music.play(-1)

    def updateVolume(self):
        musicVolume = self.masterSoundSlide.get_current_value()*self.musicSlide.get_current_value()
        masterVolume = self.masterSoundSlide.get_current_value()
        pygame.mixer.music.set_volume(musicVolume)
        for i in self.sounds:
            pygame.mixer.Sound.set_volume(i, masterVolume)

    def playButtonSound(self):
        pygame.mixer.Sound.play(self.sounds[0])

    def playNewspaperSound(self):
        pygame.mixer.Sound.play(self.sounds[1])
