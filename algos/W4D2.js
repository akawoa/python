// # Singly Linked List

// Today we're learning about Singly Linked Lists!

// A Singly Linked List is a data structure consisting of
// Nodes. Each Node contains a value attribute, and a next attribute,
// where the value is the data the node is holding on to, and the next
// attribute is the next node in the sequence.

// The list itself only has one attribute: the head. This is the START
// of the singly linked list. When the list is first initialized, the
// head is null, meaning there is nothing in the list.

// I've gone ahead and given you the starter code below:

// // ### Node
// ```js
// class Node {
//     constructor(value) {
//         this.value = value;
//         this.next = null; // Why??
//     }
// }
// ```

// // ### List
// ```js
// class SLList {
//     constructor(){
//         this.head = null;
//     }
// }
// ```

// // ## Iterating Through a Singly Linked List

// // To iterate through a singly linked list, we need to start at the
// // beginning (duh). But how? Well, we know what the start of the list is: `someList.head`.

// // And, if each node has a `.next` that points to the next node in the sequence, getting to the END
// // of a singly linked list means finding the node that has a `.next` that does not point to another node.

// // So if we initialize some kind of iterator (it's pretty standard to call it `runner`) as the list's `.head`,
// // and move `runner` to `runner.next` until `runner.next` is null, we will have iterated through
// // the entire singly linked list.

// ```js
// To stop runner on the LAST node
// var runner = this.head;
// while(runner.next != null) {
//     runner = runner.next;
// }
// ```

// ## To Create a New Instance of a Node

// ```js
// var newNode = new Node(somevalue)
// ```


/* 
    Three challenges!

    addToFront: Write a method of the SLList class that accepts a value, and adds a node with that 
    value to the front of the list. 
    
    Steps:
        1. Create a new node
        2. Assign that node's next attribute to the list's current head
        3. Assign the list's current head to the new node

    KEEP IN MIND: What dictates that a node is the first element in the list? Might need to reset that.

    addToBack: Write a method of the SLList class that accepts a value, and adds a node with that
    value to the BACK of the list.

    Steps:
        1. Create a new node
        2. Start at the head of the list
        3. Run to the last node
        4. Set the last node's next attribute to the new node
    EDGE CASE: What if the list is empty? How do we even know if the list is empty?

    contains: Write a method of the SLList class that accepts a value, and returns a boolean based
    on whether or not a node with that value exists in the list

    Steps:
        1. Start at the head of the list
        2. Check if the value of the node we're looking at equals the value passed in
        3. If it does, return true
        4. If not, go to the next node.
        5. If we checked every single node and we're still running the method, the value does not exist in the list.
*/

class Node {
    constructor(value) {
        this.value = value;
        this.next = null; // Why??
    }
}

class SLList {
    constructor(){
        this.head = null;
    }

    addToFront(value) {
        // Your Code Here
        this.prepend(Node(value))
        return this;
    }

    addToBack(value) {
        // Your Code Here
        return this;
    }

    contains(value) {
        // Your Code Here
    }
}

var newList = new SLList();

newList.addToBack(5).addToBack(1).addToFront(3);

var contains5 = newList.contains(5);
var contains5Expected = true;

var contains2 = newList.contains(2);
var contains2Expected = false;

var contains3 = newList.contains(3);
var contains3Expected = true;