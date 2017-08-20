# -*- coding: utf-8 -*-

import os
import datetime


class CodeAnalyzer():
    """
    Source code analyze
    """

    # log settings
    __log_flg = True
    __log_dir = ""

    def __init__(
        self,
        options
    ):
        """
        Initialization
        :param option:
            log_flg: Output log flg
            log_dir: Output log directory path
        """
        try:
            # settings
            if 'log_flg' in options and isinstance(options['log_flg'], bool):
                self.__log_flg = options['log_flg']
            if 'log_dir' in options and isinstance(options['log_dir'], str):
                self.__log_dir = options['log_dir']
            else:
                self.__log_dir = os.path.dirname(os.path.abspath(__file__)) + "/log"

        except ValueError as e:
            self._log(e)
            raise Exception(e)


    def _log(self, msg):
        """
        Output log
        :param msg:
        :return:
        """
        if self.__log_flg:
            now = datetime.datetime.now()
            f = open(self.__log_dir+"/"+now.strftime("%Y%m%d")+".log", 'a')
            f.write("["+now.strftime("%Y/%m/%d %H:%M:%s")+"] "+msg+"\n")
            f.close()


    def analyze(self):
        """
        code analyze
        """
        pass
