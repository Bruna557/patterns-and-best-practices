# Design Patterns

## Creational design patterns
These design patterns are concerned with class instantiation.

- Factory Method: Defines an interface for creating an object, but lets subclasses decide which class to instantiate.
- Abstract Factory: Provides an interface for creating families of related or dependent objects without specifying their concrete classes.
- Singleton: Ensures that a class has only one instance and provides global point of access to it.
- Builder: Lets you construct complex objects step by step.

## Structural design patterns
These design patterns are concerned with class and object composition.

- Decorator: Add responsibilities to objects dynamically. The decorator both has and is the class that will be decorated, thus we can have multiple layers of decorators.
- Adapter: Match interfaces of different classes.
- Facade: A single class that represents an entire subsystem.

## Behavioral design patterns
These design patterns are concerned with communication between objects.

- Strategy: Defines a family of interchangeable algorithms that can be plugged into a client without changes to the client.
- Observer: A way of notifying state changes to a number of classes. The observable (subject) has methods to register and unregister observers and a method to notify the observers of a state change. We pass the observable to the observers so we can access state.
- Command: Encapsulates command requests as objects with methods execute and unexecute (thus, commands are undoable). The invoker can receive commands and call execute/unexecute methods that will affect the receiver.

## Notes
UML arrows:
![uml arrows](./uml-arrows.png)

- Direct association = has a
- Inheritance = is a

## References
[Refactoring Guru](https://refactoring.guru/design-patterns)

[Design Patterns by Source Making](https://sourcemaking.com/design_patterns)

[Design Patterns in Object Oriented Programming by Christopher Okhravi (playlist))](https://www.youtube.com/playlist?list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc)

[Geeks for Geeks](https://www.geeksforgeeks.org/)
