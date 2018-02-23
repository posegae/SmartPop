# SmartPop

## Set-up

Goal data:

Data available for download [here](https://www.reddit.com/r/WeAreTheMusicMakers/comments/3ajwe4/the_largest_midi_collection_on_the_internet/)

Unzip it and put the contents in the empty MidiFiles folder

For now:

Following [these instructions](http://danshiebler.com/2016-08-10-musical-tensorflow-part-one-the-rbm/) to get a basic song generator.

All our current training files are available in Pop_Music_Midi. Eventually, we'll need to convert the contents of the "largest midi collection on the internet" from midi to [msgpack](https://pypi.python.org/pypi/msgpack).

If you need to re-download Pop_Music_Midi locally:

```
cd SmartPop
svn checkout https://github.com/dshieble/Musical_Matrices/trunk/Pop_Music_Midi
```
