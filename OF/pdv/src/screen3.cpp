#include "screen3.h"

screen3::screen3(){
	ofAddListener(statement.writtingFinishEvent,this,&screen3::finishedWritteStament);
}

screen3::~screen3(){
	ofRemoveListener(statement.writtingFinishEvent,this,&screen3::finishedWritteStament);
}

void screen3::setup(){
	statement.setFont(fontManager::getInstance()->getQuestionFont());
	statement.setBoxSize(900, 200);
	statement.enableCursor();
	background.loadImage("png/linesclean.png");
	cout << "load sound path:"<< ofToDataPath( settingsManager::getInstance()->getSoundPassScreen() ) << endl;
	audioPassScreen.loadSound( settingsManager::getInstance()->getSoundPassScreen() );
	audioPassScreen.setLoop(false);
}

void screen3::update(){
	
}

void screen3::draw(int x, int y){
	// 
	votesManager::getInstance()->drawFBOBegin();

	ofSetColor(255,255,255);
	background.draw(0,0);

	string temp = "";
	int posX = 38;
	// TEXTO
	temp = translateManager::getInstance()->t("text");
	std::transform(temp.begin(), temp.end(),temp.begin(), ::toupper);
	fontManager::getInstance()->setTextColor();
	fontManager::getInstance()->getTextFont()->drawString(temp,38,54);

	posX += fontManager::getInstance()->getTextFont()->stringWidth(temp)+20;

	// votation ID
	if(settingsManager::getInstance()->getTypeIdScreenDisplay()==1){
		string idScreen = ofToString(screensManager::getInstance()->getSelectedScreen());
		temp = "#"+idScreen;
	}else{
		temp = "#"+votesManager::getInstance()->getVotationID();
	}
	fontManager::getInstance()->setTextColor();
	fontManager::getInstance()->getTextFont()->drawString(temp,posX,54);
	posX += fontManager::getInstance()->getTextFont()->stringWidth(temp)+20;

	// ORDEN DEL DIA
	temp = "//"+translateManager::getInstance()->t("daySchedule");
	fontManager::getInstance()->setTextColor();
	fontManager::getInstance()->getTextFont()->drawString(temp,posX,54);
	
	// countdown
	if( screensManager::getInstance()->setOFHaveThis("countDownViz") ){
		float secondsGeneralTimer = votesManager::getInstance()->myOfxTimerVotation.getTimeLeft();
		string timeGeneralTimer = getSecondsToTime(secondsGeneralTimer);
		fontManager::getInstance()->setTextColor();
		fontManager::getInstance()->getTitleFont()->drawString(timeGeneralTimer,36,127);
	}

	// draw STATEMENT
	fontManager::getInstance()->setTextColor();
	statement.draw(36,135);

	votesManager::getInstance()->drawFBOEnd();

	ofSetColor(255,255,255);
	votesManager::getInstance()->drawFBO(x,y);
}

void screen3::finishedWritteStament(ofEventArgs& e){
	
}

void screen3::load(){
	// static text
	string questionText = screensManager::getInstance()->getCurrentTextQuestion();
	// dynamic text
	string dynamicTextMethod = screensManager::getInstance()->getDynamicTextMethod();
	if(dynamicTextMethod!=""){
		questionText = seatManager::getInstance()->getDynamicStament(dynamicTextMethod,questionText);
	}

	statement.setText(questionText);
	votesManager::getInstance()->startCountDown();

	// sound pass screen
	audioPassScreen.play();
}

void screen3::unload(){

}

string screen3::getSecondsToTime(float miliseconds){
	float seconds = miliseconds/1000;
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