from vetores import *

def test_angulo():
    assert anguloUV()

def test_BxT():
    assert BxT(0, -1/math.sqrt(2), 1/math.sqrt(2), -1/math.sqrt(3), 1/math.sqrt(3), 1/math.sqrt(3)) == np.around(-math.sqrt(2)/math.sqrt(3), 15)*N.i + np.around(-1/math.sqrt(6), 15)*N.j + np.around(-1/math.sqrt(6), 15)*N.k