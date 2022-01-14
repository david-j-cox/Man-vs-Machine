#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 
    David J. Cox, PhD, MSB, BCBA-D
    dcox33@jhmi.edu
    https://www.researchgate.net/profile/David_Cox26
    twitter: @davidjcox_
    LinkedIn: https://www.linkedin.com/in/coxdavidj/
    Website: https://davidjcox.xyz
"""

def RE24_calc(outs, runner_first, runner_second, runner_third):
    '''
    Assigns game state number dependent on the unique state of the baseball
    game at the time a pitch is thrown. RE288 uses all possible combinations of
    outs (0-2) and runners on bases (1-3). This leads to 24 possible game states.
    :param data: dataframe
    :param outs: column containing number of outs when pitch thrown; should be integer 0, 1, 2
    :param runner_first: column containing whether a runner is on first base; 0 = no runner, 1 = runner
    :param runner_second: column containing whether a runner is on first base; 0 = no runner, 1 = runner
    :param runner_third: column containing whether a runner is on first base; 0 = no runner, 1 = runner
    :return: run expectancy for that particular game state
    '''
    re24 = 'none'
    if outs==0 and runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        re24 = 0.461
    elif outs==1 and runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        re24 = 0.243
    elif outs==2 and runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        re24 = 0.095
    elif outs==0 and runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        re24 = 0.831
    elif outs==1 and runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        re24 = 0.489
    elif outs==2 and runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        re24 = 0.214

    elif outs==0 and runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        re24 = 1.068
    elif outs==1 and runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        re24 = 0.644
    elif outs==2 and runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        re24 = 0.305

    elif outs==0 and runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        re24 = 1.426
    elif outs==1 and runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        re24 = 0.865
    elif outs==2 and runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        re24 = 0.413

    elif outs==0 and runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        re24 = 1.373
    elif outs==1 and runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        re24 = 0.908
    elif outs==2 and runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        re24 = 0.343

    elif outs==0 and runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        re24 = 1.798
    elif outs==1 and runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        re24 = 1.14
    elif outs==2 and runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        re24 = 0.471

    elif outs==0 and runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        re24 = 1.92
    elif outs==1 and runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        re24 = 1.352
    elif outs==2 and runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        re24 = 0.57

    elif outs==0 and runner_first>0.0 and runner_second>0.0 and runner_third>.0:
        re24 = 2.282
    elif outs==1 and runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        re24 = 1.52
    elif outs==2 and runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        re24 = 0.736
    
    return re24
