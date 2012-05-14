#ifndef _OFX_SCREEN0_
#define _OFX_SCREEN0_

//*******************************************************
// Circular visualization of all screens - Screen 
//*******************************************************

//#include "ofMain.h"
#include "screen.h"
#include "ofTrueTypeFont.h"
#include "testApp.h"
#include "ofxTextBox.h"
#include "votesManager.h"
#include <math.h>
#include "colorPalette.h"
#include "translateManager.h"

class screen0: public screen{
public:
	screen0();
	~screen0();
	void setup();
	void update();
	void draw(int x, int y);
	void load();
	void unload();
//private:
	//ofFbo screenRenderOffline;
};

#endif