# Design Patterns

## Creational design patterns
These design patterns are concerned with class instantiation.

- Factory Method: Defines an interface for creating an object, but lets subclasses decide which class to instantiate.
    - (PRO) Single Responsibility Principle: You can move the product creation code into one place in the program, making the code easier to support.
    - (PRO) Open/Closed Principle: You can introduce new types of products into the program without breaking existing client code.
    - (CON) The code may become more complicated.

- Abstract Factory: Provides an interface for creating families of related or dependent objects without specifying their concrete classes.
    - (PRO) You can be sure that the products you're getting from a factory are compatible with each other.
    - (PRO) Single Responsibility Principle: You can move the product creation code into one place in the program, making the code easier to support.
    - (PRO) Open/Closed Principle: You can introduce new types of products into the program without breaking existing client code.
    - (CON) The code may become more complicated since a lot of new interfaces and classes are introduced.

- Singleton: Ensures that a class has only one instance and provides global point of access to it.
    - (PRO): It can provide control access to some shared resource — for example, a database or a file.

- Builder: Lets you construct complex objects step by step.
    - (PRO) You can reuse the same construction code when building various representations of products.
    - (PRO) Single Responsibility Principle. You can isolate complex construction code from the business logic of the product.
    - (CON) The overall complexity of the code increases since the pattern requires creating multiple new classes.

## Structural design patterns
These design patterns are concerned with class and object composition.

- Decorator: Add responsibilities to objects dynamically. The decorator both has and is the class that will be decorated, thus we can have multiple layers of decorators.
    - (PRO) You can extend an object's behavior without making a new subclass.
    - (PRO) You can add or remove responsibilities from an object at runtime.
    - (PRO) You can combine several behaviors by wrapping an object into multiple decorators.
    - (PRO) Single Responsibility Principle: You can divide a monolithic class that implements many possible variants of behavior into several smaller classes.
    - (CON) It's hard to remove a specific wrapper from the wrappers stack.

- Adapter: Match interfaces of different classes.
    - (PRO) Single Responsibility Principle: You can separate the interface or data conversion code from the primary business logic of the program.
    - (PRO) Open/Closed Principle. You can introduce new types of adapters into the program without breaking the existing client code.
    - (CON)  The overall complexity of the code increases because you need to introduce a set of new interfaces and classes. Sometimes it's simpler just to change the service class so that it matches the rest of your code.

- Facade: A single class that represents an entire subsystem.
    - (PRO) You can isolate your code from the complexity of a subsystem.
    - (CON) A facade can become a god object coupled to all classes of an app.

    > A god object (sometimes also called an omniscient or all-knowing object) is an object that references a large number of distinct types, has too many unrelated or uncategorized methods, or some combination of both. The god object is an example of an anti-pattern and a code smell.

## Behavioral design patterns
These design patterns are concerned with communication between objects.

- Strategy: Defines a family of interchangeable algorithms that can be plugged into a client without changes to the client.
    - (PRO) You can replace inheritance with composition.
    - (PRO) You can swap algorithms used inside an object at runtime.
    - (PRO) Open/Closed Principle: You can introduce new strategies without having to change the context.
    - (CON) If you only have a couple of algorithms and they rarely change, there's no real reason to overcomplicate the program with new classes and interfaces that come along with the pattern.

- Observer: A way of notifying state changes to a number of classes. The observable (subject) has methods to register and unregister observers and a method to notify the observers of a state change. We pass the observable to the observers so we can access state.
    - (PRO) Open/Closed Principle: You can introduce new subscriber classes without having to change the publisher's code (and vice versa if there's a publisher interface).
    - (CON) Subscribers are notified in random order.

- Command: Encapsulates command requests as objects with methods execute and unexecute (thus, commands are undoable). The invoker can receive commands and call execute/unexecute methods that will affect the receiver.
    - (PRO) Single Responsibility Principle: You can decouple classes that invoke operations from classes that perform these operations.
    - (PRO) Open/Closed Principle: You can introduce new commands into the app without breaking existing client code.
    - (PRO) You can assemble a set of simple commands into a complex one.
    - (CON) The code may become more complicated since you're introducing a whole new layer between senders and receivers.

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
