---
title: Three things that Java could learn from C++
contributors:
  - Unknown
date: 2008-11-08T16:03:00.026000Z
lastmod: 2008-11-08T17:48:32.175000Z
weight: 50
tags:
  - old-post
  - Java
  - C++
  - programming
  - offtopic
---

This is a mostly off-topic rant that is being posted because I know that a good portion of our user base is composed of programmers.

Ever since I started working with Java, a few months ago, there have been many things that I have felt SHOULD be there, but aren't. Three, in particular, have always bothered me: **stack building**, **operator overloading**, and **const-correctness**. For the rest of this post, I will write snippets in both C++ and in Java to illustrate the differences.

**1. Stack building**
Creating objects on the heap is slow. Not only does it involve complex algorithms for determining WHERE to allocate the memory, but it also means that you're giving more work for the garbage collector when you're done with the object. In many situations, you will have to allocate many small temporary objects and then never use them again. Stack building makes this much faster, not to mention EASIER. Since Java lacks this feature, you are forced to use annoying workarounds (such as keeping pools of objects) if performance becomes critical.

*C++:*

```cpp
bool isNormalPointingAt(Vector3f a,Vector3f b, Vector3f dir) {
    return (a.cross(b).dot(dir) > 0);
}
```

*Java:*

```java
boolean isNormalPointingAt(Vector3f a,Vector3f b, Vector3f dir) {
    Vector3f normal = new Vector3f();
    normal.cross(a,b);
    return (normal.dot(dir) > 0);
}
```

In the above C++ example, the result of a.cross(b) is stored in a temporary variable in the stack, which is then dot()ed with dir. This could be done in Java if every such method allocated a new instance, but that would quickly become prohibitively slow.

**2. Operator Overloading**
This is a hotly debated topic. Many people insist that operator overloading can lead to unreadable code, if you start overloading operators to perform things that are illogical - but the same is true for method names, you can have an "add()" method that performs a multiplication. However, especially when working with mathematical vectors, operator overloading makes your code way easier to understand. Bellow is a method that, given 4 control points and a "t" parameter in the range \[0,1\], finds the corresponding point along a cubic Bézier curve:

*C++:*

```cpp
Vector3f getBezierCubicPoint(Vector3f a, Vector3f b,
        Vector3f c, Vector3f d, float t) {
    float u = 1-t;
    return (u*u*u)*a + (u*u*t)*b + (u*t*t)*c + (t*t*t)*d;
}
```

*Java:*

```java
Vector3f getBezierCubicPoint(Vector3f a, Vector3f b,
        Vector3f c, Vector3f d, float t) {
    float u = 1-t;
    Vector3f result = new Vector3f();
    Vector3f tmp = new Vector3f();
    tmp.scale(u*u*u, a);
    result.add(tmp);
    tmp.scale(u*u*t, b);
    result.add(tmp);
    tmp.scale(u*t*t, c);
    result.add(tmp);
    tmp.scale(t*t*t, d);
    result.add(tmp);
    return result;
}
```

\<sarcasm>Yeah, operator overloading really made that code a *lot* harder to read...\</sarcasm> Operator overloading is a tool. It can be very useful, as the example above demonstrates. I don't think that the language designers should remove that power from their users just because some won't know how to use it wisely.

**3. Const-correctness**
This one is possibly even more infuriating than the above two points, because it makes proper encapsulation of data much more complicated (not to mention slower). Consider this class in C++ and Java:

*C++:*

```cpp
class Body {
public:
    const Vector3f& getPosition() const {
        return position;
    }
    void setPosition(const Vector3f& pos) {
        position = pos;
    }

private:
    Vector3f position;
};
```

*Java:*

```java
public class Body {
    public Vector3f getPosition() {
        return position;
    }
    public void setPosition(Vector3f pos) {
        position = pos;
    }
    private Vector3f position = new Vector3f();
}
```

What's wrong with the above example? Here, let me illustrate it with some code:

*C++:*

```cpp
Body body;
body.getPosition().x = 5.0f; // compile error
```

*Java:*

```java
Body body = new Body();
body.getPosition().x = 5.0f; // works
```

Basically, Java allows you to modify an object's private member without using its "set" method! There is no way to declare that a given object is "read-only" (final only means that the reference can't be reassigned), so you can't prevent that code from working. If you really must be sure that position can't be modified like that, then you have to change your Java class to this:

*Java:*

```java
public class Body {
    public Vector3f getPosition() {
        return (Vector3f)position.clone();
    }
    public void setPosition(Vector3f pos) {
        position = (Vector3f)pos.clone();
    }
    private Vector3f position = new Vector3f();
}
```

In other words, you're now returning a full copy of the object. There are two major problems with this: First, the previous code STILL COMPILES. Since the user will have no way to tell if he's getting the actual position or a copy of it (unless he enters the original source or look in the documentation), he might try to modify the position that he got, and then be surprised that it doesn't work. The second problem is that returning an entire copy might be SLOW. What if, instead of a vector, it was an image? And what if it was accessed many times per second? This could quickly become impossibly slow. Java offers no solution for this problem.

(In case you're wondering, I also had to add a clone() to the set method, because otherwise the caller might call the set method, but keep the reference that it passed to it and modify it later.)

**Conclusion**
While many programs don't suffer from those problems much, there are certain applications that become a true nightmare to write and maintain - physics simulations or anything to do with vectorial math are the obvious example (that's why I kept using "Vector3f" classes above). If Java is supposed to be a cleaner and easier version of C++, then why is it that writing that sort of code in Java is much harder and much less robust?

I am aware that C# supports some (all?) of the above, but it doesn't as yet have as much portability as Java does. Indeed, it seems that C# is what Java SHOULD HAVE BEEN. If Sun doesn't start fixing this sort of thing in Java, then Microsoft just might take the lead. Meanwhile, I'll have to stick to writing that kind of abomination in Java. To think that it's much easier to code this sort of thing in
C++...
