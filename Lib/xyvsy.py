"""
# Xyvsy (GXy) module
"""
##############################################################################
#                                                                            #
# Module:       xyvsy (GXy) module                                           #
#                                                                            #
# Copyright:    2000, Regents of the University of California                #
#               This software may not be distributed to others without       #
#               permission of the author.                                    #
#                                                                            #
# Authors:      PCMDI Software Team                                          #
#               Lawrence Livermore NationalLaboratory:                       #
#               support@pcmdi.llnl.gov                                       #
#                                                                            #
# Description:  Python command wrapper for VCS's xyvsy graphics method.      #
#                                                                            #
# Version:      5.0                                                          #
#                                                                            #
##############################################################################
#
#
#
##############################################################################
#                                                                            #
# Import: VCS C extension module.                                            #
#                                                                            #
##############################################################################
import queries,VCS_validation_functions,cdtime
import Canvas
from types import *
import AutoAPI
import xmldocs

##############################################################################
#                                                                            #
# Function:	setGXymember                                                 #
#                                                                            #
# Description of Function:                                                   #
# 	Private function to update the VCS canvas plot. If the canvas mode is#
#       set to 0, then this function does nothing.              	     #
#                                                                            #
#                                                                            #
# Example of Use:                                                            #
#      setGXymember(self,name,value)					     #
#              where: self is the class (e.g., GXy)                          #
#                     name is the name of the member that is being changed   #
#                     value is the new value of the member (or attribute)    #
#                                                                            #
##############################################################################
def setGXymember(self,member,value):
     # If the VCS Canvas is displayed, then bring the canvas to the front before 
     # redisplaying the updated contents.
     if (self.parent.mode == 1) and (self.parent.iscanvasdisplayed()):
        Canvas.finish_queued_X_server_requests( self.parent )
        self.parent.canvas.BLOCK_X_SERVER()
        self.parent.canvasraised()

     _vcs.setGXymember(self, member, value, self.parent.mode)

     # If the VCS Canvas is displayed, then update the backing store
     if (self.parent.mode == 1) and (self.parent.iscanvasdisplayed()):
        self.parent.flush()
        self.parent.backing_store()
        self.parent.canvas.UNBLOCK_X_SERVER()
setmember = setGXymember
#################################################################################
#                                                                               #
# Function:     getGXymember                                                    #
#                                                                               #
# Description of Function:                                                      #
#       Private function that retrieves the Xyvsy members from the C            #
#       structure and passes it back to Python.                                 #
#                                                                               #
#                                                                               #
# Example of Use:                                                               #
#      return_value =								#
#      getGXymember(self,name)                                                  #
#              where: self is the class (e.g., GXy)                             #
#                     name is the name of the member that is being found        #
#                                                                               #
#################################################################################
def getGXymember(self,member):
     return _vcs.getGXymember(self,member)
getmember=getGXymember
#################################################################################
#                                                                               #
# Function:     renameGXy                                                       #
#                                                                               #
# Description of Function:                                                      #
#       Private function that renames the name of an existing Xyvsy             #
#       graphics method.                                                        #
#                                                                               #
#                                                                               #
# Example of Use:                                                               #
#      renameGXy(old_name, new_name)                                            #
#              where: old_name is the current name of Xyvsy graphics method     #
#                     new_name is the new name for the Xyvsy graphics method    #
#                                                                               #
#################################################################################
def renameGXy(self, old_name, new_name):
     return _vcs.renameGXy(old_name, new_name)

