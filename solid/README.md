# SOLID Principles

## Single Responsability Principle
Gather together the things that change for the same reasons. Separate things that change for different reasons.

Every module should have one, and only one, reason to change.

Rule of thumb: if you can't describe what a function does without using words like "then" or "and", you might be violating the SRP.

## Open-Closed Principle
A Module should be open for extension but closed for modification.

Changes to behavior must be made by adding new code instead of modifying existing code.

## Liskov Substitution Principle
Every subclass or derived class should be substitutable for their base or parent class.

That requires the objects of your derived classes to behave in the same way as the objects of your base class. You can achieve that by following a few rules:
- An overridden method of a derived class needs to accept the same input parameter values as the method of the base class.
    - That means you can implement less restrictive validation rules, but you are not allowed to enforce stricter ones in your derived class.
- The return value of a method of the derived class needs to comply with the same rules as the return value of the method of the base class.
    - You can only decide to apply even stricter rules by returning a specific derived class of the defined return value, or by returning a subset of the valid return values of the base class.

## Interface Segregation Principle
A client should never be forced to implement an interface that it doesn't use, or clients shouldn't be forced to depend on methods they do not use.

Keep interfaces small so that users don't end up depending on things they don't need.

Several specific interfaces are better than one generic interface.

## Dependency Inverion Principle
High-level module must not depend on the low-level module, both should depend on abstractions.

Depends on the direction of abstraction. High level modules should not depend upon low level details.

Abstractions should not depend upon details. Details should depend upon abstractions.
