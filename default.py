import audrey
import os, xbmcaddon

# if you want to store your json file within the addon itself uncomment the below
#home=xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('path'))
#audrey.feedme(os.path.join(home, '', "sites.json"), "file")

# if you want to store your json file online uncomment out the below
audrey.feedme("https://www.jasonbase.com/things/W4Wx.json", "url")