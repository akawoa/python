/*
    Key focus of the day? Removing a node from the middle of a SLL.
    Let's think about this. If we have:
    H: 5 -> 4 -> 3 -> 2 -> 1 ->

    And we want to remove the node with a value of 3, how might we do this?
    The end result should look something like:
    H: 5 -> 4 -> 2 -> 1 ->

    Well in that case, all we really need to do is move 4's .next to be 3's .next, right?
    Right.

    With that in mind...

    Two challenges today!

    Challenge 1: moveMinToFront()
    Write a method that will find the node with the smallest value, and move it to the front. 
    EXAMPLE:
    H: 5 -> 3 -> 6 -> 1 -> 2 ->
    would become
    H: 1 -> 5 -> 3 -> 6 -> 2 -> 

    Challenge 2: moveMaxToBack()
    Write a method that will find the node with the largets value, and move it to the back.
    EXAMPLE:
    H: 1 -> 7 -> 11 -> 2 -> 18 -> 4 ->
    would become
    H: 1 -> 7 -> 11 -> 2 -> 4 -> 18 ->
*/


class SLNode {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class SLList {
    constructor(){
        this.head = null;
    }

    addToFront(value) {
        var newHead = new SLNode(value);
        newHead.next = this.head;
        this.head = newHead;
        return this;
    }

    addToBack(value) {
        if(this.head == null) {
            this.addToFront(value);
            return this;
        }

        var newNode = new SLNode(value);
        var runner = this.head;

        while(runner.next != null) {
            runner = runner.next;
        }

        runner.next = newNode;
        return this;
    }

    contains(value) {
        if(this.head == null) {
            return false;
        }

        var runner = this.head;

        while(runner != null) {
            if(runner.value == value) {
                return true;
            } else { 
                runner = runner.next;
            }
        }

        return false;
    }

    removeFront() {
        if(this.head == null) {
            return false;
        }

        var nodeToRemove = this.head;
        this.head = nodeToRemove.next;
        nodeToRemove.next = null;

        return nodeToRemove;
    }

    removeBack() {
        if(this.head == null) {
            return false;
        } else if(this.head.next = null) {
            return this.removeFront();
        }

        var lagger = null; 
        var leader = this.head; 
        while(leader.next != null) {
            lagger = leader;
            leader = leader.next;
        }

        lagger.next = null;
        return leader;
    }

    moveMinToFront(){
        // your code here
        return this;
    }

    moveMaxToBack(){
        // your code here
        return this;
    }
}

// 5 -> 3 -> 6 -> 1 -> 2 ->

// var node = new SLNode().addToFront(5).addToBack(3).addToBack(6).addToBack(1).addToBack(2)
var node = new SLList()
// .addToFront(5).addToBack(3).addToBack(6).addToBack(1).addToBack(2)
node.addToFront(5)
console.log(node)