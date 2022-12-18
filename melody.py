# Michael Nguyen 260970685
import musicalbeeps
from note import Note

class Melody:
    """
    A new Melody class ...
    
    Instance attributes:
    * title: str
    * author: str
    * notes: list
    """
    
    def __init__(self, filename = 'birthday.txt'):
        """ (str) -> Nonetype
        Creates a Melody type object.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> len(happy_birthday.notes)
        25
        >>> print(happy_birthday.notes[5])
        1.0 F 4 sharp
        >>> happy_birthday.title
        'Happy Birthday'
        >>> happy_birthday.author
        'Patty and Mildred J. Hill'
        """
        
        file = open(filename, "r")
        
        lines = []
        for line in file:
            lines.append(line)


        self.title = lines[0].strip()
        self.author = lines[1].strip()
        music = []
        repeated_notes = []
        for i in range(2,len(lines)):
            music_info = lines[i].split(" ")
            duration, pitch, octave, accidental, repeat = tuple(music_info)
            note = Note(float(duration),pitch,int(octave),accidental.lower())
            music.append(note)
            repeat = repeat.capitalize().strip()
            if repeat == "True" and repeated_notes == []:
                repeated_notes.append(note)
            elif repeat != "True" and repeated_notes != []:
                repeated_notes.append(note)
            elif repeat == "True" and repeated_notes != []:
                repeated_notes.append(note)
                for note in repeated_notes:
                    music.append(note)
                repeated_notes = []
        self.notes = music

        file.close()
    
    
    def play(self,music_player = musicalbeeps.Player()):
        """
        Uses music_player object and calls play method on each Note
        object.
        """
        
        for note in self.notes:
            note.play(music_player)
    
    def get_total_duration(self):
        """ () -> float
        Returns the toal duration of the song.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.get_total_duration()
        13.0
        >>> fur_elise = Melody("fur_elise.txt")
        >>> fur_elise.get_total_duration()
        25.799999999999944
        >>> twinkle = Melody("twinkle.txt")
        >>> twinkle.get_total_duration()
        24.5
        """
        
        duration = 0.0
        for note in self.notes:
            duration += note.duration
            print(type(duration))
            
        return duration
    
        
    def lower_octave(self):
        """ () -> bool
        Returns a boolean indicating whether the song was lowered by 1 octave.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.lower_octave()
        True
        >>> happy_birthday.notes[5].octave
        3
        >>> happy_birthday.lower_octave()
        True
        >>> happy_birthday.lower_octave()
        True
        >>> happy_birthday.lower_octave()
        False
        >>> happy_birthday.notes[5].octave
        1
        """
            
        for note in self.notes:
            if note.octave == note.OCTAVE_MIN:
                return False
            
        for note in self.notes:
            note.octave -= 1

        return True
    
    def upper_octave(self):
        """ () -> bool
        Returns a boolean indicating whether a song was increased by an octave.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.upper_octave()
        True
        >>> happy_birthday.notes[5].octave
        5
        >>> happy_birthday.upper_octave()
        True
        >>> happy_birthday.upper_octave()
        False
        >>> happy_birthday.notes[5].octave
        6
        """
        
        for note in self.notes:
            if note.octave == note.OCTAVE_MAX:
                return False
            
        for note in self.notes:
            note.octave += 1
        
        return True
        
    def change_tempo(self, tempo):
        """ (float) -> Nonetype
        Changes the tempo of a song by multiplying its duration
        by tempo.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.change_tempo(0.5)
        >>> happy_birthday.get_total_duration()
        6.5
        >>> happy_birthday.change_tempo(2)
        >>> happy_birthday.get_total_duration()
        13.0
        >>> happy_birthday.change_tempo(3)
        """
        
        for note in self.notes:
            note.duration = tempo*note.duration
            

            
           
        
            
