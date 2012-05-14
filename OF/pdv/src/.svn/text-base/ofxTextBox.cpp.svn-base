#include "ofxTextBox.h"

ofxTextBox::ofxTextBox()
{
	align = alignLeft;
	blinkCursor = false;
}

ofxTextBox::~ofxTextBox()
{
	
}

string ofxTextBox::getText()
{
	return allText;
}

void ofxTextBox::setText(string value){
	if(allText != value)
	{
		// store all text without split by lines
		allText =  value;
		recalculate(allText);
	}
}

void ofxTextBox::setBoxSize(int width, int height)
{
	this->width=width;
	this->height=height;
}

void ofxTextBox::recalculate(string text)
{
	// Delete all previus lines
	lines.erase(lines.begin(), lines.end());
	
	// calculate lines
	int allTextWidth = font->stringWidth(text); 
	if( allTextWidth<width ){
		line temp;
		temp.x = calculateLinePosition(text);
		temp.text = text;
		lines.push_back(temp); 
	}else{
		float numberLines = allTextWidth/width;
		string delimiter = " "; 
		vector<string> v = ofSplitString(text,delimiter);
		string tempLine;
		for(int i=0;i<v.size();i++){
			if(font->stringWidth(tempLine+" "+v[i])<width){
				if(tempLine!=""){ 
					tempLine += " "+v[i];
				}else{
					tempLine += v[i];
				}
			}else{
				line temp;
				temp.x = calculateLinePosition(tempLine);
				temp.text = tempLine;
				lines.push_back(temp);
				// add part was missing
				tempLine = v[i];
			}
		}
		// last line that didn't arrive to be fill
		if(tempLine!="")
		{
			line temp;
			temp.x = calculateLinePosition(tempLine);
			temp.text = tempLine;
			lines.push_back(temp);
		}
	}
	// Calculate position of the end text in last line
	calculatePosEndText();
}

void ofxTextBox::setBorderVisible(bool value)
{
	borderVisible = value;
}

void ofxTextBox::draw(int x, int y)
{
	ofPushMatrix();
	ofTranslate(x, y);
	
	for(int i=0;i<lines.size();i++){
		//cout << font.getLineHeight()*i << endl;
		font->drawString(lines[i].text,lines[i].x,font->getLineHeight()*(i+1));
	}
	
	if(blinkCursor){
		ofSetColor(255,255,255);
		ofRect(posEndText.x+3,posEndText.y-font->getLineHeight(), 2,font->getLineHeight());
	}
	ofPopMatrix();
}

void ofxTextBox::setAlignLeft()
{
	if(align != alignLeft){
		align = alignLeft;
		recalculate(allText);
	}else{
		align = alignLeft;
	}
}

void ofxTextBox::setAlignCenter()
{
	if(align != alignCenter){
		align = alignCenter;
		recalculate(allText);
	}else{
		align = alignCenter;
	}
}

void ofxTextBox::setAlignRight()
{
	if(align != alignRight){
		align = alignRight;
		recalculate(allText);
	}else{
		align = alignRight;
	}
	
}

void ofxTextBox::setFont(ofTrueTypeFont* fontPointer)
{
	font = fontPointer;
}

int ofxTextBox::getWidth()
{
	return width;
}

int ofxTextBox::getHeight()
{
	return height;
}

int ofxTextBox::getTextHeight()
{
	return (font->getLineHeight()*lines.size());
}

int ofxTextBox::calculateLinePosition(string text)
{
	int temp = 0;
	if(align == alignCenter){
		temp = (width*0.5f)-(font->stringWidth(text)/2);
	}else if(align == alignRight){
		temp = width-font->stringWidth(text); 
	}else if(align == alignLeft){
		temp = 0;
	}
	return temp;
}

void ofxTextBox::calculatePosEndText(){
	int posX = 0;
	if(lines.size()>0){
		posX = font->stringWidth(lines[lines.size()-1].text);
	}
	posEndText = ofVec2f(posX,font->getLineHeight()*lines.size());
}

ofVec2f ofxTextBox::getPosEndText(){
	return posEndText;
}

void ofxTextBox::enableCursor(){
	ofAddListener(myOfxTimerCursor.TIMER_REACHED,this , &ofxTextBox::timeCursor);
	myOfxTimerCursor.setup(500,true);
	myOfxTimerCursor.startTimer();
}

void ofxTextBox::disableCursor(){
	blinkCursor= false;
	myOfxTimerCursor.stopTimer();
	ofRemoveListener(myOfxTimerCursor.TIMER_REACHED,this , &ofxTextBox::timeCursor);
}

void ofxTextBox::timeCursor( ofEventArgs &e){
	blinkCursor=!blinkCursor;
}

void ofxTextBox::timeForType( ofEventArgs &e){
	if(allText!=allText_TypeWritter){
		if(allText_TypeWritter.length()<3){
			allText_TypeWritter += allText.substr(allText_TypeWritter.length(), 3);
		}else{
			allText_TypeWritter += allText.substr(allText_TypeWritter.length(), 1);
		}
		recalculate(allText_TypeWritter);
	}else{
		myOfxTimerTypeWritter.stopTimer();
		ofRemoveListener(myOfxTimerTypeWritter.TIMER_REACHED,this , &ofxTextBox::timeForType);
		finishWritting = true;
		// Notify when finish writting text
		ofEventArgs finishEvent;
		ofNotifyEvent(writtingFinishEvent,finishEvent);
	}
}

void ofxTextBox::setPlayTypingText(){
	allText_TypeWritter = "";
	lines.erase(lines.begin(), lines.end());
	ofAddListener(myOfxTimerTypeWritter.TIMER_REACHED,this , &ofxTextBox::timeForType);
	myOfxTimerTypeWritter.setup(25,true);
	myOfxTimerTypeWritter.startTimer();
	finishWritting = false;
}

int ofxTextBox::getLineHeight(){
	return font->getLineHeight();
}

void  ofxTextBox::removeLinesFromBack(int count){
	if(lines.size()>count){
		lines.erase(lines.end()-count, lines.end());
	}
}

int ofxTextBox::getTotalLines(){
	return lines.size();
}

bool ofxTextBox::getIsFinishWritting(){
	return finishWritting;
}