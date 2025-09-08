class VisitorTracker {
  constructor() {
    this.visitors = new Set();
  }

  addVisitor(userId) {
    this.visitors.add(userId);
    console.log(`Visitor ${userId} added.`);
  }

  countVisitors() {
    console.log(`Total unique visitors: ${this.visitors.size}`);
    return this.visitors.size;
  }

  hasVisited(userId) {
    if (this.visitors.has(userId)) {
      console.log(`Visitor ${userId} has already visited.`);
      return true;
    } else {
      console.log(`Visitor ${userId} has not visited before.`);
      return false;
    }
  }
}

const tracker = new VisitorTracker();

tracker.addVisitor("user1");
tracker.addVisitor("user2");
tracker.addVisitor("user3");
tracker.addVisitor("user1");

tracker.countVisitors(); 

tracker.hasVisited("user2"); 
tracker.hasVisited("user5");
