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

def RE24_calc(data, outs, runner_first, runner_second, runner_third):
    """Assigns game state number dependent on the unique state of the baseball
    game at the time a pitch is thrown. RE288 uses all possible combinations of
    balls (0-3), strikes (0-2), outs (0-2), and runners on bases (1-3). This leads
    to 288 possible game states. 
    data = name of dataframe
    balls = column containing number of balls when pitch thrown; should be integer 0,1,2,3
    strikes = column containing number of strikes when pitch thrown; should be integer 0, 1, 2
    outs = column containing number of outs when pitch thrown; should be integer 0, 1, 2
    runner_first = column containing whether a runner is on first base; 0 = no runner, 1 = runner
    runner_second = column containing whether a runner is on first base; 0 = no runner, 1 = runner
    runner_third = column containing whether a runner is on first base; 0 = no runner, 1 = runner
    """
    
    game_state = []
    for index, row in data.iterrows():
        if row[outs]==0 and row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(1)
        elif row[outs]==1 and row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(2)
        elif row[outs]==2 and row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(3)

        if row[outs]==0 and row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(1)
        elif row[outs]==1 and row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(2)
        elif row[outs]==2 and row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(3)

        if row[outs]==0 and row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(1)
        elif row[outs]==1 and row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(2)
        elif row[outs]==2 and row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(3)

        if row[outs]==0 and row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(1)
        elif row[outs]==1 and row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(2)
        elif row[outs]==2 and row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(3)

        if row[outs]==0 and row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(1)
        elif row[outs]==1 and row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(2)
        elif row[outs]==2 and row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(3)

        if row[outs]==0 and row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(1)
        elif row[outs]==1 and row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(2)
        elif row[outs]==2 and row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(3)

        if row[outs]==0 and row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(1)
        elif row[outs]==1 and row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(2)
        elif row[outs]==2 and row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(3)

        if row[outs]==0 and row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>.0:
            game_state.append(1)
        elif row[outs]==1 and row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(2)
        elif row[outs]==2 and row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(3)
    
    return game_state