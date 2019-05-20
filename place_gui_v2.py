# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import webbrowser
import requests

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 308,200 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"輸入搜尋附近地圖的關鍵字", wx.Point( -1,-1 ), wx.Size( 300,-1 ), wx.ALIGN_CENTRE )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		bSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"搜尋", wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		bSizer1.Add( self.m_button1, 0, wx.ALL, 5 )
		
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.mySquare )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def mySquare( self, event ):
		event.Skip()
	



class CalcFrame(MyFrame1):  # inheritace from square module
    def __init__(self, parent):   # got init from parent class
        MyFrame1.__init__(self, parent) 

    def mySquare(self, event):  # 定義事件處理函數
        # API KEY, this can't show to other
        API_KEY = "put your google goelocate API here"

        # api-endpoint 
        URL = "https://www.googleapis.com/geolocation/v1/geolocate?key=" + API_KEY

        # sending get request and saving the response as response object 
        res = requests.post(URL) 

        # convert into json
        data = res.json()

        # extracting lat and lng from json
        lat = data["location"]["lat"]
        lng = data["location"]["lng"]

		# set parameter
        scale_level = 16
        search_place = self.m_textCtrl1.GetValue()

		# url setup
        url_2 = 'https://www.google.com.tw/maps/search/{}/@{},{},{}z/'.format(search_place,lat,lng,scale_level)

        webbrowser.open(url_2)


# active the app
app = wx.App(False)

# active and show the frame
frame = CalcFrame(None)
frame.Show(True)


# main loop
app.MainLoop()
