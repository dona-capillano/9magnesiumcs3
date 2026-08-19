# Computational Thinking Exercise

## Smart School Canteen Queue

**Name:** Dona Capillano
**Section:** Magnesium    
**Date:** August 19, 2026  

---

## Step 1: Identify the Big Problem

### Main Problem
The school canteen queue moves very slowly during lunch break because students order manually, and staff cannot track available food stock.
--- 
## Step 2: Identify the Sub-Problems
1. Students take too long to decide what food to buy at the counter.
2. Food items run out unexpectedly without staff knowing beforehand.
3. The line gets crowded because some order and pickup food at the same place.
---
## Step 3: Apply Computational Thinking Skills
| Sub-Problem | CT Skill | Proposed Solution |
| Slow decision making | Abstraction | Show a simple menu board with only prices and available items so students choose faster. |
| Unexpected stockouts | Pattern Recognition | Track item sales to automatically count remaining stock and give low-stock warnings. |
| Crowded counter line | Decomposition | Strictly split the counter into two separate lines: one for paying and one for picking up food. |
---
## Step 4: Algorithmic Solution
## Selected Sub-Problem 
Crowded Line / Separating Order & Pick-Up
### Pseudocode
START
    Receive student order at Order Counter
    Generate unique Queue Number
    Print order receipt with Queue Number
    Send order details to Kitchen Screen
    
  WHEN kitchen finishes preparing food:
        Display Queue Number on Pick-Up Screen
        Call student to Pick-Up Counter
        Hand over food and mark order COMPLETE
END
