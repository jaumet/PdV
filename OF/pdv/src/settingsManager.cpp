#include "settingsManager.h"

// SINGLETON initalizations
bool settingsManager::instanceFlag = false;
settingsManager* settingsManager::single = NULL;

//----------------------------------------------

settingsManager* settingsManager::getInstance()
{
    if(! instanceFlag)
    {
        single = new settingsManager();
        instanceFlag = true;
        return single;
    }else{
        return single;
    }
}


settingsManager::settingsManager(){

}

settingsManager::~settingsManager(){

}

void settingsManager::setup(){
	xml.loadFile("settings.xml");//
	xml.pushTag("settings");
	selectedLanguage = xml.getValue("language-selected","",0);	
	idStartScreen = xml.getValue("id-screen-start",0,0);
	sunVoteButton.x = xml.getValue("x-sunvote-start-button",0,0);	
	sunVoteButton.y = xml.getValue("y-sunvote-start-button",0,0);	
	windowOFforFocus.x = xml.getValue("x-windowOFforFocus",0,0);	
	comPortName = xml.getValue("comPortName","",0);	
	secondsResultTimer = xml.getValue("secondsResultTimer",0,0);	
	totalSeats = xml.getValue("totalSeats",0,0);	
	screenPositionX = xml.getValue("screenPositionX",0,0);	
	dataPath = xml.getValue("data-path","",0);
	soundPassScreen = xml.getValue("sound-pass-screen","",0);
	typeIdScreenDisplay = xml.getValue("type-id-screen-display",0,0);
	midikey_start_key = xml.getValue("midikey-start-key",0,0);
	midikey_pause_key  = xml.getValue("midikey-pause-key",0,0);
	midikey_next_key  = xml.getValue("midikey-next-key",0,0);
	midikey_start_value = xml.getValue("midikey-start-value",0,0);
	midikey_pause_value  = xml.getValue("midikey-pause-value",0,0);
	midikey_next_value  = xml.getValue("midikey-next-value",0,0);

	isDebugMode = (xml.getValue("debug","yes",0)=="yes");
}

bool settingsManager::getDebugMode(){
	return isDebugMode;
}

int settingsManager::getMidikeyStartKey(){
	return midikey_start_key;
}

int settingsManager::getMidikeyPauseKey(){
	return midikey_pause_key;
}

int settingsManager::getMidikeyNextKey(){
	return midikey_next_key;
}

int settingsManager::getMidikeyStartValue(){
	return midikey_start_value;
}

int settingsManager::getMidikeyPauseValue(){
	return midikey_pause_value;
}

int settingsManager::getMidikeyNextValue(){
	return midikey_next_value;
}

int settingsManager::getTypeIdScreenDisplay(){
	return typeIdScreenDisplay;
}

int settingsManager::getSecondsResultTimer(){
	return secondsResultTimer;
}

// en, es, fr
string settingsManager::getLanguage(){
	return selectedLanguage;	
} 

int settingsManager::getTotalSeats(){
	return totalSeats;
}

int settingsManager::getIdStartScreen(){
	return idStartScreen;
}

int settingsManager::getScreenPositionX(){
	return screenPositionX;
}

ofVec2f settingsManager::getPositionStartButtonSunVote(){
	return sunVoteButton;
}
/*
ofVec2f settingsManager::getPositionWindowOF(){
	return windowOFforFocus;
}
*/

string settingsManager::getComPortName(){
	return comPortName;
}

string settingsManager::getDataPath(){
	return dataPath;
}

string settingsManager::getSoundPassScreen(){
	return soundPassScreen; 
}