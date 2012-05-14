/***********************************************************************
 
 Copyright (c) 2009, Todd Vanderlin, www.vanderlin.cc
 
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 ***********************************************************************/

#include "ofxTimer.h"

ofxTimer::ofxTimer() {
	
}

ofxTimer::~ofxTimer() {
	printf("*** Timer Destroyed ***\n");
}

// ---------------------------------------

void ofxTimer::setup(float millSeconds, bool loopTimer) {
	
	bLoop		= loopTimer;
	bPauseTimer = false;
	
	//timer
	bStartTimer = true;
	delay		= millSeconds;	// mill seconds
	timer		= 0;
	timerStart	= 0;
	
	//events
	ofAddListener(ofEvents.update, this, &ofxTimer::update);
	
	bPauseTimer2 = false;
}
void ofxTimer::remove(){
	timeLeft		= 0;
	bPauseTimer = true;
	ofRemoveListener(ofEvents.update, this, &ofxTimer::update);
}
// ---------------------------------------
void ofxTimer::loop(bool b) {
	bLoop = b;
}

// ---------------------------------------
void ofxTimer::update(ofEventArgs &e) {
	if(!bPauseTimer) {
		if(bStartTimer) {
			bStartTimer = false;
			timerStart  = ofGetElapsedTimef();
			bPauseTimer2 = false;
		}
		
		float time = ofGetElapsedTimef() - timerStart;
		time *= 1000.0;		
		timeLeft = (delay-time);

		if(time >= delay) {
			if(!bLoop) bPauseTimer = true;
			bStartTimer = true;
			static ofEventArgs timerEventArgs;
			ofNotifyEvent(TIMER_REACHED, timerEventArgs, this);
		}
		
		// Add to follow the timer value
		//timer = time - delay; 
	}
}

// ---------------------------------------
void ofxTimer::setTimer(float millSeconds) {
	delay = millSeconds;
}

void ofxTimer::startTimer() {
	bPauseTimer = false;
}

void ofxTimer::stopTimer() {
	bPauseTimer = true;
}

float ofxTimer::getTimeLeft(){
	return timeLeft>0?timeLeft:0;
}

bool ofxTimer::getIsPause(){
	return bPauseTimer2;
}

void ofxTimer::setActiveTimerPause(){
	stopTimer();
	bPauseTimer2 = true;
	timeSinceStartPause = ofGetElapsedTimef();
}

void ofxTimer::setDisabledTimerPause(){
	if(bPauseTimer2){
		float elapsedTimePause = ofGetElapsedTimef()-timeSinceStartPause;
		timerStart += elapsedTimePause;
	}
	startTimer();
	bPauseTimer2 = false;
}

