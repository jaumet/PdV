#ifndef _OFX_SCREEN_INFO_
#define _OFX_SCREEN_INFO_

//*******************************************************
// Circular visualization of all screens - Screen 
//*******************************************************


#include "screen.h"
#include "ofTrueTypeFont.h"
#include "ofxTextBox.h"
#include "votesManager.h"
#include "fontManager.h"
#include "seatManager.h"
#include "screensManager.h"

class screenInfo: public screen{
public:
	screenInfo();
	~screenInfo();
	void setup();
	void update();
	void draw(int x, int y);
	void load();
	void unload();
	bool arduinoMouseConnected;
	bool midiConnected;
private:
	ofFbo screenRenderOffline;
	ofxTextBox actions;
	string getSecondsToTime(float seconds);
};

#endif