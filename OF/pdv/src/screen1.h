#ifndef _OFX_SCREEN1_
#define _OFX_SCREEN1_

//*******************************************************
// Question - Screen 
//*******************************************************

#include "screen.h"
#include "ofxTextBox.h"
#include "screensManager.h"
#include "fontManager.h"
#include "votesManager.h"
#include "screensManager.h"
#include "colorPalette.h"
#include "translateManager.h"

class screen1: public screen{
public:
	screen1();
	~screen1();

	void setup();
	void update();
	void draw(int x, int y);
	void load();
	void unload();
	void finishedWritteStament(ofEventArgs& e);
private:
	ofSoundPlayer audioPassScreen;
	string getSecondsToTime(float  miliseconds);
	ofxTextBox question;
	ofxTextBox pro;
	ofxTextBox contra;
	//ofFbo screenRenderOffline;
	ofImage background;
	ofImage yesNoIcons;
	//statementDisplayList myStatementDisplayList;
};
#endif
