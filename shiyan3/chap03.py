from thinkdsp import CosSignal, SinSignal
from thinkdsp import decorate
cos_sig = CosSignal(freq=440, amp=1.0, offset=0)
sin_sig = SinSignal(freq=880, amp=0.5, offset=0)
oadd = SinSignal(freq=500, amp=0.7, offset=0)
mix = sin_sig + cos_sig + oadd
cos_sig.plot()
decorate(xlabel='cos_sig')
sin_sig.plot()
decorate(xlabel='sin_sig')
mix.plot()
decorate(xlabel='mix')
wave = mix.make_wave(duration=5, start=0, framerate=11025)
wave.play('temp.wav')
spectrum = wave.make_spectrum()
spectrum.plot()
decorate(xlabel='Frequency (Hz)')
