function Heap() {
  this.items = [100];

  this.getLength = function () {
    return this.items.length - 1;
  };

  this._percolate_up = function () {
    let i = this.getLength(this.items);
    let parent = Math.floor(i / 2);

    console.log(i, parent);
    while (parent > 0) {
      if (this.items[i] < this.items[parent]) {
        let temp = this.items[parent];

        this.items[parent] = this.items[i];
        this.items[i] = temp;
      }

      i = parent;
      parent = Math.floor(i / 2);
    }
  };

  this.insert = function (k) {
    this.items.push(k);
    this._percolate_up();
  };
}

const h = new Heap();
h.insert(1);
h.insert(0);

console.log(h.items, h.getLength());
