#include "fontManager.h"

// SINGLETON initalizations
bool fontManager::instanceFlag = false;
fontManager* fontManager::single = NULL;

//----------------------------------------------

fontManager* fontManager::getInstance()
{
    if(! instanceFlag)
    {
        single = new fontManager();
        instanceFlag = true;
        return single;
    }else{
        return single;
    }
}

fontManager::fontManager(){
}

fontManager::~fontManager(){

}

void fontManager::setup(){
	font_Pixelade_14.loadFont("fonts/PIXELADE.TTF",14);
	font_Monaco_12.loadFont("fonts/MONACO.TTF",12, true, true);
	font_Monaco_16.loadFont("fonts/MONACO.TTF",16, true, true);
	font_Monaco_24.loadFont("fonts/MONACO.TTF",24, true, true);
	font_Monaco_25.loadFont("fonts/MONACO.TTF",25, true, true);

	// default
	font_smalltext= &font_Monaco_12;
	font_text = &font_Monaco_16;
	font_pixel = &font_Pixelade_14;
	font_title = &font_Monaco_24;
	font_question = &font_Monaco_25;
	textColorWhite = ofColor(255,255,255); 
	textColorBlack = ofColor(0,0,0);
	textColor = &textColorWhite;
}

ofTrueTypeFont* fontManager::getSmallTextFont(){
	return font_smalltext;
}

ofTrueTypeFont* fontManager::getTextFont(){
	return font_text;
}

ofTrueTypeFont* fontManager::getPixelFont(){
	return font_pixel;
}

ofTrueTypeFont* fontManager::getTitleFont(){
	return font_title;
}

void fontManager::setTextColor(){
	ofSetColor(textColor->r,textColor->g,textColor->b);
}

ofTrueTypeFont* fontManager::getQuestionFont(){
	return font_question;
}
