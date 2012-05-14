#include "ofxVirtualKeyboard.h"

// SINGLETON initalizations
bool ofxVirtualKeyboard::instanceFlag = false;
ofxVirtualKeyboard* ofxVirtualKeyboard::single = NULL;

//----------------------------------------------

ofxVirtualKeyboard* ofxVirtualKeyboard::getInstance()
{
    if(! instanceFlag)
    {
        single = new ofxVirtualKeyboard();
        instanceFlag = true;
        return single;
    }else{
        return single;
    }
}

ofxVirtualKeyboard::ofxVirtualKeyboard(){

}

ofxVirtualKeyboard::~ofxVirtualKeyboard(){
}

void ofxVirtualKeyboard::sendKey(char c){
	
	keybd_event(VkKeyScan(c),0,KEYEVENTF_EXTENDEDKEY,0);
	keybd_event(VkKeyScan(c),0,KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP,0);
	
}

void ofxVirtualKeyboard::setNumLock( bool bState )
{
      BYTE keyState[256];

      GetKeyboardState((LPBYTE)&keyState);
      if( (bState && !(keyState[VK_NUMLOCK] & 1)) ||
          (!bState && (keyState[VK_NUMLOCK] & 1)) )
      {
      // Simulate a key press
         keybd_event( VK_NUMLOCK,
                      0x45,
                      KEYEVENTF_EXTENDEDKEY | 0,
                      0 );

      // Simulate a key release
         keybd_event( VK_NUMLOCK,
                      0x45,
                      KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP,
                      0);
	  }
}