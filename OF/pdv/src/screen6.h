#ifndef _OFX_SCREEN6_
#define _OFX_SCREEN6_

//*******************************************************
// Voting Screen 
//*******************************************************
#include "screen.h"

class screen6: public screen{
public:
	screen6();
	~screen6();

	void setup();
	void update();
	void draw(int x, int y);
	void load();
	void unload();
};
#endif
