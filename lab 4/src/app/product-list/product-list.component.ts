import { Component, Directive } from '@angular/core';

import { products } from '../products';

import { Router, RouterModule, Routes } from '@angular/router';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent {
  products = products;
  show: boolean[] = [];

  constructor( private router: Router ) {
    for(let i = 0; i < products.length; i++) {
      this.show.push(false);
    }
  }

  share(id: number) {
    let product = products.find((product) => product.id == id);
    this.router.navigate([product.link]);
  }

  onClick(id: number) {
    this.show[id-1] = this.show[id-1] !== true;
  }
}


/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/