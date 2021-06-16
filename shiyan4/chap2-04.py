from thinkdsp import TriangleSignal, decorate

triangle = TriangleSignal().make_wave(duration=0.01)
triangle.plot()
decorate(xlabel='Time (s)')

spectrum = triangle.make_spectrum()
spectrum.hs[0]

spectrum.hs[0] = 100
triangle.plot(color='gray')
spectrum.make_wave().plot()
decorate(xlabel='Time (s)')