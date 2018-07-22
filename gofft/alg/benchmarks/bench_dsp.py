import os
import sys
import numpy as np
from gofft.alg import (goertzel, goertzel_m, goertzel_st, goertzel_st_m, 
                       fft_eval, stfft_eval)
from gofft.bench import BenchmarkCase


class BenchDSP(BenchmarkCase):
    dir_data = os.path.join(os.getcwd(), 'data')

    def setup(self):
        """
        NOTE
        ----
        Desired frequency resolution is `fs / width = 1 (Hz)`.
        """
        fn = os.path.join(self.dir_data, 'rawecg.csv')
        self.data = np.loadtxt(fn, delimiter=',')

        self.enable_logging = True
        self.step = 100
        self.rd = 3

        self.fs = 1000
        self.ft = np.array([50, 60, 70])
        self.width = self.fs

    def time_goertzel(self, data):
        for f in self.ft:
            goertzel(data, self.fs, f, self.width)

    def time_goertzel_m(self, data):
        goertzel_m(data, self.fs, self.ft, self.width)

    def time_goertzel_st(self, data):
        for f in self.ft:
            goertzel_st(data, self.fs, f, self.width)

    def time_goertzel_st_m(self, data):
        goertzel_st_m(data, self.fs, self.ft, self.width)

    def time_fft_eval(self, data):
        fft_eval(data, self.fs, self.ft)

    def time_stfft_eval(self, data):
        stfft_eval(data, self.fs, self.ft, self.width)
