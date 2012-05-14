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

#pragma once
#include "ofMain.h"

class ofxTimer {
	
protected: // modified: It was private
	
	// timer
	bool		bLoop;
	bool		bPauseTimer;
	bool		bStartTimer;
	float		delay;
	float		timer;
	float		timerStart;
	float		timeLeft;
	
	void update(ofEventArgs &e);

	bool bPauseTimer2;
	float	timeSinceStartPause;
public:
	ofEvent <ofEventArgs> TIMER_REACHED;
	
	ofxTimer();
	~ofxTimer();
	
	// ---------------------------------------
	void setup(float millSeconds, bool loopTimer);
	//void draw();
	
	// ---------------------------------------
	void setTimer(float millSeconds);
	void startTimer();
	void stopTimer();
	void loop(bool b);
	float getTimeLeft();
	void remove();
	// pause
	bool getIsPause();
	void setActiveTimerPause();
	void setDisabledTimerPause();
};