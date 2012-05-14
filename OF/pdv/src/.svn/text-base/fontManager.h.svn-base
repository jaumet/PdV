#ifndef _FONT_MANAGER_
#define _FONT_MANAGER_

#include "ofMain.h"

class fontManager
{
// variables & methods for singleton
private:
static bool	instanceFlag;
static fontManager *single;	
public: 
static fontManager* getInstance();
// end singleton
public:
	fontManager();
	~fontManager();
	void setup();
	ofTrueTypeFont* getQuestionFont();
	ofTrueTypeFont* getTitleFont();
	ofTrueTypeFont* getTextFont();
	ofTrueTypeFont* getSmallTextFont();
	ofTrueTypeFont* getPixelFont();
	void setTextColor();
private:
	ofTrueTypeFont* font_title;
	ofTrueTypeFont* font_text;
	ofTrueTypeFont* font_pixel;
	ofTrueTypeFont* font_question;
	ofTrueTypeFont* font_smalltext;
	ofTrueTypeFont font_Monaco_25;
	ofTrueTypeFont font_Monaco_24;
	ofTrueTypeFont font_Monaco_16;
	ofTrueTypeFont font_Monaco_12;
	ofTrueTypeFont font_Pixelade_14;
	ofColor* textColor;
	ofColor textColorWhite;
	ofColor textColorBlack;
};

#endif

