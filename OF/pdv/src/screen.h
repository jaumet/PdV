#ifndef _OFX_SCREEN_
#define _OFX_SCREEN_

#include "settingsManager.h"
#include <ctype.h>

class screen
{
public:
	virtual void load()=0;
	virtual void unload()=0;
	virtual void setup()=0;
	virtual void update()=0;
	virtual void draw(int x, int y)=0;
	//virtual void getFBO()=0;
};

#endif