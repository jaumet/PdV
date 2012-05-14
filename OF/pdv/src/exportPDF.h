#ifndef _OFX_EXPORTPDF_
#define _OFX_EXPORTPDF_

#include "ofMain.h"
#include "votesManager.h"
#include "screensManager.h"

class exportPDF
{
public:
	exportPDF();
	~exportPDF();
	void makePDF();
	void saveScreenImageForPDF();
private:
	ofImage currentScreen;
};

#endif