#include "screen1.h"

screen1::screen1(){
	ofAddListener(question.writtingFinishEvent,this,&screen1::finishedWritteStament);
}

screen1::~screen1(){
	ofRemoveListener(question.writtingFinishEvent,this,&screen1::finishedWritteStament);
}

void screen1::setup(){
	question.setFont(fontManager::getInstance()->getQuestionFont());
	question.setBoxSize(900, 200);
	question.setAlignLeft();
	question.enableCursor();

	pro.setFont(fontManager::getInstance()->getSmallTextFont());
	pro.setBoxSize(400,185);
	pro.setAlignLeft();

	contra.setFont(fontManager::getInstance()->getSmallTextFont());
	contra.setBoxSize(400,185);
	contra.setAlignLeft();

	background.loadImage("png/linesclean.png");
	yesNoIcons.loadImage("png/yesNo.png");

	audioPassScreen.loadSound( settingsManager::getInstance()->getSoundPassScreen() );
	audioPassScreen.setLoop(false);
}

void screen1::update(){
	
}

void screen1::draw(int x, int y){
	votesManager::getInstance()->drawFBOBegin();

	// Draw background
	ofSetColor(255,255,255);
	background.draw(0,0);
	
	string temp="";
	int posX = 38;

	// TEXTO
	if( votesManager::getInstance()->getIsDebate() ){
		temp = translateManager::getInstance()->t("DEBATE");
	}else{
		temp = translateManager::getInstance()->t("QUESTION");
	}
	std::transform(temp.begin(), temp.end(),temp.begin(), ::toupper);
	fontManager::getInstance()->setTextColor();
	fontManager::getInstance()->getTextFont()->drawString(temp,38,54);

	posX += fontManager::getInstance()->getTextFont()->stringWidth(temp)+20;

	// Votation ID
	string idScreen = ofToString(screensManager::getInstance()->getSelectedScreen());
	if(settingsManager::getInstance()->getTypeIdScreenDisplay()==1){
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

	// Draw general timer
	float secondsGeneralTimer = votesManager::getInstance()->myOfxTimerVotation.getTimeLeft();
	if(question.getIsFinishWritting() && secondsGeneralTimer>0 ){	
		string timeGeneralTimer = getSecondsToTime(secondsGeneralTimer);
		fontManager::getInstance()->setTextColor();
		fontManager::getInstance()->getTitleFont()->drawString(timeGeneralTimer,36,127);
	}

	// Draw question
	fontManager::getInstance()->setTextColor();
	question.draw(36,135);

	// DEBATE
	if( votesManager::getInstance()->getIsDebate() ){
		
		// Draw PRO / CONTRA TITLE
		ofSetColor(255,255,255);
		string timeForDebate = translateManager::getInstance()->t("timeForDebate");
		std::transform(timeForDebate.begin(), timeForDebate.end(),timeForDebate.begin(), ::toupper);
		fontManager::getInstance()->getTextFont()->drawString("//"+timeForDebate,36,388);
		
		// Draw time PRO
		float secondsPRO = votesManager::getInstance()->myOfxTimerPro.getTimeLeft();
		if(secondsPRO>0){
			string timePRO = getSecondsToTime(secondsPRO);
			fontManager::getInstance()->setTextColor();
			fontManager::getInstance()->getTextFont()->drawString(timePRO,36,418);
		}
		
	// PRO/CONTRA QUESTIONS
	}else if( !votesManager::getInstance()->getIsDebate() && screensManager::getInstance()->getScreenHaveTextInProContra() ){
		
		// Draw PRO / CONTRA TITLE
		ofSetColor(0,255,0);
		string proStr = translateManager::getInstance()->t("pro");
		std::transform(proStr.begin(), proStr.end(),proStr.begin(), ::toupper);
		fontManager::getInstance()->getTextFont()->drawString("//"+proStr,36,388);
		ofSetColor(255,0,0);
		string contraStr = translateManager::getInstance()->t("contra");
		std::transform(contraStr.begin(), contraStr.end(),contraStr.begin(), ::toupper);
		fontManager::getInstance()->getTextFont()->drawString("//"+contraStr,500,388);
		
		// DRAW TEXT 
		fontManager::getInstance()->setTextColor();
		pro.draw(36,388+15);
		contra.draw(500,388+15);
	}

	// DRAW YES and NO ICON
	if( !votesManager::getInstance()->getIsDebate() ){
		// Image
		ofSetColor(255,255,255);
		yesNoIcons.draw(36,600);
		// Text
		ofSetColor(255,255,255);
		fontManager::getInstance()->getTextFont()->drawString(screensManager::getInstance()->getTextAnswerYes(),75,632);
		ofSetColor(255,255,255);
		fontManager::getInstance()->getTextFont()->drawString(screensManager::getInstance()->getTextAnswerNo(),75,672);
	}

	// END DRAW IN FBO
	votesManager::getInstance()->drawFBOEnd();

	// Draw FBO
	ofSetColor(255,255,255);
	votesManager::getInstance()->drawFBO(x,y);
}

string screen1::getSecondsToTime(float miliseconds){
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

void screen1::finishedWritteStament(ofEventArgs& e){
	//votesManager::getInstance()->startVotation();
}

void screen1::load(){
	string questionText = screensManager::getInstance()->getCurrentTextQuestion();
	string dynamicTextMethod = screensManager::getInstance()->getDynamicTextMethod();
	if(dynamicTextMethod!=""){
		questionText = seatManager::getInstance()->getDynamicStament(dynamicTextMethod,questionText);
	}

	question.setFont(fontManager::getInstance()->getQuestionFont());
	question.setText( questionText );
	votesManager::getInstance()->startVotation();

	// PRO/CONTRA SET TEXT
	if( screensManager::getInstance()->getScreenHaveTextInProContra() ){
		pro.setText(screensManager::getInstance()->getScreenProText());
		contra.setText(screensManager::getInstance()->getScreenContraText());
	}
	// sound pass screen
	audioPassScreen.play();
}

void screen1::unload(){
	
}