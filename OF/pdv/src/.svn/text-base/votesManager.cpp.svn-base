#include "votesManager.h"

// SINGLETON initalizations
bool votesManager::instanceFlag = false;
votesManager* votesManager::single = NULL;

//----------------------------------------------

votesManager* votesManager::getInstance()
{
    if(! instanceFlag)
    {
        single = new votesManager();
        instanceFlag = true;
        return single;
    }else{
        return single;
    }
}

votesManager::votesManager(){
	
}

votesManager::~votesManager(){

}

void votesManager::setup()
{
	screenRenderOffline.allocate(ofGetWidth(),ofGetHeight(),GL_RGB);
	//loadFile();
	reset();
	myOfxCurrentTimer = &myOfxTimerVotation;
	ofAddListener(myOfxTimerVotation.TIMER_REACHED,this , &votesManager::timeOutVotation);
	ofAddListener(myOfxTimerPro.TIMER_REACHED,this , &votesManager::timeOutPRO);
	ofAddListener(myOfxTimerContra.TIMER_REACHED,this , &votesManager::timeOutCONTRA);
}

void votesManager::closeAllTimers(){
	myOfxTimerPro.stopTimer();
	myOfxTimerContra.stopTimer();
	myOfxTimerVotation.stopTimer();
}

void votesManager::timeOutVotation( ofEventArgs &e){
	ofEventArgs nextScreenArgs;
	ofNotifyEvent(nextScreenEvent,nextScreenArgs);
}

void votesManager::timeOutPRO( ofEventArgs &e){
	/*
	// stop Pro-timer
	myOfxTimerPro.stopTimer();
	// start Contra-timer
	float secondTimer= screensManager::getInstance()->getTimerContraInMiliSeconds();
	myOfxTimerContra.setup(secondTimer, false);
	myOfxTimerContra.startTimer();
	// give pointer to be current timer
	myOfxCurrentTimer = &myOfxTimerContra;
	*/
	float secondTimer= screensManager::getInstance()->getTimerInMiliSeconds();
	myOfxTimerVotation.setup(secondTimer, false);
	myOfxTimerVotation.startTimer();
	// give pointer to be current timer
	myOfxCurrentTimer = &myOfxTimerVotation;
}

void votesManager::timeOutCONTRA( ofEventArgs &e){
}

void votesManager::reset()
{
	startPerformance = false;
	currentVotationID = 1;
	currentQuestionID = 0;
	currentAnswerWinnerID = 0;
	xmlSession.clear();
	statement.erase(statement.begin(),statement.end());
}

bool votesManager::getIsDebate(){
	return screensManager::getInstance()->getScreenType()=="debate";
}

void votesManager::setNextVotationID()
{
	currentVotationID += 1;
}

string votesManager::getVotationID()
{
	string votationID = ofToString(currentVotationID-1);
	if(votationID.length()==1) votationID="00"+votationID;
	if(votationID.length()==2) votationID="0"+votationID;
	return votationID;
}

void votesManager::goNextVotation(){
	ofImage currentFrame;
	currentFrame.allocate(ofGetWidth(),ofGetHeight(), OF_IMAGE_COLOR);
	ofPixels px;
	screenRenderOffline.getTextureReference().readToPixels(px);
	currentFrame.setFromPixels(px);
	screensVotations.push_back(currentFrame);
}

void votesManager::drawFBOBegin(){
	screenRenderOffline.begin();
}

void votesManager::drawFBOEnd(){
	screenRenderOffline.end();
}

void votesManager::drawFBO(int x,int y){
	screenRenderOffline.draw(x,y);
}

int votesManager::getCurrentQuestionID(){
	return currentQuestionID-1;
}

string votesManager::getCurrentStatement(){
	string statement="";
	// get statement from vote winner option
	if(seatManager::getInstance()->getTotalYesVotes() <= seatManager::getInstance()->getTotalNoVotes() ){
		statement = screensManager::getInstance()->getStatementOptionQuestion(0);
	}else{
		statement = screensManager::getInstance()->getStatementOptionQuestion(1);
	}
	// in case statement is empty then use question
	if(statement ==""){
		statement = screensManager::getInstance()->getCurrentTextQuestion();
	}
	return statement;
}

void votesManager::startVotation(){
	if( getIsDebate() ){
		// SetTimer for debate
		float secondTimer= screensManager::getInstance()->getTimerProInMiliSeconds();
		myOfxTimerPro.setup(secondTimer, false);
		myOfxTimerPro.startTimer();
		myOfxTimerVotation.remove();
		// SetTimer in 0 in case make next
		// Give pointer to be current timer
		myOfxCurrentTimer = &myOfxTimerPro;
	}else{
		float secondTimer= screensManager::getInstance()->getTimerInMiliSeconds();
		myOfxTimerVotation.setup(secondTimer, false);
		myOfxTimerVotation.startTimer();
		// Give pointer to be current timer
		myOfxCurrentTimer = &myOfxTimerVotation;
	}
}

void votesManager::startCountDown(){
	float secondTimer=0;
	if(screensManager::getInstance()->getScreenType()=="debate" || screensManager::getInstance()->getScreenType()=="question" ){
		secondTimer = settingsManager::getInstance()->getSecondsResultTimer()*1000;
	}
	if(screensManager::getInstance()->getScreenType()=="statement" || screensManager::getInstance()->getScreenType()=="text"){
		secondTimer = screensManager::getInstance()->getTimerInMiliSeconds();	
	}
	// default time = 10 seconds
	if(secondTimer ==0){
		secondTimer=10000;
	}
	myOfxTimerVotation.setup(secondTimer, false);
	myOfxTimerVotation.startTimer();
	myOfxCurrentTimer = &myOfxTimerVotation;
}

