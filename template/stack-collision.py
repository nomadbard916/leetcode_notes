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
"""
