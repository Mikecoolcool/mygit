from thinkdsp import read_wave

wave = read_wave('170255__dublie__trumpet.wav')
segment2 = wave.segment(start=1.1, duration=0.3)
spectrum = wave.make_spectrum()
spectrum.low_pass(2000)
#pectrum.high_pass(5000)
spectrum.band_stop(2000,5000)
wave2 = spectrum.make_wave()

wave2.play('temp.wav')