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

def RE288_calc(data, balls, strikes, outs, runner_first, runner_second, runner_third):
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
    
    game_state = 'none'
    if row[balls]==0 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=1
    elif row[balls]==1 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=2
    elif row[balls]==2 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=3
    elif row[balls]==3 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=4

    elif row[balls]==0 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=5
    elif row[balls]==1 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=6
    elif row[balls]==2 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=7
    elif row[balls]==3 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=8
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=9
    elif row[balls]==1 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=10
    elif row[balls]==2 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=11
    elif row[balls]==3 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=12
        
    elif row[balls]==0 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=13
    elif row[balls]==1 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=14
    elif row[balls]==2 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=15
    elif row[balls]==3 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=16
    
    elif row[balls]==0 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=17
    elif row[balls]==1 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=18
    elif row[balls]==2 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=19
    elif row[balls]==3 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=20
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=21
    elif row[balls]==1 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=22
    elif row[balls]==2 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=23
    elif row[balls]==3 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=24
        
    elif row[balls]==0 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=25
    elif row[balls]==1 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=26
    elif row[balls]==2 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=27
    elif row[balls]==3 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=28
    
    elif row[balls]==0 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=29
    elif row[balls]==1 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=30
    elif row[balls]==2 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=31
    elif row[balls]==3 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=32
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=33
    elif row[balls]==1 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=34
    elif row[balls]==2 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=35
    elif row[balls]==3 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=36
        
    elif row[balls]==0 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=37
    elif row[balls]==1 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=38
    elif row[balls]==2 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=39
    elif row[balls]==3 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=40
    
    elif row[balls]==0 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=41
    elif row[balls]==1 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=42
    elif row[balls]==2 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=43
    elif row[balls]==3 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=44
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=45
    elif row[balls]==1 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=46
    elif row[balls]==2 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=47
    elif row[balls]==3 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=48
        
    elif row[balls]==0 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=49
    elif row[balls]==1 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=50
    elif row[balls]==2 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=51
    elif row[balls]==3 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=52
    
    elif row[balls]==0 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=53
    elif row[balls]==1 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=54
    elif row[balls]==2 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=55
    elif row[balls]==3 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=56
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=57
    elif row[balls]==1 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=58
    elif row[balls]==2 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=59
    elif row[balls]==3 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=60
        
    elif row[balls]==0 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=61
    elif row[balls]==1 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=62
    elif row[balls]==2 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=63
    elif row[balls]==3 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=64
    
    elif row[balls]==0 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=65
    elif row[balls]==1 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=66
    elif row[balls]==2 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=67
    elif row[balls]==3 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=68
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=69
    elif row[balls]==1 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=70
    elif row[balls]==2 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=71
    elif row[balls]==3 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
        game_state=72
    
    elif row[balls]==0 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=73
    elif row[balls]==1 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=74
    elif row[balls]==2 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=75
    elif row[balls]==3 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=76
    
    elif row[balls]==0 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=77
    elif row[balls]==1 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=78
    elif row[balls]==2 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=79
    elif row[balls]==3 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=80
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=81
    elif row[balls]==1 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=82
    elif row[balls]==2 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=83
    elif row[balls]==3 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=84
        
    elif row[balls]==0 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=85
    elif row[balls]==1 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=86
    elif row[balls]==2 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=87
    elif row[balls]==3 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=88
    
    elif row[balls]==0 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=89
    elif row[balls]==1 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=90
    elif row[balls]==2 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=91
    elif row[balls]==3 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=92
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=93
    elif row[balls]==1 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=94
    elif row[balls]==2 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=95
    elif row[balls]==3 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=96
        
    elif row[balls]==0 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=97
    elif row[balls]==1 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=98
    elif row[balls]==2 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=99
    elif row[balls]==3 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=100
    
    elif row[balls]==0 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=101
    elif row[balls]==1 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=102
    elif row[balls]==2 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=103
    elif row[balls]==3 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=104
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=105
    elif row[balls]==1 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=106
    elif row[balls]==2 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=107
    elif row[balls]==3 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=108
        
    elif row[balls]==0 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=109
    elif row[balls]==1 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=110
    elif row[balls]==2 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=111
    elif row[balls]==3 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=112
    
    elif row[balls]==0 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=113
    elif row[balls]==1 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=114
    elif row[balls]==2 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=115
    elif row[balls]==3 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=116
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=117
    elif row[balls]==1 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=118
    elif row[balls]==2 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=119
    elif row[balls]==3 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=120
        
    elif row[balls]==0 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=121
    elif row[balls]==1 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=122
    elif row[balls]==2 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=123
    elif row[balls]==3 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=124
    
    elif row[balls]==0 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=125
    elif row[balls]==1 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=126
    elif row[balls]==2 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=127
    elif row[balls]==3 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=128
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=129
    elif row[balls]==1 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=130
    elif row[balls]==2 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=131
    elif row[balls]==3 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=132
        
    elif row[balls]==0 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=133
    elif row[balls]==1 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=134
    elif row[balls]==2 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=135
    elif row[balls]==3 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=136
    
    elif row[balls]==0 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=137
    elif row[balls]==1 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=138
    elif row[balls]==2 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=139
    elif row[balls]==3 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=140
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=141
    elif row[balls]==1 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=142
    elif row[balls]==2 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=143
    elif row[balls]==3 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=144
        
    elif row[balls]==0 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=145
    elif row[balls]==1 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=146
    elif row[balls]==2 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=147
    elif row[balls]==3 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=148
    
    elif row[balls]==0 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=149
    elif row[balls]==1 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=150
    elif row[balls]==2 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=151
    elif row[balls]==3 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=152
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=153
    elif row[balls]==1 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=154
    elif row[balls]==2 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=155
    elif row[balls]==3 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=156
        
    elif row[balls]==0 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=157
    elif row[balls]==1 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=158
    elif row[balls]==2 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=159
    elif row[balls]==3 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=160
    
    elif row[balls]==0 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=161
    elif row[balls]==1 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=162
    elif row[balls]==2 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=163
    elif row[balls]==3 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=164
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=165
    elif row[balls]==1 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=166
    elif row[balls]==2 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=167
    elif row[balls]==3 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=168
        
    elif row[balls]==0 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=169
    elif row[balls]==1 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=170
    elif row[balls]==2 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=171
    elif row[balls]==3 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=172
    
    elif row[balls]==0 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=173
    elif row[balls]==1 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=174
    elif row[balls]==2 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=175
    elif row[balls]==3 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=176
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=177
    elif row[balls]==1 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=178
    elif row[balls]==2 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=179
    elif row[balls]==3 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
        game_state=180
        
    elif row[balls]==0 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=181
    elif row[balls]==1 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=182
    elif row[balls]==2 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=183
    elif row[balls]==3 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=184
    
    elif row[balls]==0 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=185
    elif row[balls]==1 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=186
    elif row[balls]==2 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=187
    elif row[balls]==3 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=188
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=189
    elif row[balls]==1 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=190
    elif row[balls]==2 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=191
    elif row[balls]==3 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=192
        
    elif row[balls]==0 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=193
    elif row[balls]==1 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=194
    elif row[balls]==2 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=195
    elif row[balls]==3 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=196
    
    elif row[balls]==0 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=197
    elif row[balls]==1 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=198
    elif row[balls]==2 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=199
    elif row[balls]==3 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=200
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=201
    elif row[balls]==1 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=202
    elif row[balls]==2 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=203
    elif row[balls]==3 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=204
        
    elif row[balls]==0 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=205
    elif row[balls]==1 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=206
    elif row[balls]==2 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=207
    elif row[balls]==3 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=208
    
    elif row[balls]==0 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=209
    elif row[balls]==1 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=210
    elif row[balls]==2 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=211
    elif row[balls]==3 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=212
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=213
    elif row[balls]==1 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=214
    elif row[balls]==2 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=215
    elif row[balls]==3 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
        game_state=216
        
    elif row[balls]==0 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=217
    elif row[balls]==1 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=218
    elif row[balls]==2 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=219
    elif row[balls]==3 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=220
    
    elif row[balls]==0 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=221
    elif row[balls]==1 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=222
    elif row[balls]==2 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=223
    elif row[balls]==3 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=224
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=225
    elif row[balls]==1 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=226
    elif row[balls]==2 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=227
    elif row[balls]==3 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=228
        
    elif row[balls]==0 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=229
    elif row[balls]==1 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=230
    elif row[balls]==2 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=231
    elif row[balls]==3 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=232
    
    elif row[balls]==0 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=233
    elif row[balls]==1 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=234
    elif row[balls]==2 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=235
    elif row[balls]==3 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=236
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=237
    elif row[balls]==1 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=238
    elif row[balls]==2 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=239
    elif row[balls]==3 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=240
        
    elif row[balls]==0 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=241
    elif row[balls]==1 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=242
    elif row[balls]==2 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=243
    elif row[balls]==3 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=244
    
    elif row[balls]==0 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=245
    elif row[balls]==1 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=246
    elif row[balls]==2 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=247
    elif row[balls]==3 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=248
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=249
    elif row[balls]==1 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=250
    elif row[balls]==2 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=251
    elif row[balls]==3 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=252
        
    elif row[balls]==0 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=253
    elif row[balls]==1 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=254
    elif row[balls]==2 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=255
    elif row[balls]==3 and row[strikes]==0 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=256
    
    elif row[balls]==0 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=257
    elif row[balls]==1 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=258
    elif row[balls]==2 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=259
    elif row[balls]==3 and row[strikes]==1 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=260
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=261
    elif row[balls]==1 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=262
    elif row[balls]==2 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=263
    elif row[balls]==3 and row[strikes]==2 and row[outs]==0 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=264
        
    elif row[balls]==0 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=265
    elif row[balls]==1 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=266
    elif row[balls]==2 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=267
    elif row[balls]==3 and row[strikes]==0 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=268
    
    elif row[balls]==0 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=269
    elif row[balls]==1 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=270
    elif row[balls]==2 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=271
    elif row[balls]==3 and row[strikes]==1 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=272
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=273
    elif row[balls]==1 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=274
    elif row[balls]==2 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=275
    elif row[balls]==3 and row[strikes]==2 and row[outs]==1 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=276
        
    elif row[balls]==0 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=277
    elif row[balls]==1 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=278
    elif row[balls]==2 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=279
    elif row[balls]==3 and row[strikes]==0 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=280
    
    elif row[balls]==0 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=281
    elif row[balls]==1 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=282
    elif row[balls]==2 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=283
    elif row[balls]==3 and row[strikes]==1 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=284
        
    elif row[balls]==0 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=285
    elif row[balls]==1 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=286
    elif row[balls]==2 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=287
    elif row[balls]==3 and row[strikes]==2 and row[outs]==2 and \
        row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
        game_state=288
    
    return game_state