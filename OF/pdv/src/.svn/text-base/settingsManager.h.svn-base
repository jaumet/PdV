#ifndef _SETTINGS_MANAGER_
#define _SETTINGS_MANAGER_

#include "ofMain.h"
#include "ofxXmlSettings.h"

class settingsManager
{
// variables & methods for singleton
private:
static bool	instanceFlag;
static settingsManager *single;	
public: 
static settingsManager* getInstance();
// end singleton
public:
	settingsManager();
	~settingsManager();
	void setup();
	string getLanguage(); // en, es, fr
	int getIdStartScreen();
	ofVec2f getPositionStartButtonSunVote();
	string getComPortName();
	int getSecondsResultTimer();
	int getTotalSeats();
	int getScreenPositionX();//(1280-666)
	string getDataPath();
	string getSoundPassScreen();
	int getTypeIdScreenDisplay();
	int getMidikeyStartKey();
	int getMidikeyPauseKey();
	int getMidikeyNextKey();
	int getMidikeyStartValue();
	int getMidikeyPauseValue();
	int getMidikeyNextValue();
	bool getDebugMode();
private:
	bool isDebugMode;
	int midikey_start_key;
	int midikey_next_key;
	int midikey_pause_key;
	int midikey_start_value;
	int midikey_next_value;
	int midikey_pause_value;
	int typeIdScreenDisplay;
	int screenPositionX;
	int totalSeats;
	int secondsResultTimer;
	string comPortName;
	int idStartScreen;
	string selectedLanguage;
	ofxXmlSettings xml;
	ofVec2f sunVoteButton;
	ofVec2f windowOFforFocus;
	string dataPath;
	string soundPassScreen;
};

#endif