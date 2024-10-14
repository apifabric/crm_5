import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CountryHomeComponent } from './home/Country-home.component';
import { CountryNewComponent } from './new/Country-new.component';
import { CountryDetailComponent } from './detail/Country-detail.component';

const routes: Routes = [
  {path: '', component: CountryHomeComponent},
  { path: 'new', component: CountryNewComponent },
  { path: ':id', component: CountryDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Country-detail-permissions'
      }
    }
  }
];

export const COUNTRY_MODULE_DECLARATIONS = [
    CountryHomeComponent,
    CountryNewComponent,
    CountryDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CountryRoutingModule { }