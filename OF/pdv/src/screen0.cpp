#include "screen0.h"

screen0::screen0(){
}

screen0::~screen0(){
}

void screen0::setup(){

}

void screen0::update(){
}

void screen0::draw(int x, int y){
	// BEGIN DRAW IN FBO
	votesManager::getInstance()->drawFBOBegin();
	ofBackground(0,0,0);
	ofSetColor(0,0,0);
	ofRect(0,0,(ofGetWidth()-666),ofGetHeight());
	float radius = 360;
	int totalScreens = screensManager::getInstance()->getCurrentTotalScreens();
	float partionForScreen = ofDegToRad((360.0f/((float)totalScreens)));
	ofVec2f centerPos = ofVec2f((ofGetWidth()-666)/2,ofGetHeight()/2);
	int partCount = 0;

	// draw part show already
	if(screensManager::getInstance()->getScreenArId()>0){
		ofSetColor(50,50,50);
		ofBeginShape();
		for(int i=0; i<screensManager::getInstance()->getScreenArId()+1; i++){
			float degrees = partionForScreen * (float)i;
			ofVec2f pos = ofVec2f( radius*cos(degrees) , radius*sin(degrees) );
			float radius3 = radius-65;
			ofVec2f point1 = ofVec2f( centerPos.x+(radius3*cos(degrees)) , centerPos.y+(radius3*sin(degrees)) );
			ofVertex(point1.x,point1.y);
		}
		for(int i=screensManager::getInstance()->getScreenArId(); i>=0; i--){
			float degrees = partionForScreen * (float)i;
			ofVec2f pos = ofVec2f( radius*cos(degrees) , radius*sin(degrees) );
			float radius4 = radius+50;
			ofVec2f point2 = ofVec2f( centerPos.x+(radius4*cos(degrees)) , centerPos.y+(radius4*sin(degrees)) ); 
			ofVertex(point2.x,point2.y);
		}
		ofEndShape();
	}
	
	for(int i=0;i<totalScreens;i++){
		// position in circle
		float degrees = partionForScreen * (float)i;
		ofVec2f pos = ofVec2f( radius*cos(degrees) , radius*sin(degrees) );
		
		// Part
		int secondPart = screensManager::getInstance()->getTotalScreensPart1();
		int thirdPart = (screensManager::getInstance()->getTotalScreensPart1()+screensManager::getInstance()->getTotalScreensPart2());
		
		if( i==0 || secondPart==i || thirdPart==i ){
			if( secondPart==i || thirdPart==i ){ ofSetColor(190,190,190); }else{ofSetColor(255,255,255);}
			float radius3 = radius-65;
			float radius4 = radius+50;
			ofVec2f point1 = ofVec2f( centerPos.x+(radius3*cos(degrees)) , centerPos.y+(radius3*sin(degrees)) );
			ofVec2f point2 = ofVec2f( centerPos.x+(radius4*cos(degrees)) , centerPos.y+(radius4*sin(degrees)) ); 
			ofLine( point1.x, point1.y, point2.x, point2.y);
			double angleText = ofRadToDeg(atan2(point2.y-point1.y, point2.x-point1.x));
			// get total screens per part
			int totalScreensThisPart = 0;
			
			ofSetColor(190,190,190);
			if(i==0){
				totalScreensThisPart = screensManager::getInstance()->getTotalScreensPart1();
				partCount = 1;
			}else if(i==secondPart){
				totalScreensThisPart = screensManager::getInstance()->getTotalScreensPart2();
				partCount = 2;
			}else if(i==thirdPart){
				totalScreensThisPart = screensManager::getInstance()->getTotalScreensPart3();
				partCount = 3;
			}
			
			string partText = translateManager::getInstance()->t("Part");
			partText[0] = toupper(partText[0]);
			string textThisPart = partText+" "+ofToString(partCount)+"["+ofToString(totalScreensThisPart)+"]";
			int withTextThisPart = fontManager::getInstance()->getPixelFont()->stringWidth(textThisPart);
			// draw text of the part
			ofPushMatrix();
			ofTranslate(point1.x,point1.y);	
			ofRotate(angleText);
			ofTranslate(-5-withTextThisPart,0);
			fontManager::getInstance()->getPixelFont()->drawString(textThisPart,0,0);
			ofPopMatrix();
			
		}
		
		// type by colors
		string typeScreen = screensManager::getInstance()->getIdScreenType(i);
		if(typeScreen=="question"){
			ofSetColor(5,143,249);
		}else if(typeScreen=="debate"){
			ofSetColor(255,255,0);
		}else if(typeScreen=="statement"){
			ofSetColor(255,0,240);
		}else{
			ofSetColor(255,0,0);
		}
		
		// represent
		ofEllipse(centerPos.x+pos.x,centerPos.y+pos.y,2,2);
		
		float radius2 = radius+10;
		ofVec2f pos2 = ofVec2f( radius2*cos(degrees) , radius2*sin(degrees) );
		ofLine(centerPos.x+pos.x,centerPos.y+pos.y,centerPos.x+pos2.x,centerPos.y+pos2.y);
		
		// error Link
		if( screensManager::getInstance()->getScreenHasBrokenLinks(i) ){
			ofSetColor(255,0,0);
			float radius3 = radius-5;
			float radius4 = radius-150;
			ofVec2f pos3 = ofVec2f( radius3*cos(degrees) , radius3*sin(degrees) );
			ofVec2f pos4 = ofVec2f( radius4*cos(degrees) , radius4*sin(degrees) );
			ofVec2f point1 = ofVec2f(centerPos.x+pos3.x,centerPos.y+pos3.y);
			ofVec2f point2 = ofVec2f(centerPos.x+pos4.x,centerPos.y+pos4.y);
			ofLine(point1.x,point1.y,point2.x,point2.y);

			string idScreen = ofToString(screensManager::getInstance()->getIdScreen(i));
		
			double angleText = ofRadToDeg(atan2(point2.y-point1.y, point2.x-point1.x))+180.0f;
			//int stringSize = fontManager::getInstance()->getPixelFont()->stringWidth(idScreen);
			ofVec2f posText = ofVec2f(centerPos.x+pos4.x,centerPos.y+pos4.y);
			ofPushMatrix();
			ofTranslate(posText.x,posText.y);	
			ofRotate(angleText);
			ofTranslate(0,-2);
			fontManager::getInstance()->getPixelFont()->drawString(idScreen,0,0);
			ofPopMatrix();
		}
		// show current screen
		if(screensManager::getInstance()->getScreenArId()==i){
			ofSetColor(255,255,255);
			float radius3 = radius-65;
			float radius4 = radius+50;
			ofVec2f pos3 = ofVec2f( radius3*cos(degrees) , radius3*sin(degrees) );
			ofVec2f pos4 = ofVec2f( radius4*cos(degrees) , radius4*sin(degrees) );
			ofVec2f point1 = ofVec2f(centerPos.x+pos3.x,centerPos.y+pos3.y);
			ofVec2f point2 = ofVec2f(centerPos.x+pos4.x,centerPos.y+pos4.y);
			ofLine(point1.x,point1.y,point2.x,point2.y);

			string idScreen = ofToString(screensManager::getInstance()->getIdScreen(i));
			double angleText = ofRadToDeg(atan2(point2.y-point1.y, point2.x-point1.x));
			int stringSize = fontManager::getInstance()->getPixelFont()->stringWidth(idScreen);
			ofVec2f posText = ofVec2f(centerPos.x+pos3.x,centerPos.y+pos3.y);
			ofPushMatrix();
			ofTranslate(posText.x,posText.y);	
			ofRotate(angleText);
			ofTranslate(60-stringSize,-5);
			fontManager::getInstance()->getPixelFont()->drawString(idScreen,0,0);
			ofPopMatrix();
		}

	}
	// Title
	ofSetColor(255,255,255);
	string textTitle = "Screens PdV";
	int stringHalfSize = fontManager::getInstance()->getPixelFont()->stringWidth(textTitle)/2;
	fontManager::getInstance()->getPixelFont()->drawString(textTitle,(ofGetWidth()-666)/2-stringHalfSize,ofGetHeight()/2);
	
	// Total screens
	ofSetColor(90,90,90);
	string totalScreensStr = "total screens:"+ofToString(totalScreens);
	totalScreensStr[0] = toupper(totalScreensStr[0]);
	stringHalfSize = fontManager::getInstance()->getPixelFont()->stringWidth(totalScreensStr)/2;
	fontManager::getInstance()->getPixelFont()->drawString(totalScreensStr,(ofGetWidth()-666)/2-stringHalfSize,(ofGetHeight()/2)+15);

	// Total errors
	if( settingsManager::getInstance()->getDebugMode() ){
		int totalErrors = screensManager::getInstance()->getTotalXMLErrors();
		if(totalErrors>0){
			ofSetColor(255,0,0);
			stringHalfSize = fontManager::getInstance()->getPixelFont()->stringWidth("Total XML errors:"+ofToString(totalErrors))/2;
			fontManager::getInstance()->getPixelFont()->drawString("Total XML errors:"+ofToString(totalErrors),(ofGetWidth()-666)/2-stringHalfSize,(ofGetHeight()/2)+30);
		}else{
			ofSetColor(0,255,0);
			stringHalfSize = fontManager::getInstance()->getPixelFont()->stringWidth("There is no XML errors")/2;
			fontManager::getInstance()->getPixelFont()->drawString("There is no XML errors",(ofGetWidth()-666)/2-stringHalfSize,(ofGetHeight()/2)+30);
		}
	}

	ofPushMatrix();
	ofTranslate(20,-20);
	string typeScreen = "";
	// 
	ofSetColor(5,143,249);
	ofRect(15,ofGetHeight()-65,10,10);
	typeScreen = "question";
	fontManager::getInstance()->getPixelFont()->drawString(typeScreen,30,ofGetHeight()-55);
	
	ofSetColor(255,255,0);
	ofRect(15,ofGetHeight()-50,10,10);
	typeScreen = "debate";
	fontManager::getInstance()->getPixelFont()->drawString(typeScreen,30,ofGetHeight()-40);
	
	ofSetColor(255,0,240);
	ofRect(15,ofGetHeight()-35,10,10);
	typeScreen = "statement or text";
	fontManager::getInstance()->getPixelFont()->drawString(typeScreen,30,ofGetHeight()-25);
	
	if( settingsManager::getInstance()->getDebugMode() ){
		ofSetColor(255,0,0);
		ofRect(15,ofGetHeight()-20,10,10);
		typeScreen = "errors";
		fontManager::getInstance()->getPixelFont()->drawString(typeScreen,30,ofGetHeight()-10);
	}
	ofPopMatrix();

	
	// END DRAW IN FBO
	votesManager::getInstance()->drawFBOEnd();

	// Draw FBO
	ofSetColor(255,255,255);
	votesManager::getInstance()->drawFBO(x,y);
}

void screen0::load(){
}

void screen0::unload(){
}


