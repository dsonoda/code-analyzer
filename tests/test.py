"""
test code
"""
import sys
sys.path.append('../')

import os
module_dir = os.path.dirname(os.path.abspath(__file__))

from code_analyzer import CodeAnalyzer as code_analyzer


options = {
    # Output log flg
    "log_flg": True,
    # Output log directory path
    "log_dir": module_dir + "/log",
}
ca_mod = code_analyzer.CodeAnalyzer(options)

