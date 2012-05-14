#ifndef _OFX_SCREEN2_
#define _OFX_SCREEN2_

//*******************************************************
// Result MAP - Screen 
//*******************************************************


#include "screen.h"
#include "ofMain.h"

#include "ofxTextBox.h"
#include "seatManager.h"
#include "fontManager.h"
#include "votesManager.h"
#include "colorPalette.h"
#include "translateManager.h"

class screen2: public screen{
public:
	screen2();
	~screen2();
	void setup();
	void update();
	void draw(int x, int y);
	void load();
	void unload();
	void finishedWritteStament(ofEventArgs& e);
private:
	ofSoundPlayer audioPassScreen;

	ofImage background;
	ofxTextBox statement;
	ofImage genderSymbols;
	void drawTypeList(string type, vector<string> list, int &posX, int &posY, int ballSize);
	
	void drawGenderBars(int posXBars, int totalBarSize);
	void drawBars(int posXBars, int totalBarSize);

	void drawBar(int &posX, int &posY, int totalVotes, int totalBarSize, float totalCitizens);

	void drawTheatherSeats(int ballSize);
	void drawListPeopleTypes(int posX, int posY, int ballSize);
	void drawLabelBar(string name, int posX,int posY);
	void drawTitleTextBar(int posX, int posY);
};
#endif
