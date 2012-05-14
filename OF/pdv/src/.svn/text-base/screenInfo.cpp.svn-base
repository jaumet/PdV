#include "screenInfo.h"

screenInfo::screenInfo(){

}

screenInfo::~screenInfo(){
}

void screenInfo::setup(){
	actions.setFont(fontManager::getInstance()->getSmallTextFont());
	actions.setBoxSize(640,150);
	actions.setAlignLeft();

	midiConnected = false;
}

void screenInfo::update(){
}

void screenInfo::draw(int x, int y){
	// BEGIN DRAW IN FBO
	votesManager::getInstance()->drawFBOBegin();
	ofSetColor(70,70,70);
	ofRect(0,0,666,ofGetHeight());

	// ID current screen
	ofSetColor(0,0,0);
	ofRect(5,5,200,35);
	string idScreen = ofToString(screensManager::getInstance()->getSelectedScreen());
	ofSetColor(200,200,200);
	fontManager::getInstance()->setTextColor();
	fontManager::getInstance()->getSmallTextFont()->drawString("Id-screen:",10,30);

	ofSetColor(255,0,0);
	fontManager::getInstance()->setTextColor();
	fontManager::getInstance()->getSmallTextFont()->drawString(idScreen,150,30);

	// Draw action text
	ofSetColor(0,0,0);
	ofRect(5,45,650,150);
	string actionStr = "ACTIONS: ";
	actions.setText(actionStr+screensManager::getInstance()->getActionId());
	fontManager::getInstance()->setTextColor();
	actions.draw(10,50);
	ofSetColor(255,0,0);
	int actionStrSize = fontManager::getInstance()->getSmallTextFont()->stringWidth(actionStr);
	fontManager::getInstance()->getSmallTextFont()->drawString(actionStr,10,50+fontManager::getInstance()->getSmallTextFont()->getLineHeight());
	
	// Time
	string elapsedTime = "Time since started: "+getSecondsToTime(votesManager::getInstance()->getElapsedTimeVotation());
	ofSetColor(0,0,0);
	ofRect(245,5,300,35);
	ofSetColor(255,255,255);
	fontManager::getInstance()->getSmallTextFont()->drawString(elapsedTime,250,30);

	// Draw general timer
	float secondsGeneralTimer = votesManager::getInstance()->getCurrentTimer()->getTimeLeft()/1000;	
	string timeGeneralTimer = getSecondsToTime(secondsGeneralTimer);
	fontManager::getInstance()->setTextColor();
	fontManager::getInstance()->getSmallTextFont()->drawString("CountDown:"+timeGeneralTimer,10,230);
	
	// python script
	ofSetColor(255,255,0);
	string pythonScript = "Python call:"+screensManager::getInstance()->getScreenScript();
	fontManager::getInstance()->getSmallTextFont()->drawString(pythonScript,10,260);

	// display arduino-mouse connected
	if(arduinoMouseConnected){
		ofSetColor(0,255,0);
		string message = "Arduino conected";
		fontManager::getInstance()->getSmallTextFont()->drawString(message,10,290);
	}else{
		ofSetColor(255,0,0);
		string message = "Arduino disconected";
		fontManager::getInstance()->getSmallTextFont()->drawString(message,10,290);
	}
	// Split from arduino to midi
	ofSetColor(255,255,255);
	fontManager::getInstance()->getSmallTextFont()->drawString("|",250,290);
	// display Midi
	if(midiConnected){
	 ofSetColor(0,255,0);
		string message = "Midi conected";
		fontManager::getInstance()->getSmallTextFont()->drawString(message,280,290);
	}else{
		ofSetColor(255,0,0);
		string message = "Midi disconected";
		fontManager::getInstance()->getSmallTextFont()->drawString(message,280,290);
	}

	// END DRAW IN FBO
	votesManager::getInstance()->drawFBOEnd();

	// Draw FBO
	ofSetColor(255,255,255);
	votesManager::getInstance()->drawFBO(x,y);
}

void screenInfo::load(){
}

void screenInfo::unload(){

}

string screenInfo::getSecondsToTime(float seconds){
	string temp;
	float minutes = floor(seconds/60);
	seconds = seconds-(minutes*60);
	string secondsStr = ofToString(seconds,0);
	if(secondsStr.length()<2) secondsStr = "0"+secondsStr;
	string minutesStr = ofToString(minutes,0);
	if(minutesStr.length()<2) minutesStr = "0"+minutesStr;
	temp = minutesStr+":"+secondsStr;
	return temp;
}