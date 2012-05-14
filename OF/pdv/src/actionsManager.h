#ifndef _ACTIONS_MANAGER_
#define _ACTIONS_MANAGER_

#include "ofMain.h"
#include "ofxXmlSettings.h"
#include "ofxVirtualKeyboard.h"
#include "ofxVirtualMouse.h"

enum actionType{mouseEvent,keyEvent,callMethod};

struct actionItem{
	actionType type;
	int x;
	int y;
	string keys;
	float sleep;
	string methodName;
};

struct action{
	string name;
	string filename;
	vector<actionItem> actionList;
};

class actionsManager
{
public:
	actionsManager();
	~actionsManager();
	void setup();
	void loadAction(string file);
	void playAction(string file);
private:
	ofxXmlSettings xml;
	map<string,action> actionsList;
};

#endif