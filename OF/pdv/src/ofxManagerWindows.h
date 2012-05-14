#ifndef _OFX_MOVE_WINDOWS_
#define _OFX_MOVE_WINDOWS_

#include "ofMain.h"
#include <windows.h> 

class ofxManagerWindows
{
// variables & methods for singleton
private:
static bool	instanceFlag;
static ofxManagerWindows *single;	
public: 
static ofxManagerWindows* getInstance();
// end singleton
public:
	ofxManagerWindows();
	~ofxManagerWindows();
	void setWindowInPosition(string name,int x,int y);
	void setWindowWithNoDecorated(string name);
	void setWindowWithDecorated(string name);
	void SetWindowAlwaysOnTop(string name);
	void SetFocus(string name);
private:
	bool ModifyWindowStyle(HWND hWnd, DWORD dwAdd, DWORD dwRemove, BOOL bEx);
};

#endif