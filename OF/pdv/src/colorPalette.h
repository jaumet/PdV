#ifndef _COLOR_PALETTE_
#define _COLOR_PALETTE_

#include "ofMain.h"

class colorPalette
{
// variables & methods for singleton
private:
static bool	instanceFlag;
static colorPalette *single;	
public: 
static colorPalette* getInstance();
// end singleton
public:
	colorPalette();
	~colorPalette();
	void setGreen();
	void setRed();
	void setYellow();
	void setYesVotesColor();
	void setNoVotesColor();
	void setAbsVotesColor();
	void setBlockSeatsColor();
	void setManVotesColor();
	void setWomanVotesColor();
	void setUnknowVotesColor();
	void setGenderLineColor();
};
#endif