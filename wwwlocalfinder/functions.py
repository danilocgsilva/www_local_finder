import os
from wwwlocalfinder.Base_Host_Finder import Base_Host_Finder

def get_www(os_name):
    base_host_finder = Base_Host_Finder()
    base_host_finder.set_os_name(os_name)
    return base_host_finder.get_www_path()