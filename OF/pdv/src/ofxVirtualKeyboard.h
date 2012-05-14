#ifndef _OFX_VIRTUAL_KEYBOARD_
#define _OFX_VIRTUAL_KEYBOARD_

#include "ofMain.h"
#include <windows.h>

class ofxVirtualKeyboard
{
// variables & methods for singleton
private:
static bool	instanceFlag;
static ofxVirtualKeyboard *single;	
public: 
static ofxVirtualKeyboard* getInstance();
// end singleton
public:
	ofxVirtualKeyboard();
	~ofxVirtualKeyboard();
	void setNumLock( bool bState );
	void sendKey(char c);
};

#endif