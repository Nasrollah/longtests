Point(1) = {0, 0, 0, 50000000};
Point(2) = {440000, 0, 0, 500000000};
Point(3) = {0, 440000, 0, 500000000};
Point(4) = {-440000, 0, 0, 50000000};
Point(5) = {0, -440000, 0, 50000000};
Circle(1) = {2, 1, 3};
Circle(2) = {3, 1, 4};
Circle(3) = {4, 1, 5};
Circle(4) = {5, 1, 2};
Line Loop(6) = {1, 2, 3, 4};
Plane Surface(6) = {6};
Physical Line(4) = {1, 2, 3, 4};
Physical Surface(7) = {6};
Field[1] = MathEval;
Field[1].F = "(Fabs(380000-(x*x+y*y)^0.5)/5+20000)/0.2625";
Background Field = 1;
Mesh.CharacteristicLengthExtendFromBoundary = 0;
