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
    
    game_state = []
    for index, row in data.iterrows():
        if row[balls]==0 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(1)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(2)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(3)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(4)
    
        elif row[balls]==0 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(5)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(6)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(7)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(8)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(9)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(10)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(11)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(12)
            
        elif row[balls]==0 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(13)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(14)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(15)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(16)
        
        elif row[balls]==0 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(17)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(18)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(19)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(20)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(21)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(22)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(23)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(24)
            
        elif row[balls]==0 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(25)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(26)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(27)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(28)
        
        elif row[balls]==0 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(29)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(30)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(31)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(32)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(33)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(34)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(35)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(36)
            
        elif row[balls]==0 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(37)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(38)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(39)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(40)
        
        elif row[balls]==0 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(41)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(42)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(43)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(44)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(45)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(46)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(47)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(48)
            
        elif row[balls]==0 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(49)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(50)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(51)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(52)
        
        elif row[balls]==0 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(53)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(54)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(55)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(56)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(57)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(58)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(59)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(60)
            
        elif row[balls]==0 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(61)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(62)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(63)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(64)
        
        elif row[balls]==0 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(65)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(66)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(67)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(68)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(69)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(70)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(71)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]==0.0:
            game_state.append(72)
        
        elif row[balls]==0 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(73)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(74)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(75)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(76)
        
        elif row[balls]==0 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(77)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(78)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(79)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(80)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(81)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(82)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(83)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(84)
            
        elif row[balls]==0 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(85)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(86)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(87)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(88)
        
        elif row[balls]==0 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(89)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(90)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(91)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(92)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(93)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(94)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(95)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(96)
            
        elif row[balls]==0 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(97)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(98)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(99)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(100)
        
        elif row[balls]==0 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(101)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(102)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(103)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(104)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(105)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(106)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(107)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(108)
            
        elif row[balls]==0 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(109)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(110)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(111)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(112)
        
        elif row[balls]==0 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(113)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(114)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(115)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(116)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(117)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(118)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(119)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(120)
            
        elif row[balls]==0 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(121)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(122)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(123)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(124)
        
        elif row[balls]==0 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(125)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(126)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(127)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(128)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(129)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(130)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(131)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(132)
            
        elif row[balls]==0 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(133)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(134)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(135)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(136)
        
        elif row[balls]==0 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(137)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(138)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(139)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(140)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(141)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(142)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(143)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(144)
            
        elif row[balls]==0 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(145)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(146)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(147)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(148)
        
        elif row[balls]==0 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(149)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(150)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(151)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(152)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(153)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(154)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(155)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(156)
            
        elif row[balls]==0 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(157)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(158)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(159)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(160)
        
        elif row[balls]==0 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(161)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(162)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(163)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(164)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(165)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(166)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(167)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(168)
            
        elif row[balls]==0 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(169)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(170)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(171)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(172)
        
        elif row[balls]==0 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(173)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(174)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(175)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(176)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(177)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(178)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(179)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]==0.0:
            game_state.append(180)
            
        elif row[balls]==0 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(181)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(182)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(183)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(184)
        
        elif row[balls]==0 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(185)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(186)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(187)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(188)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(189)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(190)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(191)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(192)
            
        elif row[balls]==0 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(193)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(194)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(195)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(196)
        
        elif row[balls]==0 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(197)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(198)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(199)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(200)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(201)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(202)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(203)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(204)
            
        elif row[balls]==0 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(205)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(206)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(207)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(208)
        
        elif row[balls]==0 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(209)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(210)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(211)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(212)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(213)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(214)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(215)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]==0.0 and row[runner_third]>0.0:
            game_state.append(216)
            
        elif row[balls]==0 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(217)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(218)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(219)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(220)
        
        elif row[balls]==0 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(221)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(222)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(223)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(224)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(225)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(226)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(227)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(228)
            
        elif row[balls]==0 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(229)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(230)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(231)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(232)
        
        elif row[balls]==0 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(233)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(234)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(235)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(236)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(237)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(238)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(239)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(240)
            
        elif row[balls]==0 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(241)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(242)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(243)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(244)
        
        elif row[balls]==0 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(245)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(246)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(247)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(248)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(249)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(250)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(251)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]==0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(252)
            
        elif row[balls]==0 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(253)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(254)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(255)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(256)
        
        elif row[balls]==0 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(257)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(258)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(259)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(260)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(261)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(262)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(263)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==0 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(264)
            
        elif row[balls]==0 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(265)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(266)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(267)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(268)
        
        elif row[balls]==0 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(269)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(270)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(271)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(272)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(273)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(274)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(275)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==1 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(276)
            
        elif row[balls]==0 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(277)
        elif row[balls]==1 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(278)
        elif row[balls]==2 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(279)
        elif row[balls]==3 and row[strikes]==0 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(280)
        
        elif row[balls]==0 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(281)
        elif row[balls]==1 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(282)
        elif row[balls]==2 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(283)
        elif row[balls]==3 and row[strikes]==1 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(284)
            
        elif row[balls]==0 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(285)
        elif row[balls]==1 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(286)
        elif row[balls]==2 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(287)
        elif row[balls]==3 and row[strikes]==2 and row[outs]==2 and \
            row[runner_first]>0.0 and row[runner_second]>0.0 and row[runner_third]>0.0:
            game_state.append(288)
    
    return game_state