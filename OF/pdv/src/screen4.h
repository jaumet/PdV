#ifndef _OFX_SCREEN4_
#define _OFX_SCREEN4_

#include "screen.h"
#include "seatManager.h"

class screen4: public screen{
public:
	screen4();
	~screen4();

	void setup();
	void update();
	void draw(int x, int y);
	void load();
	void unload();
private:
	ofImage background;
};
#endif
