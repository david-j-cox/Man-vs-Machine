#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    David J. Cox, PhD, MSB, BCBA-D
    https://www.researchgate.net/profile/David_Cox26
    twitter: @davidjcox_
    LinkedIn: https://www.linkedin.com/in/coxdavidj/
    Website: https://davidjcox.xyz
"""
def fit_gme(df, bx_cols, sr_cols, session_col):
    '''
    The purpose of this function is to fit the generalized matching equation (Baum, 1974; McDowell, 2005) to a set
    of data passed to the function.
    :param df: the dataframe to be used for the analysis
    :param bx_cols: list of columns where each column contains one behavior of interest for the analysis
    :param sr_cols: list of columns where each column contains one reinforcer of interest for the analysis
    :param session_cols: column that contains the labels demarcating sessions from each other
    :return:
        - VAC: variance accounted for by the GME
        - residual_trend: Mann-Kendall test for trend in residuals
        - log_bias: estimated log-bias parameter using OLS linear regression to logged behavior and logged reinforcer ratios
        - sensitivity: estimated sensitivity parameter using OLS linear regression to logged behavior and logged reinforcer ratios
        - error_log: log of any exceptions that were raised when attempting to fir the GME to the dataset
    '''
    # Matching params at season level
    VAC = np.nan
    residual_trend = np.nan
    log_bias = np.nan
    sensitivity = np.nan
    err_type = []

    # Pull df for the target pitcher and break down by season
    import warnings
    warnings.filterwarnings("ignore")
    for i in range(len(uniq_p)):
        try:
            # Lists to store things in
            game_number = []
            year = []
            hard_straight_count = []
            hard_breaking_count = []
            soft_straight_count = []
            soft_breaking_count = []
            hard_straight_s_o = []
            hard_breaking_s_o = []
            soft_straight_s_o = []
            soft_breaking_s_o = []

            df = data[data['player_name' ]= =uniq_p[i]]

            for j in [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]:
                try:
                    df_year = df[df['game_year' ]= =j]
                    g_uniq = df_year['game_date'].unique()
                    if len(g_uniq) < 5:
                        continue
                    else:
                        gnum = 1
                        for k in g_uniq:
                            game_data = df_year[df_year['game_date' ]= =k]

                            if len(game_data) < 5:
                                pass
                            else:
                                # Create dfs for each pitch type
                                hard_straight = game_data.loc[game_data.pitch_name.isin(hrd_strt)]
                                hard_breaking = game_data.loc[game_data.pitch_name.isin(hrd_brkng)]
                                soft_straight = game_data.loc[game_data.pitch_name.isin(sft_strt)]
                                soft_breaking = game_data.loc[game_data.pitch_name.isin(sft_brkng)]

                                # Get the count of each pitch type per game
                                hstrt = len(hard_straight)
                                hbrk = len(hard_breaking)
                                sstrt = len(soft_straight)
                                sbrk = len(soft_breaking)

                                # Get the count of strikes/outs that followed each pitch type per game
                                hstrt_strike = len(hard_straight.loc[hard_straight.description.isin(s_o)])
                                hbrk_strike = len(hard_breaking.loc[hard_breaking.description.isin(s_o)])
                                sstrt_strike = len(soft_straight.loc[soft_straight.description.isin(s_o)])
                                sbrk_strike = len(soft_breaking.loc[soft_breaking.description.isin(s_o)])

                                # Append the vals to the respective lists
                                game_number.append(gnum)
                                gnum += 1
                                year.append(j)
                                # Pitches
                                hard_straight_count.append(hstrt)
                                hard_breaking_count.append(hbrk)
                                soft_straight_count.append(sstrt)
                                soft_breaking_count.append(sbrk)
                                # Strikes/outs
                                hard_straight_s_o.append(hstrt_strike)
                                hard_breaking_s_o.append(hbrk_strike)
                                soft_straight_s_o.append(sstrt_strike)
                                soft_breaking_s_o.append(sbrk_strike)

                        # Log pitch and outcome ratios using fastball as Bi
                        logged_bx = []
                        logged_strikes = []

                        for l in list(range(len(hard_straight_count))):
                            behavior = (hard_straight_count[l ] +1 ) / \
                                        (hard_breaking_count[l] + soft_straight_count[l] + soft_breaking_count[l ] +1)
                            strikes = (hard_straight_s_o[l ] +1 ) / \
                                        (hard_breaking_s_o[l] + soft_straight_s_o[l] + soft_breaking_s_o[l ] +1)
                            behavior = math.log(behavior, 10)
                            strikes = math.log(strikes, 10)
                            logged_bx.append(behavior)
                            logged_strikes.append(strikes)

                        # Combine the lists and save df for the pitcher
                        count_data = pd.DataFrame({'Year' :year, 'Game': game_number, \
                                                   'HStrt': hard_straight_count, 'HBrk' :hard_breaking_count, \
                                                   'SStrt' :soft_straight_count ,'SBrk' :soft_breaking_count, \
                                                   'HStrtStrike' :hard_straight_s_o, 'HBrkStrike' :hard_breaking_s_o, \
                                                   'SStrtStrike' :soft_straight_s_o, 'SBrkStrike' :soft_breaking_s_o, \
                                                   'Logged_Bx' :logged_bx, 'Logged_Strikes' :logged_strikes, \
                                                   'HStrtSpeed': hard_straight_spd, 'HBrkSpeed': hard_breaking_spd, \
                                                   'SStrtSpeed': soft_straight_spd, 'SBrkSpeed': soft_breaking_spd, \
                                                   'HStrtX': hard_straight_x, 'HBrkX': hard_breaking_x, \
                                                   'SStrtX': soft_straight_x, 'SBrkX': soft_breaking_x, \
                                                   'HStrtZ': hard_straight_z, 'HBrkZ': hard_breaking_z, \
                                                   'SStrtZ': soft_straight_z, 'SBrkZ': soft_breaking_z, \
                                                   'HStrtT': hard_straight_t, 'HBrkT': hard_breaking_t, \
                                                   'SStrtT': soft_straight_t, 'SBrkT': soft_breaking_t, \
                                                   })
                        count_data = count_data.fillna(0)

                        # Fit the GME and return the parameters
                        s_str, b_str = np.polyfit(count_data.Logged_Strikes, count_data.Logged_Bx, 1)
                        corrmatSTR = np.corrcoef(count_data.Logged_Strikes, count_data.Logged_Bx)
                        r2_str = (corrmatSTR[0 ,1] )* *2

                        # Get counts of each pitch type for later correlations
                        hstrt_season.append(count_data.HStrtSpeed.mean())
                        hbrk_season.append(count_data.HBrkSpeed.mean())
                        sstrt_season.append(count_data.SStrtSpeed.mean())
                        sbrk_season.append(count_data.SBrkSpeed.mean())

                        # Calculate differences in speed from fastball for each pitch type
                        count_data['hbrk_diff_spd'] = count_data['HStrtSpeed'] - count_data['HBrkSpeed']
                        count_data['sstrt_diff_spd'] = count_data['HStrtSpeed'] - count_data['SStrtSpeed']
                        count_data['sbrk_diff_spd'] = count_data['HStrtSpeed'] - count_data['SBrkSpeed']

                        # Calculate differences in x-break from fastball for each pitch type
                        count_data['hbrk_diff_x'] = count_data['HStrtX'] - count_data['HBrkX']
                        count_data['sstrt_diff_x'] = count_data['HStrtX'] - count_data['SStrtX']
                        count_data['sbrk_diff_x'] = count_data['HStrtX'] - count_data['SBrkX']

                        # Calculate differences in z-break from fastball for each pitch type
                        count_data['hbrk_diff_z'] = count_data['HStrtZ'] - count_data['HBrkZ']
                        count_data['sbrk_diff_z'] = count_data['HStrtZ'] - count_data['SBrkZ']

                        # Calculate differences in total break from fastball for each pitch type
                        count_data['hbrk_diff_t'] = count_data['HStrtT'] - count_data['HBrkT']
                        count_data['sbrk_diff_t'] = count_data['HStrtT'] - count_data['SBrkT']

                        # Make missing anything where pitch speed = 0
                        for n in ['hbrk_diff_spd', 'sstrt_diff_spd', 'sbrk_diff_spd']:
                            for m in range(len(count_data)):
                                if count_data[n][m] > 30:
                                    count_data[n][m] = np.nan

                        # speed correlations with bias to use pitch
                        corr_raw_spd_hstrt.append \
                            (round((np.corrcoef(count_data.HStrtSpeed, count_data.HStrtStrike)[0, 1]), 4))
                        corr_raw_spd_hbrk.append(round((np.corrcoef(count_data.HBrkSpeed, count_data.HBrkStrike)[0, 1]), 4))
                        corr_raw_spd_sstrt.append \
                            (round((np.corrcoef(count_data.SStrtSpeed, count_data.SStrtStrike)[0, 1]), 4))
                        corr_raw_spd_sbrk.append(round((np.corrcoef(count_data.SBrkSpeed, count_data.SBrkStrike)[0, 1]), 4))
                        # speed diff correlations bias to use pitch
                        corr_diff_spd_hbrk.append \
                            (round((np.corrcoef(count_data.hbrk_diff_spd, count_data.HBrkStrike)[0, 1]), 4))
                        corr_diff_spd_sstrt.append \
                            (round((np.corrcoef(count_data.sstrt_diff_spd, count_data.SStrtStrike)[0, 1]), 4))
                        corr_diff_spd_sbrk.append \
                            (round((np.corrcoef(count_data.sbrk_diff_spd, count_data.SBrkStrike)[0, 1]), 4))
                        # break correlations bias to use pitch
                        corr_raw_brk_hbrk_x.append(round((np.corrcoef(count_data.HBrkX, count_data.HBrkStrike)[0, 1]), 4))
                        corr_raw_brk_sbrk_x.append(round((np.corrcoef(count_data.SBrkX, count_data.SBrkStrike)[0, 1]), 4))
                        corr_raw_brk_hbrk_z.append(round((np.corrcoef(count_data.HBrkZ, count_data.HBrkStrike)[0, 1]), 4))
                        corr_raw_brk_sbrk_z.append(round((np.corrcoef(count_data.SBrkZ, count_data.SBrkStrike)[0, 1]), 4))
                        corr_raw_brk_hbrk_t.append(round((np.corrcoef(count_data.SBrkT, count_data.SBrkStrike)[0, 1]), 4))
                        corr_raw_brk_sbrk_t.append(round((np.corrcoef(count_data.SBrkT, count_data.SBrkStrike)[0, 1]), 4))
                        # break diff correlations bias to use pitch
                        corr_diff_brk_hbrk_x.append \
                            (round((np.corrcoef(count_data.hbrk_diff_x, count_data.HBrkStrike)[0, 1]), 4))
                        corr_diff_brk_sbrk_x.append \
                            (round((np.corrcoef(count_data.sbrk_diff_x, count_data.SBrkStrike)[0, 1]), 4))
                        corr_diff_brk_hbrk_z.append \
                            (round((np.corrcoef(count_data.hbrk_diff_z, count_data.HBrkStrike)[0, 1]), 4))
                        corr_diff_brk_sbrk_z.append \
                            (round((np.corrcoef(count_data.sbrk_diff_z, count_data.SBrkStrike)[0, 1]), 4))
                        corr_diff_brk_hbrk_t.append \
                            (round((np.corrcoef(count_data.hbrk_diff_t, count_data.HBrkStrike)[0, 1]), 4))
                        corr_diff_brk_sbrk_t.append \
                            (round((np.corrcoef(count_data.sbrk_diff_t, count_data.SBrkStrike)[0, 1]), 4))

                        # Save the GME values n
                        player.append(uniq_p[i])
                        season.append(j)

                        # Matching params
                        VAC_strikes.append(round(r2_str, 4))
                        bias_strikes.append(round(b_str, 4))
                        sens_strikes.append(round(s_str, 4))

                except:
                    continue

            # Save the data
            player_fits = pd.DataFrame({'Player' :player, \
                                        'Season' :season, \
                                        'VAC' :VAC_strikes, \
                                        'Bias' :bias_strikes, \
                                        'Sensitivity' :sens_strikes, \
                                        'HStrt_Thrown': hstrt_season, \
                                        'HBrk_Thrown': hbrk_season, \
                                        'SStrt_Thrown': sstrt_season, \
                                        'SBrk_Thrown': sbrk_season, \
                                        'HStrt_Spd_Raw': corr_raw_spd_hstrt, \
                                        'HBrk_Spd_Raw': corr_raw_spd_hbrk, \
                                        'SStrt_Spd_Raw': corr_raw_spd_sstrt, \
                                        'SBrk_Spd_Raw': corr_raw_spd_sbrk, \
                                        'HBrk_Spd_Diff': corr_diff_spd_hbrk, \
                                        'SStrt_Spd_Diff': corr_diff_spd_sstrt, \
                                        'SBrk_Spd_Diff': corr_diff_spd_sbrk, \
                                        'HBrk_X_Raw': corr_raw_brk_hbrk_x, \
                                        'SBrk_X_Raw': corr_raw_brk_sbrk_x, \
                                        'HBrk_Z_Raw': corr_raw_brk_hbrk_z, \
                                        'SBrk_Z_Raw': corr_raw_brk_sbrk_z, \
                                        'HBrk_T_Raw': corr_raw_brk_hbrk_z, \
                                        'SBrk_T_Raw': corr_raw_brk_sbrk_z, \
                                        'HBrk_X_Diff': corr_diff_brk_hbrk_x, \
                                        'SBrk_X_Diff': corr_diff_brk_sbrk_x, \
                                        'HBrk_Z_Diff': corr_diff_brk_hbrk_z, \
                                        'SBrk_Z_Diff': corr_diff_brk_sbrk_z, \
                                        'HBrk_T_Diff': corr_diff_brk_hbrk_t, \
                                        'SBrk_T_Diff': corr_diff_brk_sbrk_t, \
                                        })

            player_fits.to_csv('All_GME_Fits.csv')

            if i% 100 == 0:
                print(f"{i} players completed. Continuing...\n")

        except Exception as ex:
            err = type(Exception).__name__
            err_type.append(err)
            player_errors.append(i)

        return VAC, residual_trend, log_bias, sensitivity, error_log