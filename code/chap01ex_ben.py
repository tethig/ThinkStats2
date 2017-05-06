#!/usr/local/env python
#Ben solves CH1_Q2
'''
from __future__ import print_function, division

import sys
import numpy as np
import thinkstats2

from collections import defaultdict
'''

import nsfg

# datasets
resp = nsfg.ReadFemResp()
preg = nsfg.ReadFemPreg()

# sorted pregnancy counts
print resp.pregnum.value_counts().sort_index()

# make preg_map
preg_map = nsfg.MakePregMap(preg)

# cross-validation
for caseid in resp.caseid:
    births_resp = resp.pregnum[resp.caseid==caseid]
    indices = preg_map[caseid]
    births_preg = len(preg.outcome[indices].values) # could be any variable
    print int(births_resp), births_preg
    assert int(births_resp) == births_preg

print('Tests passed.')
