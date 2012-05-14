#ifndef _OFX_VIRTUALMOUSE_
#define _OFX_VIRTUALMOUSE_

#include "ofMain.h"
#include <windows.h> 

class ofxVirtualMouse
{
// variables & methods for singleton
private:
static bool	instanceFlag;
static ofxVirtualMouse *single;	
public: 
static ofxVirtualMouse* getInstance();
// end singleton
public:
	ofxVirtualMouse();
	~ofxVirtualMouse();
	void sendMouseDownAndUp(int x, int y);
};

#endif
