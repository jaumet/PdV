#ifndef _GUI_MANAGER_
#define _GUI_MANAGER_

#include "ofMain.h"
#include "ofEvents.h"
#include "ofxControlPanel.h"

class guiManager
{
// variables & methods for singleton
private:
static bool	instanceFlag;
static guiManager *single;	
public: 
static guiManager* getInstance();
// end singleton
public:
	guiManager();
	~guiManager();
	void setup();
	bool getVisible();
	void setVisible(bool value);
	void toggleVisible();
	
private:
	void update(ofEventArgs & args);
	void draw(ofEventArgs & args);
	void keyPressed(ofKeyEventArgs & args);
	void mouseDragged(ofMouseEventArgs & args);
	void mousePressed(ofMouseEventArgs & args);
	void mouseReleased(ofMouseEventArgs & args);
	ofxControlPanel gui;
	simpleFileLister lister;
	bool visible;
};

#endif