#include "colorPalette.h"

// SINGLETON initalizations
bool colorPalette::instanceFlag = false;
colorPalette* colorPalette::single = NULL;

//----------------------------------------------

colorPalette* colorPalette::getInstance()
{
    if(! instanceFlag)
    {
        single = new colorPalette();
        instanceFlag = true;
        return single;
    }else{
        return single;
    }
}

colorPalette::colorPalette(){
}

colorPalette::~colorPalette(){

}

void colorPalette::setGreen(){
	ofSetColor(49,168,51);
}

void colorPalette::setRed(){
	ofSetColor(244,21,15);
}

void colorPalette::setYellow(){
	ofSetColor(242,220,39);
}


void colorPalette::setYesVotesColor(){
	setGreen();
}

void colorPalette::setNoVotesColor(){
	setRed();
}

void colorPalette::setAbsVotesColor(){
	setYellow();
}

void colorPalette::setBlockSeatsColor(){
	ofSetColor(255,255,255);
}

void colorPalette::setManVotesColor(){
	ofSetColor(137,233,254);
}
void colorPalette::setWomanVotesColor(){
	ofSetColor(237,14,234);
}

void colorPalette::setUnknowVotesColor(){
	ofSetColor(254,183,11);
}

void colorPalette::setGenderLineColor(){
	ofSetColor(255,255,255);
}

