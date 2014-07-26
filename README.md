dragv2
======

Designed with problem creators in mind, dragv2 problems can be made _without writing any code_.
Features of dragv2 include:
* multi-touch/mobile support
* _very_ responsive
* draggables can be .svg files, among several other file types (.png, .jpg, ...)
* draggables start at a custom location on the drop image
* draggables snap to their initial location (reusable draggables delete when this happens)
* reset button is _always_ present
* simple and readable XML with JSInput
* easily create sophisticated custom grading methods (_via python code_)
* built-in capability for custom CSS formatting of draggables: default _and_ hover
* optional draggable expansion on hover (pre-written CSS)
* one special (readable) JSON file in the static folder per problem (on top of image files)

Quick Taste
-----------
[See examples here](http://www.lucasmorales.co/resources/relate/dragv2_examples.html "Made with Dragcreator!")

Dragcreator
===========

The best way to learn more about Dragcreator is to play around with it yourself.

[Dragcreator Online](http://www.lucasmorales.co/resources/relate/Dragcreator.html)

Dragcreator automatically creates the JSON file necessary for each dragv2 problem and generates the XML (with python grading) for edX. It also gives an intuitive interface for designing the solution, which then gets updates into the XML.