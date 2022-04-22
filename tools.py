#Setup

# Install Packages
import sys
from sklearn import preprocessing
import os, requests
import numpy as np
import pandas as pd


# Data Retrieval
def get_patient(patient = 2):

    fname = 'joystick_track.npz'
    url = "https://osf.io/6jncm/download"

    if not os.path.isfile(fname):
      try:
        r = requests.get(url)
      except requests.ConnectionError:
        print("!!! Failed to download data !!!")
      else:
        if r.status_code != requests.codes.ok:
          print("!!! Failed to download data !!!")
        else:
          with open(fname, "wb") as fid:
            fid.write(r.content)


    # Data Loading
    alldat = np.load(fname, allow_pickle=True)['dat']

    # Select just one of the recordings here. This is subject 1, block 1.
    dat = alldat[0, patient]
    
    return dat