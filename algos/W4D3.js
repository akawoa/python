/*
    More Singly Linked Lists!

    Today we're going to be adding two new methods to our SLL class.

    Method 1:
    Remove Front
        - This method should remove the first node in the list, and
        reassign the head of the list.
        - Returns the node that was removed. If there was no node to return, return false
        Potential Edge Cases: Empty list and only one node??
    
    Remove Back
        - This method should remove the LAST node in the list.
        This one can be a little bit tricky.
        - Returns the node that was removed. If there was no node to return, return false.
        Potential Edge Cases: Empty list and only one node??
    
*/

class SLNode {
    constructor(value) {
        this.value = value;
        this.next = null; // Why??
    }
}

class SLList {
    constructor() {
        this.head = null;
    }

    addToFront(value) {
        // Step 1: Create a new node for our new head
        var newHead = new SLNode(value);

        // Step 2: Assign the new node's .next attribute to be the current list's head node
        newHead.next = this.head;

        // Step 3: Reassign the list's head node to be the new node
        this.head = newHead;

        return this;
    }

    addToBack(value) {
        // EDGE CASE: If the list is empty, adding to the back is the same as adding to the front
        if (this.head == null) { // the list is empty if there IS no head
            // and we've already built out our method for adding to the front, soooo
            this.addToFront(value);
            return this;
        }

        // Step 1: Create our new node
        var newNode = new SLNode(value);

        // Step 2: Start at the head of the list
        var runner = this.head;

        // Step 3: Run to the last node
        while (runner.next != null) {
            runner = runner.next;
        }

        // Step 4: Set the last node's .next to be the new node
        runner.next = newNode;
        return this;
    }

    contains(value) {
        // EDGE CASE: What if the list is empty?
        if (this.head == null) {
            // If there's nothing in the list, it can't contain a node with any value. Duh.
            return false;
        }

        // Start at the head of the list
        var runner = this.head;

        // We need to check every single node
        while (runner != null) {
            // Check if the value of runner matches the value passed in
            if (runner.value == value) {
                // If it does, we're done
                return true;
            } else { // Otherwise, we need to move runner down the line
                runner = runner.next;
            }
        }

        // If we're still here, then we've checked every node, so we're done, and it's not there.
        return false;
    }

    // Function to remove the first node
    // of the linked list /
    removeFront() {
        if (this.head == null)
            return null;

        // Move the head pointer to the next node
        var temp = this.head;
        this.head = this.head.next;

        return this.head;
    }

    removeBack() {
        // your code here
    }
}

var newList = new SLList();

newList.addToBack(5).addToBack(1).addToFront(3);

// var contains5 = newList.contains(5);
// var contains5Expected = true;
// console.log(contains5 == contains5Expected);

// var contains2 = newList.contains(2);
// var contains2Expected = false;
// console.log(contains2 == contains2Expected);

// var contains3 = newList.contains(3);
// var contains3Expected = true;
// console.log(contains3 == contains3Expected);
console.log(newList)
newList.removeFront()
console.log(newList)

