stack = []

for element in sequence:
    # 1. Can this element collide with stack top?
    if no_collision_possible(element, stack):
        stack.append(element)  # just push, move on
        continue

    # 2. Resolve collisions
    survivor = True
    while survivor and collision_possible(stack, element):
        outcome = resolve(stack[-1], element)  # who wins?

        if outcome == "stack_wins":
            survivor = False  # current destroyed
        elif outcome == "current_wins":
            stack.pop()  # stack top destroyed, keep fighting
        elif outcome == "mutual":
            stack.pop()
            survivor = False  # both destroyed

    # 3. Survivor settles
    if survivor:
        stack.append(element)

return stack

"""

**This skeleton is the same across ALL stack collision problems.** Only the specifics change: what triggers collision, and how resolution works.

## 📚 Taxonomy: Types of Stack Collision

There are fundamentally different *flavors* of collision. Learning to distinguish them is the key skill.

---

### Type 1: Opposing Direction Collision
**"Two forces moving toward each other, strength determines winner"**

The purest form. Elements have literal or metaphorical *direction*, and only opposite directions collide.
Pattern:  [→ → → ← ← ]
              ^^^^^^^^^^^
              collision zone
735 - Asteroid Collision is the textbook example you already solved.
Recognition keywords: direction, moving, right/left, positive/negative, size, destroy

Type 2: Matching Pair Collision
"An opening element waits on the stack for its matching closer"
Here the collision isn't about strength — it's about matching. The stack holds "open" elements, and when a "close" element arrives, it either matches or invalidates.
e.g. # 20 Valid Parentheses

Type 3: Trigger Collision
"One element type acts as a command that destroys/modifies the other"
No strength comparison. One type always wins — it's a trigger, not a fight.
e.g. 2390, 71

Type 4: Adjacent Same-Element Collision
"Identical neighbors destroy each other"
No opposing types here — instead, sameness triggers the collision.
e.g. 1047,

Type 5: Operator-Operand Collision
"Operators consume operands from the stack to produce new values"
Not destruction — it's transformation. Operands sit on the stack waiting, operators collide with them and produce a result.
e.g. 150,

🎯 The One Unifying Principle
Across all five types, the stack's role is always the same:

The stack holds elements that are "waiting" — waiting to be matched, waiting to be destroyed, waiting to be consumed. The moment a new element arrives that can interact with them, the collision resolves.

When you see a problem, use this decision tree:
```
Does the problem involve sequential elements that interact?
│
├─ Do elements have two opposing types/directions?
│   ├─ Does strength/size determine winner?  →  Type 1 (Asteroid)
│   └─ Does matching determine outcome?      →  Type 2 (Parentheses)
│
├─ Does one element type act as a command?   →  Type 3 (Trigger)
│
├─ Do identical adjacent elements cancel?    →  Type 4 (Adjacent Duplicate)
│
└─ Do operators consume operands?            →  Type 5 (RPN)
```

## 📊 Summary Table
```
┌────────┬─────────────────────┬──────────────┬─────────────────────┬─────────────┐
│ Type   │ Collision Trigger   │ Resolution   │ Key Signal          │ Example     │
├────────┼─────────────────────┼──────────────┼─────────────────────┼─────────────┤
│ Type 1 │ Opposite directions │ Size wins    │ "destroy/collision" │ 735         │
│ Type 2 │ Open meets Close    │ Match or fail│ "valid/balanced"    │ 20          │
│ Type 3 │ Command meets Data  │ Command wins │ "remove/undo"       │ 2390, 71    │
│ Type 4 │ Same meets Same     │ Mutual dest. │ "adjacent/duplicate"│ 1047        │
│ Type 5 │ Operator meets Data │ Transform    │ "evaluate/compute"  │ 150         │
└────────┴─────────────────────┴──────────────┴─────────────────────┴─────────────┘
"""
