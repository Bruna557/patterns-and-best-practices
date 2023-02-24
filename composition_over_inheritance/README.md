# Composition over Inheritance
Favor composition (has a) over inheritance (is a).

Inheritance is when you design your types based on what they are.
Composition is when you design your types based on what they do.

Inheritance is good for sharing behavior vertically but not horizontaly.

              ----
              |  |  superclass
              ----
           /        \    vertical share
          v          v
       ----          ----
       |  |  ---->   |  |   subclasses
       ----          ----
         horizontal share
