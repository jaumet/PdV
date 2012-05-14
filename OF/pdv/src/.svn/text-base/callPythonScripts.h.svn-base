#ifndef _OFX_CALL_PYTHON_SCRIPT_
#define _OFX_CALL_PYTHON_SCRIPT_

#include "ofMain.h"

class callPythonScripts
{
// variables & methods for singleton
private:
static bool	instanceFlag;
static callPythonScripts *single;	
public: 
static callPythonScripts* getInstance();
// end singleton
public:
	callPythonScripts();
	~callPythonScripts();
	void callScript(string script);
private:
	string path;
};

#endif