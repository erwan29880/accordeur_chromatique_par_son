class Note:

    def __init__(self):
    # initalise un dictionnaire avant de calculer les bonnes fréquences
        self.__notes = {
            1: ["A" ,0],
            2: ["A#",0],
            3: ["B" ,0],
            4: ["C" ,0],
            5: ["C#",0],
            6: ["D" ,0],
            7: ["D#",0],
            8: ["E" ,0],
            9: ["F" ,0],
            10:["F#",0],
            11:["G" ,0],
            12:["G#",0]
        }

    def __frequences(self):
        z = 0
        for i, j in zip(self.__notes.keys(), self.__notes.values()):
            liste = []

            # r est la valeur du demi-ton
            r = 2**(1/12)

            # valeur des notes incrémentées
            lis = round(440 * r**(z), 2)
            liste.append(j[0])
            liste.append(lis)
            z = z+1
            self.__notes[z] = liste
        
        return self.__notes


    def set_octave(self, octave = 4):
        lis = self.__frequences()
        liste = []
        for i in self.__notes.values():
            frequency = i[1] * 2 ** (((octave*12)-48) / 12) 
            liste.append(frequency)

            


        return liste




if __name__ == "__main__":    

# vérification 

    notes = Note().set_octave(3)

    print(notes)
