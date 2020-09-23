# Recreate work from APF Tutorial with amp193
import numpy as np
import pyfits as pf
import matplotlib
from matplotlib import pyplot as plt
import lmfit
from lmfit import minimize, Parameters, report_fit, fit_report
from IPython.display import Image

apf_file = pf.open('ucb-amp193.fits copy')
