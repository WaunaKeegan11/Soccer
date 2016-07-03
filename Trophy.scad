sphere(d = 40);
// this will create a high resolution sphere with a 2mm radius
sphere($fn=200); 
// will also create a 2mm high resolution sphere but this one 
// does not have as many small triangles on the poles of the sphere
color("gold") sphere(40);
sphere($fa=100, $fs=0.1);
cylinder(h=100, r=10, center=false);