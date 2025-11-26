## 1. Instance Methods (as a reference point)

First, the “normal” method:

```python
class Something:
    def instance_method(self, x):
        ...
```

* You call it with: `obj.instance_method(10)`
* The first parameter is `self` → **the specific instance**.
* You use it when the method needs to **access or modify the data of that particular object** (its attributes).

With this in mind, the other two kinds of methods make more sense.

---

## 2. `@classmethod` — Class Methods

**Concept:**

> A *class method* is a method that works with **the class as a whole**, not with one specific object.

* Its first parameter is `cls` (by convention), not `self`.
* `cls` represents **the class itself** (e.g., `Person`, `Account`, `Order`), not an individual instance.

You use a class method **conceptually** when:

* What you are doing makes sense for **the entire class**, not just a single object.
* Typical situations:

  * You want **alternative constructors**, such as:

    * `from_json(...)`
    * `from_dict(...)`
    * `from_db_row(...)`
  * You want to work with **class-level information**:

    * counters,
    * configuration shared by all instances,
    * some registry of all created instances.

Key idea:

> If the method needs to know **which class** it is working with (especially with inheritance and subclasses), it usually makes sense to make it a `@classmethod`.

It is not “owned” by one object; it is “about the class”.

---

## 3. `@staticmethod` — Static Methods

**Concept:**

> A *static method* is simply a regular function that is *stored inside the class* for logical grouping, but it **does not need `self` or `cls`**.

* It does not receive the instance (`self`) or the class (`cls`) automatically.
* It behaves like a normal function defined at module level, but you place it inside the class to show that it is related to that class’s domain.

You use a static method **conceptually** when:

* The operation is related to the **same domain as the class**,
* but it **does not need to read or modify**:

  * any instance data,
  * or any class-level data.

Typical examples of what might be `@staticmethod`:

* Small utility or helper functions:

  * format validation,
  * small pure calculations,
  * transformations,
* that conceptually belong next to the class, but do not depend on the object or the class.

Key idea:

> It is about organization: grouping related functions inside the class, while making it clear that they do not depend on instance or class state.

---

## 4. Conceptual Comparison in One Shot

* **Instance method** (normal):
  Works with **a specific object** → needs `self`.
  It reads or modifies the state of that particular instance.

* **`@classmethod`**:
  Works with **the class itself** → receives `cls`.
  You use it when the logic is “about the class” (alternative constructors, class-wide behavior).

* **`@staticmethod`**:
  Does **not** depend on the class or any instance → no `self`, no `cls`.
  It is just a regular function you choose to place inside the class for logical grouping and clarity.
