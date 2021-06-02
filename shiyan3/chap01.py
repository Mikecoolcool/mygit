from thinkdsp import read_wave
from thinkdsp import decorate

wave1 = read_wave('170255__dublie__trumpet.wav')
spectrum1 = wave1.make_spectrum()
spectrum1.plot(high=5000)
decorate(xlabel='Frequency (Hz)')

wave2 = read_wave('170255__dublie__trumpet.wav')
segment2 = wave2.segment(start=1.1, duration=0.3)
spectrum2 = segment2.make_spectrum()
spectrum2.plot(high=5000)
decorate(xlabel='Frequency (Hz)')