void votesManager::nextScreen(){
	string typeScreen = screensManager::getInstance()->getScreenType();
		
	if( typeScreen=="question" || typeScreen=="debate" ){
		// save statement
		saveStatementVotation();
		// get new id to next screen though the winner in the votation
		if(seatManager::getInstance()->getTotalYesVotes() <= seatManager::getInstance()->getTotalNoVotes() ){
			screensManager::getInstance()->setIdQuestionNoWinner();
		}else{
			screensManager::getInstance()->setIdQuestionYesWinner();
		}
		// next id votation (internal from this session)
		setNextVotationID();
		saveScreenShowed();
	}
	if( typeScreen=="statement" || typeScreen=="text" ){
		screensManager::getInstance()->setScreenLinkAsSelectedScreen();
	}
	//save
	xmlSession.saveFile("mySettings.xml");
}

void votesManager::prepareDebate(){

}

int votesManager::getAnswerWinnerID(){
	string typeScreen = screensManager::getInstance()->getScreenType();
	if( typeScreen=="question" || typeScreen=="debate" ){
		if(seatManager::getInstance()->getTotalYesVotes() <= seatManager::getInstance()->getTotalNoVotes() ){
			currentAnswerWinnerID = 1;
		}else{
			currentAnswerWinnerID = 0;
		}
	}
	return currentAnswerWinnerID;
}

void votesManager::setStartPerformance(){
	reset();
	startPerformance = true;
	startTimeVotation = ofGetElapsedTimef();
}

float votesManager::getElapsedTimeVotation(){
	float temp =ofGetElapsedTimef()-startTimeVotation;
	if(temp<0 || !getStartPerformance()) temp=0;
	return temp;
}

bool votesManager::getStartPerformance(){
	return startPerformance;
}

void votesManager::setStartPerformance(bool value){
	startPerformance = value;
}

string votesManager::getResultStatement(){
	string temp = "";
	if(seatManager::getInstance()->getTotalYesVotes() <= seatManager::getInstance()->getTotalNoVotes() ){
		string dynamicTextMethod = screensManager::getInstance()->getNoQuestionDynamicTextMethod();
		if(dynamicTextMethod!=""){
			temp = screensManager::getInstance()->getStatementOptionQuestion(1);
			temp = seatManager::getInstance()->getDynamicStament(dynamicTextMethod,temp);
		}else{
			temp = screensManager::getInstance()->getStatementOptionQuestion(1);
		}
	}else{
		string dynamicTextMethod = screensManager::getInstance()->getYesQuestionDynamicTextMethod();
		if(dynamicTextMethod!=""){
			temp = screensManager::getInstance()->getStatementOptionQuestion(1);
			temp = seatManager::getInstance()->getDynamicStament(dynamicTextMethod,temp);
		}else{
			temp = screensManager::getInstance()->getStatementOptionQuestion(0);	
		}
	}
	// when is empty then show question
	if(temp == ""){
		temp = screensManager::getInstance()->getCurrentTextQuestion();
	}
	return temp;
}

void votesManager::saveStatementVotation(){
	string temp = "";
	bool result= false;
	if(seatManager::getInstance()->getTotalYesVotes() <= seatManager::getInstance()->getTotalNoVotes() ){
		temp = screensManager::getInstance()->getStatementOptionQuestion(1);
		result= false;
	}else{
		temp = screensManager::getInstance()->getStatementOptionQuestion(0);	
		result= true;
	}
	if(temp == ""){
		temp = screensManager::getInstance()->getCurrentTextQuestion();
		if(result){
			temp = "Sí."+temp; 	
		}else{
			temp = "No."+temp; 	
		}
	}

	statementInfo tempInfoStament;
	tempInfoStament.text = "#"+getVotationID()+" "+temp;
	tempInfoStament.id = "#"+getCurrentVotation3digits();
	tempInfoStament.result = result;
	statement.push_back(tempInfoStament);
}

string votesManager::getCurrentVotation3digits(){
	string idStatement = ofToString(currentVotationID-1);
	if(idStatement.length()==1) idStatement = "00"+idStatement;
	if(idStatement.length()==2) idStatement = "0"+idStatement;
	return idStatement;
}

int votesManager::getTotalStatements(){
	return statement.size();
}

string votesManager::getStatementText(int i){
	return statement[i].text;
}

string votesManager::getStatementId(int i){
	return statement[i].id;
}


bool votesManager::getStatementResult(int i){
	return statement[i].result;
}

ofFbo* votesManager::getFBO(){
	return &screenRenderOffline;
}

ofxTimer * votesManager::getCurrentTimer(){
	return myOfxCurrentTimer;
}

void votesManager::setPauseTimer(){
	if(myOfxCurrentTimer->getIsPause()){
		myOfxCurrentTimer->setDisabledTimerPause();
	}else{
		myOfxCurrentTimer->setActiveTimerPause();
	}
}

int votesManager::lastStoredScreenShowed(){
	ofxXmlSettings XMLtheaterInfo;
	XMLtheaterInfo.loadFile("settings.xml");
	int storedIdScreen = XMLtheaterInfo.getValue("settings:last-votation-id",0,0);	
	return storedIdScreen;
}

void votesManager::saveScreenShowed(){
	XMLscreenShowed.loadFile("settings.xml");
	string votationID = ofToString(currentVotationID);
	XMLscreenShowed.setValue("settings:last-votation-id", votationID );
	XMLscreenShowed.saveFile("settings.xml");
}

void votesManager::setVotationID(int id){
	currentVotationID = id;
}