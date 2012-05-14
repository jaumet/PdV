#ifndef _TRANSLATE_MANAGER_
#define _TRANSLATE_MANAGER_

#include "ofMain.h"
#include "ofxXmlSettings.h"
#include "settingsManager.h"


class translateManager
{
// variables & methods for singleton
private:
static bool	instanceFlag;
static translateManager *single;	
public: 
static translateManager* getInstance();
// end singleton
public:
	translateManager();
	~translateManager();
	void setup();
	string t(string word);
private:
	ofxXmlSettings xml;
	map<string,string> translations;
};

#endif