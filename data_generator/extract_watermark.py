# !/usr/bin/python
# -*- coding: utf-8 -*-

# Chao-Chuan Lu 20181215
##                                                       &mmmm@@@%%%%%%%%8%%88888%%%%%%%%@@@@@@@@
##                                                       @@@@@%%%%%%8888888888888g&&&%@@@@@@@@@@@
##                                                       @@@%%%%%%88888gggg&8g&g@@M@@%%%%%*""""`?
##                          _ggg_    _ggg                @@@@%%%%%%%%%%%M@@@@@@@@@@@@@@Mg_       
##                         m@N@@@g _@@F@@M               %%%@@%%%%^"`` @@@@@@@@@@@@@@@@@@@@w     
##                        ]@M   7" M@K   "               8        _m@E@@@@@@@@@@@@@@@@@@@@@M-    
## qmmg                   @@K      @@C                             g@@@@@@@@@@@@@@@@@@@@@@@@K    
## "@@M                   M@L     0@M          _g_               ,@@@@@@@@@@@@@@@@@@@@@@@@@M     
##  M@K      pmg  q@@M ___@@L_____]@M____mmg  0@@@               m@@@@@@@@@@@@@@@@@@@@@@@@%g     
##  M@P      @@@   @@$4@@@@@@@W@@@@@@@@W@@@M   @@W                m@@@@@@@@@@@@@@@@@@@@@@%%%     
##  @@L      ]@@  0@@$    M@L      @M    @@M  ]@@M                 @@@@@@@@@@@@@@@@@@@W%8"`g_    
## ]@@L ____  @@C_@@@K    M@L      @@    "@@L_@@@M                 *@@@@@@@@@Km%@@@@%%8^<m@#C    
## ]@@@@@@@@P M@@@@@@@g   M@@_     @@M    @@@@@@@M                  "@@@@@@@M@@M%%%%8   8@@L     
##  %@W"`     *@@W  @@N   W@@^     @@W    "@@Y ]@M                   @@@@@@@@@@gg@@@&&ggg%@@     
##                                             ]@M                    M@@@@@@Mg7%@@@@@@@@@@W?,   
##                                             ]@M       >            "@@@@@@@@@M@@@@@@@@@@M"    
##                                             M@W       88>           M@@@@@@@@@@@@@@@@@@@M     
##                                             *W        %888>         M@@@@@@@@@@@@@@@@@@@L     
##                                                       %%%%888      q@@@@@@@@@@@@@@@@@@@K    <8
##                                                       %%%%%%%88> _m@@@@@@@@@@@@@@@@@@@MC  <888

from PIL import Image
import numpy as np
img = Image.open("data_generator/template.png")
print(img.format, img.size, img.mode)

