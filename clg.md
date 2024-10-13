Here is a collection of algorithms for linked list operations written in the format you requested. Each algorithm has its corresponding overflow condition where necessary, and the steps are clearly outlined.

---

### **1. Insertion at the Beginning**

1. **Allocate memory for a new node**:  
   - Set `NEW-NODE = malloc(sizeof(Node))`.

2. **Check for memory overflow**:  
   - If `NEW-NODE == NULL`, print "Overflow" and exit the algorithm.

3. **Set the data for the new node**:  
   - `NEW-NODE->DATA = VAL`.

4. **Link the new node to the current list**:  
   - Set `NEW-NODE->NEXT = HEAD`.

5. **Update the head to point to the new node**:  
   - Set `HEAD = NEW-NODE`.

6. **Exit the algorithm**.

---

### **2. Insertion at the End**

1. **Allocate memory for a new node**:  
   - Set `NEW-NODE = malloc(sizeof(Node))`.

2. **Check for memory overflow**:  
   - If `NEW-NODE == NULL`, print "Overflow" and exit the algorithm.

3. **Set the data for the new node**:  
   - `NEW-NODE->DATA = VAL`.

4. **Set the `NEXT` pointer of the new node to NULL**:  
   - `NEW-NODE->NEXT = NULL`.

5. **If the list is empty** (HEAD == NULL):  
   - Set `HEAD = NEW-NODE`.
   - Exit the algorithm.

6. **Traverse to the last node**:  
   - Set `TEMP = HEAD`.
   - While `TEMP->NEXT != NULL`, move to the next node (`TEMP = TEMP->NEXT`).

7. **Link the last node to the new node**:  
   - Set `TEMP->NEXT = NEW-NODE`.

8. **Exit the algorithm**.

---

### **3. Insertion at a Specific Position**

1. **Allocate memory for a new node**:  
   - Set `NEW-NODE = malloc(sizeof(Node))`.

2. **Check for memory overflow**:  
   - If `NEW-NODE == NULL`, print "Overflow" and exit the algorithm.

3. **Set the data for the new node**:  
   - `NEW-NODE->DATA = VAL`.

4. **If position is 0**:  
   - Set `NEW-NODE->NEXT = HEAD`.
   - Set `HEAD = NEW-NODE`.
   - Exit the algorithm.

5. **Traverse to the (position - 1)-th node**:  
   - Set `TEMP = HEAD`.
   - For `i = 0` to `position - 1`, move to the next node (`TEMP = TEMP->NEXT`).

6. **If `TEMP == NULL` (position out of bounds)**:  
   - Print "Position out of bounds" and exit the algorithm.

7. **Link the new node in the list**:  
   - Set `NEW-NODE->NEXT = TEMP->NEXT`.
   - Set `TEMP->NEXT = NEW-NODE`.

8. **Exit the algorithm**.

---

### **4. Deletion from the Beginning**

1. **Check if the list is empty** (HEAD == NULL):  
   - If `HEAD == NULL`, print "Underflow" and exit the algorithm.

2. **Set TEMP = HEAD**.

3. **Update the head**:  
   - Set `HEAD = HEAD->NEXT`.

4. **Free the old head node**:  
   - Free `TEMP`.

5. **Exit the algorithm**.

---

### **5. Deletion from the End**

1. **Check if the list is empty** (HEAD == NULL):  
   - If `HEAD == NULL`, print "Underflow" and exit the algorithm.

2. **If the list has only one node** (HEAD->NEXT == NULL):  
   - Free `HEAD`.
   - Set `HEAD = NULL`.
   - Exit the algorithm.

3. **Traverse to the second last node**:  
   - Set `TEMP = HEAD`.
   - While `TEMP->NEXT->NEXT != NULL`, move to the next node (`TEMP = TEMP->NEXT`).

4. **Free the last node**:  
   - Free `TEMP->NEXT`.

5. **Set `TEMP->NEXT = NULL`**.

6. **Exit the algorithm**.

---

### **6. Deletion from a Specific Position**

1. **Check if the list is empty** (HEAD == NULL):  
   - If `HEAD == NULL`, print "Underflow" and exit the algorithm.

2. **If position is 0**:  
   - Set `TEMP = HEAD`.
   - Set `HEAD = HEAD->NEXT`.
   - Free `TEMP`.
   - Exit the algorithm.

3. **Traverse to the (position - 1)-th node**:  
   - Set `TEMP = HEAD`.
   - For `i = 0` to `position - 1`, move to the next node (`TEMP = TEMP->NEXT`).

4. **If `TEMP == NULL` or `TEMP->NEXT == NULL` (position out of bounds)**:  
   - Print "Position out of bounds" and exit the algorithm.

5. **Set `NODE-TO-DELETE = TEMP->NEXT`**.

6. **Link the previous node to the next node**:  
   - Set `TEMP->NEXT = NODE-TO-DELETE->NEXT`.

7. **Free the node to be deleted**:  
   - Free `NODE-TO-DELETE`.

8. **Exit the algorithm**.

---

### **7. Search for an Element**

1. **Set TEMP = HEAD**.

2. **Traverse the list**:  
   - While `TEMP != NULL`:
     - If `TEMP->DATA == KEY`, print "Element found" and exit the algorithm.
     - Move to the next node (`TEMP = TEMP->NEXT`).

3. **If the key was not found**:  
   - Print "Element not found".

4. **Exit the algorithm**.

---

### **8. Reverse the Linked List**

1. **Initialize three pointers**:  
   - Set `PREV = NULL`, `CURRENT = HEAD`, and `NEXT = NULL`.

2. **Traverse the list**:  
   - While `CURRENT != NULL`:
     - Set `NEXT = CURRENT->NEXT`.
     - Set `CURRENT->NEXT = PREV`.
     - Move `PREV = CURRENT` and `CURRENT = NEXT`.

3. **Set `HEAD = PREV`** (the new head of the reversed list).

4. **Exit the algorithm**.

---

### **9. Find the Length of the Linked List**

1. **Initialize a counter**:  
   - Set `COUNT = 0`.

2. **Set TEMP = HEAD**.

3. **Traverse the list**:  
   - While `TEMP != NULL`:
     - Increment the counter (`COUNT++`).
     - Move to the next node (`TEMP = TEMP->NEXT`).

4. **Print the length of the list**:  
   - Print `COUNT`.

5. **Exit the algorithm**.

---

### **10. Detect Cycle in the Linked List (Floyd's Cycle Detection)**

1. **Initialize two pointers**:  
   - Set `SLOW = HEAD` and `FAST = HEAD`.

2. **Traverse the list with two pointers**:  
   - While `FAST != NULL` and `FAST->NEXT != NULL`:
     - Move `SLOW = SLOW->NEXT`.
     - Move `FAST = FAST->NEXT->NEXT`.
     - If `SLOW == FAST`, print "Cycle detected" and exit the algorithm.

3. **If no cycle is detected**:  
   - Print "No cycle".

4. **Exit the algorithm**.

---

These algorithms cover the most common linked list operations, each presented with a clear structure and an appropriate overflow or underflow condition where necessary.