#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 15:38:47 2019

@author: revanthkorrapolu
"""

import pandas as pd
player_data = pd.read_csv('player_data.csv')
season_data = pd.read_csv('Seasons_Stats.csv')

season_data_2017 = pd.DataFrame()
season_data_2017 = season_data[season_data['Year'] == 2017]
season_data_2017['PTS/G'] = season_data['PTS'] / season_data['G']