#include "ofxVirtualMouse.h"

// SINGLETON initalizations
bool ofxVirtualMouse::instanceFlag = false;
ofxVirtualMouse* ofxVirtualMouse::single = NULL;

//----------------------------------------------

ofxVirtualMouse* ofxVirtualMouse::getInstance()
{
    if(! instanceFlag)
    {
        single = new ofxVirtualMouse();
        instanceFlag = true;
        return single;
    }else{
        return single;
    }
}

ofxVirtualMouse::ofxVirtualMouse()
{
	
}

ofxVirtualMouse::~ofxVirtualMouse()
{

}

void ofxVirtualMouse::sendMouseDownAndUp(int x, int y)
{
   POINT pt;
   pt.x = x;
   pt.y = y;
   SetCursorPos(pt.x, pt.y);
   mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0);  
   mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0);  
}

