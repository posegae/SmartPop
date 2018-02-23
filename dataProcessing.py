import numpy as np
import midi_manipulation
from tqdm import tqdm

# data processing information taken from here: http://danshiebler.com/2016-08-10-musical-tensorflow-part-one-the-rbm/
def get_songs(path):
    # TODO: refine file choices
    # TODO: replace Pop_Music_Midi with out pop music repo
    files = glob.glob('{}/*.mid*'.format(path))
    songs = []
    for f in tqdm(files):
        try:
            song = np.array(midi_manipulation.midiToNoteStateMatrix(f))
            if np.array(song).shape[0] > 50:
                songs.append(song)
        except Exception as e:
            raise e
    return songs

songs = get_songs('Pop_Music_Midi') #These songs have already been converted from midi to msgpack
print "{} songs processed".format(len(songs))
