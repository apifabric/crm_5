import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Country-card.component.html',
  styleUrls: ['./Country-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Country-card]': 'true'
  }
})

export class CountryCardComponent {


}