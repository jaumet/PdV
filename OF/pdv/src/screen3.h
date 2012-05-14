#ifndef _OFX_SCREEN3_
#define _OFX_SCREEN3_

//*******************************************************
// Statement or Text - Screen 
//*******************************************************

#include "screen.h"
#include "ofxTween.h"
#include "screensManager.h"
#include "fontManager.h"
#include "ofxTextBox.h"
#include "votesManager.h"
#include "translateManager.h"

class screen3: public screen{
public:
	screen3();
	~screen3();

	void setup();
	void update();
	void draw(int x, int y);
	void load();
	void unload();
	void finishedWritteStament(ofEventArgs& e);

private:
	string getSecondsToTime(float  miliseconds);
	ofxTextBox statement;
	ofImage background;
	ofSoundPlayer audioPassScreen;
};
#endif
