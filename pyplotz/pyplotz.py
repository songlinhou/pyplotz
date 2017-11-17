#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 18:00:50 2017

@author: Ray
"""


import matplotlib.pyplot as plt
from pyversion import cprint

class PyplotZ():
    
    def __init__(self):
        #!/usr/bin/python
        # -*- coding: utf-8 -*-
        pass
    
    def __fetch_font(self,file_path):
        import requests
        default_url = 'https://github.com/201528015329004/pyplotz/raw/master/downloads/plot_zh.ttf'
        cprint('start downloading default chinese font(only for first time)')
        r = requests.get(default_url)
        with open(file_path, "wb") as code:
            code.write(r.content)
        cprint('downloading complete')       
    def __utf8__(self,s):
        if type(s) is str:
            s = s.decode("utf-8")
        return s
    def _get_font_property(self):
        if hasattr(self,'zh_font'):
            return self.zh_font
        return None
    def enable_chinese(self,prefer_internal=False):
        import os
        import platform
        from matplotlib.font_manager import FontProperties
        use_internal = prefer_internal
        if use_internal:
            platform = platform.system().lower()
            if platform.startswith('win'):
                use_internal = False
            else:
                interal_zh = '/Library/Fonts/Songti.ttc'
                if not os.path.exists(interal_zh):
                    use_internal = False
                else:
                    self.zh_font = FontProperties(fname = interal_zh)
                    self.using_fname = interal_zh
        if not use_internal:
            import os
            inner_path = os.path.dirname(os.path.realpath(__file__))
            font_name = 'plot_zh.ttf'
            font_lib = '~/Library/Fonts/'
            font_lib = os.path.expanduser(font_lib)
            try_download = False
            
            if not os.path.exists(font_lib):
                os.makedirs(font_lib)
            try:
                if not os.path.exists(font_lib + font_name):   
                    import shutil
                    font_full_path = os.path.join(inner_path,font_name)
                    shutil.copy2(font_full_path, font_lib)
                    cprint('Font installed at the first runtime')                 
            except Exception:
                # try downloading
                cprint('try downloading')
                try_download = True
            if try_download:
                try:
                    self.__fetch_font(font_lib + font_name)
                    if os.path.exists(font_lib + font_name):
                        cprint("Font installed at the first time")
                    else:
                        cprint("cannot download")
                except Exception as e:
                    raise Exception("Download Failed:" + str(e))
            
            if os.path.exists(font_lib + font_name):
                self.zh_font = FontProperties(fname = font_lib + font_name)
                self.using_fname = font_lib + font_name
    def automate_font_size(self,default=None,scale=1.0,auto_size=True):
        if default is not None:
            default = int(default * scale)
            self.xlabel_size(default)
            self.ylabel_size(default)
            self.xtick_size(default)
            self.ytick_size(default)
            self.title_size(default * 2)
        else:
            shorter_inch = min(self.get_figure_inches())
            inferred = int(shorter_inch * 3)
            inferred = int(inferred * scale)
            self.xlabel_size(inferred)
            self.ylabel_size(inferred)
            self.xtick_size(inferred)
            self.ytick_size(inferred)
            self.title_size(inferred * 2)
    def get_figure_dpis(self):
        fig = plt.gcf()
        size = fig.get_size_inches()*fig.dpi # size in pixels
        return size
    def get_figure_inches(self):
        fig = plt.gcf()
        size = fig.get_size_inches()
        return size
    def set_figure_size(self,width,height):
        plt.figure(figsize=(width,height))
        
    def plot(self,*arg,**kwargs):
        arg = [self.__utf8__(a) for a in arg]
        kwargs = {k:self.__utf8__(v) for k,v in kwargs.iteritems()}
        plt.plot(*arg,**kwargs)
    def hist(self,*arg,**kwargs):
        arg = [self.__utf8__(a) for a in arg]
        kwargs = {k:self.__utf8__(v) for k,v in kwargs.iteritems()}
        plt.hist(*arg,**kwargs)
    def hist2d(self,*arg,**kwargs):
        arg = [self.__utf8__(a) for a in arg]
        kwargs = {k:self.__utf8__(v) for k,v in kwargs.iteritems()}
        plt.hist2d(*arg,**kwargs)
    def pie(self,*arg,**kwargs):
        arg = [self.__utf8__(a) for a in arg]
        kwargs = {k:self.__utf8__(v) for k,v in kwargs.iteritems()}
        plt.pie(*arg,**kwargs)
    def polar(self,*arg,**kwargs):
        arg = [self.__utf8__(a) for a in arg]
        kwargs = {k:self.__utf8__(v) for k,v in kwargs.iteritems()}
        plt.polar(*arg,**kwargs)
    def hexbin(self,*arg,**kwargs):
        arg = [self.__utf8__(a) for a in arg]
        kwargs = {k:self.__utf8__(v) for k,v in kwargs.iteritems()}
        plt.hexbin(*arg,**kwargs)
    def bar(self,*arg,**kwargs):
        arg = [self.__utf8__(a) for a in arg]
        kwargs = {k:self.__utf8__(v) for k,v in kwargs.iteritems()}
        plt.bar(*arg,**kwargs)
    def barbs(self,*arg,**kwargs):
        arg = [self.__utf8__(a) for a in arg]
        kwargs = {k:self.__utf8__(v) for k,v in kwargs.iteritems()}
        plt.barbs(*arg,**kwargs)
    def barh(self,*arg,**kwargs):
        arg = [self.__utf8__(a) for a in arg]
        kwargs = {k:self.__utf8__(v) for k,v in kwargs.iteritems()}
        plt.barh(*arg,**kwargs)
    def title(self,*arg,**kwargs):
        if hasattr(self,'zh_font'):
            if self.zh_font is not None:
                kwargs['fontproperties'] = self.zh_font
                arg = [self.__utf8__(a) for a in arg]
        plt.title(*arg,**kwargs)
    def text(self,*arg,**kwargs):
        if hasattr(self,'zh_font'):
            if self.zh_font is not None:
                kwargs['fontproperties'] = self.zh_font
                arg = [self.__utf8__(a) for a in arg]
        plt.text(*arg,**kwargs)
    def title_size(self,font_size):
        ax = plt.gca()
        ax.title.set_size(font_size)
    def xlabel_size(self,font_size):
        ax = plt.gca()
        ax.xaxis.label.set_size(font_size)
    def ylabel_size(self,font_size):
        ax = plt.gca()
        ax.yaxis.label.set_size(font_size)
    def xtick_size(self,font_size):
        ax = plt.gca()
        for label in (ax.get_xticklabels()):
            label.set_fontsize(int(font_size)) # Size here overrides font_prop
    def ytick_size(self,font_size):
        ax = plt.gca()
        for label in (ax.get_yticklabels()):
            label.set_fontsize(int(font_size)) # Size here overrides font_prop
    def xlabel(self,*arg,**kwargs):
        if hasattr(self,'zh_font'):
            if self.zh_font is not None:
                kwargs['fontproperties'] = self.zh_font
                arg = [self.__utf8__(a) for a in arg]
        plt.xlabel(*arg,**kwargs)
    def ylabel(self,*arg,**kwargs):
        if hasattr(self,'zh_font'):
            if self.zh_font is not None:
                kwargs['fontproperties'] = self.zh_font
                arg = [self.__utf8__(a) for a in arg]
        plt.ylabel(*arg,**kwargs)
    def xticks(self,*arg,**kwargs):
        if hasattr(self,'zh_font'):
            if self.zh_font is not None:
                kwargs['fontproperties'] = self.zh_font
                arg = [self.__utf8__(a) for a in arg]
        plt.xticks(*arg,**kwargs)
    def yticks(self,*arg,**kwargs):
        if hasattr(self,'zh_font'):
            if self.zh_font is not None:
                kwargs['fontproperties'] = self.zh_font
                arg = [self.__utf8__(a) for a in arg]
        plt.yticks(*arg,**kwargs)

    def legend(self,*arg,**kwargs):
        if hasattr(self,'zh_font'):
            kwargs['prop'] = self.zh_font
        plt.legend(*arg,**kwargs)
    def show(self,*args,**kw):
        plt.show(*args,**kw)
    #~/Library/Fonts/
    
    
    
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np
    pltz = PyplotZ()
    pltz.enable_chinese()
    pltz.set_figure_size(10,5)
    pltz.enable_chinese()
    pltz.plot(np.linspace(-10,10),np.sin(np.linspace(-10,10)),'b', label='sin数据',alpha=0.7)
    pltz.plot(np.linspace(-10,10),np.cos(np.linspace(-10,10)),'r', label='cos数据',alpha=0.7)
    pltz.title("数据图")
    pltz.xlabel("横坐标")
    pltz.ylabel("纵坐标")
    plt.grid()
    pltz.legend()
    pltz.automate_font_size(scale=0.6)
    #pltz.title_size(30)