class GXy(object,AutoAPI.AutoAPI):
    """
    Options:::
%s
%s
%s
%s
 Class:	GXy				# Xyvsy

 Description of GXy Class:
    The Xyvsy graphics method displays a line plot from a 1D data array (i.e. a
    plot of X(y), where y represents the 1D coordinate values). The example below
    shows how to change line and marker attributes for the Xyvsy graphics method.

    This class is used to define an Xyvsy table entry used in VCS, or it can be 
    used to change some or all of the Xyvsy attributes in an existing Xyvsy table
    entry.

 Other Useful Functions:
          a=vcs.init()                  # Constructor
          a.show('xyvsy')               # Show predefined Xyvsy graphics methonds
          a.show('line')                # Show predefined VCS line objects
          a.show('marker')              # Show predefined VCS marker objects
          a.setcolormap("AMIP")         # Change the VCS color map
          a.xyvsy(s, x, 'default')       # Plot data 's' with Xyvsy 'x'
                                           and 'default' template
          a.update()                    # Updates the VCS Canvas at user's request
          a.mode=1, or 0                  If 1, then automatic update, else if
                                          0, then use update function to

 Example of Use:
    a=vcs.init()
    To Create a new instance of Xyvsy use:
     xyy=a.createxyvsy('new','quick')    # Copies content of 'quick' to 'new'
     xyy=a.createxyvsy('new')            # Copies content of 'default' to 'new'

    To Modify an existing Xyvsy use:
     xyy=a.getxyvsy('AMIP_psl')

    xyy.list()                          # Will list all the Xyvsy attribute values
    xyy.projection='linear'             # Can only be 'linear'
    lon30={-180:'180W',-150:'150W',0:'Eq'}
    xyy.xticlabels1=lon30
    xyy.xticlabels2=lon30
    xyy.xticlabels(lon30, lon30)        # Will set them both
    xyy.xmtics1=''
    xyy.xmtics2=''
    xyy.xmtics(lon30, lon30)            # Will set them both
    xyy.yticlabels1=lat10
    xyy.yticlabels2=lat10
    xyy.yticlabels(lat10, lat10)        # Will set them both
    xyy.ymtics1=''
    xyy.ymtics2=''
    xyy.ymtics(lat10, lat10)            # Will set them both
    xyy.datawc_y1=-90.0
    xyy.datawc_y2=90.0
    xyy.datawc_x1=-180.0
    xyy.datawc_x2=180.0
    xyy.datawc(-90, 90, -180, 180)      # Will set them all
    xyy.yaxisconvert='linear'

    Specify the Xyvsy line type:
     xyy.line=0                         # same as xyy.line = 'solid'
     xyy.line=1                         # same as xyy.line = 'dash'
     xyy.line=2                         # same as xyy.line = 'dot'
     xyy.line=3                         # same as xyy.line = 'dash-dot'
     xyy.line=4                       	# same as xyy.line = 'long-dash

    Specify the Xyvsy line color:
    xyy.linecolor=16    # color range: 16 to 230, default color is black
    xyy.linewidth=16    # width range: 1 to 100, default color is black

    Specify the Xyvsy marker type:
     xyy.marker=1                       # Same as xyy.marker='dot'
     xyy.marker=2                       # Same as xyy.marker='plus'
     xyy.marker=3                       # Same as xyy.marker='star'
     xyy.marker=4                       # Same as xyy.marker='circle'
     xyy.marker=5                       # Same as xyy.marker='cross'
     xyy.marker=6                       # Same as xyy.marker='diamond'
     xyy.marker=7                       # Same as xyy.marker='triangle_up'
     xyy.marker=8                       # Same as xyy.marker='triangle_down'
     xyy.marker=9                       # Same as xyy.marker='triangle_left'
     xyy.marker=10                      # Same as xyy.marker='triangle_right'
     xyy.marker=11                      # Same as xyy.marker='square'
     xyy.marker=12                      # Same as xyy.marker='diamond_fill'
     xyy.marker=13                      # Same as xyy.marker='triangle_up_fill'
     xyy.marker=14                      # Same as xyy.marker='triangle_down_fill'
     xyy.marker=15                      # Same as xyy.marker='triangle_left_fill'
     xyy.marker=16                      # Same as xyy.marker='triangle_right_fill'
     xyy.marker=17                      # Same as xyy.marker='square_fill'
     xyy.marker=None                   	# Draw no markers

    There are four possibilities for setting the marker color index (Ex):
     xyy.markercolors=22                # Same as below
     xyy.markercolors=(22)              # Same as below
     xyy.markercolors=([22])            # Will set the markers to a specific
                                        # 	color index
     xyy.markercolors=None             	# Color index defaults to Black

    To set the Xyvsy Marker sizie:
     xyy.markersize=5
     xyy.markersize=55
     xyy.markersize=100
     xyy.markersize=300
     xyy.markersize=None
"""
    rename=renameGXy
    __slots__=[
         '__doc__',
         'parent',
         'name',
         'g_name',
         'yaxisconvert',
         'linecolor',
         'line',
         'linewidth',
         'marker',
         'markersize',
         'markercolor',
         'projection',
         'xticlabels1',
         'xticlabels2',
         'yticlabels1',
         'yticlabels2',
         'xmtics1',
         'xmtics2',
         'ymtics1',
         'ymtics2',
         'datawc_x1',
         'datawc_x2',
         'datawc_y1',
         'datawc_y2',
         'datawc_timeunits',
         'datawc_calendar',
         '_name',
         '_yaxisconvert',
         '_linecolor',
         '_line',
         '_linewidth',
         '_marker',
         '_markersize',
         '_markercolor',
         '_projection',
         '_xticlabels1',
         '_xticlabels2',
         '_yticlabels1',
         '_yticlabels2',
         '_xmtics1',
         '_xmtics2',
         '_ymtics1',
         '_ymtics2',
         '_datawc_x1',
         '_datawc_x2',
         '_datawc_y1',
         '_datawc_y2',
         '_datawc_timeunits',
         '_datawc_calendar',
         ]
    def _getname(self):
         return self._name
    def _setname(self,value):
         value=VCS_validation_functions.checkname(self,'name',value)
         if value is not None:
              self._name=value
              setmember(self,'name',value)
    name=property(_getname,_setname)

    def _getcalendar(self):
         return self._datawc_calendar
    def _setcalendar(self,value):
         value=VCS_validation_functions.checkCalendar(self,'datawc_calendar',value)
         setmember(self,'datawc_calendar',value)
         self._datawc_calendar=value
    datawc_calendar=property(_getcalendar,_setcalendar)

    def _gettimeunits(self):
         return self._datawc_timeunits
    def _settimeunits(self,value):
         value=VCS_validation_functions.checkTimeUnits(self,'datawc_timeunits',value)
         setmember(self,'datawc_timeunits',value)
         self._datawc_timeunits=value
    datawc_timeunits=property(_gettimeunits,_settimeunits)

    def _getyaxisconvert(self):
         return self._yaxisconvert
    def _setyaxisconvert(self,value):
         value=VCS_validation_functions.checkAxisConvert(self,'yaxisconvert',value)
         self._yaxisconvert=value
         setmember(self,'yaxisconvert',value)
    yaxisconvert=property(_getyaxisconvert,_setyaxisconvert)

    def _getprojection(self):
         return self._projection
    def _setprojection(self,value):
         value=VCS_validation_functions.checkProjection(self,'projection',value)
         self._projection=value
         setmember(self,'projection',value)
    projection=property(_getprojection,_setprojection)

    def _getxticlabels1(self):
         return self._xticlabels1
    def _setxticlabels1(self,value):
         value=VCS_validation_functions.checkStringDictionary(self,'xticlabels1',value)
         self._xticlabels1=value
         setmember(self,'xticlabels1',value)
    xticlabels1=property(_getxticlabels1,_setxticlabels1)

    def _getxticlabels2(self):
         return self._xticlabels2
    def _setxticlabels2(self,value):
         value=VCS_validation_functions.checkStringDictionary(self,'xticlabels2',value)
         self._xticlabels2=value
         setmember(self,'xticlabels2',value)
    xticlabels2=property(_getxticlabels2,_setxticlabels2)

    def _getyticlabels1(self):
         return self._yticlabels1
    def _setyticlabels1(self,value):
         value=VCS_validation_functions.checkStringDictionary(self,'yticlabels1',value)
         self._yticlabels1=value
         setmember(self,'yticlabels1',value)
    yticlabels1=property(_getyticlabels1,_setyticlabels1)

    def _getyticlabels2(self):
         return self._yticlabels2
    def _setyticlabels2(self,value):
         value=VCS_validation_functions.checkStringDictionary(self,'yticlabels2',value)
         self._yticlabels2=value
         setmember(self,'yticlabels2',value)
    yticlabels2=property(_getyticlabels2,_setyticlabels2)

    def _getxmtics1(self):
         return self._xmtics1
    def _setxmtics1(self,value):
         value=VCS_validation_functions.checkStringDictionary(self,'xmtics1',value)
         self._xmtics1=value
         setmember(self,'xmtics1',value)
    xmtics1=property(_getxmtics1,_setxmtics1)

    def _getxmtics2(self):
         return self._xmtics2
    def _setxmtics2(self,value):
         value=VCS_validation_functions.checkStringDictionary(self,'xmtics2',value)
         self._xmtics2=value
         setmember(self,'xmtics2',value)
    xmtics2=property(_getxmtics2,_setxmtics2)

    def _getymtics1(self):
         return self._ymtics1
    def _setymtics1(self,value):
         value=VCS_validation_functions.checkStringDictionary(self,'ymtics1',value)
         self._ymtics1=value
         setmember(self,'ymtics1',value)
    ymtics1=property(_getymtics1,_setymtics1)

    def _getymtics2(self):
         return self._ymtics2
    def _setymtics2(self,value):
         value=VCS_validation_functions.checkStringDictionary(self,'ymtics2',value)
         self._ymtics2=value
         setmember(self,'ymtics2',value)
    ymtics2=property(_getymtics2,_setymtics2)

    def _getdatawc_x1(self):
         if getmember(self,'_tdatawc_x1') :
              return cdtime.reltime(self._datawc_x1,self.datawc_timeunits).tocomp(self.datawc_calendar)
         else:
              return self._datawc_x1
    def _setdatawc_x1(self,value):
         value=VCS_validation_functions.checkDatawc(self,'datawc_x1',value)
         self._datawc_x1=value[0]
         setmember(self,'datawc_x1',value[0])
         setmember(self,'_tdatawc_x1',value[1])
    datawc_x1=property(_getdatawc_x1,_setdatawc_x1)

    def _getdatawc_x2(self):
         if getmember(self,'_tdatawc_x2') :
              return cdtime.reltime(self._datawc_x2,self.datawc_timeunits).tocomp(self.datawc_calendar)
         else:
              return self._datawc_x2
    def _setdatawc_x2(self,value):
         value=VCS_validation_functions.checkDatawc(self,'datawc_x2',value)
         self._datawc_x2=value[0]
         setmember(self,'datawc_x2',value[0])
         setmember(self,'_tdatawc_x2',value[1])
    datawc_x2=property(_getdatawc_x2,_setdatawc_x2)
    
    def _getdatawc_y1(self):
         if getmember(self,'_tdatawc_y1') :
              return cdtime.reltime(self._datawc_y1,self.datawc_timeunits).tocomp(self.datawc_calendar)
         else:
              return self._datawc_y1
    def _setdatawc_y1(self,value):
         value=VCS_validation_functions.checkDatawc(self,'datawc_y1',value)
         self._datawc_y1=value[0]
         setmember(self,'datawc_y1',value[0])
         setmember(self,'_tdatawc_y1',value[1])
    datawc_y1=property(_getdatawc_y1,_setdatawc_y1)

    def _getdatawc_y2(self):
         if getmember(self,'_tdatawc_y2') :
              return cdtime.reltime(self._datawc_y2,self.datawc_timeunits).tocomp(self.datawc_calendar)
         else:
              return self._datawc_y2
    def _setdatawc_y2(self,value):
         value=VCS_validation_functions.checkDatawc(self,'datawc_y2',value)
         self._datawc_y2=value[0]
         setmember(self,'datawc_y2',value[0])
         setmember(self,'_tdatawc_y2',value[1])
    datawc_y2=property(_getdatawc_y2,_setdatawc_y2)
    
    def _getlinewidth(self):
         return self._linewidth
    def _setlinewidth(self,value):
         if not value is None:
              value = VCS_validation_functions.checkNumber(self,'linewidth',value,0,300)
         self._linewidth=value
         setmember(self,'linewidth',value)
    linewidth=property(_getlinewidth,_setlinewidth)
    
    def _getlinecolor(self):
         return self._linecolor
    def _setlinecolor(self,value):
         if not value is None:
              value = VCS_validation_functions.checkColor(self,'linecolor',value)
         self._linecolor=value
         setmember(self,'linecolor',value)
    linecolor=property(_getlinecolor,_setlinecolor)
    
    def _getline(self):
         return self._line
    def _setline(self,value):
         if not value is None:
              value = VCS_validation_functions.checkLineType(self,'line',value)
         self._line=value
         setmember(self,'line',value)
    line=property(_getline,_setline)
    
    def _getmarker(self):
         return self._marker
    def _setmarker(self,value):
         if not value is None:
              value = VCS_validation_functions.checkMarker(self,'marker',value)
         self._marker=value
         setmember(self,'marker',value)
    marker=property(_getmarker,_setmarker)

    def _getmarkersize(self):
         return self._markersize
    def _setmarkersize(self,value):
         if not value is None:
              value = VCS_validation_functions.checkInt(self,'markersize',value,1,300)
         self._markersize=value
         setmember(self,'markersize',value)
    markersize=property(_getmarkersize,_setmarkersize)
    
    def _getmarkercolor(self):
         return self._markercolor
    def _setmarkercolor(self,value):
         if not value is None:
              value = VCS_validation_functions.checkColor(self,'markercolor',value)
         self._markercolor=value
         setmember(self,'markercolor',value)
    markercolor=property(_getmarkercolor,_setmarkercolor)
    def __init__(self, parent, GXy_name=None, GXy_name_src='default', createGXy=0):
	#                                                         #
        ###########################################################
	# Initialize the Xyvsy class and its members              #
        #							  #
	# The getGXymember function retrieves the values of the   #
        # Xyvsy members in the C structure and passes back the    #
	# appropriate Python Object.                              #
        ###########################################################
	#                                                         #
        self.parent=parent
        if (createGXy == 0):
           if (GXy_name == None):
              raise ValueError, 'Must provide a Xyvsy name.'
           else:
              _vcs.copyGXy(GXy_name_src, GXy_name)
              self._name = GXy_name
        else:
              self._name=GXy_name_src
              
        self._projection=getmember(self, 'projection')
        self._xticlabels1=getmember(self, 'xticlabels1')
        self._xticlabels2=getmember(self, 'xticlabels2')
        self._xmtics1=getmember(self, 'xmtics1')
        self._xmtics2=getmember(self, 'xmtics2')
        self._yticlabels1=getmember(self, 'yticlabels1')
        self._yticlabels2=getmember(self, 'yticlabels2')
        self._ymtics1=getmember(self, 'ymtics1')
        self._ymtics2=getmember(self, 'ymtics2')
        self._datawc_y1=getmember(self, 'datawc_y1')
        self._datawc_y2=getmember(self, 'datawc_y2')
        self._datawc_x1=getmember(self, 'datawc_x1')
        self._datawc_x2=getmember(self, 'datawc_x2')
        self.g_name='GXy'
        self._yaxisconvert=getmember(self, 'yaxisconvert')
        self._line='solid'
        self._linecolor=241
        self._linewidth=1
        self._marker='dot'
        self._markercolor=241
        self._markersize=1
        self._datawc_timeunits=getmember(self, 'datawc_timeunits')
        self._datawc_calendar=getmember(self, 'datawc_calendar')
        self.info=AutoAPI.Info(self)
        self.info.expose=['ALL']
        self.__doc__ = self.__doc__ % (xmldocs.graphics_method_core,xmldocs.yaxisconvert,xmldocs.linedoc,xmldocs.markerdoc)
        #                                                         #
        ###########################################################
        # Find and set the Xyvsy structure in VCS C pointer       #
        # list. If the Xyvsy name does not exist, then use        #
        # default Xyvsy.                                          #
        ###########################################################
        #                                                         #


