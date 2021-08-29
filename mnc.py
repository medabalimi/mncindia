#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 09:55:11 2021

@author: anand
"""
import json
import os
artifactdb='artifacts/cellular.json'


if os.path.isfile(artifactdb):
    mobdict=json.load(open(artifactdb,'r'))
else:
    mobdict=None

def __init__json__(mobile:str,circle:str,mnc:str):
    """
    

    Parameters
    ----------
    mobile : TYPE
        DESCRIPTION.
    state : TYPE
        DESCRIPTION.
    mnc : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
    with open(mobile,'r') as mobf, \
         open(circle, 'r') as circf, \
         open(mnc,'r') as mncf:
             
        #Read mnc
        mncdict = {k.strip('"'):v.strip('"') for k,v in \
                   [line.strip('\n').split(';', maxsplit=1) for line in mncf] }
        
        circdict = {k.strip('"'):v.strip('"') for v,k in \
                   [line.strip('\n').split(';', maxsplit=1) for line in circf] }
        
        mobdict=dict()
        for line in mobf:
            num, mnc, circ= line.strip('\n').split(';',maxsplit=2)
            num = num.strip('"')
            mnc = mnc.strip('"')
            circ = circ.strip('"')
            if num not in mobdict:
                mobdict[num]=[]
            mobdict[num].append({'mnc': mncdict.get(mnc,mnc), 
                          'circle':circdict.get(circ,circ)})
        with open(artifactdb,'w') as artf:
            json.dump(mobdict, artf)
        


def get_info(mobile_number:str):
    assert mobile_number.isdigit()
    mobinfo=mobdict.get(mobile_number[0:4], {'mnc': None, 'circle': None})
    return mobinfo

    
    
    
        