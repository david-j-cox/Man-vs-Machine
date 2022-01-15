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

def RE288_calc(balls, strikes, outs, runner_first, runner_second, runner_third):
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
    if balls==0 and strikes==0 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=1
    elif balls==1 and strikes==0 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=2
    elif balls==2 and strikes==0 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=3
    elif balls==3 and strikes==0 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=4

    elif balls==0 and strikes==1 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=5
    elif balls==1 and strikes==1 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=6
    elif balls==2 and strikes==1 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=7
    elif balls==3 and strikes==1 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=8
        
    elif balls==0 and strikes==2 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=9
    elif balls==1 and strikes==2 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=10
    elif balls==2 and strikes==2 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=11
    elif balls==3 and strikes==2 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=12
        
    elif balls==0 and strikes==0 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=13
    elif balls==1 and strikes==0 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=14
    elif balls==2 and strikes==0 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=15
    elif balls==3 and strikes==0 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=16
    
    elif balls==0 and strikes==1 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=17
    elif balls==1 and strikes==1 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=18
    elif balls==2 and strikes==1 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=19
    elif balls==3 and strikes==1 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=20
        
    elif balls==0 and strikes==2 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=21
    elif balls==1 and strikes==2 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=22
    elif balls==2 and strikes==2 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=23
    elif balls==3 and strikes==2 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=24
        
    elif balls==0 and strikes==0 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=25
    elif balls==1 and strikes==0 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=26
    elif balls==2 and strikes==0 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=27
    elif balls==3 and strikes==0 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=28
    
    elif balls==0 and strikes==1 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=29
    elif balls==1 and strikes==1 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=30
    elif balls==2 and strikes==1 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=31
    elif balls==3 and strikes==1 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=32
        
    elif balls==0 and strikes==2 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=33
    elif balls==1 and strikes==2 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=34
    elif balls==2 and strikes==2 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=35
    elif balls==3 and strikes==2 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=36
        
    elif balls==0 and strikes==0 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=37
    elif balls==1 and strikes==0 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=38
    elif balls==2 and strikes==0 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=39
    elif balls==3 and strikes==0 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=40
    
    elif balls==0 and strikes==1 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=41
    elif balls==1 and strikes==1 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=42
    elif balls==2 and strikes==1 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=43
    elif balls==3 and strikes==1 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=44
        
    elif balls==0 and strikes==2 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=45
    elif balls==1 and strikes==2 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=46
    elif balls==2 and strikes==2 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=47
    elif balls==3 and strikes==2 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=48
        
    elif balls==0 and strikes==0 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=49
    elif balls==1 and strikes==0 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=50
    elif balls==2 and strikes==0 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=51
    elif balls==3 and strikes==0 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=52
    
    elif balls==0 and strikes==1 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=53
    elif balls==1 and strikes==1 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=54
    elif balls==2 and strikes==1 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=55
    elif balls==3 and strikes==1 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=56
        
    elif balls==0 and strikes==2 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=57
    elif balls==1 and strikes==2 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=58
    elif balls==2 and strikes==2 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=59
    elif balls==3 and strikes==2 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=60
        
    elif balls==0 and strikes==0 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=61
    elif balls==1 and strikes==0 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=62
    elif balls==2 and strikes==0 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=63
    elif balls==3 and strikes==0 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=64
    
    elif balls==0 and strikes==1 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=65
    elif balls==1 and strikes==1 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=66
    elif balls==2 and strikes==1 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=67
    elif balls==3 and strikes==1 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=68
        
    elif balls==0 and strikes==2 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=69
    elif balls==1 and strikes==2 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=70
    elif balls==2 and strikes==2 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=71
    elif balls==3 and strikes==2 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third==0.0:
        game_state=72
    
    elif balls==0 and strikes==0 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=73
    elif balls==1 and strikes==0 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=74
    elif balls==2 and strikes==0 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=75
    elif balls==3 and strikes==0 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=76
    
    elif balls==0 and strikes==1 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=77
    elif balls==1 and strikes==1 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=78
    elif balls==2 and strikes==1 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=79
    elif balls==3 and strikes==1 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=80
        
    elif balls==0 and strikes==2 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=81
    elif balls==1 and strikes==2 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=82
    elif balls==2 and strikes==2 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=83
    elif balls==3 and strikes==2 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=84
        
    elif balls==0 and strikes==0 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=85
    elif balls==1 and strikes==0 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=86
    elif balls==2 and strikes==0 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=87
    elif balls==3 and strikes==0 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=88
    
    elif balls==0 and strikes==1 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=89
    elif balls==1 and strikes==1 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=90
    elif balls==2 and strikes==1 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=91
    elif balls==3 and strikes==1 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=92
        
    elif balls==0 and strikes==2 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=93
    elif balls==1 and strikes==2 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=94
    elif balls==2 and strikes==2 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=95
    elif balls==3 and strikes==2 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=96
        
    elif balls==0 and strikes==0 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=97
    elif balls==1 and strikes==0 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=98
    elif balls==2 and strikes==0 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=99
    elif balls==3 and strikes==0 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=100
    
    elif balls==0 and strikes==1 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=101
    elif balls==1 and strikes==1 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=102
    elif balls==2 and strikes==1 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=103
    elif balls==3 and strikes==1 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=104
        
    elif balls==0 and strikes==2 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=105
    elif balls==1 and strikes==2 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=106
    elif balls==2 and strikes==2 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=107
    elif balls==3 and strikes==2 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=108
        
    elif balls==0 and strikes==0 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=109
    elif balls==1 and strikes==0 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=110
    elif balls==2 and strikes==0 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=111
    elif balls==3 and strikes==0 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=112
    
    elif balls==0 and strikes==1 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=113
    elif balls==1 and strikes==1 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=114
    elif balls==2 and strikes==1 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=115
    elif balls==3 and strikes==1 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=116
        
    elif balls==0 and strikes==2 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=117
    elif balls==1 and strikes==2 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=118
    elif balls==2 and strikes==2 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=119
    elif balls==3 and strikes==2 and outs==0 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=120
        
    elif balls==0 and strikes==0 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=121
    elif balls==1 and strikes==0 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=122
    elif balls==2 and strikes==0 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=123
    elif balls==3 and strikes==0 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=124
    
    elif balls==0 and strikes==1 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=125
    elif balls==1 and strikes==1 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=126
    elif balls==2 and strikes==1 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=127
    elif balls==3 and strikes==1 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=128
        
    elif balls==0 and strikes==2 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=129
    elif balls==1 and strikes==2 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=130
    elif balls==2 and strikes==2 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=131
    elif balls==3 and strikes==2 and outs==1 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=132
        
    elif balls==0 and strikes==0 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=133
    elif balls==1 and strikes==0 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=134
    elif balls==2 and strikes==0 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=135
    elif balls==3 and strikes==0 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=136
    
    elif balls==0 and strikes==1 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=137
    elif balls==1 and strikes==1 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=138
    elif balls==2 and strikes==1 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=139
    elif balls==3 and strikes==1 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=140
        
    elif balls==0 and strikes==2 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=141
    elif balls==1 and strikes==2 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=142
    elif balls==2 and strikes==2 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=143
    elif balls==3 and strikes==2 and outs==2 and \
        runner_first==0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=144
        
    elif balls==0 and strikes==0 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=145
    elif balls==1 and strikes==0 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=146
    elif balls==2 and strikes==0 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=147
    elif balls==3 and strikes==0 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=148
    
    elif balls==0 and strikes==1 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=149
    elif balls==1 and strikes==1 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=150
    elif balls==2 and strikes==1 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=151
    elif balls==3 and strikes==1 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=152
        
    elif balls==0 and strikes==2 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=153
    elif balls==1 and strikes==2 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=154
    elif balls==2 and strikes==2 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=155
    elif balls==3 and strikes==2 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=156
        
    elif balls==0 and strikes==0 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=157
    elif balls==1 and strikes==0 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=158
    elif balls==2 and strikes==0 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=159
    elif balls==3 and strikes==0 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=160
    
    elif balls==0 and strikes==1 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=161
    elif balls==1 and strikes==1 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=162
    elif balls==2 and strikes==1 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=163
    elif balls==3 and strikes==1 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=164
        
    elif balls==0 and strikes==2 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=165
    elif balls==1 and strikes==2 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=166
    elif balls==2 and strikes==2 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=167
    elif balls==3 and strikes==2 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=168
        
    elif balls==0 and strikes==0 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=169
    elif balls==1 and strikes==0 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=170
    elif balls==2 and strikes==0 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=171
    elif balls==3 and strikes==0 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=172
    
    elif balls==0 and strikes==1 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=173
    elif balls==1 and strikes==1 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=174
    elif balls==2 and strikes==1 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=175
    elif balls==3 and strikes==1 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=176
        
    elif balls==0 and strikes==2 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=177
    elif balls==1 and strikes==2 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=178
    elif balls==2 and strikes==2 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=179
    elif balls==3 and strikes==2 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third==0.0:
        game_state=180
        
    elif balls==0 and strikes==0 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=181
    elif balls==1 and strikes==0 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=182
    elif balls==2 and strikes==0 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=183
    elif balls==3 and strikes==0 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=184
    
    elif balls==0 and strikes==1 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=185
    elif balls==1 and strikes==1 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=186
    elif balls==2 and strikes==1 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=187
    elif balls==3 and strikes==1 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=188
        
    elif balls==0 and strikes==2 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=189
    elif balls==1 and strikes==2 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=190
    elif balls==2 and strikes==2 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=191
    elif balls==3 and strikes==2 and outs==0 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=192
        
    elif balls==0 and strikes==0 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=193
    elif balls==1 and strikes==0 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=194
    elif balls==2 and strikes==0 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=195
    elif balls==3 and strikes==0 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=196
    
    elif balls==0 and strikes==1 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=197
    elif balls==1 and strikes==1 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=198
    elif balls==2 and strikes==1 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=199
    elif balls==3 and strikes==1 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=200
        
    elif balls==0 and strikes==2 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=201
    elif balls==1 and strikes==2 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=202
    elif balls==2 and strikes==2 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=203
    elif balls==3 and strikes==2 and outs==1 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=204
        
    elif balls==0 and strikes==0 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=205
    elif balls==1 and strikes==0 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=206
    elif balls==2 and strikes==0 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=207
    elif balls==3 and strikes==0 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=208
    
    elif balls==0 and strikes==1 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=209
    elif balls==1 and strikes==1 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=210
    elif balls==2 and strikes==1 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=211
    elif balls==3 and strikes==1 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=212
        
    elif balls==0 and strikes==2 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=213
    elif balls==1 and strikes==2 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=214
    elif balls==2 and strikes==2 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=215
    elif balls==3 and strikes==2 and outs==2 and \
        runner_first>0.0 and runner_second==0.0 and runner_third>0.0:
        game_state=216
        
    elif balls==0 and strikes==0 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=217
    elif balls==1 and strikes==0 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=218
    elif balls==2 and strikes==0 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=219
    elif balls==3 and strikes==0 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=220
    
    elif balls==0 and strikes==1 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=221
    elif balls==1 and strikes==1 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=222
    elif balls==2 and strikes==1 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=223
    elif balls==3 and strikes==1 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=224
        
    elif balls==0 and strikes==2 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=225
    elif balls==1 and strikes==2 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=226
    elif balls==2 and strikes==2 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=227
    elif balls==3 and strikes==2 and outs==0 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=228
        
    elif balls==0 and strikes==0 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=229
    elif balls==1 and strikes==0 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=230
    elif balls==2 and strikes==0 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=231
    elif balls==3 and strikes==0 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=232
    
    elif balls==0 and strikes==1 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=233
    elif balls==1 and strikes==1 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=234
    elif balls==2 and strikes==1 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=235
    elif balls==3 and strikes==1 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=236
        
    elif balls==0 and strikes==2 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=237
    elif balls==1 and strikes==2 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=238
    elif balls==2 and strikes==2 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=239
    elif balls==3 and strikes==2 and outs==1 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=240
        
    elif balls==0 and strikes==0 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=241
    elif balls==1 and strikes==0 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=242
    elif balls==2 and strikes==0 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=243
    elif balls==3 and strikes==0 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=244
    
    elif balls==0 and strikes==1 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=245
    elif balls==1 and strikes==1 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=246
    elif balls==2 and strikes==1 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=247
    elif balls==3 and strikes==1 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=248
        
    elif balls==0 and strikes==2 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=249
    elif balls==1 and strikes==2 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=250
    elif balls==2 and strikes==2 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=251
    elif balls==3 and strikes==2 and outs==2 and \
        runner_first==0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=252
        
    elif balls==0 and strikes==0 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=253
    elif balls==1 and strikes==0 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=254
    elif balls==2 and strikes==0 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=255
    elif balls==3 and strikes==0 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=256
    
    elif balls==0 and strikes==1 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=257
    elif balls==1 and strikes==1 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=258
    elif balls==2 and strikes==1 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=259
    elif balls==3 and strikes==1 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=260
        
    elif balls==0 and strikes==2 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=261
    elif balls==1 and strikes==2 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=262
    elif balls==2 and strikes==2 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=263
    elif balls==3 and strikes==2 and outs==0 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=264
        
    elif balls==0 and strikes==0 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=265
    elif balls==1 and strikes==0 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=266
    elif balls==2 and strikes==0 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=267
    elif balls==3 and strikes==0 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=268
    
    elif balls==0 and strikes==1 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=269
    elif balls==1 and strikes==1 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=270
    elif balls==2 and strikes==1 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=271
    elif balls==3 and strikes==1 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=272
        
    elif balls==0 and strikes==2 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=273
    elif balls==1 and strikes==2 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=274
    elif balls==2 and strikes==2 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=275
    elif balls==3 and strikes==2 and outs==1 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=276
        
    elif balls==0 and strikes==0 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=277
    elif balls==1 and strikes==0 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=278
    elif balls==2 and strikes==0 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=279
    elif balls==3 and strikes==0 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=280
    
    elif balls==0 and strikes==1 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=281
    elif balls==1 and strikes==1 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=282
    elif balls==2 and strikes==1 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=283
    elif balls==3 and strikes==1 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=284
        
    elif balls==0 and strikes==2 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=285
    elif balls==1 and strikes==2 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=286
    elif balls==2 and strikes==2 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=287
    elif balls==3 and strikes==2 and outs==2 and \
        runner_first>0.0 and runner_second>0.0 and runner_third>0.0:
        game_state=288
    
    return game_state