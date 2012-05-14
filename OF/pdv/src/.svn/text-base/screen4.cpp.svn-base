#include "screen4.h"

screen4::screen4(){

}

screen4::~screen4(){

}

void screen4::setup(){

}

void screen4::update(){

}

void screen4::draw(int x, int y){
	for(int i=0;i<seatManager::getInstance()->getTotalSeats();i++ ){
		ofVec2f temp = seatManager::getInstance()->getSeatArToPixel(i);
		ofSetColor(255,0,0);
		ofEllipse(temp.x,temp.y, 50, 50);
	}
}

void screen4::load(){
}

void screen4::unload(){
}