# 
# Doesn't make sense to inherit. This would mean more coding in C.
# I put this code back.                                 
#

    def xticlabels(self, xtl1='', xtl2=''):
        mode=self.parent.mode
        self.parent.mode=0
        self.xticlabels1= xtl1
        self.parent.mode=mode
        self.xticlabels2= xtl2
    xticlabels.__doc__ = xmldocs.xticlabelsdoc

    def xmtics(self,xmt1='', xmt2=''):
        mode=self.parent.mode
        self.parent.mode=0
        self.xmtics1= xmt1
        self.parent.mode=mode
        self.xmtics2= xmt2
    xmtics.__doc__ = xmldocs.xmticsdoc

    def yticlabels(self, ytl1='', ytl2=''):
        mode=self.parent.mode
        self.parent.mode=0
        self.yticlabels1= ytl1
        self.parent.mode=mode
        self.yticlabels2= ytl2
    yticlabels.__doc__ = xmldocs.yticlabelsdoc

    def ymtics(self, ymt1='', ymt2=''):
        mode=self.parent.mode
        self.parent.mode=0
        self.ymtics1= ymt1
        self.parent.mode=mode
        self.ymtics2= ymt2
    ymtics.__doc__ = xmldocs.ymticsdoc

    def datawc(self, dsp1=1e20, dsp2=1e20, dsp3=1e20, dsp4=1e20):
        mode=self.parent.mode
        self.parent.mode=0
        self.datawc_y1= dsp1
        self.datawc_y2= dsp2
        self.datawc_x1= dsp3
        self.parent.mode=mode
        self.datawc_x2= dsp4
    datawc.__doc__ = xmldocs.datawcdoc

    def list(self):
        if (self.name == '__removed_from_VCS__'):
           raise ValueError, 'This instance has been removed from VCS.'
        print "","----------Xyvsy (GXy) member (attribute) listings ----------"
        print 'Canvas Mode =',self.parent.mode
        print "graphics method =", self.g_name
        print "name =", self.name
        print "projection =", self.projection
        print "xticlabels1 =", self.xticlabels1
        print "xticlabels2 =", self.xticlabels2
        print "xmtics1 =", self.xmtics1
        print "xmtics2 =", self.xmtics2
        print "yticlabels1 =", self.yticlabels1
        print "yticlabels2 =", self.yticlabels2
        print "ymtics1 = ", self.ymtics1
        print "ymtics2 = ", self.ymtics2
        print "datawc_x1 =", self.datawc_x1
        print "datawc_y1 = ", self.datawc_y1
        print "datawc_x2 = ", self.datawc_x2
        print "datawc_y2 = ", self.datawc_y2
        print "datawc_timeunits = ", self.datawc_timeunits
        print "datawc_calendar = ", self.datawc_calendar
        print "yaxisconvert = ", self.yaxisconvert
        print "line = ", self.line
        print "linecolor = ", self.linecolor
        print "linewidth = ", self.linewidth
        print "marker = ", self.marker
        print "markercolor = ", self.markercolor
        print "markersize = ", self.markersize
    list.__doc__ = xmldocs.listdoc

    #############################################################################
    #                                                                           #
    # Script out primary Xyvsy graphics method in VCS to a file.                #
    #                                                                           #
    #############################################################################
    def script(self, script_filename=None, mode=None):
        """
%s
 Function:     script                           # Calls _vcs.scriptGXy

 Description of Function:
       Saves out a Xyvsy graphics method in Python or VCS script form to a
       designated file.

 Example of Use:
    script(scriptfile_name, mode)
              where: scriptfile_name is the output name of the script file.
                     mode is either "w" for replace or "a" for append.

              Note: If the the filename has a ".py" at the end, it will produce a
                    Python script. If the filename has a ".scr" at the end, it will
                    produce a VCS script. If neither extensions are give, then by
                    default a Python script will be produced.

    a=vcs.init()
    Xy=a.createboxfill('temp')
    Xy.script('filename.py')         # Append to a Python file "filename.py"
    Xy.script('filename.scr')        # Append to a VCS file "filename.scr"
    Xy.script('filename','w')
"""
        if (script_filename == None):
          raise ValueError, 'Error - Must provide an output script file name.'

        if (mode == None):
           mode = 'a'
        elif (mode not in ('w', 'a')):
          raise ValueError, 'Error - Mode can only be "w" for replace or "a" for append.'

        # By default, save file in python script mode
        scr_type = script_filename[len(script_filename)-4:len(script_filename)]
        if (scr_type == '.scr'):
           print _vcs.scriptGXy(self.name,script_filename,mode)
        else:
           mode = mode + '+'
           py_type = script_filename[len(script_filename)-3:len(script_filename)]
           if (py_type != '.py'):
              script_filename = script_filename + '.py'

           # Write to file
           fp = open(script_filename,mode)
           if (fp.tell() == 0): # Must be a new file, so include below
              fp.write("#####################################\n")
              fp.write("#                                 #\n")
              fp.write("# Import and Initialize VCS     #\n")
              fp.write("#                             #\n")
              fp.write("#############################\n")
              fp.write("import vcs\n")
              fp.write("v=vcs.init()\n\n")

           unique_name = '__GXy__' + self.name
           fp.write("#----------Xyvsy (GXy) member (attribute) listings ----------\n")
           fp.write("gxy_list=v.listelements('xyvsy')\n")
           fp.write("if ('%s' in gxy_list):\n" % self.name)
           fp.write("   %s = v.getxyvsy('%s')\n" % (unique_name, self.name))
           fp.write("else:\n")
           fp.write("   %s = v.createxyvsy('%s')\n" % (unique_name, self.name))
           # Common core graphics method attributes
           fp.write("%s.projection = '%s'\n" % (unique_name, self.projection))
           fp.write("%s.xticlabels1 = '%s'\n" % (unique_name, self.xticlabels1))
           fp.write("%s.xticlabels2 = '%s'\n" % (unique_name, self.xticlabels2))
           fp.write("%s.xmtics1 = '%s'\n" % (unique_name, self.xmtics1))
           fp.write("%s.xmtics2 = '%s'\n" % (unique_name, self.xmtics2))
           fp.write("%s.yticlabels1 = '%s'\n" % (unique_name, self.yticlabels1))
           fp.write("%s.yticlabels2 = '%s'\n" % (unique_name, self.yticlabels2))
           fp.write("%s.ymtics1 = '%s'\n" % (unique_name, self.ymtics1))
           fp.write("%s.ymtics2 = '%s'\n" % (unique_name, self.ymtics2))
           if isinstance(self.datawc_x1,(int,long,float)):
                fp.write("%s.datawc_x1 = %g\n" % (unique_name, self.datawc_x1))
           else:
                fp.write("%s.datawc_x1 = '%s'\n" % (unique_name, self.datawc_x1))
           if isinstance(self.datawc_y1,(int,long,float)):
                fp.write("%s.datawc_y1 = %g\n" % (unique_name, self.datawc_y1))
           else:
                fp.write("%s.datawc_y1 = '%s'\n" % (unique_name, self.datawc_y1))
           if isinstance(self.datawc_x2,(int,long,float)):
                fp.write("%s.datawc_x2 = %g\n" % (unique_name, self.datawc_x2))
           else:
                fp.write("%s.datawc_x2 = '%s'\n" % (unique_name, self.datawc_x2))
           if isinstance(self.datawc_y2,(int,long,float)):
                fp.write("%s.datawc_y2 = %g\n" % (unique_name, self.datawc_y2))
           else:
                fp.write("%s.datawc_y2 = '%s'\n" % (unique_name, self.datawc_y2))
           fp.write("%s.datawc_calendar = %g\n" % (unique_name, self.datawc_calendar))
           fp.write("%s.datawc_timeunits = '%s'\n\n" % (unique_name, self.datawc_timeunits))
           fp.write("%s.yaxisconvert = '%s'\n" % (unique_name, self.yaxisconvert))
           # Unique attribute for xyvsy
           fp.write("%s.line = %s\n" % (unique_name, self.line))
           fp.write("%s.linecolor = %s\n" % (unique_name, self.linecolor))
           fp.write("%s.linewidth = %s\n" % (unique_name, self.linewidth))
           fp.write("%s.marker = %s\n" % (unique_name, self.marker))
           fp.write("%s.markercolor = %s\n" % (unique_name, self.markercolor))
           fp.write("%s.markersize = %s\n\n" % (unique_name, self.markersize))
    script.__doc__ = script.__doc__ % xmldocs.scriptdoc


#################################################################################
#        END OF FILE								#
#################################################################################
