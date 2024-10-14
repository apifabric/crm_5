import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {COUNTRY_MODULE_DECLARATIONS, CountryRoutingModule} from  './Country-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    CountryRoutingModule
  ],
  declarations: COUNTRY_MODULE_DECLARATIONS,
  exports: COUNTRY_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class CountryModule { }