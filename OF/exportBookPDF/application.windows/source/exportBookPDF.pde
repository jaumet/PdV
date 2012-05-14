/**
 * RandomBook
 * 
 * Creates a 768 page book of random lines.
 */

import processing.pdf.*;

PGraphicsPDF pdf;
File[] files;
String path;
 
void setup() {
  size(1024, 768);
  // Path
  path = "C:\\PdV\\data\\png_export_export\\";
  println("Listing all filenames in a directory: ");
  String[] filenames = listFileNames(path);
  println(filenames);
  
  println("\nListing info about all files in a directory: ");
  files = listFiles(path);
  
  pdf = (PGraphicsPDF)beginRecord(PDF, "pdv_Book.pdf");
  beginRecord(pdf);
}

void draw() {  
  background(255);
  
  for (int i = 0; i < files.length; i++) {
    File f = files[i];    
    println("Name: " + f.getName());
    println("Is directory: " + f.isDirectory());
    println("Size: " + f.length());
    String lastModified = new Date(f.lastModified()).toString();
    println("Last Modified: " + lastModified);
    println("-----------------------");
    
    if(!f.getName().equals(".svn")){
      String imagePath = path+f.getName();
      println(imagePath);
      PImage img = loadImage(imagePath);
      image(img,0,0);
      if( (i+1) < files.length)pdf.nextPage(); 
    }
  }
  
  endRecord();
  exit();  // Quit
}

// This function returns all the files in a directory as an array of Strings  
String[] listFileNames(String dir) {
  File file = new File(dir);
  if (file.isDirectory()) {
    String names[] = file.list();
    return names;
  } else {
    // If it's not a directory
    return null;
  }
}

// This function returns all the files in a directory as an array of File objects
// This is useful if you want more info about the file
File[] listFiles(String dir) {
  File file = new File(dir);
  if (file.isDirectory()) {
    File[] files = file.listFiles();
    return files;
  } else {
    // If it's not a directory
    return null;
  }
}
