# Michael Nguyen 260970685
import musicalbeeps

class Note:
    """
    A new note class that represents the musical notes in their
    written format.
    
    Instance attributes:
    * duration: float
    * pitch : str
    * octave : int
    * accidental: str
    """
    
    OCTAVE_MIN = 1
    OCTAVE_MAX = 7
    
    def __init__(self,duration,pitch,octave = 1,accidental = 'natural'):
        """ (float, str, int, str) -> Nonetype
        Creates object of type Note.
        
        >>> note= Note(2.0, "B", 4, "natural")
        >>> note.pitch
        'B'
        >>> note = Note(2.0, "B", 4)
        >>> note.accidental
        'natural'
        >>> note = Note(2.0, "B", 9)
        Traceback (most recent call last):
        AssertionError: Incorrect Input
        """

        accidental_values = ["sharp", "flat", "natural"]
        pitch_values = ["A", "B","C","D","E","F","G", "R"]
        
        
        if type(duration) != float or duration < 0 or type(pitch) != str \
           or type(octave) != int or type(accidental) != str \
           or octave > 7 or octave < 1 or accidental.lower() not \
           in accidental_values or pitch not in pitch_values \
           or pitch == pitch.lower():
            raise AssertionError("Incorrect Input")
        
        self.duration = duration
        self.pitch = pitch
        self.octave = octave
        self.accidental = accidental.lower()
    
    def __str__(self):
        """ () -> Nonetype
        Returns string of the format "Duration Pitch Octave Accidental"
        
        >>> note = Note(2.0, "B", 4, "natural")
        >>> print(note)
        2.0 B 4 natural
        >>> note = Note(2.0, "B", 6, "natural")
        >>> print(note)
        2.0 B 6 natural
        >>> note = Note(1.5, "B", 6, "natural")
        >>> print(note)
        1.5 B 6 natural
        """
        
        return str(self.duration) + " " + self.pitch + " " + \
                      str(self.octave) + " " + self.accidental
    
    def play(self, music_player = musicalbeeps.Player()):
        """ (Player) -> Nonetype
        Takes music player object and constructs the note string
        and duration for input in the play_note method.
        """
        
        musical_info = []
        notes = []
        
        if self.pitch == "R":
            musical_info.append("pause")
        else:        
            musical_info.append(self.pitch)
            musical_info.append(str(self.octave))
            
            if self.accidental == "flat":
                musical_info.append("b")
            elif self.accidental == "sharp":
                musical_info.append("#")
            
        note_string = "".join(musical_info)
        notes.append(note_string)
        notes.append(self.duration)

        music_player.play_note(notes[0], notes[1])
        
