# Imports padrões 
import numpy as np
import matplotlib.pyplot as plt

# Funções para leitura e escrita de arquivos .WAV
## Atenção: 
# Arquivos .WAV fornecidos são codificados como inteiros 
# de 16-bit (int16), variando de -32768 a +32767. 
# Para sua reprodução correta, o vetor passado na função 
# write deve conter elementos do tipo np.int16 
#
# Exemplo: 
#         taxa_de_amostragem, x = read("audio.wav")
#         write("vetor_x.wav", taxa_de_amostragem, x.astype(np.int16))
#
from scipy.io.wavfile import read, write

# Funções para calcular a transformada de Fourier discreta
from numpy.fft import fft, ifft, fftfreq, fftshift

# Caso esteja em ambiente Jupyter, função útil para reproduzir 
# um vetor via Jupyter widgets no próprio notebook.
#
# Exemplo:
#         play(x, rate=taxa_de_amostragem)
#
from IPython.display import Audio as play

# Extra:
# Função auxiliar para plotagem de um vetor no domínio da frequência em dB
def spectrum(x_freq):
# 
# x_freq: vetor no domínio da frequência, complexo
#
    x_magnitude = np.abs(x)
    # Normalização para o valor máximo ser 0dB
    x_magnitude /= np.max(x_magnitude)
    return 20*np.log10(x_magnitude)


