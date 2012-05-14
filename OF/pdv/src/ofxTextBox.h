#ifndef _OFX_TEXTBOX_
#define _OFX_TEXTBOX_

#include "ofMain.h"
#include "ofxTimer.h"

enum alignMode{alignCenter,alignLeft,alignRight};

struct line{
	string text;
	int x;
};

class ofxTextBox{
public:
	ofxTextBox();
	~ofxTextBox();
	string getText();
	void setText(string value);
	void setBoxSize(int width, int height);
	void draw(int x, int y);
	void setAlignLeft();
	void setAlignCenter();
	void setAlignRight();
	void setFont(ofTrueTypeFont* fontPointer);
	int getWidth();
	int getHeight();
	void setBorderVisible(bool value);
	ofVec2f getPosEndText();
	void calculatePosEndText();
	void enableCursor();
	void disableCursor();
	void setPlayTypingText();
	int getTextHeight();
	int getLineHeight();
	void removeLinesFromBack(int count);
	int getTotalLines();
	bool getIsFinishWritting();
	ofEvent<ofEventArgs> writtingFinishEvent;

private:
	int calculateLinePosition(string text);
	void recalculate(string text);
	vector<line> lines;
	string allText;
	string allText_TypeWritter;
	alignMode align;
	ofTrueTypeFont* font;
	int width;
	int height;
	bool borderVisible;
	ofVec2f posEndText;
	bool blinkCursor;
	ofxTimer myOfxTimerCursor;
	ofxTimer myOfxTimerTypeWritter;
	void timeCursor( ofEventArgs &e);
	void timeForType( ofEventArgs &e);
	bool finishWritting;
	
};
#endif
