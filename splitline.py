#!/usr/bin/python
str = "Line1-a b c d e f\n Line2- a b c\n\n Line4- a b c d";
print str.splitlines( );
print str.splitlines( 0 );
print str.splitlines( 3 );
print str.splitlines( 4 );
print str.splitlines( 5 );