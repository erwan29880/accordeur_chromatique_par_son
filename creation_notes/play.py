import numpy
from notes import Note
import simpleaudio
import time
from scipy.io.wavfile import write 
import matplotlib.pyplot as plt

class Play(Note):


    def __init__(self, note: int, duree_relative: int, octave: int):
        super().__init__()

        # note commence à "1" par La
        # second la durée de note

        self.inc = note
        self.octave = octave
        self.note = super().set_octave(self.octave)
        self.fs = 44100 # 44100 samples per second
        self.seconds = duree_relative
        self.seconds = self.seconds /4
        self.play_obj = None


    def creation_note(self):
        
        # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
        t = numpy.linspace(0, self.seconds, int(self.seconds * self.fs), False)

        # Generate a sine wave from the frequency
        notes = numpy.sin(self.note[self.inc] * t * 2 * numpy.pi)

        # Ensure that highest value is in 16-bit range
        audio = notes * (2**15 - 1) / numpy.max(numpy.abs(notes))
        # Convert to 16-bit data
        audio = audio.astype(numpy.int16)

        return audio

    def save_note(self, nom_fichier: str):
        res = self.creation_note()
        write(nom_fichier, 44100, res)

    def play_note(self):   
        audio = self.creation_note() 
        self.play_obj = simpleaudio.play_buffer(audio, 1, 2, self.fs)
        time.sleep(self.seconds)

    def play_numpy(self, tableau_numpy):   
        
        self.play_obj = simpleaudio.play_buffer(tableau_numpy, 1, 2, self.fs)
        time.sleep(self.seconds)


    def stop_note(self):
        self.play_obj.stop()


if __name__ == "__main__":

    
    #pour lire une note 
    # note = Play(note= 0, duree_relative = 10, octave = 5).play_note()

    #pour enregistrer une note
    # note = Play(note= 0, duree_relative = 10, octave = 5).save_note('sib3.wav')
   
   
    # liste des notes, octave3, et enregistrement des notes dans le dossier audio
    # liste = ['la3', 'sib3', 'si3', 'do3', 'do_diese3', 're3', 'mib3', 'mi3', 'fa3', 'fa_diese3', 'sol3', 'lab3']
    # for i in range(0,12):
    #     nom_de_la_note = 'audio/'+str(i+1)+'_'+liste[i]+'.wav'
    #     note = Play(note= i, duree_relative = 10, octave = 4).save_note(nom_de_la_note)
        

    #voir la courbe sinusoidale
    # plt.figure()
    # note = Play(note= 0, duree_relative = 10, octave = 5).creation_note()[:60]
    # plt.plot(note)
    # plt.show()

    #créer plusieurs notes
    note1 = Play(note= 0, duree_relative = 2, octave = 4).creation_note()
    note2 = Play(note= 2, duree_relative = 2, octave = 4).creation_note()
    note3 = Play(note= 4, duree_relative = 2, octave = 4).creation_note()
    note4 = Play(note= 5, duree_relative = 2, octave = 4).creation_note()
    melodie = numpy.vstack((note1, note2, note3, note4))

    note = Play(0,duree_relative=8,octave=4).play_numpy(melodie)
